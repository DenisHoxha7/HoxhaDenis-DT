import { Component, OnInit, ChangeDetectorRef } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { DeliveryService } from '../delivery';

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './dashboard.html',
  styleUrl: './dashboard.css'
})
export class DashboardComponent implements OnInit {
  deliveries: any[] = [];
  isProcessing = false;
  newDelivery = { destinatario: '', indirizzo: '', fascia_oraria: '', priorita: 'LOW' };

  constructor(private ds: DeliveryService, private cdr: ChangeDetectorRef) {}

  ngOnInit() {
    this.loadData();
  }

  loadData() {
    this.ds.getDeliveries().subscribe({
      next: (data) => {
        this.deliveries = data;
        this.isProcessing = false; // Sblocca sempre qui
        this.cdr.detectChanges(); // FORZA AGGIORNAMENTO UI
      },
      error: (err) => {
        console.error(err);
        this.isProcessing = false;
      }
    });
  }

  generateTrackingCode(): string {
    const randomStr = Math.random().toString(36).substring(2, 8).toUpperCase();
    return `TRK-${randomStr}`;
  }

  onSubmit() {
    if (this.isProcessing) return;
    if (!this.newDelivery.destinatario || !this.newDelivery.indirizzo) {
      alert("Compila i campi obbligatori!");
      return;
    }

    this.isProcessing = true;
    const body = { ...this.newDelivery, tracking_code: this.generateTrackingCode() };

    this.ds.addDelivery(body).subscribe({
      next: () => {
        this.newDelivery = { destinatario: '', indirizzo: '', fascia_oraria: '', priorita: 'LOW' };
        this.loadData(); // Ricarica subito
      },
      error: (err) => {
        alert("Errore nell'inserimento");
        this.isProcessing = false;
      }
    });
  }

  onUpdateStatus(id: number, status: string) {
    if (this.isProcessing) return;
    this.isProcessing = true;

    this.ds.updateStatus(id, status).subscribe({
      next: () => {
        this.loadData(); // Ricarica subito dopo l'aggiornamento
      },
      error: (err) => {
        console.error(err);
        this.isProcessing = false;
      }
    });
  }
}