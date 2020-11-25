Feature: Hello World Feature Test

  Scenario: Call Hello World from Main
    Given I have an main object initialized
     When I call run
     Then I should see "Hello World!"
