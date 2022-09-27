import io.github.bonigarcia.wdm.WebDriverManager;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.interactions.Actions;

public class ScrollToElement {

    public static void main(String[] args) throws InterruptedException {

        WebDriverManager.chromedriver().setup();
        WebDriver driver = new ChromeDriver();
        driver.get("https://formy-project.herokuapp.com/scroll");
        Thread.sleep(3000);
        WebElement name = driver.findElement(By.id("name"));
        Actions actions = new Actions(driver);
        Thread.sleep(3000);
        actions.moveToElement(name);
        Thread.sleep(3000);
        name.sendKeys("Meaghan Lewis");
        WebElement date = driver.findElement(By.id("date"));
        Thread.sleep(3000);
        date.sendKeys("01/01/2020");
        Thread.sleep(3000);
        driver.quit();

    }
}
