##Brownie Modifiers Test
This project shows a bug in the test coverage functionality. When using function modifiers on your solidity code which call functions in a base-class, there is no way to get 100% coverage in the tests. 

###Steps to reproduce
Get the code

    git clone https://github.com/dishmop/brownie_modifiers_test.git
    cd brownie_modifiers_test
    
Install pipenv if you don't already have it

    pip install pipenv
    
Activate virtual environment

    pipenv shell
    pipenc install
    
 Run tests with coverage
 
    brownie test -C

    
 Note that not all the functions have 100% coverage. Check out the GUI:
 
    brownie gui
    
Note that the only red areas are in the modifier code. Try to change the tests in a way which does give us 100% coverage - I wasn't able to.




