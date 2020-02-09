import { Component, OnInit } from '@angular/core';
import { DataService } from '../data.service';

@Component({
  selector: 'app-master',
  templateUrl: './master.component.html',
  styleUrls: ['./master.component.scss']
})
export class MasterComponent implements OnInit {

  constructor(public data:DataService) { }

  ngOnInit() {
    console.log("VERSION 0.0.9");
  }

  portfolio = [
    { "name": "Nike", "symbol": "NKE", "price": "0.0", "score": "0.0", "extra": "0.0", "sentimentAvg": "0.0", "magnitude": "0.0" },
    { "name": "Microsoft", "symbol": "MSFT", "price": "0.0", "score": "0.0", "extra": "0.0", "sentimentAvg": "0.0", "magnitude": "0.0" },
    { "name": "Google", "symbol": "GOOG", "price": "0.0", "score": "0.0", "extra": "0.0", "sentimentAvg": "0.0", "magnitude": "0.0" },
  ]; 

  //refreshes the stock data
  refresh() {
    console.log("Refreshing");
    this.updatePrices();
    this.
    this.calculateMetric();


  }

  //opens a help prompt
  help() {
    console.log("Helping");
  }

  //signs the user out 
  exit() {
    console.log("Exiting");
  }

  //clears the console
  clear() {
    console.clear();
  }
  add() {
    let addSymbol = (<HTMLInputElement>document.getElementById("addField")).value;
    let addName = (<HTMLInputElement>document.getElementById("addName")).value;
    //console.log("adding "+addSymbol+" ");
    this.portfolio.push({ "name": addName, "symbol": addSymbol, "price": "0.00", "score": "0.0", "extra": "0.0%","sentimentAvg":"0.0","magnitude":"0.0" });
  }
  calculateMetric(){

    for(let stock of this.portfolio){
      let sA = +(stock.sentimentAvg);
      let mA = +(stock.magnitude);
      let trend = +(stock.extra);
      let numerator = sA*mA;
      let denominator = 1;
      if(numerator<0){
        if(trend>=0){
          denominator=2;
        }
      }
      if(numerator>=0){
        if(trend<0){
          denominator=2;
        }
      }
      let value = (numerator/denominator);
      stock.score=value.toString();
      //console.log(JSON.stringify(stock.score));
    }
  }
  updatePrices(){
    for (let stock of this.portfolio) {
      
      let sym = stock.symbol;
      //console.log(JSON.stringify(stock.symbol));
      this.data.getPercent(sym).subscribe(res => {
        //console.log(res);
        let jString = JSON.stringify(res);
        let result = JSON.parse(jString);
        stock.extra=result.value;
        //console.log(JSON.stringify(stock.extra));
      });

      this.data.getPrice(sym).subscribe(res => {
        //console.log(res);
        let jString = JSON.stringify(res);
        let result = JSON.parse(jString);
        stock.price = result.value;
        //console.log(JSON.stringify(stock.price));
      });      
    }
  }
  updateSentiment(){
    for (let stock of this.portfolio) {

      let sym = stock.symbol;
      let name=stock.name;
      this.data.getSentiment(sym,name).subscribe(res => {
        console.log(res);
        let jString = JSON.stringify(res);
        let result = JSON.parse(jString);
        let sentimentString=result.value;
        let space = sentimentString.indexOf(' ');
        console.log(space);
        let magnitude = sentimentString.substring(space);
        sentimentString = sentimentString.substring(0,space);
        console.log("Sentiment: " + sentimentString +" Magnitude:" + magnitude);
        stock.sentimentAvg = sentimentString;
        stock.magnitude = magnitude;
      });
    

    }
  }
}
