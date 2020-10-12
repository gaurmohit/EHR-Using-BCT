import { Component, OnInit } from "@angular/core";
import { Process } from "../services/process";
import { HttpService } from "../services/http.service";
import { MatSnackBar } from "@angular/material/snack-bar";

@Component({
  selector: "app-download",
  templateUrl: "./download.component.html",
  styleUrls: ["./download.component.scss"],
})
export class DownloadComponent implements OnInit {
  constructor(private HS: HttpService, private SBS: MatSnackBar) {}

  ngOnInit(): void {}
  download(method = "k") {
    let p = new Process(this.HS, method, "all");
    p.download();
    p.$status.subscribe((s) => {
      this.SBS.open(
        [
          "",
          "Finished Data Processing, downloading file",
          "Processing",
          "Finding Data",
        ][s],
        "Ok",
        {
          duration: 100000,
        }
      );
      // if (s == 1 || s == 4) subs.unsubscribe();
    });
  }
}
