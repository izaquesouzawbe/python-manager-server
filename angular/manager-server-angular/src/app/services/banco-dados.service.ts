import { Injectable } from '@angular/core';
import {Observable} from "rxjs";
import {HttpClient} from "@angular/common/http";

@Injectable({
  providedIn: 'root'
})
export class BancoDadosService {
  private url = 'http://localhost:5000';

  constructor(private http: HttpClient) { }

  consultar(): Observable<any[]> {
    return this.http.get<any[]>(this.url + '/consultar_banco_dados');
  }

  adicionar(bancos: any): Observable<any> {
    return this.http.post(this.url + '/inserir_banco_dados', bancos);
  }

  apagar(id: number): Observable<any> {
    const url = this.url + `/apagar_banco_dados/${id}`;
    return this.http.delete(url);
  }

}
