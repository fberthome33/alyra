import { Injectable } from '@angular/core';
import Web3 from 'web3';
import SceneOuverte from './abis/placeDeMarche.json'
declare let require: any;
declare let window: any;

//const rpcURL = "https://ropsten.infura.io/v3/461e417d912441f78958e476ebc11f47"
const rpcURL = "http://localhost:8545/0xd2BAeFA16469b784EFBFd83D077157319a27551a"
const web3 = new Web3(rpcURL)

@Injectable({
  providedIn: 'root'
})   

export class Demande {  
  remuneration : number;
  delai_acceptation : number;
  description : string;
  etat : number;
  min_reputation : number;
}   //
export class ContractsService {

  constructor() { 

  }

  async loadWeb3() {
    if (window.ethereum) {
      window.web3 = new Web3(window.ethereum) // permet d’initialiser l’objet Web3 en se basant sur le provider injecté dans la page web 
      await window.ethereum.enable() //demande à Metamask de laisser la page web accéder à l’objet web3 injecté
    }
    else if (window.web3) {
      window.web3 = new Web3(window.web3.currentProvider) // si l’objet web3 existe déjà, l’objet Web3 est initialisé en se basant sur le provider du web3 actuel
    }
    else {
      window.alert('Non-Ethereum browser detected. You should consider trying MetaMask!') // message d’erreur si le navigateur ne détecte pas Ethereum
    }
  }


  async loadBlockchainData() {

    console.log("Heyy")
    const web3 = window.web3
    const accounts = await web3.eth.getAccounts()
    console.log("accounts" + accounts);
    // Update state 
    // Récupérer le networkId actuel (en se basant sur le fichier SceneOuverte.json) 
    const networkId = await web3.eth.net.getId()
    console.log("networkId" + networkId);
    const networkData = SceneOuverte.networks[networkId];
    console.log("networkData" + networkData);
    // Vérifier si on a un contrat déjà déployé ou pas encore 
    
    if(networkData.address !== "") {
      const sceneOuverte = new web3.eth.Contract(SceneOuverte.abi,  networkData.address);
      console.log(sceneOuverte);
      // Faire appel au smart contract et récupérer le tour actuel 
      const listerDemandes = await sceneOuverte.methods.listerDemandes().call();
      console.log(listerDemandes);
      return listerDemandes;
    } else {
      // Afficher un message d'erreur 
      window.alert('SceneOuverte contract not deployed to detected network.')
    }
  }
}
