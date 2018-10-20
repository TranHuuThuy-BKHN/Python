
package java.huuthuy.ex1;
import java.awt.Button;
import javafx.application.Application;
import static javafx.application.Application.launch;
import javafx.scene.Scene;
import javafx.scene.layout.StackPane;
import javafx.stage.Stage;

public class Main extends Application {
    
    @Override
    public void start(Stage primaryStage) throws Exception {
        primaryStage.setTitle("Hello World");
        Button button = new Button();
        button.setName("click me");
        
        StackPane layout = new StackPane();
        
        Scene scene = new Scene(layout, 300, 300);
        primaryStage.setScene(scene);
        
        primaryStage.show();
                
                
    }
    
      
    public static void main(String[] args) {
        launch(args);
    }
    
}
