import { HttpService } from "./http.service";
import { BehaviorSubject } from "rxjs";
import { HttpParams } from "@angular/common/http";
import { MatSnackBar } from "@angular/material/snack-bar";

export class Process {
  count = 0;
  status = 0;
  $status = new BehaviorSubject(0);
  constructor(
    private HS: HttpService,
    public type: string,
    public user: string
  ) {}
  async download() {
    this.status = 3;
    this.$status.next(this.status);

    let res1 = await this.HS.post("block/add-process/", {
      user: this.user,
      type: this.type,
    });
    if (res1.error) {
      console.log("Error occurred");
    }
    this.status = 2;
    this.$status.next(this.status);
    while (!res1.error) {
      let res2 = await this.HS.get("block/status/?id=" + res1.id);
      if (res2.status == 4) {
        console.log("No such id found");
        return;
      } else {
        if (res2.status == 1) {
          this.status = 1;
          this.$status.next(this.status);

          window.open(
            this.HS.env.server.base + "block/download-finished/?id=" + res1.id,
            "_blank"
          );
          return;
        }
      }
      await this.pause(2000);
      this.count++;
      if (this.count > 20) return;
    }
  }

  pause(t = 1000) {
    return new Promise((resolve) => {
      setTimeout(() => resolve(), t);
    });
  }
}
