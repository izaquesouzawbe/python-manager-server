import {Component, OnInit} from '@angular/core';
import {ActivatedRoute, Router} from "@angular/router";
import {HttpClient} from "@angular/common/http";
import {ServerService} from "../../../services/server.service";
import {error} from "@angular/compiler-cli/src/transformers/util";
import {load} from "@angular-devkit/build-angular/src/utils/server-rendering/esm-in-memory-file-loader";
import {Server} from "../../../domains/server";

@Component({
  selector: 'app-server-form',
  templateUrl: './server-form.component.html',
  providers: [ServerService],
  styleUrls: ['./server-form.component.css']
})
export class ServerFormComponent implements OnInit {

  id: string | null = '';
  password: string = '';

  server: Server[] = [];

  constructor(private http: HttpClient, private route: ActivatedRoute, private router: Router, private serverService: ServerService) {
  }

  ngOnInit(): void {
    this.id = this.route.snapshot.paramMap.get('id');
    this.load();
  }

  load() {

    if (!this.id) {
      return;
    }

    this.serverService.findById(parseInt(this.id)).subscribe(data => {
      this.server = data;
    });

  }

  save(): void {
    const server = {
      id: this.id,
      name: this.server,
      host: server.host,
      username: server.username,
      password: server.password,
      privateKey: server.privateKey
    };

    this.serverService.save(server)
      .subscribe(
        (response) => {
          this.router.navigate(['/server-list']);
        },
        (error) => {
          console.error('Erro ao adicionar servidor:', error);
        }
      );

  }


}
