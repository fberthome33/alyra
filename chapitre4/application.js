async function createMetaMaskDapp() {
    try {
      // Demande à MetaMask l'autorisation de se connecter
      const addresses = await ethereum.enable();
      const address = addresses[0]
      // Connection au noeud fourni par l'objet web3
      provider = new ethers.providers.Web3Provider(ethereum);
      dapp = { address, provider };
      console.log(dapp)
    } catch(err) {
      // Gestion des erreurs
      console.error(err);
    }
  }


  async function balance(){
    dapp.provider.getBalance(dapp.address).then((balance) => {
      let etherString = ethers.utils.formatEther(balance);
      console.log("Balance: " + etherString);
    });
   }

   async function remettre(){
    let abi = JSON.parse('[{"inputs":[{"internalType":"bytes32","name":"dev","type":"bytes32"}],"name":"remettre","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"destinataire","type":"address"},{"internalType":"uint256","name":"valeur","type":"uint256"}],"name":"transfer","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"cred","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"url","type":"string"}],"name":"produireHash","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"pure","type":"function"}]');
    signer = provider.getSigner(0);
    let contratCredibilite = new ethers.Contract("0x451875bdd0e524882550ec1ce52bcc4d0ff90eae", abi, signer);
    contratCredibilite.remettre('0xef0607fc6479afc1918e5e418d49390a5d9a9a317a0c6bc370e1385782a24a4b');
    
   }

   async function credibilite(abiJson) {
    let abi = JSON.parse('[{"inputs":[{"internalType":"bytes32","name":"dev","type":"bytes32"}],"name":"remettre","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"destinataire","type":"address"},{"internalType":"uint256","name":"valeur","type":"uint256"}],"name":"transfer","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"cred","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"url","type":"string"}],"name":"produireHash","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"pure","type":"function"}]');

    let contratCredibilite = new ethers.Contract("0x451875bdd0e524882550ec1ce52bcc4d0ff90eae", abi, dapp.provider);
    contratCredibilite.cred(dapp.address).then((credValue) => {
      console.log("credibilite: " + credValue);
      });
    }
  