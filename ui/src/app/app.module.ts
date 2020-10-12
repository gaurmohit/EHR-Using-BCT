import { BrowserModule } from "@angular/platform-browser";
import { NgModule } from "@angular/core";

import { AppRoutingModule } from "./app-routing.module";
import { AppComponent } from "./app.component";
import { BrowserAnimationsModule } from "@angular/platform-browser/animations";
import { CommonModule } from "@angular/common";
import { FormsModule, ReactiveFormsModule } from "@angular/forms";
import { DemoMaterialModule } from "./mat-includes";
import { AccountComponent } from "./account/account.component";
import { DownloadComponent } from "./download/download.component";
import { HttpClientModule } from "@angular/common/http";
import { ProfileComponent } from "./profile/profile.component";

@NgModule({
  declarations: [
    AppComponent,
    AccountComponent,
    DownloadComponent,
    ProfileComponent,
  ],
  imports: [
    CommonModule,
    BrowserModule,
    BrowserAnimationsModule,
    DemoMaterialModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule,
  ],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
