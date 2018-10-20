
import java.io.File;
import javax.swing.JFileChooser;
import javax.swing.JOptionPane;

public class JFilechooserDemo extends javax.swing.JFrame {

    private static final int OPEN = 0;
    private static final int SAVE = 1;
    private static int select = 0;

    public JFilechooserDemo() {
        initComponents();
    }

    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        jMenuItem3 = new javax.swing.JMenuItem();
        jScrollPane1 = new javax.swing.JScrollPane();
        jTextArea1 = new javax.swing.JTextArea();
        jMenuBar1 = new javax.swing.JMenuBar();
        mFile = new javax.swing.JMenu();
        mNew = new javax.swing.JMenuItem();
        open = new javax.swing.JMenuItem();
        save = new javax.swing.JMenuItem();
        jSeparator1 = new javax.swing.JPopupMenu.Separator();
        exit = new javax.swing.JMenuItem();
        edit = new javax.swing.JMenu();

        jMenuItem3.setText("jMenuItem3");

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);
        setTitle("Notepad");

        jTextArea1.setColumns(20);
        jTextArea1.setRows(5);
        jScrollPane1.setViewportView(jTextArea1);

        mFile.setText("File");
        mFile.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                mFileActionPerformed(evt);
            }
        });

        mNew.setAccelerator(javax.swing.KeyStroke.getKeyStroke(java.awt.event.KeyEvent.VK_N, java.awt.event.InputEvent.CTRL_MASK));
        mNew.setText("New");
        mNew.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                mNewActionPerformed(evt);
            }
        });
        mFile.add(mNew);

        open.setAccelerator(javax.swing.KeyStroke.getKeyStroke(java.awt.event.KeyEvent.VK_O, java.awt.event.InputEvent.CTRL_MASK));
        open.setText("Open...");
        open.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                openActionPerformed(evt);
            }
        });
        mFile.add(open);

        save.setAccelerator(javax.swing.KeyStroke.getKeyStroke(java.awt.event.KeyEvent.VK_S, java.awt.event.InputEvent.CTRL_MASK));
        save.setText("Save");
        save.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                saveActionPerformed(evt);
            }
        });
        mFile.add(save);
        mFile.add(jSeparator1);

        exit.setText("Exit");
        exit.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                exitActionPerformed(evt);
            }
        });
        mFile.add(exit);

        jMenuBar1.add(mFile);

        edit.setText("Edit");
        jMenuBar1.add(edit);

        setJMenuBar(jMenuBar1);

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addComponent(jScrollPane1, javax.swing.GroupLayout.DEFAULT_SIZE, 408, Short.MAX_VALUE)
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addComponent(jScrollPane1, javax.swing.GroupLayout.DEFAULT_SIZE, 206, Short.MAX_VALUE)
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void mNewActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_mNewActionPerformed
        // TODO add your handling code here:
    }//GEN-LAST:event_mNewActionPerformed

    private void mFileActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_mFileActionPerformed
        // TODO add your handling code here:
    }//GEN-LAST:event_mFileActionPerformed

    private void exitActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_exitActionPerformed
        System.exit(0);
    }//GEN-LAST:event_exitActionPerformed

    private void openActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_openActionPerformed
        JFilechooserDemo.select = OPEN;
        osFile();
    }//GEN-LAST:event_openActionPerformed

    private void saveActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_saveActionPerformed
        JFilechooserDemo.select = SAVE;
        osFile();
    }//GEN-LAST:event_saveActionPerformed

    public void osFile() {
        JFileChooser fileChooer = new JFileChooser();
        int choose = 0;
        switch (JFilechooserDemo.select) {
            case OPEN:
                choose = fileChooer.showOpenDialog(null);
                break;
            case SAVE:
                choose = fileChooer.showSaveDialog(null);
                break;
        }
        if (choose == JFileChooser.APPROVE_OPTION) {
            File file = fileChooer.getSelectedFile();
            switch (JFilechooserDemo.select) {
                case OPEN:
                    JOptionPane.showMessageDialog(null, "Open " + file.getPath());
                    break;
                case SAVE:
                    break;
            }
        }
    }

    public static void main(String args[]) {

        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new JFilechooserDemo().setVisible(true);
            }
        });
    }

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JMenu edit;
    private javax.swing.JMenuItem exit;
    private javax.swing.JMenuBar jMenuBar1;
    private javax.swing.JMenuItem jMenuItem3;
    private javax.swing.JScrollPane jScrollPane1;
    private javax.swing.JPopupMenu.Separator jSeparator1;
    private javax.swing.JTextArea jTextArea1;
    private javax.swing.JMenu mFile;
    private javax.swing.JMenuItem mNew;
    private javax.swing.JMenuItem open;
    private javax.swing.JMenuItem save;
    // End of variables declaration//GEN-END:variables
}
