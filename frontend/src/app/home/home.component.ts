import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {
  images = ["image1.png", "image2.png", "image3.png", "image4.png"].map((n) => `../../assets/home/${n}`);

  constructor() { }

  ngOnInit(): void {
  }

}
