import io.github.bonigarcia.wdm.WebDriverManager;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

public class Autocomplete {

    public static void main(String[] args) throws InterruptedException {
        WebDriverManager.chromedriver().setup();
        WebDriver driver = new ChromeDriver();
        driver.get("https://formy-project.herokuapp.com/autocomplete");
        Thread.sleep(3000);
        WebElement autocomplete = driver.findElement(By.id("autocomplete"));
        Thread.sleep(3000);
        autocomplete.sendKeys("1555 park Blvd, Palo Alto, CA");
        Thread.sleep(3000);
        WebElement autocompleteResult = driver.findElement(By.className("pac-item"));
        Thread.sleep(3000);
        autocompleteResult.click();
        Thread.sleep(3000);
        // driver.quit();

    }
}