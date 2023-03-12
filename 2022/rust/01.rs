use std::fs;

fn main() {
    let file_path = "../inputs/01_input.txt";

    let contents = fs::read_to_string(file_path)
        .expect("Should have been able to read the file");

    let mut soma: u32 = 0;
    let mut all_elves_total_calories: Vec<u32> = vec![];
    for line in contents.lines() {
        if line == "" {
            all_elves_total_calories.push(soma);
            soma = 0;
        } else {
            soma += line.parse::<u32>().unwrap();
        }
    }
    all_elves_total_calories.sort();
    all_elves_total_calories.reverse();
    println!("Top 3 calories carrying elves: {:?}", &all_elves_total_calories[0..3]);
    println!("Total colories of the top 3 together: {:?}", &all_elves_total_calories[0..3].iter().sum::<u32>());
}
