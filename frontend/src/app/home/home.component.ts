import { Component, OnInit } from '@angular/core';
import { ApiService } from 'src/app/api.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {
  images = ["image1.png", "image2.png", "image3.png", "image4.png"].map((n) => `../../assets/home/${n}`);
  events: any;

  constructor(private api:ApiService) { }

  ngOnInit(): void {
    this.getEvent();
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

}
