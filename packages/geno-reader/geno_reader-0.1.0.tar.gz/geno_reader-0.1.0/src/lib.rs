use numpy::{Ix1, PyArray, ToPyArray};
use pyo3::exceptions::PyIOError;
use pyo3::prelude::*;
use rayon::prelude::*;
use std::cmp::min;
use std::fs;
use std::io;
use std::io::{Read, Seek, SeekFrom};
use std::mem;
use std::io::BufReader;

mod plink_reader;
use plink_reader::bed;
use plink_reader::bim::BimRecord;
use plink_reader::fam::FamRecord;

#[pyclass]
pub struct GenoReader{
    bed_reader: BufReader<fs::File>,
    fam_records: Vec<FamRecord>,
    bim_records: Vec<BimRecord>,
    current_individual_index: usize,
    chunk_size: usize,
    chunk_buffer: Vec<Vec<u8>>,
    decoded_chunk_buffer: Vec<Vec<u8>>,
}

#[pymethods]
impl GenoReader {
    #[new]
    fn new(plink_suffix: &str, chunk_size: usize) -> PyResult<Self> {
        let result = GenoReader::from_plink_suffix(plink_suffix, chunk_size)?;
        Ok(result)
    }

    fn __iter__(slf: Py<Self>) -> Py<Self> {
        slf
    }

    fn __len__(&self) -> PyResult<usize> {
        Ok(self.fam_records.len())
    }

    fn __next__(&mut self) -> PyResult<Option<SampleInfo>> {
        let result = self.next();

        match result {
            Some(Ok(sample_info)) => {
                Ok(Some(sample_info))
            },
            None => Ok(None),
            Some(Err(e)) => Err(PyIOError::new_err(e.to_string()))
        }

    }
}

impl GenoReader {
    pub fn from_plink_suffix(plink_suffix: &str, chunk_size: usize) -> Result<GenoReader, io::Error> {
        let bed_file = format!("{plink_suffix}{}", ".bed");
        let fam_file = format!("{plink_suffix}{}", ".fam");
        let bim_file = format!("{plink_suffix}{}", ".bim");

        bed::gather_data(&bed_file, &fam_file, &bim_file, chunk_size)
    }

    fn read_next_chunk(&mut self) -> Result<usize, io::Error> {
        let n_inds = self.fam_records.len();
        let remaining = n_inds.saturating_sub(self.current_individual_index);

        if remaining == 0 {
            return Ok(0);
        }

        let n_individuals_in_chunk = min(self.chunk_size, remaining);
        let n_snps = self.bim_records.len();
        let n_magic_bytes: usize = 3;

        let bytes_per_snp_row = (self.fam_records.len() + 3) / 4;
        let chunk_byte_start_index_in_row = self.current_individual_index / 4;
        let end_individual_index = self.current_individual_index + n_individuals_in_chunk - 1;
        let chunk_byte_end_index_in_row = end_individual_index / 4;
        let n_bytes_to_read = chunk_byte_end_index_in_row - chunk_byte_start_index_in_row + 1;

        // This holds a chunk of data, where each column is an individual, and each
        // row is an SNP.
        let mut all_snp_bytes: Vec<Vec<u8>> = Vec::with_capacity(n_snps);
        for snp_index in 0..n_snps {
            let snp_row_start_pos = n_magic_bytes + (snp_index * bytes_per_snp_row);
            let start_byte_pos = snp_row_start_pos + chunk_byte_start_index_in_row;
            self.bed_reader.seek(SeekFrom::Start(start_byte_pos as u64))?;

            let mut snp_chunk_bytes = vec![0u8; n_bytes_to_read];
            self.bed_reader.read_exact(&mut snp_chunk_bytes)?;
            all_snp_bytes.push(snp_chunk_bytes);
        }

        let bytes_per_individual = (n_snps + 3) / 4;
        let mut current_chunk_buffer: Vec<Vec<u8>> = vec![vec![0u8; bytes_per_individual]; n_individuals_in_chunk];

        // Here we are ultimately, transposing the SNP-major format to individual-major format
        // working with how PLINK organizes the data (e.g., 4 individuals per byte) to extract
        // the individual level genotypes
        current_chunk_buffer
            .par_iter_mut()
            .enumerate()
            .for_each(|(chunk_ind_index, individual_buffer)| {
                for (snp_index, snp_chunk_bytes) in all_snp_bytes.iter().enumerate() {
                    let absolute_ind_index = self.current_individual_index + chunk_ind_index;
                    let absolute_byte_index = absolute_ind_index / 4;
                    let in_chunk_relative_byte_index = absolute_byte_index - chunk_byte_start_index_in_row;

                    // Note: this byte contains 4 individuals
                    let packed_genotype_byte = snp_chunk_bytes[in_chunk_relative_byte_index];
                    let genotype_index_in_byte = absolute_ind_index % 4;

                    // So here the PLINK file format is the reason we do this, because of how
                    // individuals are structured internally, so for e.g., byte index 32,
                    // we actually have
                    // index:               [128, 129, 130, 131]
                    // individual index:    [131, 130, 129, 128]
                    // this is why we do the right shift below
                    // for example, if absolute ind_index is 3, we are in byte [0, 1, 2, 3]
                    // with individual indices being [3, 2, 1, 0], so we shift to get ultimately
                    // [na, na, na, 3]
                    let mask = 0b00000011;
                    let shifted = packed_genotype_byte >> (genotype_index_in_byte * 2);
                    let extracted_genotype = shifted & mask;

                    let target_byte_index = snp_index / 4;
                    let target_genotype_index_in_byte = snp_index % 4;

                    // shift what is now stored in the last 2 bits in masked_read to the target index
                    let repositioned_genotype = extracted_genotype << (target_genotype_index_in_byte * 2);
                    individual_buffer[target_byte_index] |= repositioned_genotype;
                }
            });

        self.chunk_buffer = current_chunk_buffer;
        self.chunk_buffer.reverse();
        self.current_individual_index += n_individuals_in_chunk;
        Ok(n_individuals_in_chunk)
    }
}

