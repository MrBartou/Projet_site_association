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

  getPartnerships(): Observable<any>{
    return this.http.get(this.baseurl + '/partnership/', {headers: this.httpHeaders})
  }

  getAdmins(): Observable<any>{
    return this.http.get(this.baseurl + '/admins/', {headers: this.httpHeaders})
  }

  getSubscription(): Observable<any>{
    return this.http.get(this.baseurl + '/subscription/', {headers: this.httpHeaders})
  }

  postActivity(data: any): Observable<any>{
    return this.http.post(this.baseurl + '/event/', JSON.stringify(data) , {headers: this.httpHeaders})
  }

  deleteEvent(name: string): Observable<any>{
    return this.http.delete(this.baseurl + `/events/${name}`)
  }

  postSubscription(data: any): Observable<any>{
    return this.http.post(this.baseurl + '/users/', JSON.stringify(data), {headers: this.httpHeaders})
  }
}
