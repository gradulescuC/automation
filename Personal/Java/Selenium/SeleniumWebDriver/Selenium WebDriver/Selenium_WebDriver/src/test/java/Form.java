import io.github.bonigarcia.wdm.WebDriverManager;
import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

public class Form {

    public static void main(String[] args) throws InterruptedException {
        WebDriverManager.chromedriver().setup();
        WebDriver driver = new ChromeDriver();
        driver.get("https://formy-project.herokuapp.com/form");
        driver.findElement(By.id("first-name")).sendKeys("John");
        Thread.sleep(3000);
        driver.findElement(By.id("last-name")).sendKeys("Doe");
        Thread.sleep(3000);
        driver.findElement(By.id("job-title")).sendKeys("QA Engineer");
        Thread.sleep(3000);
        driver.findElement(By.id("radio-button-2")).click();
        Thread.sleep(3000);
        driver.findElement(By.id("checkbox-2")).click();
        Thread.sleep(3000);
        driver.findElement(By.cssSelector("option[value='1']")).click();
        Thread.sleep(3000);
        driver.findElement(By.id("datepicker")).sendKeys("05/28/2019");
        Thread.sleep(3000);
        driver.findElement(By.id("datepicker")).sendKeys(Keys.RETURN);
        Thread.sleep(3000);
        // driver.findElement(By.cssSelector(".btn.btn-lg.btn-primary")).click();
        driver.findElement(By.cssSelector("a[class='btn btn-lg btn-primary']")).click();
        Thread.sleep(3000);
        driver.quit();
    }
}
