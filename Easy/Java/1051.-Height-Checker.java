class Solution {
    public int heightChecker(int[] heights) {
        int n=heights.length;
        int e[] = new int[n];
        for(int i=0;i<n;i++){
            e[i]=heights[i];
        }
        Arrays.sort(e);int s=0;
        for(int i=0;i<n;i++){
            if (e[i]!=heights[i]){
                s+=1;
            }
        }
        return s;
    }
}