
package javasparator;

import java.awt.event.ActionEvent;

import javax.swing.*;


public class JavaSparator {

    public static void main(String[] args) {
        JFrame fr = new JFrame();
        JMenuBar mb = new JMenuBar();
        
        JMenu menu = new JMenu("Menu");
        
        JMenuItem i1, i2;
        i1 = new JMenuItem("Item 1");
        i2 = new JMenuItem("Item 2");
        i1.addActionListener((ActionEvent e) -> {
            JOptionPane.showMessageDialog(menu, "Day la item 1");
        });
        JSeparator sp = new JSeparator();
        
        menu.add(i1);
        menu.add(sp);
        menu.add(i2);
        mb.add(menu);
        
        fr.setJMenuBar(mb);
           
                
        
        fr.setSize(200, 200);
        fr.setLocationRelativeTo(null);
        fr.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        fr.setLayout(null);
        fr.setVisible(true);
    }
    
}
