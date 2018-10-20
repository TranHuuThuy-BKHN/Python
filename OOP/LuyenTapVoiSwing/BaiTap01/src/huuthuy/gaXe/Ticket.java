
package huuthuy.gaXe;

import java.util.Date;

public abstract  class Ticket {
    protected Date issuedDate;
    protected int value;
    
    public Ticket(int value, Date issuedDate) {
        this.value = value;
        this.issuedDate = issuedDate;
    }
    
    public int getValue() {
        return this.value;
    }
    
    public void setOrigin(Gate gate) {
        
    }
    
    public Gate getOrigin() {
        return null;
    }
    
    public void ajustValue(int value) {
        
    }
    
    public boolean isValid() {
        return false;
    }
}
