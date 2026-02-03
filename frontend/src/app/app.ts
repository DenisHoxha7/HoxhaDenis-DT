import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { DashboardComponent } from './dashboard/dashboard'; // Importa il componente

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, DashboardComponent], // Aggiungilo qui
  template: '<app-dashboard></app-dashboard>'   // Visualizzalo nel template
})
export class AppComponent {}