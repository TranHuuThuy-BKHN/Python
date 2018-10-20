
package samsung.java.week2.square;

public class Square {
    
    private float height, weight, p, s;
    
    public Square() {
        
    }
    
    public Square(float height, float weight) {
        this.height = height;
        this.weight = weight;
        this.s = this.height * this.weight;
        this.p = this.height * 2 + this.weight * 2;
    }
    
    public void inPutEdges() {
        System.out.println("Chiều dài : " + this.weight);
        System.out.println("Chiều rộng : " + this.height);
    }
    
    public void inPutP() {
        System.out.println("Chu vi hình chữ nhật : " + this.p);
    }
    
    public void inPutS() {
        System.out.println("Diện tích hình chữ nhật : " + this.s);
    }
    
    public void inPut() {
        this.inPutEdges();
        this.inPutP();
        this.inPutS();
    }
}
