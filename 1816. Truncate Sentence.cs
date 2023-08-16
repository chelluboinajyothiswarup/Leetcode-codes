public class Solution {
    public string TruncateSentence(string s, int k) {
        string[] x = s.Split(" ");
        string up="";
        for(int i=0;i<k;i++){
            up+=(x[i]+" ");
        }
        return up.Trim();
    }
}
