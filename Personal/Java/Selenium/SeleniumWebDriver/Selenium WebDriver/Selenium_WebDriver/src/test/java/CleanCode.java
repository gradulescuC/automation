import io.github.bonigarcia.wdm.WebDriverManager;
import org.openqa.selenium.*;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import static org.junit.Assert.assertEquals;

import java.util.HashMap;
import java.util.Map;
import java.util.concurrent.TimeUnit;


public class CleanCode {

    public static void main(String[] args) {
        WebDriverManager.chromedriver().setup();
        WebDriver driver = new ChromeDriver();
        driver.get("https://formy-project.herokuapp.com/form");
        submitForm(driver);
        waitForAlertBanner(driver);
        assertEquals("The form was successfully submitted!",getAlertBannerText(driver));
        driver.quit();
    }
    public static void submitForm(WebDriver drv)
    {
        drv.findElement(By.id("first-name")).sendKeys("John");
        drv.findElement(By.id("last-name")).sendKeys("Doe");
        drv.findElement(By.id("job-title")).sendKeys("QA Engineer");
        drv.findElement(By.id("radio-button-2")).click();
        drv.findElement(By.id("checkbox-2")).click();
        drv.findElement(By.cssSelector("option[value='1']")).click();
        drv.findElement(By.id("datepicker")).sendKeys("05/28/2019");
        drv.findElement(By.id("datepicker")).sendKeys(Keys.RETURN);
        drv.findElement(By.cssSelector("a[class='btn btn-lg btn-primary']")).click();
    }

    public static void waitForAlertBanner(WebDriver driver)
    {
        driver.manage().timeouts().implicitlyWait(5, TimeUnit.SECONDS);
        WebDriverWait wait = new WebDriverWait(driver,20);
        WebElement alert = wait.until(ExpectedConditions.visibilityOfElementLocated((By.cssSelector("div[class='alert alert-success']"))));
    }
    public static String getAlertBannerText (WebDriver driver)
    {
        return driver.findElement(By.className("alert")).getText();
    }
}
