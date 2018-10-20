
package javajcheckbox;

import java.awt.GridLayout;

import java.awt.event.ItemEvent;

import javax.swing.*;


public class JavaJCheckBox {

    public static void main(String[] args) {
        JFrame fr = new JFrame("JCheckBox");
        
        JCheckBox cb = new JCheckBox("Java");
        
        cb.addItemListener((ItemEvent e) -> {
           if(e.getStateChange() == 1) {
               
           }
        });
        fr.add(cb);
        
        fr.setResizable(false);
        fr.setSize(300, 100);
        fr.setLocationRelativeTo(null);
        fr.setLayout(new GridLayout(1, 2));
        fr.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        fr.setVisible(true);
    }
    
}
