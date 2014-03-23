Feature: Web

	Scenario: Text inside home
	Given I access the url "/home"
	Then I see the header "Home"


	Scenario: Text inside help
	Given I access the url "/help"
	Then I see the header "Help"
	
	Scenario: Text inside about
	Given I access the url "/about"
	Then I see the header "About"
