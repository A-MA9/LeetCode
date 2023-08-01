class Solution {
    public boolean isPalindrome(int x) {
        if (x<0){
            return false;
        }
        else{
            String c = "";
        String s = Integer.toString(x);
        for(int i = s.length()-1;i>=0;i--){
            c+=s.charAt(i);
        }
        return c.equals(s);
        }
    }
}
