#include <vector>
#include <queue>
#include <cassert>
#include <iostream>

using namespace std;

class KthLargest 
{
    priority_queue<int, vector<int>, greater<int>> heap;
    int k;
    
public:

    KthLargest(int k, vector<int>& nums) : k(k)
    {
        for (int n : nums) heap.push(n);
    }
    
    int add(int val) 
    {
        this->heap.push(val);
        while (this->heap.size() > this->k) this->heap.pop();
        return this->heap.top();
    }
};

void test_kth_largest_1()
{
    int         k        = 3;
    vector<int> nums     = {4,5,8,2};
    vector<int> stream   = {3,5,10,9,4};
    vector<int> expected = {4,5,5,8,8};
    
    KthLargest* obj = new KthLargest(k, nums);
    vector<int> output;
    for (int n : stream) output.push_back(obj->add(n));

    assert(output == expected);
    std :: cout << "[OK] test_kth_largest_1() passed \n";
}

int main()
{
    test_kth_largest_1();
    return 0;
}
