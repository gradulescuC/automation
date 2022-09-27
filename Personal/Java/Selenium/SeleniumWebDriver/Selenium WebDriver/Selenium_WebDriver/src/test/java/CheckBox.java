import io.github.bonigarcia.wdm.WebDriverManager;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;


public class CheckBox {

    public static void main(String[] args) {
        WebDriverManager.chromedriver().setup();
        WebDriver driver = new ChromeDriver();
        driver.get("https://formy-project.herokuapp.com/checkbox");
        WebElement checkbox1 = driver.findElement(By.id("checkbox-1"));
        checkbox1.click();
        WebElement checkbox2 = driver.findElement(By.id("checkbox-2"));
        checkbox2.click();
        WebElement checkbox3 = driver.findElement(By.id("checkbox-3"));
        checkbox3.click();
    }
}
