import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { DashboardComponent } from './dashboard/dashboard'; 

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, DashboardComponent],
  template: '<app-dashboard></app-dashboard>'
})
export class AppComponent {} // IL NOME DEVE ESSERE QUESTO