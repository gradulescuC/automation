import io.github.bonigarcia.wdm.WebDriverManager;
import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.openqa.selenium.WebElement;
import static org.junit.Assert.assertEquals;

import java.util.concurrent.TimeUnit;


public class FormAndMessageCheck {

    public static void main(String[] args) throws InterruptedException {
        WebDriverManager.chromedriver().setup();
        WebDriver driver = new ChromeDriver();
        driver.get("https://formy-project.herokuapp.com/form");
        driver.findElement(By.id("first-name")).sendKeys("John");
        driver.findElement(By.id("last-name")).sendKeys("Doe");
        driver.findElement(By.id("job-title")).sendKeys("QA Engineer");
        driver.findElement(By.id("radio-button-2")).click();
        driver.findElement(By.id("checkbox-2")).click();
        driver.findElement(By.cssSelector("option[value='1']")).click();
        driver.findElement(By.id("datepicker")).sendKeys("05/28/2019");
        driver.findElement(By.id("datepicker")).sendKeys(Keys.RETURN);
        // driver.findElement(By.cssSelector(".btn.btn-lg.btn-primary")).click();
        driver.findElement(By.cssSelector("a[class='btn btn-lg btn-primary']")).click();
        Thread.sleep(3000);
        // driver.findElement(By.cssSelector("div[class='alert alert-success']")).click();
        driver.manage().timeouts().implicitlyWait(5, TimeUnit.SECONDS);
        WebDriverWait wait = new WebDriverWait(driver,10);
        WebElement alert = wait.until(ExpectedConditions.visibilityOfElementLocated(By.cssSelector("div[class='alert alert-success']")));
        String alertText = alert.getText();
        assertEquals("The form was successfully submitted!",alertText);
        driver.quit();
    }



}
