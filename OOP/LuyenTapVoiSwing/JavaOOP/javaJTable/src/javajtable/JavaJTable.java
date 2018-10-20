
package javajtable;


import java.awt.GridLayout;

import java.awt.event.ActionEvent;

import javax.swing.*;


public class JavaJTable {

    public static void main(String[] args) {
       JFrame fr = new JFrame("JTable");
       
       String cols[] = {"Name", "Msv", "address"};
       String rows[][] = {{"Trần Hữu Thúy", "20163983", "Hưng Yên"},
                            {"Phan Thanh Phong", "20160000", "Hưng Yên"}, {"Nguyễn Thế Anh", "20160001", "Hưng Yên"}};
       
       
       JTable table = new JTable(rows, cols);
       JScrollPane sp = new JScrollPane(table);
       
       JButton button = new JButton("delete");
       
       button.addActionListener((ActionEvent e) -> {
           int rows1 = table.getSelectedRow();
          
       });
       
       fr.add(sp); 
       fr.add(button);
      
       
       
       fr.setSize(400, 400);
       fr.setLocationRelativeTo(null);
       fr.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
       fr.setLayout(new GridLayout(2, 1));
       fr.setVisible(true);
    }
    
}
