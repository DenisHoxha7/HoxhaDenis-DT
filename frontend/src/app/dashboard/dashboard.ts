import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { DeliveryService } from '../delivery'; // Importa il tuo service

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './dashboard.html', // Controlla se il tuo file si chiama così o dashboard.component.html
  styleUrl: './dashboard.css'     // Controlla se il tuo file si chiama così o dashboard.component.css
})
export class DashboardComponent implements OnInit {
  deliveries: any[] = [];

  constructor(private deliveryService: DeliveryService) {}

  ngOnInit(): void {
    this.loadDeliveries();
  }

  loadDeliveries() {
    this.deliveryService.getDeliveries().subscribe({
      next: (data) => this.deliveries = data,
      error: (err) => console.error('Errore API:', err)
    });
  }

  // Funzione per gestire i colori dei bordi richiesti dal prof
  getBorderColor(stato: string): string {
    switch (stato) {
      case 'READY': return 'grey';
      case 'OUT_FOR_DELIVERY': return 'blue';
      case 'DELIVERED': return 'green';
      case 'FAILED': return 'red';
      default: return 'black';
    }
  }
}