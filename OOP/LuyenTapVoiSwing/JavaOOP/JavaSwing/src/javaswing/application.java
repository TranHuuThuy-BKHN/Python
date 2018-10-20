
package javaswing;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.*;

public class application {

    public static void main(String[] args) {
        JFrame f = new JFrame();
        
        JButton b = new JButton();
        JTextField jt = new JTextField();
        
        
       // b.setText("click me");
        b.setIcon(new ImageIcon("AnhNen.png"));
        jt.setText("Hello Java Swing");
       
        b.setBounds(50, 50, 100, 100);
        jt.setBounds(100, 0, 200, 20);
        
        b.addActionListener((ActionEvent e) -> {
                jt.setText("Huu Thuy dep trai");
            
        });
        
        f.add(b);
        f.add(jt);
        
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        f.setSize(400, 400);
        f.setLayout(null);
        
        f.setVisible(true);
    }
    
}
