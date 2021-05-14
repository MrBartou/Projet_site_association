import { Component, OnInit } from '@angular/core';
import { faFacebook, faInstagram, faLinkedin } from '@fortawesome/free-brands-svg-icons';
import { faMailBulk } from '@fortawesome/free-solid-svg-icons';

@Component({
  selector: 'app-equipe',
  templateUrl: './equipe.component.html',
  styleUrls: ['./equipe.component.scss']
})
export class EquipeComponent implements OnInit {

  faFacebook = faFacebook;
  faInstagram = faInstagram;
  faGithub = faLinkedin;
  faMailBulk = faMailBulk;

  constructor() { }

  ngOnInit(): void {
  }

}
