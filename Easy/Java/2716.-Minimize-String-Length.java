import java.util.HashSet;
class Solution {
    public int minimizedStringLength(String s) {
        HashSet<Character> uniqueChars = new HashSet<>();
        StringBuilder a = new StringBuilder();

        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            if (!uniqueChars.contains(ch)) {
                uniqueChars.add(ch);
                a.append(ch);
            }
        }
        return a.length();
    }
}
// OR
class Solution {
    public int minimizedStringLength(String s) {
        String a="";
        for (int i=0;i<s.length();i++){
            if (!a.contains(String.valueOf(s.charAt(i)))){
                a+=s.charAt(i);
            }
        }
        return a.length();
    }
}