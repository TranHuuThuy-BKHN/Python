/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package simpledateformatdemo;

import java.text.SimpleDateFormat;
import java.util.Date;

/**
 *
 * @author TranHuuThuy
 */
public class SimpleDateFormatDemo {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
       SimpleDateFormat s = new SimpleDateFormat("hh:mm");
        System.out.println(s.format(new Date()));
    }
    
}
