import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators} from '@angular/forms';
import {CriptosistemasService} from '../../shared/services/criptosistemas.service'

@Component({
  selector: 'app-permutacion',
  templateUrl: './permutacion.component.html',
  styleUrls: ['./permutacion.component.css']
})


export class PermutacionComponent implements OnInit {
  formPermutation: FormGroup;
  permutation = {text:"",key:""}
  text: string;
  key: string;
  textEncrypt: string = '';



  constructor(private coneccion: CriptosistemasService, private formBuilder: FormBuilder) { 
    this.text = '';
    this.key = '';
    this.formPermutation = this.formBuilder.group({
      text:["",Validators.compose([Validators.required])],
      key:["",Validators.compose([Validators.required])]
    })
  }  
  
  ngOnInit(): void {    
  }

  capturarValores(){
    if(this.formPermutation.valid){
      this.permutation = this.formPermutation.getRawValue();
    this.coneccion.getPermutacionE(this.permutation.text,this.permutation.key)
    .subscribe(data=>{
      this.textEncrypt = data.TextoEncriptado;
    },
    error=>console.log(error))

    }
    
    
  //console.log(this.textEncrypt);
  }
  

}
