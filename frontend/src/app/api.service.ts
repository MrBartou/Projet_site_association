import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http'
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  baseurl = "http://127.0.0.1:8000";
  httpHeaders = new HttpHeaders({'Content-Type': 'application/json'});

  constructor(private http: HttpClient) { }

  getAllEvent(): Observable<any>{
    return this.http.get(this.baseurl + '/event/', {headers: this.httpHeaders})
  }

  // getAllUsers(): Observable<any>{
  //   return this.http.get(this.baseurl + '/users/', {headers: this.httpHeaders})
  // }

  // getPartenariat(): Observable<any>{
  //   return this.http.get(this.baseurl + '/partership/', {headers: this.httpHeaders})
  // }

  postSubscription(): Observable<any>{
    return this.http.get(this.baseurl + '/subscription/', {headers: this.httpHeaders})
  }
}
