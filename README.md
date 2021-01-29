## Brownie Modifiers Test
This project shows a bug in the test coverage functionality. When using function modifiers on your solidity code which call functions in a base-class, there is no way to get 100% coverage in the tests. 

### Steps to reproduce
Get the code

    git clone https://github.com/dishmop/brownie_modifiers_test.git
    cd brownie_modifiers_test
    
Install pipenv if you don't already have it

    pip install pipenv
    
Activate virtual environment

    pipenv shell
    pipenv install
    
Run tests. The first one passes and the next two fail - just because we try and make an interface to the contract
 
    brownie test

    
You can demo it in the console too. 
 
    brownie console
    
Paste these lines in one at a time

    bar = Bar.deploy({"from": accounts[0]})
    
    # Note that the test event is fired
    tx1 = bar.testEvent()
    tx1.events


    # try again and all fine
    tx2 = bar.testEvent()
    tx2.events
    
    # attempt to get an interface object
    iFoo = interface.IFoo(bar)
    
    # Now the TestEvent isn't there
    tx3 = bar.testEvent()
    tx3.events    
