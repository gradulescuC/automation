package actions;

import org.openqa.selenium.WebDriver;
import steps.Environment;

public class CommonActions {
    private WebDriver driver;

    Environment environment;

    public CommonActions(Environment environment){
        this.driver = environment.getDriver();
    }

    public void goToURL(String url){
        driver.get(url);
    }

    public String getCurrentPageUrl()
    {
        return driver.getCurrentUrl();
    }

    public String getCurrentPageTitle()
    {
        return driver.getTitle();
    }

    public void quitWebDriver()
    {
        driver.quit();
    }
}
