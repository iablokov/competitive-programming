function longestCommonPrefix(strs: string[]): string 
{
    function prefix(s1: string, s2: string): string
    {
        let m: number = Math.min(s1.length, s2.length);
        for (let i = 0; i < m; i++)
            if (s1[i] != s2[i]) return s1.slice(0, i);

        return s1.slice(0, m);
    }

    return strs.reduce(prefix, strs[0]);
};

function test()
{
    test_longestCommonPrefix_1();
    test_longestCommonPrefix_2();
}

function test_longestCommonPrefix_1()
{
    let strs = ["flower","flow","flight"]; 
    let expected = "fl";
    let output = longestCommonPrefix(strs);
    console.log(output == expected);
}

function test_longestCommonPrefix_2()
{
    let strs = ["dog","racecar","car"];
    let expected = "";
    let output = longestCommonPrefix(strs);
    console.log(output == expected);
}

test();