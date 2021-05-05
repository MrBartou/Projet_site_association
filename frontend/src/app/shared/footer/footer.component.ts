import { Component, OnInit } from '@angular/core';
import { faFacebook, faInstagram, faGithub } from '@fortawesome/free-brands-svg-icons';
import { faMailBulk } from '@fortawesome/free-solid-svg-icons';

@Component({
  selector: 'app-footer',
  templateUrl: './footer.component.html',
  styleUrls: ['./footer.component.scss']
})
export class FooterComponent implements OnInit {

  faFacebook = faFacebook;
  faInstagram = faInstagram;
  faGithub = faGithub;
  faMailBulk = faMailBulk;

  constructor() { }

  ngOnInit(): void {
  }

}
