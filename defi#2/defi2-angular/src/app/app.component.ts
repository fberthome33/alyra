import { Component } from '@angular/core';
import {ContractsService} from './contracts.service';

enum Statut{
  OUVERTE, ENCOURS, FERMEE
}

interface Demande {  
  remuneration : number;
  delai_acceptation : number;
  description : string;
  etat : string;
  min_reputation : number;
}   //



@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent {
  dataSource: Demande[];
  title = 'defi2-angular';
  displayedColumns: string[] = ['remuneration', 'delai_acceptation', 'description', 'etat', 'min_reputation'];
  constructor(private contractsService: ContractsService) {
    contractsService.loadWeb3()
      .then( () => {
        return contractsService.loadBlockchainData();
      })
      .then(data => {
        console.log(data);
        this.dataSource = data.map(demande => {
          const map_demande : Demande = { 
            remuneration : demande[0],
            delai_acceptation : demande[1],
            description : demande[2],
            etat : Statut[demande[3]],
            min_reputation : demande[4]
          };
          return map_demande;
      });
      });
  }

}
