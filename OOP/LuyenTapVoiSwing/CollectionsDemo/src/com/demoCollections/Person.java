package com.demoCollections;

public class Person {

    private String name = "Trần Hữu Thúy", address = "Hưng Yên-Trung Nghĩa";
    private int age = 1;

    public Person() {
        this.name = "Trần Hữu Thúy";
        address = "Hưng Yên-Trung Nghĩa";
        age = 1;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        if (name.matches("(Trần|trần)\\s.+")) {
            this.name = name;
        }
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        if (address.matches("Hưng Yên-.+")) {
            this.address = address;
        }
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        if (age > 0) {
            this.age = age;
        }
    }

    @Override
    public boolean equals(Object obj) {
        return this.age == ((Person) obj).getAge();
    }

    @Override
    public int hashCode() {
        return this.age;
    }

}
