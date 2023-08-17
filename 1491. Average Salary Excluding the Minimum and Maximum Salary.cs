public class Solution {
    public double Average(int[] salary) {
        int x=salary.Min(), y = salary.Max();
        int z = salary.Sum();
        return (double)(z-(x+y))/(salary.Length-2);
    }
}
