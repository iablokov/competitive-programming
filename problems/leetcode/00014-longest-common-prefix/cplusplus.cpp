#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <numeric>

using namespace std;

class Solution 
{
public:
    string longestCommonPrefix(vector<string>& strs) 
    {
        auto prefix = [](string s1, string s2) -> string 
        {
            size_t m = min(s1.size(), s2.size());
            for (size_t i = 0; i < m; ++i)
                if (s1[i] != s2[i]) return s1.substr(0, i);
            return s1.substr(0, m);
        };
        
        sort(strs.begin(), strs.end());
        return reduce(strs.begin(), strs.end(), strs[0], prefix);
    }
};

//============================================================================

int main()
{
    Solution sol;
    vector<string> strs = {"flower","flow","flight"};
    cout << sol.longestCommonPrefix(strs) << endl;
    return 0;
}