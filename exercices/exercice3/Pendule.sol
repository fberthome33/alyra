pragma solidity ^0.6.0;
pragma experimental ABIEncoderV2;

import "./Pulsation.sol";


contract Pendule {

 string[] public balancier;
 Pulsation tac;
 Pulsation tic;

 constructor(string memory _messageTic, string memory _messageTac) public {
     ajouterTacTic(new Pulsation(_messageTic), new Pulsation(_messageTac));
 }


 function ajouterTacTic(Pulsation _tic, Pulsation _tac) private{
     tic = _tic;
     tac = _tac;
 }

 function mouvementsBalancier(uint k) public {
     for(uint i = 0 ; i < k ; i++) {
        balancier.push(tic.ajouterBattement());
        balancier.push(tac.ajouterBattement());
     }
 }

 function getBalancier() public view returns (string[] memory) {
     return balancier;
 }
}