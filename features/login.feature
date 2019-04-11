Feature: Login

  Scenario: Login
    Given I open login page
    When I login with "allmailnamesoccupied@gmail.com" and "!Q2w3e4r"
    Then I am on main page
