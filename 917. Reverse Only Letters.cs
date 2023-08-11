public class Solution {
    public string ReverseOnlyLetters(string s) {
        int i = 0,j = s.Length-1;
        char[] charArray = s.ToCharArray();
        char temp;
        while(i<j){
            if(!char.IsLetter(charArray[i])){
                i+=1;
            }
            else if(!char.IsLetter(charArray[j])){
                j-=1;
            }
            else{
                temp = charArray[i];
                charArray[i] = charArray[j];
                charArray[j] = temp;
                i+=1;
                j-=1;
            }
        }

        return new string(charArray);
    }

}
