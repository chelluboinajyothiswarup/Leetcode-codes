public class Solution {
    public string FinalString(string s) {
        string x = "";
        for(int i=0;i<s.Length;i++){
            if(s[i]=='i'){
                char[] stringArray = x.ToCharArray();
                Array.Reverse(stringArray);
                x = new string(stringArray);
            }
            else{
                x+=s[i];
            }
        }
        return x;
    }
}
