
package merchandise;

import java.util.ArrayList;

public class merchandiseManager {
    
    private ArrayList<Merchandise> list = null;
    
    public merchandiseManager(){
        list = new ArrayList<>();
    }
    
    //phương thức thêm một loại hàng hóa với các thuộc tính đã đc xác định
    public void addMerchandise(Merchandise m) {
        Merchandise merchandise = null;
        for(Merchandise mer : list) {
            if(mer.equals(m)) {
                merchandise = mer;
                break;
            }
        }
        if(merchandise != null) {
            merchandise.setAmount(m.getAmount() + merchandise.getAmount());
        }else {
            list.add(m);
        }
    }
    
    //phương thức lấy một loại hàng hóa với số lượng đã cho, trả về false nếu ko có hàng
    public boolean  removeMerchandise(String name, String code, int amount) {
        Merchandise merchandise = null;
        for(Merchandise mer : list) {
            if(mer.getName().equals(name) && mer.getCode().equals(code)) {
                merchandise = mer;
                break;
            }
        }
        if(merchandise == null || merchandise.getAmount() < amount) {
            return false;
        } else {
            merchandise.setAmount(merchandise.getAmount() - amount);
            return true;
        }
    }
    
    //phương thức lấy tất cả một lại hàng hóa
    public boolean  removeAll(String name, String code) {
        Merchandise m = null;
        for(int i =0; i < list.size(); i++) {
           m = list.get(i);
           if(m.getName().equals(name) && m.getCode().equals(code)) {
               list.remove(i);
               return true;
           }
        }
        return false;
    }
    
    //phương thức xóa tất cả hàng hóa
    public void removeAll() {
        list.clear();
    }
   
}
