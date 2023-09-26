struct Solution;

impl Solution 
{
    pub fn search_matrix(matrix: Vec<Vec<i32>>, target: i32) -> bool 
    {
        let r = matrix.binary_search_by(|row| row[0].cmp(&target));
        match r 
        {
            Ok(_)  => true,  // found target at 0-th position of some row
            Err(0) => false, // insertion position is before 0-th row

            // insertion position is inside the (i-1)-th row, search there
            Err(i) => matrix[i-1].binary_search(&target).is_ok()
        }
    }
}

#[cfg(test)]
mod tests
{
    use super::Solution;

    #[test]
    fn test_search_matrix_1()
    {
        let matrix = vec![
            vec![1,3,5,7],
            vec![10,11,16,20],
            vec![23,30,34,60]
        ];
        let target = 3;
        
        let expected = true;
        let output = Solution::search_matrix(matrix, target);
        assert_eq!(output, expected);
    }

    #[test]
    fn test_search_matrix_2()
    {
        let matrix = vec![
            vec![1,3,5,7],
            vec![10,11,16,20],
            vec![23,30,34,60]
        ];
        let target = 13;
        
        let expected = false;
        let output = Solution::search_matrix(matrix, target);
        assert_eq!(output, expected);
    }
}

