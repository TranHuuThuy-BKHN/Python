/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package huuthuy.gaXe;

public class Line {
    public int getFare(int distance) {
        if(distance <= 0) return -1;
        else if(distance <= 6)
            return 9_000;
        else {
            distance = distance - 6;
            if(distance % 2 == 0) 
                return 9_000 + (distance / 2) * 2000;
            return  9_000 + (distance / 2 + 1)* 2000;
        }
    }
   
}
