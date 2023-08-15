function longestCommonPrefix(strs) {
    function prefix(s1, s2) {
        var m = Math.min(s1.length, s2.length);
        for (var i = 0; i < m; i++)
            if (s1[i] != s2[i])
                return s1.slice(0, i);
        return s1.slice(0, m);
    }
    return strs.reduce(prefix, strs[0]);
}
;
function test() {
    test_longestCommonPrefix_1();
    test_longestCommonPrefix_2();
}
function test_longestCommonPrefix_1() {
    var strs = ["flower", "flow", "flight"];
    var expected = "fl";
    var output = longestCommonPrefix(strs);
    console.log(output == expected);
}
function test_longestCommonPrefix_2() {
    var strs = ["dog", "racecar", "car"];
    var expected = "";
    var output = longestCommonPrefix(strs);
    console.log(output == expected);
}
test();
