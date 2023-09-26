#include <iostream>
#include <vector>
#include <algorithm>
#include <cassert>

using namespace std;

class Solution 
{
public:
    vector<int> findClosestElements(vector<int>& arr, int k, int x)
    {
        auto p = lower_bound(arr.begin(), arr.end(), x);
        auto l = p, r = p;

        while (r - l < k)
        {
            if (l == arr.begin()) { r = arr.begin() + k; break; }
            if (r == arr.end())   { l = arr.end()   - k; break; }

            if (abs(*(l-1) - x) <= abs(*r - x)) { l--; }
            else                                { r++; }
        }
        
        return vector<int>(l, r);
    }
};

//============================================================================

void test_findClosestElements_1()
{
    vector<int> arr = {1,2,3,4,5};
    int k = 4, x = 3;
    vector<int> expected = {1,2,3,4};

    vector<int> output = Solution().findClosestElements(arr, k, x);
    
    assert(output == expected);
    std :: cout << "[OK] test_findClosestElements_1() passed \n";
}

void test_findClosestElements_2()
{
    vector<int> arr = {1,2,3,4,5};
    int k = 4, x = -1;
    vector<int> expected = {1,2,3,4};

    vector<int> output = Solution().findClosestElements(arr, k, x);
    
    assert(output == expected);
    std :: cout << "[OK] test_findClosestElements_2() passed \n";
}

int main()
{
    test_findClosestElements_1();
    test_findClosestElements_2();
    return 0;
}
