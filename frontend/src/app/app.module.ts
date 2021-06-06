import { BrowserModule } from '@angular/platform-browser';
import { NgModule} from '@angular/core';


import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { RoutingModule } from './routing/routing.module';
import { HomeComponent } from './home/home.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MaterialModule } from './material/material.module';
import { HeaderComponent } from './shared/header/header.component';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { EvenementComponent } from './page/evenement/evenement.component';
import { PartenariatComponent } from './page/partenariat/partenariat.component';
import { EquipeComponent } from './page/equipe/equipe.component';
import { ContactComponent } from './page/contact/contact.component';
import { FooterComponent } from './shared/footer/footer.component';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';
import { CalendarModule, DateAdapter } from 'angular-calendar';
import { adapterFactory } from 'angular-calendar/date-adapters/date-fns';
import { ReactiveFormsModule } from '@angular/forms';
import { Page404Component } from './page/page404/page404.component';
import { LoginComponent } from './dashboard/login/login.component';
import { HttpClientModule } from '@angular/common/http'
import { CommonModule } from "@angular/common";
import { HomeAdminComponent } from "./dashboard/home/home.component";
import { FormsModule } from "@angular/forms";
import { TermsComponent } from './page/terms/terms.component';


@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    HeaderComponent,
    EvenementComponent,
    PartenariatComponent,
    EquipeComponent,
    ContactComponent,
    FooterComponent,
    Page404Component,
    LoginComponent,
    HomeAdminComponent,
    TermsComponent,
  ],
  imports: [
    CommonModule,
    BrowserModule,
    AppRoutingModule,
    RoutingModule,
    BrowserAnimationsModule,
    MaterialModule,
    NgbModule,
    FontAwesomeModule,
    AppRoutingModule,
    CalendarModule.forRoot({
      provide: DateAdapter,
      useFactory: adapterFactory,
    }),
    ReactiveFormsModule,
    HttpClientModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
