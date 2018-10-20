
package javajradiobutton;

import com.sun.glass.events.KeyEvent;
import java.awt.FlowLayout;
import java.awt.event.ActionEvent;
import javax.swing.*;

public class JavaJRadioButton {

    public static void main(String[] args) {
        JFrame fr = new JFrame("JradioButton");
        
        JRadioButton r1, r2;
        r1 = new JRadioButton("java", true);
        r2 = new JRadioButton("C++");
        
        r1.addActionListener((ActionEvent e) -> {
            JOptionPane.showMessageDialog(fr, "This is Java");
        });
        r1.setMnemonic(KeyEvent.VK_C);
        
        r2.addActionListener((ActionEvent e) -> {
            JOptionPane.showMessageDialog(fr, "This is C++");
        });
        ButtonGroup bg = new ButtonGroup();
        bg.add(r1);
        bg.add(r2);
        
        
        fr.add(r1);
        fr.add(r2);
        
        fr.setSize(200, 200);
        fr.setResizable(false);
        fr.setLocationRelativeTo(null);
        fr.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        fr.setLayout(new FlowLayout());
        fr.setVisible(true);
    }
    
}
