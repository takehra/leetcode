mod p_00001_two_sum;

use p_00001_two_sum::Solution;

fn main() {
    let solution = Solution {};

    let result = solution.solve_001(&[2, 7, 11, 15], 9);

    match result {
        Some(indices) => {
            println!("Indices: {:?}", indices);
        }
        None => {
            println!("No indices found.");
        }
    }
}
