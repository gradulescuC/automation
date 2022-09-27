import io.github.bonigarcia.wdm.WebDriverManager;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.WebElement;


public class FileUpload {

    public static void main(String[] args) throws InterruptedException {
        WebDriverManager.chromedriver().setup();
        WebDriver driver = new ChromeDriver();
        driver.get("https://formy-project.herokuapp.com/fileupload");
        Thread.sleep(3000);
        WebElement fileUpload = driver.findElement(By.id("file-upload-field"));
        Thread.sleep(3000);
        fileUpload.sendKeys("file-to-upload.png");
        WebElement resetButton = driver.findElement(By.cssSelector("button[class='btn btn-warning btn-reset']"));
        Thread.sleep(3000);
        resetButton.click();
        driver.quit();
    }
}