#[pyclass]
pub struct SampleInfo {
    #[pyo3(get)]
    pub genotypes: Vec<u8>,
    #[pyo3(get)]
    pub sample_id: String,
}

#[pymethods]
impl SampleInfo {
    fn genotypes_as_numpy<'py>(&self, py: Python<'py>) -> Bound<'py, PyArray<u8, Ix1>> {
        self.genotypes.to_pyarray(py)
    }
}

impl Iterator for GenoReader {
    type Item = Result<SampleInfo, io::Error>;

    fn next(&mut self) -> Option<Self::Item> {
        loop {
            if !self.decoded_chunk_buffer.is_empty() {
                // the current individual index has already been incremented to the *end* of the current chunk
                let current_absolute_index = self.current_individual_index - self.decoded_chunk_buffer.len();
                let sample_id = self.fam_records[current_absolute_index].individual_id.clone();

                let genotypes = self.decoded_chunk_buffer.pop()?;
                return Some(Ok(SampleInfo{genotypes, sample_id}))
            }

            if !self.chunk_buffer.is_empty() {
                let n_snps = self.bim_records.len();

                self.decoded_chunk_buffer = mem::replace(&mut self.chunk_buffer, Vec::new())
                    .into_par_iter()
                    .map(|packed_genotypes| unpack_individual_data(&packed_genotypes, n_snps))
                    .collect();

                continue
            }

            if self.current_individual_index >= self.fam_records.len() {
                return None;
            }

            match self.read_next_chunk() {
                Ok(0) => return None,
                Ok(_) => continue,
                Err(e) => return Some(Err(e)),
            }
        }
    }
}

fn unpack_individual_data(packed_data: &[u8], n_snps: usize) -> Vec<u8> {
    let mut unpacked = Vec::with_capacity(n_snps);
    let mask: u8 = 0b00000011;

    let zeros: u8;
    let ones: u8;

    let count_a1 = true;
    if count_a1 {
        zeros = 2;
        ones = 0;
    }
    else {
        zeros = 0;
        ones = 2;

    }

    for snp_index in 0..n_snps {
        let cur_byte_index = snp_index / 4;
        let cur_byte = packed_data[cur_byte_index];

        let cur_slot = snp_index % 4;
        let shifted = cur_byte >> (cur_slot * 2);
        let masked = shifted & mask;



        let value = match masked {
            0b00 => zeros,
            0b10 => 1,
            0b11 => ones,
            0b01 => 3,
            _ => 3,
        };

        unpacked.push(value);
    }

    unpacked

}


