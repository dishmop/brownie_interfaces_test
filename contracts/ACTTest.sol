pragma solidity ^0.6.0;
import "OpenZeppelin/openzeppelin-contracts@3.2.0/contracts/access/AccessControl.sol";



contract ACTTest is AccessControl {
    EnumerableSet.UintSet docHashes;

    /**
        construction
    */
    constructor() public {
         _setupRole(DEFAULT_ADMIN_ROLE, msg.sender);
    }

    /**
        Access control interface
    */
    bytes32 public constant SECURITY_GENERATOR = keccak256("SECURITY_GENERATOR");

    modifier onlySecurityGenerator() {
        require(hasRole(SECURITY_GENERATOR, msg.sender));
        _;
    }

    function registerSecurityGenerator(address generator) public {
        grantRole(SECURITY_GENERATOR, generator);
    }


    /**
        Adding, removing and verifying document hashes. Adding and removing must be done while security is incomplete
    */
    function addDocHash(bytes32 docHash) public
        onlySecurityGenerator
    {
        EnumerableSet.add(docHashes, uint256(docHash));
    }

    function removeDocHash(bytes32 docHash) public
        onlySecurityGenerator
    {
        EnumerableSet.remove(docHashes, uint256(docHash));
    }

}


