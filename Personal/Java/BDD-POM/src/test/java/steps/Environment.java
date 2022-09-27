package steps;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import io.cucumber.java.Before;
import io.cucumber.java.After;

public class Environment {

    private static WebDriver driver;

    @Before(order = 0)
    public void setup(){
        System.out.println("Global Hook");
        System.setProperty("webdriver.chrome.driver","/Users/gradulescu/Desktop/chromedriver");
        driver = new ChromeDriver();
    }


    @After(order=0)
    public void tearDown() throws Exception {
        System.out.println("After Hook");
        driver.quit();
        Thread.sleep(1000);
    }

    public static WebDriver getDriver(){
        return driver;
    }
}
