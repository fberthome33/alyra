pragma solidity ^0.5.7;
contract Pulsation {

 uint public battement;
 string message;

 constructor(string memory _message) public {
   message = _message;
 }

 function ajouterBattement() public view returns(string memory){
   return message;
 }
}

contract Pendule  {

 Pulsation pulse;

 function provoquerUnePulsation() public view {
   pulse.ajouterBattement();
 }
}