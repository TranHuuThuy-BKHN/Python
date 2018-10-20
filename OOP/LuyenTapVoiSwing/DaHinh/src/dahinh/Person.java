/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package dahinh;
import java.util.Date;
import javax.swing.JOptionPane;

/**
 *
 * @author TranHuuThuy
 */
public class Person {
   protected String name;
   
   protected Date birthday;

   public Person() {
       
   }
   
    public Person(String name, Object birthday) {
        this.name = name;
        Object obj = null;
        
        if(obj instanceof Person) {
            this.birthday = (Date) birthday;
        }
    }

    public void setName(String name) {
        if(name != null && name.length() > 0) {
            this.name = name;
        }
    }

    public void setBirthday(Date birthday) {
        this.birthday = birthday;
    }

    public  void talk(Object p) {
        if(p instanceof Person) {
            JOptionPane.showMessageDialog(null, "I am a person");
        }
        else{
             JOptionPane.showMessageDialog(null, "I am an employee");
        }
    }
    
    public static void main(String[] args) {
        Person p = new Person("Tran Huu Thuy", new Date());
       
        
        System.out.println();
    }
   
}
