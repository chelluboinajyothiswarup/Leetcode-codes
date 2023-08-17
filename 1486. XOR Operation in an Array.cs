public class Solution {
    public int XorOperation(int n, int start) {
        int[] array = new int[n];
        int x = 0;
        for(int i=0;i<n;i++){
            array[i] = start+2*i;
            x^=array[i];
        }
        return x;
    }
}
