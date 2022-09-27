import io.github.bonigarcia.wdm.WebDriverManager;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
public class GoogleSearch {

    public static void main(String[] args) throws InterruptedException {
        WebDriverManager.chromedriver().setup();
        WebDriver driver = new ChromeDriver();
        driver.get("http://www.google.com");
        Thread.sleep(2000);
        WebElement el = driver.findElement(By.id("L2AGLb"));
        Thread.sleep(2000);
        el.click();
        Thread.sleep(2000);
        WebElement element = driver.findElement(By.name("q"));
        Thread.sleep(2000);
        element.sendKeys("Cheese!");
        Thread.sleep(2000);
        element.submit();
        Thread.sleep(2000);
        driver.quit();
    }
}