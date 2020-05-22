pragma solidity ^0.6.0;
contract Assemblee {
 struct Decision {
   string description;
   uint votesPour;
   uint votesContre;

   mapping (address => bool) aVote;
   bool ouvert;
   address administrateur;
 }

 mapping (address => int) blames;
 address[] membres;
 address[] administrateurs;
 Decision[] decisions;

 string public nombAssemblee;

 constructor(string memory nom) public {
   nombAssemblee = nom;
   administrateurs.push(msg.sender);
 }

 function rejoindre() public {
   require(estMembre(msg.sender) == false, "Vous êtes déjà membre");
   require(blames[msg.sender] != 2, "Vous avez été expulsé de cette assemblée");
   membres.push(msg.sender);
 }

 function estMembre(address utilisateur) public view returns (bool) {
    for (uint i=0; i<membres.length; i++) {
        if(membres[i] == utilisateur) {
            return true;
        }
    }
    return false;
 }

 function estAdministrateur() public view returns (bool) {
    for (uint i=0; i<administrateurs.length; i++) {
        if(administrateurs[i] == msg.sender) {
            return true;
        }
    }
    return false;
 }

 function proposerDecision(string memory description) public {
   require(estMembre(msg.sender), "Il faut être membre!");
   Decision memory decision;
   decision.description = description;
   decision.ouvert = true;
   decisions.push(decision);
 }

  function proposerAdministrateur(string memory description, address  admninistrateur) public {
   require(estMembre(msg.sender), "Il faut être membre!");
   Decision memory decision;
   decision.description = description;
   decision.ouvert = true;
   decision.administrateur = admninistrateur;
   decisions.push(decision);
 }

 function voter(uint indice, bool value) public {
    require(decisions[indice].aVote[msg.sender] == false, "Vous avez déjà voté pour cette decision");
    require(decisions[indice].ouvert, "La decision n est pas ouverte au vote");
    require(estMembre(msg.sender), "Il faut être membre!");
    if(value) {
        decisions[indice].votesPour++;
    } else {
        decisions[indice].votesContre++;
    }
    decisions[indice].aVote[msg.sender] = true;
 }

 function comptabiliser(uint indice) public view returns (int){
    return int(decisions[indice].votesPour - decisions[indice].votesContre);
 }

 function nommerAdministrateur(address administrateur) public {
    require(estAdministrateur(), "Vous devez être administrateur");
    for (uint i=0; i < administrateurs.length; i++) {
        if(administrateurs[i] == administrateur) {
            revert();
        }
    }
    administrateurs.push(administrateur);
 }

  function demissionAdministrateur() public {
    require(estAdministrateur(), "Vous devez être administrateur");
    for (uint i=0; i < administrateurs.length; i++) {
        if(administrateurs[i] == msg.sender) {
            delete administrateurs[i];
        }
    }
 }

   function fermerDecision(uint indice) public {
    require(estAdministrateur(), "Vous devez être administrateur");
    decisions[indice].ouvert = false;
    if(decisions[indice].administrateur != address(0) &&  comptabiliser(indice) > 0) {
        administrateurs.push(decisions[indice].administrateur);
   }
   }


    function blame(address membre) public {
        require(estAdministrateur(), "Vous devez être administrateur");
        blames[membre]++;
        if( blames[membre] == 2) {
           for (uint i=0; i<membres.length; i++) {
              if(membres[i] == membre) {
                 delete membres[i];
              }
           }
        }
    }

}

