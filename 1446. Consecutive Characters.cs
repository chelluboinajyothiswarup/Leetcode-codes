public class Solution {
    public int MaxPower(string s) {
        int x=1,m=0;
        for(int i=0;i<s.Length-1;i++){
            if(s[i]==s[i+1]){
                x++;
                m = Math.Max(m, x);
            }else{
                x = 1;
            }
        }

        if(m==0){
            return 1;
        }else{
            return m;
        }
    }
}
