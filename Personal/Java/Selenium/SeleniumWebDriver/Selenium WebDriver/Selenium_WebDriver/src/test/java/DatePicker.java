import io.github.bonigarcia.wdm.WebDriverManager;
import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;



public class DatePicker {
    public static void main(String[] args) throws InterruptedException {
        WebDriverManager.chromedriver().setup();
        WebDriver driver = new ChromeDriver();
        driver.get(" https://formy-project.herokuapp.com/datepicker");
        WebElement dateField = driver.findElement(By.id("datepicker"));
        Thread.sleep(3000);
        dateField.sendKeys("22/08/2021");
        Thread.sleep(3000);
        dateField.sendKeys(Keys.RETURN);
        Thread.sleep(3000);
        driver.quit();

    }
}
