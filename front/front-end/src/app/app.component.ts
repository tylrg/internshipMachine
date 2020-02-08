import { Component } from '@angular/core';




@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'front-end';
  
  portfolio = [
    { "name": "Nike", "symbol": "NKE", "price": "5.23", "score": "7.8", "extra":"-43.%"},
    { "name": "Microsoft", "symbol": "MSFT", "price": "5.23", "score": "7.8", "extra":"-43.%"},
    { "name": "Google", "symbol": "ABC", "price": "444.333", "score": "7.8", "extra":"-43.%"},
  ]; 
}
