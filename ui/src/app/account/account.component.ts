import { Component, OnInit, ViewChild } from "@angular/core";
import { HttpClient } from "@angular/common/http";
import { environment as env } from "../../environments/environment";
import { MatPaginator } from "@angular/material/paginator";
import { MatTableDataSource } from "@angular/material/table";
import { MatSort } from "@angular/material/sort";
import { Process } from "../services/process";
import { HttpService } from "../services/http.service";
import { MatSnackBar } from "@angular/material/snack-bar";

export interface UserVals {
  id: number;
  previous_hash: string;
  my_hash: string;
  created_on: Date;
  UserId: string;
  Gender: string;
  Years_in_US: string;
  Maritial_Status: string;
  People_Family: string;
  People_Household: string;
  Family_income?: any;
  Household_Income: number;
  GlycoHemoglobin: string;
  ArmCircum: string;
  SaggitalAbdominal: string;
  GripStrength: string;
  Breast_fed: string;
  Taking_Insulin: string;
  Taking_Oral_Agents: string;
  Eyes_Affected: string;
  Recent_BP: number;
  Diabetes: string;
}

@Component({
  selector: "app-account",
  templateUrl: "./account.component.html",
  styleUrls: ["./account.component.scss"],
})
export class AccountComponent implements OnInit {
  dataSource = new MatTableDataSource<UserVals>([]);
  displayedColumns = ["id", "UserId", "action"];

  @ViewChild(MatPaginator, { static: true }) paginator: MatPaginator;
  @ViewChild(MatSort, { static: true }) sort: MatSort;

  constructor(
    private http: HttpClient,
    private HS: HttpService,
    public SBS: MatSnackBar
  ) {
    console.log(this);
  }

  ngOnInit(): void {
    this.getAccounts();
    this.dataSource.paginator = this.paginator;
    this.dataSource.sort = this.sort;
  }

  async getAccounts() {
    let acc = await this.http
      .get<UserVals[]>(env.server.base + "block/user-list/?start=0")
      .toPromise();
    this.dataSource.data = acc;
  }

  applyFilter(event: Event) {
    const filterValue = (event.target as HTMLInputElement).value;
    this.dataSource.filter = filterValue.trim().toLowerCase();
  }

  individual_status = 0;
  download_user_data(uid, method = "k") {
    let p = new Process(this.HS, method, uid);
    p.download();
    const subs = p.$status.subscribe((s) => {
      this.individual_status = s;
      this.SBS.open(
        [
          "",
          "Finished Data Processing, downloading file",
          "Processing",
          "Finding Data",
        ][s],
        "Ok",
        {
          duration: 3000,
        }
      );
      // if (s == 1 || s == 4) subs.unsubscribe();
    });
  }

  async createAccount() {
    let res = await this.HS.get("block/create-user/");
    if (res.error) {
      this.SBS.open(res.message, "Ok", {
        duration: 10 * 1000,
      });
      return;
    } else {
      this.SBS.open(res.message, "Ok");
      this.dataSource.data.push(res.result);
      this.sort.start = "desc";
    }
  }
}
