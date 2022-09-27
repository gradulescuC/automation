package elements;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;

import java.util.List;

public class Ebay_Home_Elements {

    WebDriver driver;

    @FindBy(linkText="Advanced") public WebElement advancedLink;
    @FindBy(xpath="//input[@id='gh-ac']") public WebElement searchBox;
    @FindBy(xpath="//input[@id='gh-btn']") public WebElement searchButton;
    @FindBy(xpath="//*[@id=\"mainContent\"]/div[1]/div/div[2]/div[1]/div[1]/h1/span[1]") public WebElement numItems;
    @FindBy(xpath ="//select[@id='gh-cat']/option") public List<WebElement> catOptions;

    public Ebay_Home_Elements(WebDriver driver)
    {
        this.driver = driver;
        PageFactory.initElements(driver,this);
    }
}
