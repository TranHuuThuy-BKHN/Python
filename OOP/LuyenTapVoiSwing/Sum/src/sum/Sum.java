
package sum;

import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.*;

public class Sum {

    public static void main(String[] args) {
       JFrame jr = new JFrame("Tổng hai số");
       
       JLabel l1, l2, l3;
       
       l1 = new JLabel("Số thứ nhất");
       l2 = new JLabel("Số thứ hai");
       l3 = new JLabel("Kết quả :");
       
       l1.setHorizontalAlignment(JLabel.CENTER);
       l2.setHorizontalAlignment(JLabel.CENTER);
       l3.setHorizontalAlignment(JLabel.CENTER);
       
       
       JTextField e1, e2;
       e1 = new JTextField("enter number 1");
       e2 = new JTextField("enter number 2");
       e1.setHorizontalAlignment(JTextField.CENTER);
       e2.setHorizontalAlignment(JTextField.CENTER);
       
        JButton b = new JButton("sum");
        b.setEnabled(false);
        b.addActionListener((ActionEvent e) -> {
            
            String s1 = e1.getText(), s2 = e2.getText();
            int num1 = Integer.parseInt(s1), num2 = Integer.parseInt(s2);
            int result = num1 + num2;
            l3.setText("Kết quả : " + result);
       });
        
        e1.addActionListener((ActionEvent e) -> {
          if(e1.getText().matches("\\d{1,4}") && e2.getText().matches("\\d{1,4}"))
              b.setEnabled(true);
          else  b.setEnabled(false);
       });
       
        e2.addActionListener((ActionEvent e) -> {
          if(e1.getText().matches("\\d{1,4}") && e2.getText().matches("\\d{1,4}"))
              b.setEnabled(true);
          else  b.setEnabled(false);
       });
        
        
        jr.add(l1); jr.add(e1);
        jr.add(l2); jr.add(e2);
        jr.add(l3);jr.add(b);
        
        jr.setSize(300, 150);
        jr.setResizable(false);
        jr.setLayout(new GridLayout(3, 2, 5, 5));
        jr.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        jr.setVisible(true);
    }
    
}
