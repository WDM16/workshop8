Feature: Test Calculator Functionality 

Scenario:Addition
Given Calculator program is running 
When I input "2" and "1" to calculator
Then I get result "3"

Scenario:Subtraction
Given Calculator program has executed 
When I provide "4" and "2" to the calculator
Then I get the result "2"

Scenario:Multiplication
Given Calculator program has been executed 
When I provide "4" and "2" to a calculator
Then I get a result "8"

Scenario:Division
Given Calculator program is executing 
When I provide "4" and "2" to the calculator program
Then I get the resulting factor "2"

Scenario:DivisionByZero
Given Calculator program has executed 
When I provide "4" and "0" to the calculator
Then I get the result "0"