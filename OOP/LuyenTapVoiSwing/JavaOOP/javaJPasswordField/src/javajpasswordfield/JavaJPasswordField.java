
package javajpasswordfield;

import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.*;

public class JavaJPasswordField {

    public static void main(String[] args) {
        
        JFrame fr = new JFrame("JPasswordField");
        
        JLabel l = new JLabel("password");
        l.setHorizontalAlignment(JLabel.CENTER);
        
        JPasswordField pw = new JPasswordField();
        
        pw.setText("enter your password");
        pw.setHorizontalAlignment(JPasswordField.CENTER);
        
        JButton b = new JButton("display");
        b.addActionListener((ActionEvent e) -> {
            JOptionPane.showMessageDialog(pw, pw.getPassword());
        });
        
        fr.add(l); fr.add(pw);
        fr.add(b);
        
        fr.setLocationRelativeTo(null);
        fr.setSize(250, 75);
        fr.setLayout(new GridLayout(2, 2));
        fr.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        fr.setResizable(false);
        fr.setVisible(true);
        
    }
    
}
