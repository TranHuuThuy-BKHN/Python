package lthdt.group7.sub09;

import java.util.ArrayList;
import java.util.Calendar;
import java.util.Date;

public class User {

    private String name = "Trần Hữu Thúy", username;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    //danh sach cac cong viec da duoc sap xep theo thoi gian bat dau cua user, se duoc doc tren database
    private ArrayList<word> words = new ArrayList<>();

    //danh sach cac cong viec se duoc hien thi len man hinh voi mot ngay da xac dinh
    private ArrayList<word> wordView = new ArrayList();

    public ArrayList<word> getWords() {
        return words;
    }

    public ArrayList<word> getWordView() {
        return wordView;
    }

    //doc co so du lieu toan bo cong viec cua user
    public void readDataBase() {

    }

    //doc wordView voi ngay(dd/MM/yyyy) hien thi tren man hinh, nen thuc hien sau phuong thuc nay readDatabase, nhung tuy thoi
    public void readWordView(Date date) {
        wordView.clear();
        Calendar calendar = Calendar.getInstance();
        calendar.setTime(view.cal.getTime());
        calendar.add(Calendar.DAY_OF_MONTH, 1);
        //ngay hien tai tren man hinh la dd/MM/yyyy 00:00
        for(word i : words) {
           if(i.getTimeStart().compareTo(view.cal.getTime()) > 0 && i.getTimeStart().compareTo(calendar.getTime()) < 0){
               wordView.add(i);
           }
        }
    }

    //ham cat nhat co so du lieu moi khi them, sua, xoa 1 cong viec nao do
    //phai sap xep cong viec theo thoi gian bat dau trong database cho thuan tien
    public void insertDataBase() {

    }
}
