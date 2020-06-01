pragma solidity ^0.6.0;
pragma experimental ABIEncoderV2;

import "github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol";


contract CagnotteFestival{
    using SafeMath for uint;
    struct Ticket {
        address owner;
        uint8 value;
        uint montant;
    }

    mapping (address => uint) gains;
    mapping (uint => Ticket[]) tickets;
    uint dateFinLotterie;
    address[]  gagnant;
    uint dateDebutLotterie;
    constructor(uint _dateDebutLotterie) public {
       dateDebutLotterie = jour(_dateDebutLotterie);
       dateFinLotterie = dateDebutLotterie.add(5 days);
    }

    function jour(uint t) internal pure returns (uint) {
        // Indice du jour du moment t
        return SafeMath.div(t, 1 days) * 1 days;
    }

    function tirer() public {

        //require(block.timestamp > dateFinLotterie, "Vous ne pouvez pas encore effectuer le tirage");
        for (uint nbJour =  0; nbJour <= 5 ; nbJour++) {

            uint dd = nbJour.mul(1 days);
            uint jourDate = jour(dateDebutLotterie).add(dd);
            log0( bytes32(jourDate));
            tirerJour(jourDate);

        }
    }

    function tirerJour(uint jourDate ) public {

       uint8 numeroTire = generateRandom();
        Ticket[] memory ticketsJour =  tickets[jour(jourDate)];

        uint8 nombreGagnant = 0;
        uint sommeGain=0;
        for(uint i = 0; i < ticketsJour.length; i++) {
            if(ticketsJour[i].value == numeroTire) {
               nombreGagnant++;
            }
            sommeGain += ticketsJour[i].montant;
        }

        for(uint i = 0; i < ticketsJour.length; i++) {
            if(ticketsJour[i].value == numeroTire) {
               gains[ticketsJour[i].owner] = sommeGain / 2 / nombreGagnant;
            }
        }
    }

    function retirerGain() public payable {
        msg.sender.transfer(gains[msg.sender]);
    }

    function acheterTicket(uint date, uint8 _value) public payable {
       require(msg.value == 100 finney,"Place à 0.1 Ethers");
       require(date >= dateDebutLotterie && date <= dateFinLotterie, "date du ticket invalide");
       Ticket memory currentTicket;

       currentTicket.owner = msg.sender;
       currentTicket.montant = msg.value;
       currentTicket.value = _value;

       tickets[jour(date)].push(currentTicket);
    }

    function generateRandom() public view returns (uint8){
       return uint8(uint256(keccak256(abi.encodePacked(block.timestamp, block.difficulty)))) % 251;

    }
}