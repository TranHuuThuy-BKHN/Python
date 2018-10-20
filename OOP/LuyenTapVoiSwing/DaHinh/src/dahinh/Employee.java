
package dahinh;

import java.util.Date;

/**
 *
 * @author TranHuuThuy
 */
public class Employee extends Person{
    private double salary;
    
    public Employee(String name) {
        this.name = name;
    }
    
    public Employee(String name, Date birthday) {
        super(name, birthday);
    }

    
    public void setSalary(double salary) {
        if(salary > 0)
            this.salary = salary;
    }

  
    
    
}
