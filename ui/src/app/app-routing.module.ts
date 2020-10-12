import { NgModule } from "@angular/core";
import { Routes, RouterModule } from "@angular/router";
import { AccountComponent } from "./account/account.component";
import { ProfileComponent } from "./profile/profile.component";

const routes: Routes = [
  { path: "", pathMatch: "full", redirectTo: "home" },
  { path: "home", component: AccountComponent },
  { path: "profile/:id", component: ProfileComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
