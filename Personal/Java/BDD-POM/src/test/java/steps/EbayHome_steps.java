package steps;
import actions.CommonActions;
import actions.EbayHome_Action;
import io.cucumber.java.af.En;
import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import java.util.List;
import java.util.Locale;

import static org.junit.Assert.fail;

public class EbayHome_steps {

    CommonActions commonActions;
    EbayHome_Action ebayHome_action;

   public EbayHome_steps(CommonActions commonActions, EbayHome_Action ebayHome_action){
       this.commonActions = commonActions;
       this.ebayHome_action = ebayHome_action;
   }

    @Given("I am on ebay homepage")
    public void i_am_on_ebay_homepage() {
        commonActions.goToURL("https://www.ebay.com");
    }

    @When("I click on Advanced Link")
    public void i_click_on_advanced_link()  {
       ebayHome_action.clickAdvancedLink();
    }

    @Then("I navigate to Advanced Search page")
    public void i_navigate_to_advanced_search_page() {
        String expURL = "https://www.ebay.com/sch/ebayadvsearch";
        String actURL = commonActions.getCurrentPageUrl();
        if (!expURL.equals(actURL))
        {
            fail("Page does not navigate to expected page");
        }
        else {
            System.out.println("test completed successfully");
        }
    }


    @When("I search for {string}")
    public void i_search_for_iphone(String str1) throws  Exception {
        ebayHome_action.searchItem(str1);
        ebayHome_action.clickSearchButton();
        Thread.sleep(1000);
    }
    @Then("I have at least {int} search items returned")
    public void i_have_at_least_search_items_returned(int count) {
        int itemCount = ebayHome_action.getSearchItemsCount();
        if (itemCount<=count){
            fail("Less than 1000 items");
        }
    }

    @When("I search for {string} in {string} category")
    public void i_search_for_in_category(String string, String string2) throws InterruptedException {
       ebayHome_action.searchItem(string);
       ebayHome_action.selectCategoryOption(string2);
       ebayHome_action.clickSearchButton();
       Thread.sleep(1000);
    }

    @When("I click on {string}")
    public void i_click_on_string(String string) throws InterruptedException {
       ebayHome_action.clickOnLinkByText(string);
       Thread.sleep(3000);
    }

    @Then("I validate that the page navigates to {string} and title contains {string}")
    public void i_validate_that_the_page_navigates_to_and_title_contains(String url, String title){
       String actURL = commonActions.getCurrentPageUrl();
       String actTitle = commonActions.getCurrentPageTitle();
        if (!(actURL.equals(url)))
        {
            fail("Page does not navigate to the expected page: " + url);
        }
        if(!actTitle.contains(title)){
            fail("Title mismatch");
        }
    }
}
