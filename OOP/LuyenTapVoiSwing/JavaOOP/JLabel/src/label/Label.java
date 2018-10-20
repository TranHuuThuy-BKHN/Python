
package label;

import java.awt.GridLayout;
import javax.swing.*;


public class Label {

   
    public static void main(String[] args) {
        JFrame jr = new JFrame("JLabel");
        
        JLabel jl1 = new JLabel("Hello Java Swing");
        JLabel jl2 = new JLabel("Tran Huu Thuy");
        
        jl1.setHorizontalAlignment(30);
        
        jr.add(jl1);
        jr.add(jl2);
     
        
        jr.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        jr.setLayout(new GridLayout(1, 2));
        jr.setSize(400, 400);
        jr.setVisible(true);
        
    }

   
    
}
