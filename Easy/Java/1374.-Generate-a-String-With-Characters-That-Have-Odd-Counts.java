class Solution {
    public String generateTheString(int n) {
        if(n%2==1){
            String s="a";
            s=s.repeat(n);
            return s;
        }
        else{
            String b="a";
            b=b.repeat(n-1);
            b+="c";
            return b;
        }
    }
}