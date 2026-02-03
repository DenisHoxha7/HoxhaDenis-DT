import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class DeliveryService {
  private apiUrl = 'https://obscure-trout-jjr6vwwj9vxrhvgr-5000.app.github.dev/deliveries';

  constructor(private http: HttpClient) { }

  getDeliveries(): Observable<any[]> {
    return this.http.get<any[]>(this.apiUrl);
  }

  // Aggiunto per il commit 5
  addDelivery(delivery: any): Observable<any> {
    return this.http.post(this.apiUrl, delivery);
  }
  // Aggiunto per il commit 6
  updateStatus(id: number, status: string): Observable<any> {
    return this.http.put(`${this.apiUrl}/${id}/status`, { stato: status });
  }
}