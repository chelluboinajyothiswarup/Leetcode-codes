class Solution {
    public List<List<Integer>> minimumAbsDifference(int[] arr) {
        Arrays.sort(arr);
        int x = Integer.MAX_VALUE;
        int z = arr.length-1;
        List<List<Integer>> lst = new ArrayList<>();
        for(int i=0;i<z;i++){
            int y = arr[i+1]-arr[i];
            if(y<x){
                x = y;
            }
        }
        for(int i=0;i<z;i++){
            if(arr[i+1]-arr[i]==x){
                ArrayList<Integer> pair=new ArrayList<>(2);
                pair.add(arr[i]);
                pair.add(arr[i+1]);
                lst.add(pair);
            }
        }
        return lst;

    }
}
