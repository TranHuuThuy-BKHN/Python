
package samsung.java.hw1;

import static java.lang.Math.cos;
import static java.lang.Math.log;
import static java.lang.Math.pow;
import static java.lang.Math.sqrt;
import java.util.Scanner;

public class Problem1 {
    
    public static double fx(double x) {
        double tu = log(x * x + 1) + sqrt(pow(x, 4) + 1);
        double mau = x * x - x + 1;
        return tu / mau;
    }
    
    public static double gxy(double x, double y) {
        return cos (2 * x) + y * y - y + 1;
    }
 
    public static void main(String[] args) {
        double x = 0.0, y = 0.0;
        Scanner sc = new Scanner(System.in);
        
        System.out.print("Nhập số thực x = ");
        x = sc.nextDouble();
        System.out.print("Nhập số thực y = ");
        y = sc.nextDouble();
        
        System.out.println("f(x) = " + fx(x));
        System.out.println("g(x, y) = " + gxy(x, y));
    }
    
}
