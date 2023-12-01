public class Solution {
    public int NumberOfSteps(int num) {
        int c = 0;
        while(num!=0){
            if(num%2==0){
                num=num/2;
                c=c+1;
            }
            else{
                num = num-1;
                c+=1;
            }
        }
        return c;
    }
}
