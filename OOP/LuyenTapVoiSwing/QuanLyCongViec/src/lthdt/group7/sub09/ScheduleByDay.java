package lthdt.group7.sub09;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.Date;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.Timer;
import java.util.TimerTask;
import java.util.logging.Level;
import java.util.logging.Logger;
import javazoom.jl.decoder.JavaLayerException;
import javazoom.jl.player.Player;

public class ScheduleByDay extends Thread {

    ArrayList<word> listWork = new ArrayList<>();

    public static word w = new word();

    public ScheduleByDay() {
        listWork.clear();
        for (word w : view.user.getWords()) {
            if (w.getState() == 0) {
                listWork.add(w);
            }
        }
    }

    public void clear() {
        listWork.clear();
    }

    @Override
    public void run() {
        class Task extends TimerTask {

            private Date date = null;

            @Override
            public void run() {
                Date now = new Date();
                if (!listWork.isEmpty()) {
                    Iterator itr = listWork.iterator();
                    while (itr.hasNext()) {
                        w = (word) itr.next();
                        date = w.getTimeStart();
                        if (date.getHours() == now.getHours() && date.getMinutes() == now.getMinutes()
                                && date.getDay() == now.getDay() && date.getMonth() == now.getMonth()
                                && date.getYear() == now.getYear() || true) {
                            Player player;
                            try {
                                try {
                                    notificationByWindow n = new notificationByWindow();
                                    n.start();
                                    player = new Player(new FileInputStream("audio2.mp3"));
                                    player.play(256);
                                    try {
                                        n.join(5000);
                                    } catch (InterruptedException ex) {
                                        Logger.getLogger(ScheduleByDay.class.getName()).log(Level.SEVERE, null, ex);
                                    }
                                    if (n.isAlive()) {
                                        n.interrupt();
                                    }
                                } catch (JavaLayerException ex) {
                                    Logger.getLogger(ScheduleByDay.class.getName()).log(Level.SEVERE, null, ex);
                                }
                            } catch (FileNotFoundException ex) {
                                Logger.getLogger(ScheduleByDay.class.getName()).log(Level.SEVERE, null, ex);
                            }
                            itr.remove();
                        }
                    }
                }
            }
        }
        Timer timer = new Timer();
        Task task = new Task();
        timer.scheduleAtFixedRate(task, 0, 30000);
    }
}
