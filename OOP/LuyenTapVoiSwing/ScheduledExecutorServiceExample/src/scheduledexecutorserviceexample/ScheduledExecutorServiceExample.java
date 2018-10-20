/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package scheduledexecutorserviceexample;

import java.util.concurrent.Callable;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.Executors;
import java.util.concurrent.ScheduledExecutorService;
import java.util.concurrent.ScheduledFuture;
import java.util.concurrent.TimeUnit;

/**
 *
 * @author TranHuuThuy
 */
public class ScheduledExecutorServiceExample {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) throws InterruptedException, ExecutionException {
        ScheduledExecutorService scheduledExecutorService
                = Executors.newScheduledThreadPool(5);

        ScheduledFuture scheduledFuture
                = scheduledExecutorService.schedule(new Callable() {
                    public Object call() throws Exception {
                        System.out.println("Executed!");
                        return "Called!";
                    }
                },
                        5,
                        TimeUnit.SECONDS);

        System.out.println("result = " + scheduledFuture.get());

        scheduledExecutorService.shutdown();

    }

}
