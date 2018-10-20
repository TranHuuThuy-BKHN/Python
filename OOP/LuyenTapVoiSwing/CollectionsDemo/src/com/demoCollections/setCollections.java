package com.demoCollections;

import java.util.Iterator;
import java.util.LinkedHashSet;
import java.util.Set;

public class setCollections {

    public static void main(String[] args) {
//        Set<Person> setPerson = new HashSet<Person>();
        Set<Person> setPerson = new LinkedHashSet<Person>();

        Person p1 = new Person();
        p1.setAge(10);
        Person p2 = new Person();
        p2.setAge(14);
        Person p3 = new Person();
        p3.setAge(11);
        Person p4 = new Person();
        p4.setAge(11);
        Person p5 = new Person();
        p5.setAge(12);

        setPerson.add(p1);
        setPerson.add(p2);
        setPerson.add(p3);
        setPerson.add(p4);
        setPerson.add(p5);

        Iterator itr = setPerson.iterator();
        while (itr.hasNext()) {
            System.out.println(((Person) itr.next()).getAge());
        }

    }
}
