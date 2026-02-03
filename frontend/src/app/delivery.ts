import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class DeliveryService {
  // In Codespaces usa l'URL pubblico della porta 5000 se necessario
  private apiUrl = 'http://127.0.0.1:5000/deliveries';

  constructor(private http: HttpClient) { }

  getDeliveries(): Observable<any[]> {
    return this.http.get<any[]>(this.apiUrl);
  }
}