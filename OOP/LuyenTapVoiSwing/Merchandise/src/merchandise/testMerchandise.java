
package merchandise;

public class testMerchandise {
    public static void main(String[] args) {
        
        merchandiseManager manager = new merchandiseManager();
        
        Merchandise m = new Merchandise("Coca Cola", "20163983", 10, 10_000);
        
        manager.addMerchandise(m);
        boolean value = manager.removeMerchandise(m.getName(), m.getCode(), 9);
        System.out.println(value);
        System.out.println(m.getAmount());
    }
}
