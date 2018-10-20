
package javajtextarea;

import java.awt.GridLayout;
import javax.swing.*;

public class JavaJTextArea {

    public static void main(String[] args) {
        JFrame fr = new JFrame("JTextArea");
        
        JTextArea ta = new JTextArea(1, 2);
        
        fr.add(ta);
        
        fr.setResizable(false);
        fr.setSize(300, 300);
        fr.setLayout(new GridLayout(2, 3));
        fr.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        fr.setVisible(true);
    }
    
}
