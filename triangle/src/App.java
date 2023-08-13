import java.util.ArrayList;
import java.util.List;

public class App {
  //**************************testing*****************************************/
    public static void main(String[] args) {
        List<List<Integer>> triangle = new ArrayList<>(0);
        List<Integer> firstLayer = new ArrayList<>(); 
        firstLayer.add(0, 1);
        List<Integer> secondLayer = new ArrayList<>(); 
        secondLayer.add(0,1); 
        secondLayer.add(1,2); 
        triangle.add(0, firstLayer);
        triangle.add(1,secondLayer); 
        List<Integer> thirdLayer = new ArrayList<>(); 
        thirdLayer.add(0, 1);
        thirdLayer.add(1,5);
        thirdLayer.add(2,5); 
        triangle.add(2,thirdLayer); 
        Solution a = new Solution();  
        System.out.println(a.minimumTotal(triangle));
    }
} 
//*************************************************************************



class Solution {
    int minimumTotal(List<List<Integer>> triangle) {
        if (triangle.size() == 0)
            return 0;

        for (int i = 1; i < triangle.size(); i++) {
            List<Integer> copyList1 = new ArrayList<>(triangle.get(i-1)); 
            List<Integer> copyList = new ArrayList<>(triangle.get(i));
                for (int j = 0; j < copyList.size(); j++){

                    if(j==0){
                      copyList.set(j, copyList.get(j)+copyList1.get(j));
                    }else if(j==copyList.size()-1){
                      copyList.set(j, copyList.get(j)+copyList1.get(j-1)); 
                    }else{
                      copyList.set(j, Math.min(copyList.get(j)+copyList1.get(j-1),copyList.get(j)+copyList1.get(j))); 
                    }
                }
                triangle.set(i,copyList);
            }
        int min = Integer.MAX_VALUE;     
        for(int i = 0; i<triangle.get(triangle.size()-1).size(); i++){
            if(triangle.get(triangle.size()-1).get(i) < min){
                min = triangle.get(triangle.size()-1).get(i); 
            }
        }
        return min; 
    }
}

