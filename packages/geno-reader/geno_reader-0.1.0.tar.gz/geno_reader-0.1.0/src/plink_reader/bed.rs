use std::{fs, io};
use std::io::BufReader;
use crate::GenoReader;
use crate::plink_reader::{bim, fam};

pub(crate) fn gather_data(bed_file: &str, fam_file: &str, bim_file: &str, chunk_size: usize) -> Result<GenoReader, io::Error> {
    let fam_records = fam::read_fam(fam_file)?;
    let bim_records = bim::read_bim(bim_file)?;

    let bed_reader = BufReader::new(fs::File::open(bed_file)?);

    let current_individual_index = 0;

    let chunk_buffer = Vec::new();
    let decoded_chunk_buffer = Vec::new();

    Ok(GenoReader{
        bed_reader,
        fam_records,
        bim_records,
        current_individual_index,
        chunk_size,
        chunk_buffer,
        decoded_chunk_buffer,
    })

}