public class Solution {
    public int MaxDistance(int[] colors) {
        int max = 0, diff = 0;
        for(int i=0;i<colors.Length-1;i++){
            for(int j=i+1;j<colors.Length;j++){
                if(colors[i]==colors[j]){
                    continue;
                }
                else{
                    diff = j-i;
                    max = Math.Max(max,diff);
                }
            }
        }
        return max;
    }
}
