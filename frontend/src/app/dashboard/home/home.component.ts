import { Component, OnInit } from '@angular/core';
import { ApiService } from '../../api.service';


export interface UsersEvent {
  fst_name: string,
  snd_name: string,
  mail: string,
  phone: string,
  school: string,
  promo: string,
}

let ELEMENT_DATA: UsersEvent[] = [
  {fst_name: "bla", snd_name: "bla", mail: "bla", phone: "bla", school: "bla", promo: "bla"}
];
@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss'],
  providers: [ApiService]
})
export class HomeAdminComponent implements OnInit {

  events: any;

  constructor(private api:ApiService) {
    this.getEvent();
    this.getSubscription();
  }

  ngOnInit() {
  }

  getEvent = () => {
    this.api.getAllEvent().subscribe(
      data => {
        this.events = data;
      },
      error => {
        console.log(error);
      }
    )
  }

  getSubscription = () => {
    this.api.postSubscription().subscribe(
      data => {
        data.forEach(element => {
          const data = this.dataSource;
          data.push({fst_name: element.fst_name, snd_name: element.snd_name, mail: element.mail, phone: element.phone, school: element.school, promo: element.promo});
          this.dataSource = data;
        });
        this.dataSource = ELEMENT_DATA;
      },
      error => {
        console.log(error);
      }
    )
  }

  displayedColumns: string[] = ['fst_name', 'snd_name', 'mail', 'phone', 'school', 'promo'];
  dataSource = ELEMENT_DATA;
}
