package steps;

import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;

public class Autocomplete {
    WebDriver driver = new Environment().getDriver(); //am definit o variabila noua care sa preia driverul returnat de metoda getDriver
    public Autocomplete() {};  //un constructor este ca un muncitor care creeaza obiecte pe baza clasei (tiparului descris in clasa)

    @Given("I am on \"formy project\" page")
    // atunci cand avem un simbol care are o functionalitate specifica in Java dar care vrem sa apara pe
    // ecran putem sa-l precedam de caracterul Escape(\) pentru a anunta sistemul ca trebuie sa ii ignore functionalitatea

    public void i_am_on_page() {
        driver.get("https://formy-project.herokuapp.com/autocomplete"); //am deschis pagina pe care vrem sa o testam
        driver.manage().window().maximize();
    }

    @When("I insert data in the auto-complete field")
    public void i_insert_data_in_the_auto_complete_field() throws InterruptedException {
        Thread.sleep(3000);
        WebElement autocomplete = driver.findElement(By.id("autocomplete"));
        Thread.sleep(3000);
        autocomplete.sendKeys("1555 park Blvd, Palo Alto, CA");
    }

    @Then("I am able to see the data in the web-browser")
    public void i_am_able_to_see_the_data_in_the_web_browser() {
        System.out.println("Test is completed!");
    }    //cu Ctrl+Alt+l formatam frumos codul :))
}