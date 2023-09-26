use std::collections::BinaryHeap;
use std::cmp::Reverse;

struct KthLargest 
{
    k    : usize,
    heap : BinaryHeap<Reverse<i32>>,
}

impl KthLargest 
{

    fn new(k: i32, nums: Vec<i32>) -> Self 
    {
        let mut obj = KthLargest {k : k as usize, heap : BinaryHeap::new() };
        for n in nums { obj.heap.push(Reverse(n)); }
        obj
    }
    
    fn add(&mut self, val: i32) -> i32 
    {
        self.heap.push(Reverse(val));
        while self.heap.len() > self.k { self.heap.pop(); }
        
        if let Some(&Reverse(kth_largest)) = self.heap.peek()
        {
            return kth_largest;
        }
        return 0;
    }
}

//==============================================================================

#[cfg(test)]
mod tests
{
    use super::KthLargest;

    #[test]
    fn test_kth_largest()
    {
        let k        = 3;
        let nums     = vec![4,5,8,2];
        let stream   = vec![3,5,10,9,4];
        let expected = vec![4,5,5,8,8];

        let mut obj = KthLargest::new(k, nums);
        let output  = stream.iter()
                            .map(|&n| obj.add(n))
                            .collect::<Vec<i32>>();
        assert_eq!(output, expected);
    }   
}

