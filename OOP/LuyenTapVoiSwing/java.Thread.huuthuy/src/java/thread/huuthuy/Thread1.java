
package java.thread.huuthuy;

import java.util.logging.Level;
import java.util.logging.Logger;
import javax.swing.JOptionPane;

public class Thread1 extends Thread{
    
    private int value = 40;
    @Override
    public void run() {
         for(int i = 0; i < 100; i++) {
             try {
                 Thread.sleep(100);
             } catch (InterruptedException ex) {
                 Logger.getLogger(Thread1.class.getName()).log(Level.SEVERE, null, ex);
             }
             if(i == this.value) {
                 JOptionPane.showMessageDialog(null, "I am Thread1");
             }
         }
    }

    
    
}
