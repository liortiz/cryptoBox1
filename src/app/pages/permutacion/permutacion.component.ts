import { Component, OnInit } from '@angular/core';
import {CriptosistemasService} from '../../shared/services/criptosistemas.service'

@Component({
  selector: 'app-permutacion',
  templateUrl: './permutacion.component.html',
  styleUrls: ['./permutacion.component.css']
})
export class PermutacionComponent implements OnInit {

  constructor(private coneccion: CriptosistemasService) { }

  ngOnInit(): void {
    this.coneccion.getPermutacionE('hola','0,2')
    .subscribe(data=>{
      console.log(data)
    },
    error=>console.log(error))
  }

}
