import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss']
})
export class HeaderComponent implements OnInit {

  constructor() { }

  ngOnInit() {
    console.log("Header has been created");
  }

  refresh(){ 
    console.log("refreshing");
  }


  help(){
    console.log("helping");
  }

  exit(){
    console.log("exiting");
  }

}
