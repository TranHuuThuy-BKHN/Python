
package dahinh;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;


public class DaHinh {

    public static void main(String[] args) {
       
        List<Employee> list = new ArrayList<Employee>();
        
        Employee e1 = new Employee("a");
        Employee e2 = new Employee("d");
        Employee e3 = new Employee("b");
        Employee e4 = new Employee("e");
        Employee e5 = new Employee("a");
        Employee e6 = new Employee("c");
        
        list.add(e1);
        list.add(e2);
        list.add(e3);
        list.add(e4);
        list.add(e5);
        
        for(Employee element : list) {
            System.out.println(element.name);
        }
        list.remove(e6);
        System.out.println();
        for(Employee element : list) {
            System.out.println(element.name);
        }
        
        Collections.sort(list, );
    }
    
}
