class Solution {
    public boolean lemonadeChange(int[] bills) {
        int five = 0;
        int ten = 0;
        if(bills[0]!=5){
            return false;
        }
        for(int i=0;i<bills.length;i++){
            if(bills[i]==5){
                five = five +5;
            }
            else if(bills[i]==10){
                if(five>0){
                    five = five - 5;
                    ten = ten + 10;
                }
                else{
                    return false;
                }
            }
            else{
                if(ten>0 && five>0){
                    ten = ten - 10;
                    five = five - 5;
                }
                else{
                    if(five>10){
                        five = five -15;
                    }
                    else{
                        return false;
                    }
                }
            }
        }
        return true;
    }
}
