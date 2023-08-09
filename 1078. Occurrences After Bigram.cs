public class Solution {
    public string[] FindOcurrences(string text, string first, string second) {
        string[] s = text.Split(" ");
        List<string> x = new List<string>();
        for(int i=0;i<s.Length-2;i++){
            if(s[i]==first && s[i+1]==second){
                x.Add(s[i+2]);
            }
        }
        return x.ToArray();

    }
}
