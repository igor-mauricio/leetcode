/*
 * @lc app=leetcode id=1768 lang=java
 *
 * [1768] Merge Strings Alternately
 */

// @lc code=start
class Solution {
    public String mergeAlternately(String word1, String word2) {
        int smallerSize = word1.length() < word2.length() ? word1.length() : word2.length();

        StringBuilder result = new StringBuilder();

        for (int i = 0; i < smallerSize; i++) {
            result.append(word1.charAt(i));
            result.append(word2.charAt(i));
        }
        if (word1.length() > word2.length()) {
            result.append(word1.substring(smallerSize));
        }
        if (word2.length() > word1.length()) {
            result.append(word2.substring(smallerSize));
        }
        return result.toString();

    }
}
// @lc code=end

