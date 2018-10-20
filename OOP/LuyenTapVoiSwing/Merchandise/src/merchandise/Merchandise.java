
package merchandise;

public class Merchandise {
    
    private   String name, code;
    private int amount, cost;
    
    public Merchandise() {
        
    }
    
    public  Merchandise(String name,String code, int amount, int cost) {
        this.name = name;
        this.code = code;
        this.amount = amount;
        this.cost = cost;
    }
    
    //so sánh hai hàng hoa giống nhau
    public boolean equals(Merchandise m) {
        return this.getName().equals(m.getName()) && this.getCode().equals(m.getCode());
    }
    
    public String getName() {
        return name;
    }

    public void setName(String name) {
        if(name != null && name.length() > 0)
            this.name = name;
    }

    public int getAmount() {
        return amount;
    }

    public void setAmount(int amount) {
        if(amount >= 0)
           this.amount = amount;
    }

    public int getCost() {
        return cost;
    }

    public void setCost(int cost) {
        if(cost > 0)
           this.cost = cost;
    }

    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        if(code != null && code.length() > 0)
            this.code = code;
    }
}
