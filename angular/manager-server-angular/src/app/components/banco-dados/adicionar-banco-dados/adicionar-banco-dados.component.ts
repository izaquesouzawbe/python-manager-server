import { Component } from '@angular/core';
import {Router} from "@angular/router";
import {HttpClient} from "@angular/common/http";
import {BancoDadosService} from "../../../services/banco-dados.service";
import {BancoDados} from "../../../domains/banco-dados";

@Component({
  selector: 'app-adicionar-banco-dados',
  templateUrl: './adicionar-banco-dados.component.html',
  styleUrls: ['./adicionar-banco-dados.component.css'],
  providers: [BancoDadosService]
})
export class AdicionarBancoDadosComponent {

  banco: BancoDados;

  constructor(private http: HttpClient, private router: Router, private bancoDadosService: BancoDadosService) {
    this.banco = new BancoDados();
  }

  adicionar(): void {

    this.bancoDadosService.adicionar(this.banco)
      .subscribe(
        (response) => {
          this.router.navigate(['/banco-dados-list']);
        },
        (error) => {
          console.error('Erro ao adicionar banco de dados:', error);
        }
      );

  }

}
