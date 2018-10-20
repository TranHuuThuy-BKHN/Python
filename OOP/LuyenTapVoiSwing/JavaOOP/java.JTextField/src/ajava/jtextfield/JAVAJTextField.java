
package ajava.jtextfield;

import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import javax.swing.*;


public class JAVAJTextField {

    public static void main(String[] args) {
       JFrame fr = new JFrame("JTextField");
       
       JLabel l1 = new JLabel("username");
       JLabel l2 = new JLabel("password");
       
       
       JTextField e1, e2;
       e1 = new JTextField("enter username");
       e2 = new JTextField("enter password");
       
       fr.add(l1);
       fr.add(e1);
       fr.add(l2);
       fr.add(e2);
       
       e1.addActionListener((ActionEvent e) -> {
           System.out.println(e1.getText());
       });
       
       fr.setSize(300, 100);
       fr.setLayout(new GridLayout(2, 2, 5, 5));
       fr.setResizable(false);
       fr.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
       fr.setVisible(true);
       
    }
    
}
