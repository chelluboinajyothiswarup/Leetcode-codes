class Solution {
    public int dayOfYear(String date) {
        int sum=0;
        int[] arr = {31,28,31,30,31,30,31,31,30,31,30,31};
        String[] y = date.split("-");
        int year = Integer.valueOf(y[0]);
        int month = Integer.valueOf(y[1]);
        int day = Integer.valueOf(y[2]);
        boolean leap = false;
        if((year%400==0) || (year%100!=0) && (year%4==0)){
            leap = true;
        }
        if(month<=2){
            for(int i=0;i<month-1;i++){
                sum+=arr[i];
            }
            return sum+day;
        }
        if(leap){
            for(int i=0;i<month-1;i++){
                sum+=arr[i];
            }
            return sum+1+day;
        }
        else{
            for(int i=0;i<month-1;i++){
                sum+=arr[i];
            }
            return sum+day;
        }
    }
}
