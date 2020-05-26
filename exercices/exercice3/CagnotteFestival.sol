pragma solidity ^0.6.0;

import "github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol";


contract CagnotteFestival{

 using SafeMath for uint;


 uint constant NB_MAX_SPONSORS = 10; // Limite des sponsors à ajouter
 uint constant MAX_DEPENSE_PER_DAY = 100; // Limite des sponsors à ajouter
 uint nbOrganisateur;
 string[] sponsors;
 mapping (address => uint) organisateurs;

 mapping (address => bool) festivaliers;
 mapping (uint => uint) limiteDepense;

 uint256 placesRestantes = 10;
 uint dateFestival;
 uint dateLiquidation;

 constructor(uint date) public {

   organisateurs[msg.sender] = 100;
   nbOrganisateur++;
   dateFestival = date;
   dateLiquidation = dateFestival + 2 weeks;

 }



  function transfererOrga(address orga, uint parts) public {

    require(organisateurs[msg.sender] >= parts);

    require(!estOrga(orga));



    organisateurs[msg.sender] = organisateurs[msg.sender].sub(parts);

    organisateurs[orga] = parts;
    nbOrganisateur++;
  }



   function estOrga(address orga) public view returns (bool){

        return organisateurs[orga] > 0;

    }



    function verifierDepense(uint montant) private view returns (bool) {
        uint timestamp = block.timestamp;
        uint secondDay = 24 * 60 * 60;
        uint date = timestamp / secondDay;

        return limiteDepense[date].add(montant) > MAX_DEPENSE_PER_DAY;

    }

    function acheterTicket() public payable {

       require(msg.value>= 500 finney,"Place à 0.5 Ethers");

       require(placesRestantes>0,"Plus de places !");

       festivaliers[msg.sender]=true;

 }

function retraitOrganisateur(address payable organisateur) public payable {
        require(block.timestamp >= dateLiquidation, "Vous devez attendre la date de liquidation");
        uint amount = (address(this).balance).mul(organisateurs[organisateur]).div(100);
        organisateur.transfer(amount);
        delete organisateurs[organisateur];
        nbOrganisateur--;

        if(nbOrganisateur == 0)
            selfdestruct(organisateur);
}



 function sponsoriser(string memory nom) public payable {

     require(msg.value>= 30 ether,"Sponsor à 30 Ethers");

     require(sponsors.length < NB_MAX_SPONSORS,"Nb Max sponsors atteint");

     sponsors.push(nom);

 }

}

