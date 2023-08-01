class Solution {
    public int singleNumber(int[] nums) {
        int l = nums.length;
        Arrays.sort(nums);
        for (int i=0;i<l-3;i+=3){
            if (nums[i]!=nums[i+2]){
                return nums[i];
            }
    }
    return nums[l-1];
    }
}