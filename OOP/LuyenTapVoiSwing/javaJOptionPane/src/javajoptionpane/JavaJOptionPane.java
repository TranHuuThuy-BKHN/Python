
package javajoptionpane;



import java.awt.event.ActionEvent;
import javax.swing.*;

public class JavaJOptionPane {

    public static void main(String[] args) {
        JFrame fr = new JFrame();
        
        JOptionPane op = new JOptionPane();
        
        JButton button = new JButton("show message");
        button.setBounds(100, 50, 150, 20);
        button.addActionListener((ActionEvent e) -> {
            int cf = JOptionPane.showConfirmDialog(fr, "Do you want exit ?", "Exit", JOptionPane.OK_CANCEL_OPTION);
            if(cf == JOptionPane.OK_OPTION) 
                System.exit(0);
           
        });
        
        fr.add(button);
        
        fr.setTitle("JoptionPane");
        fr.setSize(300, 200);
        fr.setLocationRelativeTo(null);
        fr.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        fr.setLayout(null);
        
        fr.setVisible(true);
        
    }
    
}
