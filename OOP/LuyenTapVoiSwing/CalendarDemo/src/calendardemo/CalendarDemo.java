
package calendardemo;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import javazoom.jl.decoder.JavaLayerException;
import javazoom.jl.player.Player;



/**
 *
 * @author TranHuuThuy
 */
public class CalendarDemo {

    public static void main(String[] args) throws FileNotFoundException, JavaLayerException {
        Player player = new Player(new FileInputStream("Test01.mp3"));
        player.play();
    }
    
}
