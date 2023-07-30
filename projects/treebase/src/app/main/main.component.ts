import { AfterViewInit, Component, ElementRef } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { delay } from 'rxjs';
import { indicators } from '../indicators';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.less']
})
export class MainComponent {

  muniLogos: number[] = [];
  indicators = indicators;

  constructor() {
    for (let i = 0 ; i < 20 ; i++) {
      this.muniLogos.push(i);
    }
  }
}
