import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';


@Injectable({
  providedIn: 'root'
})
export class DataService {

  constructor(public http: HttpClient) { }

  baseUrl ="http://localhost:3000";

  test(){
    return this.http.get(this.baseUrl+'/posts');
  }
}
