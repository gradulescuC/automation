package actions;

import elements.Ebay_Home_Elements;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import steps.Environment;

import java.util.List;

public class EbayHome_Action {
    private WebDriver driver;

    Ebay_Home_Elements ebay_home_elements;

    public EbayHome_Action(Environment environment){
        this.driver = environment.getDriver();
        ebay_home_elements = new Ebay_Home_Elements(driver);
    }
        public void clickAdvancedLink()
        {
        ebay_home_elements.advancedLink.click();
    }

    public void searchItem(String searchString){
        ebay_home_elements.searchBox.sendKeys(searchString);
    }

    public void clickSearchButton(){
        ebay_home_elements.searchBox.click();
    }

    public int getSearchItemsCount(){
        String itemCount = ebay_home_elements.numItems.getText().trim();
        String itemCount2 = itemCount.replace(",","");
        int itemCountInt = Integer.parseInt(itemCount2);
        return  itemCountInt;
    }

    public void selectCategoryOption(String option){
        List<WebElement> cat  = ebay_home_elements.catOptions;
        for(WebElement x:cat){
            if(x.getText().trim().toLowerCase().equals(option.toLowerCase())){
                x.click();
                break;
            }
        }
    }

    public void clickOnLinkByText(String text){

        driver.findElement(By.linkText(text)).click();
    }

}
