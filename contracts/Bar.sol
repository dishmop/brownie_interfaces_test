// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

import "interfaces/IFoo.sol";

contract Bar is IFoo {
    event TestEvent(uint256 value);

    function randomFunction() external view override returns (bool) {return true;}

    function testEvent() public {
        emit TestEvent(99);
    }

}
