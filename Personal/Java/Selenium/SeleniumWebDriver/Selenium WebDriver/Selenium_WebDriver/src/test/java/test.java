import io.github.bonigarcia.wdm.WebDriverManager;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.interactions.Actions;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

public class test {

    public static void main(String[] args) throws InterruptedException {
        WebDriverManager.chromedriver().setup();
        WebDriver driver = new ChromeDriver();
        driver.get("https://politrip.com/account/sign-up");
        Thread.sleep(1000);
        driver.findElement(By.id("cookiescript_accept")).click();
        driver.manage().window().maximize();
        WebElement fbButton  = driver.findElement(By.xpath("//*[@id=\"sign-up-form-container\"]/app-social-media-account"));
        System.out.println(fbButton.isEnabled());
        System.out.println(fbButton.isDisplayed());
        Actions actions = new Actions(driver);
        actions.moveToElement(fbButton,500,50).build().perform();
        Thread.sleep(3000);
        driver.quit();
    }
}
