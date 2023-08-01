class Solution {
    public int findNonMinOrMax(int[] nums) {
        int min = nums[0];int max=nums[0];
        for(int i=0;i<nums.length;i++){
            if (nums[i]<min){
            min=nums[i];}
            if (nums[i]>max){
                max=nums[i];
            }
        }
        for (int i=0;i<nums.length;i++){
            if (nums[i]!=min && nums[i]!=max){
                return nums[i];
            }
        }
        return -1;
    }
}