#[pymodule]
mod geno_reader {
    #[pymodule_export]
    use super::GenoReader;
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_load_test_files() {
        let geno_reader = GenoReader::from_plink_suffix("test_data/test", 2);
        assert!(geno_reader.is_ok(), "Should successfully load test PLINK files");
        
        let reader = geno_reader.unwrap();
        assert_eq!(reader.fam_records.len(), 4, "Should have 4 individuals");
        assert_eq!(reader.bim_records.len(), 4, "Should have 4 SNPs");
    }
    
    #[test]
    fn test_individual_iteration() {
        let geno_reader = GenoReader::from_plink_suffix("test_data/test", 4);
        let mut results = Vec::new();

        for item in geno_reader.unwrap() {
            results.push(item);
        }

        assert_eq!(results.len(), 4, "Should have 4 items")

    }
    
    #[test]
    fn test_genotype_correctness() {
        // Individual IND001: All homozygous major (should be [2,2,2,2] if counting major allele)
        // Individual IND002: All heterozygous (should be [1,1,1,1])  
        // Individual IND003: All homozygous minor (should be [0,0,0,0] if counting major allele)
        // Individual IND004: All homozygous major (should be [2,2,2,2] if counting major allele)
        
        let geno_reader = GenoReader::from_plink_suffix("test_data/test", 4);
        let mut genotypes = Vec::new();

        for item in geno_reader.unwrap() {
            genotypes.push(item.unwrap().genotypes);
        }

        assert_eq!(genotypes[0], vec![2,2,2,2], "Should be 2 for first individual");
        assert_eq!(genotypes[1], vec![1,1,1,1], "Should be 1 for first individual");
        assert_eq!(genotypes[2], vec![0,0,0,0], "Should be 0 for first individual");
        assert_eq!(genotypes[3], vec![2,2,2,2], "Should be 2 for first individual");

    }
    
    #[test]
    fn test_chunked_reading() {
        let geno_reader_chunk_4 = GenoReader::from_plink_suffix("test_data/test", 4);
        let mut genotypes_chunk_4 = Vec::new();
        let mut ids_chunk_4 = Vec::new();

        for item in geno_reader_chunk_4.unwrap() {
            let sample_info = item.unwrap();
            genotypes_chunk_4.push(sample_info.genotypes);
            ids_chunk_4.push(sample_info.sample_id);
        }

        let geno_reader_chunk_1 = GenoReader::from_plink_suffix("test_data/test", 1);
        let mut genotypes_chunk_1 = Vec::new();
        let mut ids_chunk_1 = Vec::new();

        for item in geno_reader_chunk_1.unwrap() {
            let sample_info = item.unwrap();
            genotypes_chunk_1.push(sample_info.genotypes);
            ids_chunk_1.push(sample_info.sample_id);
        }
        assert_eq!(genotypes_chunk_4, genotypes_chunk_1, "Genotypes with different chunk sizes not equal.");
        assert_eq!(ids_chunk_4, ids_chunk_1, "IDs with different chunk sizes not equal.");

    }
    
    #[test]
    fn test_sample_metadata() {
        // Expected IDs: ["IND001", "IND002", "IND003", "IND004"]

        let geno_reader = GenoReader::from_plink_suffix("test_data/test", 4);

        let mut ids = Vec::new();
        for item in geno_reader.unwrap() {
            ids.push(item.unwrap().sample_id);
        }

        assert_eq!(ids[0], "IND001");
        assert_eq!(ids[1], "IND002");
        assert_eq!(ids[2], "IND003");
        assert_eq!(ids[3], "IND004");

    }
    
    #[test]
    fn test_snp_count_per_individual() {
        let geno_reader = GenoReader::from_plink_suffix("test_data/test", 4);

        for item in geno_reader.unwrap() {
            assert_eq!(item.unwrap().genotypes.len(), 4);
        }
    }
    
    #[test]
    fn test_missing_files() {
        let geno_reader = GenoReader::from_plink_suffix("test_data/nonexistent", 4);

        assert!(geno_reader.is_err());

    }
}