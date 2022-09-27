package actions;

import com.github.dockerjava.core.dockerfile.DockerfileStatement;
import elements.EbayAdvancedSearch_Elements;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import steps.EbayAdvancedSearch_steps;
import steps.Environment;

public class EbayAdvancedSearch_Action {
    private WebDriver driver;
    EbayAdvancedSearch_Elements ebayAdvancedSearch_elements;

    public EbayAdvancedSearch_Action(Environment environment){
        this.driver = environment.getDriver();
        ebayAdvancedSearch_elements = new EbayAdvancedSearch_Elements((driver));
    }

    public void clickOnEbayLogo(){
        ebayAdvancedSearch_elements.ebayLogo.click();
    }

    public void enterSearchString(String string){ebayAdvancedSearch_elements.searchString.sendKeys(string);}

    public void enterExcludeString(String string){
        ebayAdvancedSearch_elements.excludeString.sendKeys(string);
    }

    public void enterMinPrice(String string){
        ebayAdvancedSearch_elements.minPrice.sendKeys(string);
    }
    public void enterMaxPrice(String string){
        ebayAdvancedSearch_elements.maxPrice.sendKeys(string);
    }

    public void clickOnSearchButton(){
        ebayAdvancedSearch_elements.searchButton.click();
    }
}
