
package javascrollbar;



import java.awt.event.AdjustmentEvent;

import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JScrollBar;


public class JavaScrollbar {

    public static void main(String[] args) {
        JFrame frame = new JFrame("JList");
        JLabel lable = new JLabel();
        lable.setBounds(150, 150, 40, 40);
        
        JScrollBar scroll = new JScrollBar();
        scroll.setBounds(100, 100, 20, 200);
        scroll.addAdjustmentListener((AdjustmentEvent e) -> {
        String s = "" + scroll.getValue();
           lable.setText(s);
        });
        
        frame.add(scroll);
        frame.add(lable);
        
        
        frame.setSize(400, 400);
        frame.setLocationRelativeTo(null);
        frame.setLayout(null);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
    }
    
}
