
package java.thread.huuthuy;

import java.util.logging.Level;
import java.util.logging.Logger;
import javax.swing.JOptionPane;

/**
 *
 * @author TranHuuThuy
 */
public class Thread2 extends Thread{
    private int value = 10;

    @Override
    public void run() {
        for(int i = 0; i < 100 ;i++) {
            try {
                Thread.sleep(100);
            } catch (InterruptedException ex) {
                Logger.getLogger(Thread2.class.getName()).log(Level.SEVERE, null, ex);
            }
            if(i == value) {
                JOptionPane.showMessageDialog(null, "I am Thread2");
            
            }
        }
    }
    
    
}
