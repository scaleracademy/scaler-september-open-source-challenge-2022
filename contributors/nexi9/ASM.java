public class ASM{

    public static int asm(String source,String target){
        int m=source.length();
        int n=target.length();
        int[][] mat=new int[m+1][n+1];
        for(int i=0;i<=m||i<=n;i++){
            if(i<m){
                mat[i][0]=i;
            }
            if(i<n){
                mat[0][i]=i;
            }
        }
        for(int i=1;i<=n;i++){
            for(int j=1;j<=m;j++){
                if(source.charAt(i-1)==target.charAt(j-1)){
                    mat[i][j]=mat[i-1][j-1];
                }else{
                    mat[i][j]=Math.min(mat[i-1][j-1]+1, Math.min(mat[i][j-1]+1, mat[i-1][j]+1));
                }
            }
        }
        return mat[m][n];
    }

    public static void main(String[] args){
        String s1="aba";
        String s2="bab";
        System.out.println(asm(s1, s2));

    }
}
