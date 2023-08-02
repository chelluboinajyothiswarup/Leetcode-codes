public class Solution {
    public int LengthOfLastWord(string s) {
        string[] x = s.Trim().Split(" ");
        Console.WriteLine(x[x.Length-1]);
        return x[x.Length-1].Length;
    }
}
