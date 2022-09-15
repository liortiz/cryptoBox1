import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { PermutacionRoutingModule } from './permutacion-routing.module';
import { PermutacionComponent } from './permutacion.component';


@NgModule({
  declarations: [
    PermutacionComponent
  ],
  imports: [
    CommonModule,
    PermutacionRoutingModule
  ]
})
export class PermutacionModule { }
