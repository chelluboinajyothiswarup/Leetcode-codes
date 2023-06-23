class Solution {
    public int findLUSlength(String a, String b) {
        if(a.equals(b)){
            return -1;
        }
        int x = a.length();
        int y = b.length();
        if(x>y){
            return x;
        }
        else{
            return y;
        }
    }
}
