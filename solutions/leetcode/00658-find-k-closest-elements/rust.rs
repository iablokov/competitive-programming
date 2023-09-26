struct Solution;

impl Solution 
{
    pub fn find_closest_elements(arr: Vec<i32>, k: i32, x: i32) -> Vec<i32> 
    {
        let p = arr.binary_search(&x).unwrap_or_else(|e| e);
        let k = k as usize;
        let mut l = p as usize;
        let mut r = p as usize;
        
        while r - l < k
        {
            if l == 0         { return arr[..k].to_vec(); }
            if r == arr.len() { return arr[(arr.len() - k)..].to_vec(); }

            if (x - arr[l - 1]).abs() <= (arr[r] - x).abs() { l -= 1; }
            else                                            { r += 1; }
        }

        arr[l..r].to_vec()
    }
}

//==============================================================================

#[cfg(test)]
mod tests
{
    use super::Solution;

    #[test]
    fn test_find_closest_elements_1()
    {
        let arr = vec![1,2,3,4,5];
        let k = 4;
        let x = 3;
        let expected = vec![1,2,3,4];

        let output = Solution::find_closest_elements(arr, k, x);
        assert_eq!(output, expected);
    }   
}

