public class Solution {
    public bool IsCovered(int[][] ranges, int left, int right) {
        bool satisfy;
        for(int i=left;i<=right;i++){
            satisfy = false;
            for(int m=0;m<ranges.Length;m++){
                if(i>=ranges[m][0] && i <=ranges[m][1]){
                    satisfy = true;
                    break;
                }                
            }
            if(!satisfy){
                return false;
            }
        }
        return true;
    }
}
