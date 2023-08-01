class Solution {
    public int countPrefixes(String[] words, String s) {
        int n=words.length;int l=s.length();int c=0;
        for(int i=0;i<n;i++){
            String d=words[i];
            if (d.length()<=l){
                if(d.equals(s.substring(0,d.length()))){
                    c+=1;
                }
            }
        }
        return c;
    }
}