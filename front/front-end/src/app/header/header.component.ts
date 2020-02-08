import { Component, OnInit } from '@angular/core';
import { DataService } from '../data.service';



@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss']
})
export class HeaderComponent implements OnInit {

  constructor(public data: DataService) { }

  ngOnInit() {
    console.log("Header has been created");
  }

  //refreshes the stock data
  refresh(){ 
    console.log("Refreshing");
  }

  //opens a help prompt
  help(){
    console.log("Helping");
  }

  //signs the user out 
  exit(){
    console.log("Exiting");
  }

  //tests the html connection with a given api
  test(){
    console.log("Testing");
    this.data.test().subscribe(res => {
      console.log(res);
    });
  }

  //clears the console
  clear(){
    console.clear();
  }

  add(){
    console.log("adding");
  }

}
