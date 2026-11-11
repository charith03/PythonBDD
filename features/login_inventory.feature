Feature: Complete Purchase Flow
    Scenario: Verify Inventory and Complete Purchase
        Given I login to SauceDemo and verify inventory page
        When I verify inventory details
        And I add random products to cart
        And I enter checkout information
        Then order should be placed successfully
        And I navigate back to inventory page