import {Component} from '@angular/core';
import {ServerService} from "../../../services/server.service";
import {Router} from "@angular/router";

@Component({
  selector: 'app-server-list',
  templateUrl: './server-list.component.html',
  styleUrls: ['./server-list.component.css']
})

export class ServerListComponent {

  servers: any[] = [];
  useServer: any;

  constructor(private serverService: ServerService, private router: Router) {

  }

  ngOnInit(): void {
    this.findAll();
  }

  findAll(): void {
    this.serverService.findAll().subscribe(data => {
      this.servers = data;
      this.showUse()
    });
  }

  showUse(): void {
    this.servers.forEach(item => {
      this.serverService.getStatusServer(item.id).subscribe(data => {
        this.useServer = data;
        item.use = this.useServer.result_ssh;
      });
    });
  }

  edit(server: any): void {
    this.router.navigate([`/server-form/${server.id}`]);
  }

  delete(server: any): void {

    this.serverService.delete(server.id)
      .subscribe(
        () => {
          console.log('Servidor apagado com sucesso!');
          this.findAll();
        },
        (error) => {
          console.error('Erro ao apagar servidor:', error);
        }
      );
  }

}
