class Solution {
    public int[] runningSum(int[] nums) {
        int l=nums.length;
        int sum[] = new int[l];
        int c=0;
        for (int i=0;i<l;i++){
            sum[i]=c+nums[i];
            c+=nums[i];
        }   
        return sum;
    }
}