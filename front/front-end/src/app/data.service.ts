import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';

const httpOptions = {
  headers: new HttpHeaders({
    'Content-Type': 'text/plain'
  })
};

@Injectable({
  providedIn: 'root'
})
export class DataService {

  constructor(public http: HttpClient) { }

  baseUrl ="http://localhost:5000";

  test(){
    return this.http.get(this.baseUrl);
  }

  getSentiment(value,name){
    return this.http.get(this.baseUrl + '/sentiment?symbol='+value+'&name='+name);
  }
  getPercent(value){
    return this.http.get(this.baseUrl + '/percent?symbol='+value);
  }
  getPrice(value) {
    return this.http.get(this.baseUrl + '/price?symbol=' + value);
  }
}
