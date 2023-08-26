import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {MenuComponent} from "./components/main/menu/menu.component";
import {ServerListComponent} from "./components/servidor/server-list/server-list.component";
import {ServerFormComponent} from "./components/servidor/server-form/server-form.component";
import {DeployListComponent} from "./components/deploy/deploy-list/deploy-list.component";
import {BancoDadosListComponent} from "./components/banco-dados/banco-dados-list/banco-dados-list.component";
import {AdicionarBancoDadosComponent} from "./components/banco-dados/adicionar-banco-dados/adicionar-banco-dados.component";

const routes: Routes = [
  { path: 'menu', component: MenuComponent },
  { path: 'server-list', component: ServerListComponent },
  { path: 'server-form', component: ServerFormComponent },
  { path: 'server-form/:id', component: ServerFormComponent },
  { path: 'deploy-list', component: DeployListComponent },
  { path: 'banco-dados-list', component: BancoDadosListComponent },
  { path: 'adicionar-banco-dados', component: AdicionarBancoDadosComponent },
  { path: '**', redirectTo: '/' }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
