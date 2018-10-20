
package javajtable;

import com.sun.javafx.font.t2k.T2KFactory;
import java.awt.GridLayout;
import javax.swing.*;
import javax.swing.event.TableModelEvent;
import javax.swing.event.TableModelListener;
import javax.swing.table.DefaultTableModel;
import javax.swing.table.TableColumn;
import javax.swing.table.TableModel;
import jdk.internal.dynalink.DefaultBootstrapper;

public class JavaJTable {

    
    public static void main(String[] args) {
        
        JFrame fr = new JFrame("JTable");
        String rows[][] = {{"Tran Huu Thuy", "20163983"},{"Phan Thanh Phong", "20160000"}};
        String cols[] = {"Name", "Msv"};
        
        JTable table = new JTable(rows, cols);
        JScrollPane sp = new JScrollPane(table);
        
        
        
        
        fr.add(sp);
        DefaultTableModel model = (DefaultTableModel)table.getModel();
        model.removeRow(0);
        
        
     
        
        fr.setSize(300, 300);
        fr.setLocationRelativeTo(null);
        fr.setLayout(new GridLayout());
        fr.setResizable(false);
        fr.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        fr.setVisible(true);
    }
    
}
