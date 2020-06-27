pragma solidity ^0.6.0;

import "github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol";

contract Credibilite {
  
   using SafeMath for uint256;
  
   mapping (address => uint256) public cred;
   bytes32[] private devoirs;


    event Transfer(bytes32 hash, address emetteur);
    
    function produireHash(string memory url)  public pure returns (bytes32) {
        return keccak256(abi.encodePacked(url));
    }

    function transfer(address destinataire, uint256 valeur) public {
        require(cred[msg.sender] > valeur, "Vous ne pouvez pas transferer toute votre credibilite");
        require(cred[destinataire] > 0, "Le destinataire doit avoir une Credibilite > 0");

        cred[msg.sender] -= valeur;
        cred[destinataire] += valeur;
    }
    
    function remettre(bytes32 dev) public returns (uint) {
        if (cred[msg.sender] > 0) 
            revert("Vous avez deja depose un devoir");
   
        if(devoirs.length == 0) {
            cred[msg.sender] = 30;
        } else {
            cred[msg.sender] = 10;
        }
        devoirs.push(dev);
        emit Transfer(dev, msg.sender);
        return devoirs.length;
    }
}