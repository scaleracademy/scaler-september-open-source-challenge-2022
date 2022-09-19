import java.lang.*;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
 
        int unit = sc.nextInt();
        double amt=0;
        double surcharge= 0.2;

        if (unit <= 50){
            amt += 0.5*unit;   
       }
       else if (50<unit && unit <=150){
            amt +=0.5*50;
            amt +=0.75*(unit-50);
       }
       else if (150 < unit && unit <=250){
            amt +=0.5*50;
            amt +=0.75*100;
            amt +=1.20*(unit-150); 
       }
       else{
            amt +=0.5*50;
            amt +=0.75*100;
            amt +=1.20*100;
            amt +=1.50*(unit-250);     
      }
      System.out.println((int)(amt + (surcharge*amt))); 

    }
}
