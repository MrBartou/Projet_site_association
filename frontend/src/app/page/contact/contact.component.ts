import { Component, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms'
import { HttpHeaders, HttpClient } from '@angular/common/http'

@Component({
  selector: 'app-contact',
  templateUrl: './contact.component.html',
  styleUrls: ['./contact.component.scss']
})
export class ContactComponent implements OnInit {
  constructor(private http: HttpClient) {
  }

  ngOnInit(): void {
  }

  onSubmit(contactForm: NgForm) {
    if (contactForm.valid) {
      const email = contactForm.value;
      const headers = new HttpHeaders({ 'Content-Type': 'application/json' });
      this.http.post('https://formspree.io/f/xdoygdkj',
        { name: email.name, replyto: email.email, message: email.messages },
        { 'headers': headers }).subscribe(
          response => {
            alert("Merci de nous avoir contacter ! Nous vous répondrons sous 48h");
          }
        );
    }
  }
}
