package com.huuthuy.regex;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Demo {

    public static void main(String[] args) {
        final String  text = "Hoa yêu Thúy      adbhd Hoa yêu Thúysbasas     Hoa yêu Thúy";
        String regex = "Hoa yêu Thúy";
        Pattern pattern = Pattern.compile(regex);
        Matcher macher = pattern.matcher(text);
        while(macher.find()) {
            System.out.println("start : " + macher.start());
            System.out.println("end : " + macher.end());
            System.out.println("group : " + macher.group());
            System.out.println();
        }
    }

}
