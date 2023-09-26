# Rust for LeetCode. Functional Programming.

## zip

To iterate simultaneously over two iterators, there is a `zip` method.

```rust
let vec1 = vec![1,2,3];
let vec2 = vec![4,5];
let zipped = vec1.iter().zip(vec2.iter());
for (n1, n2) in zipped { print!("({n1},{n2}) "); }
```
The output for the code above is `(1,4) (2,5)`.

#### Problem list:
* ##### [14. [Easy] Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/) ( solution : [GitHub](./../../../solutions/leetcode/00014-longest-common-prefix) [LeetCode](https://leetcode.com/problems/longest-common-prefix/solutions/3869696/python-rust-functional-solution/) )

## binary_search / binary_search_by / binary_search_by_key

Log-time search in sorted collections (e.g., a `Vec`) is achieved using `binary_search*` methods.
If the searched element is found, it's position is returned as `Ok(i)`. Otherwise, the *insertion position* is returned as `Err(i)`.

```rust
let vector = vec![1, 3, 6, 10, 12];
let target = 10;
let result = vector.binary_search(&target);
match result 
{
   Ok(i)  => println!("Found {} at index {}", target, i),       // this case is matched 
   Err(i) => println!("{} not found, insert at {}", target, i),
}
```


#### Problem list:
* ##### [74. [Medium] Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/) ( solution : [GitHub](./../../../solutions/leetcode/00074-search-a-2d-matrix) )


## reduce

To...

```
reduce
```

* ##### [136. [Easy] Single Number](https://leetcode.com/problems/single-number/) ( solution : [GitHub](./../../../solutions/leetcode/00074-search-a-2d-matrix) )
