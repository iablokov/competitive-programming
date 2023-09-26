# C++ for Competitive Programming. Functions.

Here are some tricks the demonstrate the efficient use of functions in typical CP problems.

## Recursion with cache using lambdas
The code below shows how to use recursion with cache on the example of classical Fibonacci numbers problem.
```cpp
unordered_map<int,int> cache;
function<int(int)> dfs = [&](int n) -> int
{
    // check if the value was already computed
    if (auto it = cache.find(n); it != cache.end()) return it->second;

    // make recursive computation
    int res = n;
    if (n > 1) res = dfs(n-1) + dfs(n-2);

    // store in cache and return
    return cache[n] = res;
};

int n = 10;
int fib = dfs(n);
```