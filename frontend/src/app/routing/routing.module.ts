import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Routes, RouterModule } from '@angular/router'
import { HomeComponent } from '../home/home.component';
import { EvenementComponent } from '../page/evenement/evenement.component';
import { PartenariatComponent } from '../page/partenariat/partenariat.component';
import { EquipeComponent } from '../page/equipe/equipe.component';
import { ContactComponent } from '../page/contact/contact.component';
import { Page404Component } from '../page/page404/page404.component';
import { LoginComponent } from '../dashboard/login/login.component';
import { HomeAdminComponent } from '../dashboard/home/home.component';
import { TermsComponent } from '../page/terms/terms.component'

const routes: Routes = [
    { path: 'home', component: HomeComponent },
    { path: 'contact', component: ContactComponent},
    { path: 'admin/login', component:LoginComponent },
    { path: 'admin/home', component:HomeAdminComponent },
    { path: 'evenement', component: EvenementComponent},
    { path: 'partenariat', component: PartenariatComponent},
    { path: 'terms', component: TermsComponent},
    { path: 'equipe', component: EquipeComponent},
    { path: '', redirectTo: '/home', pathMatch: 'full' },
    { path: '**', component: Page404Component }
];

@NgModule({
  declarations: [],
  imports: [
    CommonModule,
    RouterModule.forRoot(routes)
  ],
  exports: [
      RouterModule
  ]
})
export class RoutingModule { }
