use std::fs;
use std::file;

fn main() {
    let file_path = "../inputs/02_input.txt";

    let contents = fs::read_to_string(file_path)
        .expect("Should have been able to read the file");

    println!("{}", file!().replace(".rs", ""));
}