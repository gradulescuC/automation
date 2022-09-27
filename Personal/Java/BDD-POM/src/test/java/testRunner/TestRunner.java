// the name of the file can be different, but by convention it is called TestRunner.

package testRunner;

import io.cucumber.junit.Cucumber;
import io.cucumber.junit.CucumberOptions;
import org.junit.runner.RunWith;

@RunWith(Cucumber.class) // TestRunner will run with the cucumber class
@CucumberOptions(
        features = {"features"}, // Specifies where to find the feature files
        glue = {"steps"}, // Specifies where to find the step definitions
        // plugin = {"pretty","html:Reports.html"} // format for the test report in HTML Format
              plugin = {"pretty","html:Reports/cucumber-reports.html"}, // Same as the above, only that it is specified the folder name where the report will be generated
                                                        // If the folder does not exist, it will be created automatically
         // plugin = {"pretty", "json:Reports/cucumber-reports.json" } // format for the test report in json format
          // plugin = { "pretty", "junit:Reports/cucumber-reports.java" } // format for the test report in junit format
       // there can be three formats: HTML, json and junit.
        dryRun = false, // true = will not run code but it will find out if there are scenarios or
                                    // steps that do not have step definitions
        monochrome = true // removes redundant information from the console result
         ,tags = "@P1" // running all the feature files having that specific tag
        // name = "link" // runs the tests having that specific keyword in the scenario name
)

public class TestRunner {}

