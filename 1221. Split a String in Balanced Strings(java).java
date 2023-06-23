class Solution {
    public int balancedStringSplit(String s) {
        int l=0;
        int m=0;
        for(int i=0;i<s.length();i++){
            if(s.charAt(i)=='R'){
                l+=1;
            }
            else{
                l-=1;
            }
            if(l==0){
                m+=1;
                l=0;
            }
        }
        return m;
    }
}
