public class App {
    public static void main(String[] args) throws Exception {
        
    }
}


class Solution {
    public int minFallingPathSum(int[][] matrix) {
        if(matrix.length == 1)
            return matrix[0][0]; 

        for(int i = 1; i< matrix.length; i++){
            for(int j = 0; j<matrix[0].length; j++){
                // 3 cases ? two edges and in between
                if(j == 0){
                    matrix[i][j] += Math.min(matrix[i-1][j], matrix[i-1][j+1]); 
                }else if(j == matrix[0].length-1){
                    matrix[i][j] += Math.min(matrix[i-1][j], matrix[i-1][j-1]); 
                }else{
                    matrix[i][j] += Math.min(matrix[i-1][j], Math.min(matrix[i-1][j-1],matrix[i-1][j+1])); 
                }
            }
        }
        int m = Integer.MAX_VALUE; 
        for(int x : matrix[matrix.length-1]){
            if(x < m)
                m = x; 
        }
        return m; 
    }   
}