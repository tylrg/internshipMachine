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
  }

  portfolio = [
    { "name": "Nike", "symbol": "NKE", "price": "5.23", "score": "7.8", "extra": "-43.%" },
    { "name": "Microsoft", "symbol": "MSFT", "price": "5.23", "score": "7.8", "extra": "-43.%" },
    { "name": "Google", "symbol": "ABC", "price": "444.333", "score": "7.8", "extra": "-43.%" },
  ]; 

  //refreshes the stock data
  refresh() {
    console.log("Refreshing");
    this.data.getSentiment().subscribe(res => {
      console.log(res);
    });
    this.data.getSentiment().subscribe(res => {
      console.log(res);
    });  
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
    console.log("adding "+addSymbol);
    this.portfolio.push({ "name": "unknown", "symbol": addSymbol, "price": "0.00", "score": "0.0", "extra": "0.0%" });
  }

}
