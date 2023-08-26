import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { MenuComponent } from './components/main/menu/menu.component';
import { ServerListComponent } from './components/servidor/server-list/server-list.component';
import {HttpClientModule} from "@angular/common/http";
import { ServerFormComponent } from './components/servidor/server-form/server-form.component';
import {FormsModule} from "@angular/forms";
import { DeployListComponent } from './components/deploy/deploy-list/deploy-list.component';
import {BancoDadosListComponent} from "./components/banco-dados/banco-dados-list/banco-dados-list.component";
import {AdicionarBancoDadosComponent} from "./components/banco-dados/adicionar-banco-dados/adicionar-banco-dados.component";

@NgModule({
  declarations: [
    AppComponent,
    MenuComponent,
    ServerListComponent,
    ServerFormComponent,
    DeployListComponent,
    BancoDadosListComponent,
    AdicionarBancoDadosComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
