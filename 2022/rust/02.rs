use std::fs;
use std::collections::HashMap;

fn main() {
    let file_path = "../inputs/02_input.txt";

    let contents = fs::read_to_string(file_path)
        .expect("Should have been able to read the file");

    let win_rules = HashMap::from([
        ("A", "C"), // Rock
        ("B", "A"), // Paper
        ("C", "B"), // Scissors
    ]);

    let shape_scores = ["A", "B", "C"];

    let mut total_points: u16 = 0;
    for line in contents.lines() {
        let line = line.trim().replace("X", "A").replace("Y", "B").replace("Z", "C");
        let line = line.split(' ').collect::<Vec<&str>>(); // e.g. ["A", "B"]
        // 0 - oponent; 1 - yourself
        if win_rules.get(line[1]).unwrap() == &line[0] { // Win
            total_points += 6
        } else { // Draw
            total_points += 3
        }
        total_points += shape_scores.iter().position(|x| x == &line[1]).unwrap() as u16 + 1;
    };
    println!("Total points: {}", total_points);
}