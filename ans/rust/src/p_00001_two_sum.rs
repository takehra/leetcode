pub struct Solution {}

impl Solution {
    pub fn solve_001(&self, nums: &[i32], target: i32) -> Option<Vec<usize>> {
        if !self.validate_args(nums, target) {
            return None;
        }

        for (idx1, &elm1) in nums.iter().enumerate() {
            for (idx2, &elm2) in nums.iter().enumerate() {
                if idx1 == idx2 {
                    continue;
                } else {
                    if elm1 + elm2 == target {
                        return Some(vec![idx1, idx2]);
                    }
                }
            }
        }

        None
    }

    pub fn solve_002(&self, nums: &[i32], target: i32) -> Option<Vec<usize>> {
        if !self.validate_args(nums, target) {
            return None;
        }

        let mut seen = std::collections::HashSet::new();
        for (idx, &elm) in nums.iter().enumerate() {
            let remaining = target - elm;
            if seen.contains(&remaining) {
                return Some(vec![idx, nums.iter().position(|&x| x == remaining).unwrap()]);
            }
            seen.insert(elm);
        }

        None
    }

    pub fn solve_003(&self, nums: &[i32], target: i32) -> Option<Vec<usize>> {
        if !self.validate_args(nums, target) {
            return None;
        }

        let mut hashmap = std::collections::HashMap::new();
        for (key, &val) in nums.iter().enumerate() {
            let remaining = target - val;
            if hashmap.contains_key(&remaining) {
                return Some(vec![key, *hashmap.get(&remaining).unwrap()]);
            } else {
                hashmap.insert(val, key);
            }
        }

        None
    }

    fn validate_args(&self, nums: &[i32], target: i32) -> bool {
        if !nums.iter().all(|&num| num >= -10i32.pow(9) && num <= 10i32.pow(9)) {
            return false;
        }
        if target < -10i32.pow(9) || target > 10i32.pow(9) {
            return false;
        }
        true
    }
}
