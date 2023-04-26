use std::fs;

pub fn read_file(path_and_filename: &str) -> String {
    let file_path: &str = path_and_filename;

    let contents: String = fs::read_to_string(file_path)
        .expect("Should have been able to read the file, also check the case sensitivity");

    contents
}