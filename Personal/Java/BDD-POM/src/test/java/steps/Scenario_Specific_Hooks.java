package steps;

import io.cucumber.java.After;
import io.cucumber.java.Before;
import org.openqa.selenium.WebDriver;

public class Scenario_Specific_Hooks {

    private WebDriver driver;

    public Scenario_Specific_Hooks(){}

    @Before(value = "@setCookies",order = 1)
    public void setCookies(){
        System.out.println("Scenario Specific Hook");
    } // The scenario specfic hook must come after the global hook


    @After(value = "@Test", order = 1)
    public void testAfterHook(){
        System.out.println("Test  After Hook");
    }
}
