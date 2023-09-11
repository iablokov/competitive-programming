struct Solution;

impl Solution 
{
    pub fn longest_common_prefix(strs: Vec<String>) -> String 
    {
        strs.into_iter()
            .reduce(|r, s|
            {
                r.chars()
                 .zip(s.chars())
                 .take_while(|(rc,rs)| rc == rs)
                 .map(|(rc, _)| rc)
                 .collect()
            }).unwrap()
    }
}

//============================================================================

#[cfg(test)]
mod tests
{
    use super::Solution;

    #[test]
    fn test_longest_common_prefix_1()
    {
        let strs = vec![
            "flower".to_owned(), 
            "flow".to_owned(),
            "flight".to_owned()
        ];
        
        let expected = "fl".to_owned();
        let output = Solution::longest_common_prefix(strs);
        assert_eq!(output, expected);
    }

    #[test]
    fn test_longest_common_prefix_2()
    {
        let strs = vec![
            "dog".to_owned(), 
            "racecar".to_owned(),
            "car".to_owned()
        ];

        let expected = "".to_owned();
        let output = Solution::longest_common_prefix(strs);
        assert_eq!(output, expected);
    }
}
