import io.github.bonigarcia.wdm.WebDriverManager;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

public class DragAndDrop {

    public static void main(String[] args) throws InterruptedException {

        WebDriverManager.chromedriver().setup();
        WebDriver driver = new ChromeDriver();
        driver.get("https://formy-project.herokuapp.com/");
        WebElement components = driver.findElement(By.id("navbarDropdownMenuLink"));
        components.click();
        WebElement dropdown = driver.findElement(By.xpath("//*[contains(text(), 'Drag and Drop')]"));
        dropdown.click();
        Thread.sleep(3000);
        driver.quit();
    }
}

    /*JavascriptExecutor executor = (JavascriptExecutor) driver;
    executor.executeScript("arguments[0].scrollIntoView(true);", element1);
    executor.executeScript("arguments[0].click();", element1);*/