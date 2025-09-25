use std::{fs, io};

pub(crate) enum Sex {
    Male,
    Female,
    Unknown,
}

pub(crate) struct FamRecord {
    pub(crate) individual_id: String,
    _family_id: String,
    _paternal_id: String,
    _maternal_id: String,
    _sex: Sex,
    _phenotype: i8,

}

pub(crate) fn parse_fam_line(line: &str) -> Result<FamRecord, String> {
    let line_split: Vec<&str> = line.split_whitespace().collect();

    if line_split.len() != 6 {
        Err("Failed to split fam line not enough entries.".to_string())
    } else {

        let sex = line_split[4].to_string();
        let sex_parsed = match sex.as_str() {
            "2" => Ok(Sex::Female),
            "1" => Ok(Sex::Male),
            "0" => Ok(Sex::Unknown),
            _ => Err("Sex is not '1', '2' or '0'.")
        }?;

        let phenotype_parsed = line_split[5]
            .parse::<i8>()
            .map_err(|e| format!("Failed to parse phenotype {}: {}", line_split[5], e))?;

        Ok(FamRecord {
            individual_id: line_split[1].to_string(),
            _family_id: line_split[0].to_string(),
            _paternal_id: line_split[2].to_string(),
            _maternal_id: line_split[3].to_string(),
            _sex: sex_parsed,
            _phenotype: phenotype_parsed,
        })
    }
}

pub(crate) fn read_fam(path: &str) -> Result<Vec<FamRecord>, io::Error> {
    let contents = fs::read_to_string(path)?;

    let records = contents
        .lines()
        .map(parse_fam_line)
        .filter_map(|result| match result {
            Ok(record) => Some(record),
            Err(e) => {
                println!("Skipping invalid line {}", e);
                None
            }
        })
        .collect();

    Ok(records)
}