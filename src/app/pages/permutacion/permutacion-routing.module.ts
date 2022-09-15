import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { PermutacionComponent } from './permutacion.component';

const routes: Routes = [{ path: '', component: PermutacionComponent }];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class PermutacionRoutingModule { }
