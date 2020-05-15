pragma solidity ^0.6.0;

contract SceneOuverte {
    string[12] passagesArtistes;
    uint creneauxLibres = 12;

    uint tour;
    function sInscrire(string memory nomDArtiste) public {
        if (creneauxLibres > 0) {
            passagesArtistes[12 - creneauxLibres] = nomDArtiste;
            creneauxLibres -= 1;
        }
    }

    function nombreCreneauxLibre() public view returns (uint) {
        return creneauxLibres;
    }

    function passerArtisteSuivant() public {
        if (tour < 12)
            tour += 1;
    }

  function artisteEncours() public view returns (string memory) {
      if (tour < 12) {
          return passagesArtistes[tour];
      }
      return "FIN";
      }
}