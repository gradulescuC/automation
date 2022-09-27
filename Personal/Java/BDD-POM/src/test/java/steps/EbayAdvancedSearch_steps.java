package steps;

import actions.CommonActions;
import actions.EbayAdvancedSearch_Action;
import io.cucumber.datatable.DataTable;
import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import org.openqa.selenium.By;

import static org.junit.Assert.fail;

public class EbayAdvancedSearch_steps {
    CommonActions commonActions;
    EbayAdvancedSearch_Action ebayAdvancedSearch_action;

    public EbayAdvancedSearch_steps(CommonActions commonActions,EbayAdvancedSearch_Action ebayAdvancedSearch_action){
        this.commonActions = commonActions;
        this.ebayAdvancedSearch_action = ebayAdvancedSearch_action;
    }

    @Given("I am on Ebay Advanced Search Page")
    public void i_am_on_ebay_advanced_search_page() {
        // driver.get("https://www.ebay.com/sch/ebayadvsearch");
        commonActions.goToURL("https://www.ebay.com/sch/ebayadvsearch");
    }

    @When("I click on Ebay Logo")
    public void i_click_on_ebay_logo() {
       // driver.findElement(By.xpath("//a[@id='gh-la']")).click();
        ebayAdvancedSearch_action.clickOnEbayLogo();
    }

    @Then("I am navigated to Ebay homepage")
    public void i_am_navigated_to_ebay_homepage() {
        String expURL = "https://www.ebay.com/";
        String actualURL = commonActions.getCurrentPageUrl();
        System.out.println(actualURL);
        if(!expURL.equals(actualURL)){
            fail("Logo does not navigate to homepage");
        }
    }

    @When("I advance search an item")
    public void i_advance_search_an_item(DataTable dataTable) throws InterruptedException {
        ebayAdvancedSearch_action.enterSearchString(dataTable.cell(1,0));
        ebayAdvancedSearch_action.enterExcludeString(dataTable.cell(1,1));
        ebayAdvancedSearch_action.enterMinPrice(dataTable.cell(1,2));
        ebayAdvancedSearch_action.enterMaxPrice(dataTable.cell(1,3));
        ebayAdvancedSearch_action.clickOnSearchButton();
        Thread.sleep(3000);
    }


}
