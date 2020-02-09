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
    console.log("VERSION 0.0.6");
  }

  portfolio = [
    { "name": "Nike", "symbol": "NKE", "price": "0.0", "score": "7.8", "extra": "0.0" },
    { "name": "Microsoft", "symbol": "MSFT", "price": "0.0", "score": "7.8", "extra": "0.0" },
    { "name": "Google", "symbol": "GOOG", "price": "0.0", "score": "7.8", "extra": "0.0" },
  ]; 

  //refreshes the stock data
  refresh() {
    console.log("Refreshing");
    this.updatePrices();
    //this.calculateMetric();

    // this.data.getSentiment().subscribe(res => {
    //   console.log(res);
    // });
  }

  //opens a help prompt
  help() {
    console.log("Helping");
  }

  //signs the user out 
  exit() {
    console.log("Exiting");
  }

  //tests the html connection with a given api
  test() {
    console.log("Testing");
    this.data.test().subscribe(res => {
      console.log(res);
    });
  }

  //clears the console
  clear() {
    console.clear();
  }

  add() {
    let addSymbol = (<HTMLInputElement>document.getElementById("addField")).value;
    let addName = (<HTMLInputElement>document.getElementById("addName")).value;
    console.log("adding "+addSymbol+" ");
    this.portfolio.push({ "name": addName, "symbol": addSymbol, "price": "0.00", "score": "0.0", "extra": "0.0%" });
  }

  calculateMetric(){

    for(let stock of this.portfolio){
      console.log(JSON.stringify(stock.score));
    }
  }

  updatePrices(){
    for (let stock of this.portfolio) {
      
      let sym = stock.symbol;
      //console.log(JSON.stringify(stock.symbol));
      this.data.getPercent(sym).subscribe(res => {
        console.log(res);
        let jString = JSON.stringify(res);
        let result = JSON.parse(jString);
        stock.extra=result.value;
        console.log(JSON.stringify(stock.extra));
      });

      this.data.getPrice(sym).subscribe(res => {
        console.log(res);
        let jString = JSON.stringify(res);
        let result = JSON.parse(jString);
        stock.price = result.value;
        console.log(JSON.stringify(stock.price));
      });      
    }
  }
}
