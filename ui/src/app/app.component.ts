import { Component } from "@angular/core";
import { HttpService } from "./services/http.service";
import { Process } from "./services/process";

@Component({
  selector: "app-root",
  templateUrl: "./app.component.html",
  styleUrls: ["./app.component.scss"],
})
export class AppComponent {
  title = "ui";
  constructor(private HS: HttpService) {}
}
