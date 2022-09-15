import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ReactiveFormsModule ,FormsModule } from '@angular/forms';

import { PermutacionRoutingModule } from './permutacion-routing.module';
import { PermutacionComponent } from './permutacion.component';


@NgModule({
  declarations: [
    PermutacionComponent
  ],
  imports: [
    CommonModule,
    PermutacionRoutingModule, 
    FormsModule,
    ReactiveFormsModule
  ]
})
export class PermutacionModule { }
