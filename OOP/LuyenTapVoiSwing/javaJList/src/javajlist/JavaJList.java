

package javajlist;

import java.awt.GridLayout;
import javax.swing.DefaultListModel;
import javax.swing.JFrame;
import javax.swing.JList;
import javax.swing.JOptionPane;
import javax.swing.event.ListSelectionEvent;



public class JavaJList {

    public static void main(String[] args) {
        JFrame frame = new JFrame("JList");
        
        DefaultListModel<String> modelList = new DefaultListModel<>();
        modelList.addElement("Item 1");
        modelList.addElement("Item 2");
        modelList.addElement("Item 3");
        modelList.addElement("Item 4");
        modelList.addElement("Item 5");
        
        JList list = new JList(modelList);
        
        list.addListSelectionListener((ListSelectionEvent e) -> {
            JOptionPane.showMessageDialog(frame, "Day la " + list.getSelectedValue());
        });
        
        frame.add(list);
        
        
        frame.setSize(400, 400);
        frame.setLocationRelativeTo(null);
        frame.setLayout(new GridLayout());
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
    }
    
}
