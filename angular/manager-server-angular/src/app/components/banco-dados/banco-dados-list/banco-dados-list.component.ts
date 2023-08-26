import {Component} from '@angular/core';
import {BancoDadosService} from "../../../services/banco-dados.service";

@Component({
  selector: 'app-banco-dados-list',
  templateUrl: './banco-dados-list.component.html',
  styleUrls: ['./banco-dados-list.component.css']
})

export class BancoDadosListComponent {

  bancos: any[] = [];

  constructor(private bancoDadosService: BancoDadosService) {

  }

  ngOnInit(): void {
    this.consultar();
  }

  consultar(): void {
    this.bancoDadosService.consultar().subscribe(data => {
      this.bancos = data;
    });
  }

  apagar(banco: any): void {

    this.bancoDadosService.apagar(banco.id)
      .subscribe(
        () => {
          console.log('Banco de dados apagado com sucesso!');
          this.consultar();
        },
        (error) => {
          console.error('Erro ao apagar banco de dados:', error);
        }
      );
  }

}
