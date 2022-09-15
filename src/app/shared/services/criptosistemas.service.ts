import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class CriptosistemasService {
  private baseURL = 'http://127.0.0.1:5000'

  constructor(private http: HttpClient) { }

  getPermutacionE(text:String,permutation:String):Observable<any>{
    return this.http.get(`${this.baseURL}/permutacion/encript/${text}&${permutation}`)
  }


}
