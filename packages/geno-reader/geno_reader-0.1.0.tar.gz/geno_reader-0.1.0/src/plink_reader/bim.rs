use std::{fs, io};

pub(crate) struct BimRecord {
    _chr_code: String,
    _var_id: String,
    _position: String,
    _bp_coord: i32,
    _allele_1: String,
    _allele_2: String,
}

pub(crate) fn parse_bim_line(line: &str) -> Result<BimRecord, String> {
    let line_split: Vec<&str> = line.split_whitespace().collect();

    if line_split.len() != 6 {
        Err(format!("Failed parsing bim line: {}", line))
    } else {

        let bp_parsed = line_split[3]
            .parse::<i32>()
            .map_err(|e| format!("Failed to parse BP coordinates {}: {}", line_split[3], e))?;

        Ok(
            BimRecord{
                _chr_code: line_split[0].to_string(),
                _var_id: line_split[1].to_string(),
                _position: line_split[2].to_string(),
                _bp_coord: bp_parsed,
                _allele_1: line_split[4].to_string(),
                _allele_2: line_split[5].to_string(),
            }
        )

    }
}

pub(crate) fn read_bim(path: &str) -> Result<Vec<BimRecord>, io::Error> {
    let contents = fs::read_to_string(path)?;

    let results = contents
        .lines()
        .map(parse_bim_line)
        .filter_map(|result| match result {
            Ok(record) => Some(record),
            Err(record) => {
                println!("Failed to parse record: {}", record);
                None
            }
        })
        .collect();

    Ok(results)

}