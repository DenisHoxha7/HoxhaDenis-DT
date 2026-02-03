import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms'; // Importa FormsModule
import { DeliveryService } from '../delivery';

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [CommonModule, FormsModule], // Aggiungi FormsModule qui
  templateUrl: './dashboard.html',
  styleUrl: './dashboard.css'
})
export class DashboardComponent implements OnInit {
  deliveries: any[] = [];
  
  // Modello per il nuovo inserimento
  newDelivery = {
    tracking_code: '',
    destinatario: '',
    indirizzo: '',
    fascia_oraria: '',
    priorita: 'LOW'
  };

  constructor(private ds: DeliveryService) {}

  ngOnInit() {
    this.loadData();
  }

  loadData() {
    this.ds.getDeliveries().subscribe(data => this.deliveries = data);
  }

  onSubmit() {
    this.ds.addDelivery(this.newDelivery).subscribe(() => {
      this.loadData(); // Ricarica la lista dopo l'inserimento
      // Reset del form
      this.newDelivery = { tracking_code: '', destinatario: '', indirizzo: '', fascia_oraria: '', priorita: 'LOW' };
    });
  }

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