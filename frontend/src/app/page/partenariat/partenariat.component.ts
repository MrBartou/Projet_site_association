import { Component, OnInit } from '@angular/core';
import { ApiService } from 'src/app/api.service';

@Component({
  selector: 'app-partenariat',
  templateUrl: './partenariat.component.html',
  styleUrls: ['./partenariat.component.scss']
})
export class PartenariatComponent implements OnInit {
  partener = [];

  constructor(private api: ApiService) { }

  ngOnInit() {
    this.getPartenership();
  }

  getPartenership = () => {
    this.api.getPartnerships().subscribe(
      data => {
        this.partener = []
        data.forEach(element => {
          const EventData = this.partener
          EventData.push({
            category: element.category,
            img_abs_path: element.img_abs_path,
            title: element.title,
            description: element.description});
          this.partener = EventData;
        });
      },
      error => {
        console.log(error);
        alert("Une erreur est survenue veuillez réessayer");
      }
    )
  }

}
