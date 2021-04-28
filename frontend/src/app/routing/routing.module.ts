import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Routes, RouterModule } from '@angular/router'
import { HomeComponent } from '../home/home.component';
import { EvenementComponent } from '../page/evenement/evenement.component';
import { PartenariatComponent } from '../page/partenariat/partenariat.component';
import { EquipeComponent } from '../page/equipe/equipe.component';
import { ContactComponent } from '../page/contact/contact.component';

const routes: Routes = [
    { path: 'home', component: HomeComponent },
    { path: 'evenement', component: EvenementComponent},
    { path: 'partenariat', component: PartenariatComponent},
    { path: 'equipe', component: EquipeComponent},
    { path: 'contact', component: ContactComponent},
    { path:'', redirectTo: '/home', pathMatch: 'full' }
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
