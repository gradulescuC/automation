import io.github.bonigarcia.wdm.WebDriverManager;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

public class CheckBoxes {
    public static void main(String[] args) {

        WebDriverManager.chromedriver().setup();
        WebDriver driver = new ChromeDriver();
        driver.get("https://formy-project.herokuapp.com/checkbox");
        WebElement checkbox1 = driver.findElement(By.id("checkbox-1"));
        checkbox1.click();
        WebElement checkbox2 = driver.findElement(By.cssSelector("input[value='checkbox-2']"));
        checkbox2.click();
        WebElement checkbox3 = driver.findElement(By.xpath("/html/body/div/div[3]/div/div/input"));
        checkbox3.click();
    }


}
