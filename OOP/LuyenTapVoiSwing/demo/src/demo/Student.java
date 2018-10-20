package demo;

public class Student {

    static int count = 0;
    private String name, address;

    public Student(String name, String address) {
        this.name = name;
        this.address = address;
        count++;
    }

    public Student() {
        count++;
    }

    public void set(String name) {
        this.name = name;
    }

    public void set(String name, String address) {
        this.name = name;
        this.address = address;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        if (name.matches("(tran huu|Tran Huu)\\s.+")) {
            this.name = name;
        }
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    
    public static void talk() {
        System.out.println("hello");
    }
    
    public static void main(String[] args) {
        Student s =  new Student();
        Student s1 =  new Student();
        
        System.out.println(Student.count);
    }
}
