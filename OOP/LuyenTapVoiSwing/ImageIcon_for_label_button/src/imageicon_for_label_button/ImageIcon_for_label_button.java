
package imageicon_for_label_button;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.image.BufferedImage;
import java.io.File;
import javax.imageio.ImageIO;
import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;

public class ImageIcon_for_label_button extends JFrame implements ActionListener {
    private JLabel label;
    private JButton button;
    
    public ImageIcon_for_label_button() {
        setSize(300, 300); 
        label = new JLabel();
        label.setSize(200, 200);
        button = new JButton();
        button.setBounds(100, 100, 20, 20);
        try {
           BufferedImage image = ImageIO.read(new File("huy.png"));
           ImageIcon icon = new ImageIcon(image.getScaledInstance(10, 10, 0));
           label.setIcon(icon);
           button.setIcon(icon);
        } catch (Exception e) {
        }
        
        button.addActionListener(this);
       //add(label);
       add(button);
        setLayout(null);
        setLocationRelativeTo(null);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
       
    }
    
    public static void main(String[] args) {
        ImageIcon_for_label_button im = new ImageIcon_for_label_button();
        im.setVisible(true);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        JButton b = (JButton)e.getSource();
        if(b == button) {
            System.exit(0);
        }
    }
    
}
