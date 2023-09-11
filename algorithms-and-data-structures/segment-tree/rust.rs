struct SegmentTree<'a, T> where T: Clone
{
    data    : Vec<T>,
    op      : &'a dyn Fn(&T,&T) -> T,
    default : &'a dyn Fn() -> T,
    size    : usize,
    offset  : usize,
}

impl<'a, T> SegmentTree<'a, T> where T: Clone
{
    pub fn new(data: Vec<T>, op: &'a dyn Fn(T,T) -> T, default: &'a dyn Fn() -> T) -> Self
    {
        let size = data.len();
        let offset = 1 << (usize::BITS - size.leading_zeros());
        let data = std::iter::repeat_with(default)
            .take(offset)
            .chain(data.into_iter())
            .collect();

        let mut tree = Self { data : data, op : op, default : default, size : size, offset : offset };
        tree.build();
        tree
    }

    fn build(&mut self)
    {
        for i in (1..self.offset).rev()
        {
            let l = i << 1;
            let r = l + 1;
            let lval = if l < self.data.len() { &self.data[l] } else { (self.default)() };
            let rval = if r < self.data.len() { &self.data[r] } else { (self.default)() };
            self.data[i] = (self.op)(lval, rval);
        }
    }

    pub fn update(&mut self, index: usize, value: T)
    {
        let mut i = index + self.offset;
        self.data[i] = value;
        while i > 1
        {
            i >>= 1;
            let l = i << 1;
            let r = l + 1;
            let lval = if l < self.data.len() { self.data[l].clone() } else { (self.default)() };
            let rval = if r < self.data.len() { self.data[r].clone() } else { (self.default)() };
            self.data[i] = (self.op)(lval, rval);
        }
    }

    pub fn query_with<U>(&self, left: usize, right: usize, op: &dyn Fn(U,&T) -> U, default: &dyn Fn() -> U) -> Result<U, String>
    {
        if left >= right                 { return Err("Invalid range"); }
        if left < 0 || right > self.size { return Err("Out of range"); }

        let mut res = (default)();
        let mut l = left + self.offset;
        let mut r = right + self.offset;
        while l < r
        {
            if l & 1 == 1 { res = (op)(res, &self.data[l].clone()); }
            if r & 1 == 1 { res = (op)(res, &self.data[r].clone()); }
            l >>= 1;
            r >>= 1;
        }

        Ok(res)
    }

    pub fn query(&self, left: usize, right: usize) -> Result<T, String>
    {
        self.query_with(left, right, self.op, self.default)
    }
}




fn main()
{
    let mut tree = SegmentTree::new(vec![1,2,3,4,5], &|&a,&b| a+b, &|| 0);
    tree.update(2, 10);
    
    // Define a closure
    let my_closure = |x| x * 2;

    // Create a vector of numbers
    let numbers = vec![1, 2, 3, 4, 5];

    // Iterate through the numbers and pass the closure to another function
    for &num in &numbers {
        process_with_closure(num, &my_closure);
    }
}

// Function that takes a closure as an argument
fn process_with_closure(value: i32, closure: &dyn Fn(i32) -> i32) {
    let result = closure(value);
    println!("Result: {}", result);
}