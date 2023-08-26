import { Injectable } from '@angular/core';
import {Observable} from "rxjs";
import {HttpClient} from "@angular/common/http";

@Injectable({
  providedIn: 'root'
})
export class ServerService {

  private baseUrl = 'http://localhost:5000';

  constructor(private http: HttpClient) { }

  findAll(): Observable<any[]> {
    return this.http.get<any[]>(this.baseUrl + '/find_all_server');
  }

  findById(id: number): Observable<any[]> {
    return this.http.get<any[]>(this.baseUrl + `/find_by_id_server/${id}`);
  }

  getStatusServer(id: number): Observable<any[]> {
    return this.http.get<any[]>(this.baseUrl + `/status_server/${id}`);
  }

  save(server: any): Observable<any> {
    return this.http.post(this.baseUrl + '/save_server', server);
  }

  delete(id: number): Observable<any> {
    return this.http.delete(this.baseUrl + `/delete_server/${id}`);
  }

}
