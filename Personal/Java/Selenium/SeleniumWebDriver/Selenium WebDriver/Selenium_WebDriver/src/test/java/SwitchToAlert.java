import io.github.bonigarcia.wdm.WebDriverManager;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.Alert;

public class SwitchToAlert {
    public static void main(String[] args) throws InterruptedException {
        WebDriverManager.chromedriver().setup();
        WebDriver driver = new ChromeDriver();
        driver.get("https://formy-project.herokuapp.com/switch-window");
        Thread.sleep(5000);
        WebElement alertButton = driver.findElement(By.id("alert-button"));
        Thread.sleep(5000);
        alertButton.click();
        Thread.sleep(5000);
        Alert alert = driver.switchTo().alert();
        Thread.sleep(3000);
        alert.dismiss();
        Thread.sleep(5000);
        driver.close();

    }
}
