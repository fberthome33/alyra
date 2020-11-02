import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import Web3 from 'web3';
import {ContractsService} from './contracts.service';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MatTableModule } from '@angular/material/table';

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule, MatTableModule
  ],
  providers: [ContractsService],
  bootstrap: [AppComponent]
})
export class AppModule {
  constructor (){};

}
