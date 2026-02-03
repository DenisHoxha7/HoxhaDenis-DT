import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class DeliveryService {
  private apiUrl = 'http://127.0.0.1:5000/deliveries';

  constructor(private http: HttpClient) { }

  getDeliveries(): Observable<any[]> {
    return this.http.get<any[]>(this.apiUrl);
  }

  // Aggiunto per il commit 5
  addDelivery(delivery: any): Observable<any> {
    return this.http.post(this.apiUrl, delivery);
  }
}