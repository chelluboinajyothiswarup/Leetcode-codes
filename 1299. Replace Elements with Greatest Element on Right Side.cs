public class Solution {
    public int[] ReplaceElements(int[] arr) {
        int rightMax = -1, newMax = 0;
        for(int i = arr.Length-1;i>-1;i--){
            newMax = Math.Max(arr[i],rightMax);
            arr[i] = rightMax;
            rightMax = newMax;
        }
        arr[arr.Length-1] = -1;
        return arr;
    }
}
