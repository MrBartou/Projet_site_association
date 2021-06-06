import { Component, OnInit, TemplateRef, ViewChild, Input } from '@angular/core';
import { ApiService } from '../../api.service';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { FormBuilder } from '@angular/forms';

export interface UsersEvent {
  fst_name: string,
  snd_name: string,
  mail: string,
  phone: string,
  school: string,
  promo: string,
}

let ELEMENT_DATA: UsersEvent[] = [
];
@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss'],
  providers: [ApiService]
})
export class HomeAdminComponent implements OnInit {
  @ViewChild('editModal') editModal : TemplateRef<any>;
  @ViewChild('createActi') createactivity : TemplateRef<any>;

  events: any;

  public title: any;
  public endDate : any;
  public startDate: any;

  from = this.formBuilder.group({
    start: "",
    end: "",
    title: ""
  })

  constructor(private api:ApiService, private modalService: NgbModal, private formBuilder: FormBuilder) {
    this.getEvent();
    this.getSubscription();
  }

  ngOnInit() {
  }

  suppr_event(name: string) {
    this.api.deleteEvent(name).subscribe(
      error => {
        console.log(error);
      }
    );
    alert("L'évènement a bien été modifié");
  }

  onSubmit2(): void {
    this.api.deleteEvent(this.events[0].title).subscribe(
      error => {
        console.log(error);
      }
    );
    this.api.postActivity(this.from.value).subscribe(
      error => {
        console.log(error);
      }
    );
    alert("Votre activité a bien été modifier");
  }

  onSubmit(): void {
    this.api.postActivity(this.from.value).subscribe(
      error => {
        console.log(error);
      }
    );
    alert("Votre activité a bien été créer");
  }

  openmodal() {
    this.modalService.open(this.editModal);
  }

  openmodal2() {
    this.modalService.open(this.createactivity);
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
    this.api.getSubscription().subscribe(
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
