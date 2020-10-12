import { Component, OnInit, OnDestroy } from "@angular/core";
import { ActivatedRoute } from "@angular/router";
import { UserVals } from "../account/account.component";
import { BehaviorSubject, Subscription } from "rxjs";
import { HttpService } from "../services/http.service";
import { stringify } from "querystring";
import { HttpParams } from "@angular/common/http";

@Component({
  selector: "app-profile",
  templateUrl: "./profile.component.html",
  styleUrls: ["./profile.component.scss"],
})
export class ProfileComponent implements OnInit, UserVals, OnDestroy {
  UserId;
  id: number;
  previous_hash: string;
  my_hash: string;
  created_on: Date;
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

  chain: Chain;
  subscriber: Subscription;

  constructor(private router: ActivatedRoute, private HS: HttpService) {
    router.params.subscribe((param) => {
      this.UserId = param.id;
      this.chain = new Chain(HS, this.UserId);
      this.chain.fetchDetails();
      this.subscriber = this.chain.$updates.subscribe((blocks) => {
        console.log(blocks);

        if (blocks.length != 0) this.set(this.chain.compile());
      });
    });
  }
  ngOnInit(): void {}

  update() {
    this.chain.update(this);
  }

  ngOnDestroy() {
    this.subscriber.unsubscribe();
  }
  keys(d) {
    return Object.keys(d);
  }
  s(d) {
    return String(d);
  }
  set(v: UserVals) {
    for (let x in v) {
      this[x] = v[x];
    }
  }
}

export class Block {
  verified: boolean;
  data: UserVals;
}

export class Chain {
  data: Block[] = [];
  $updates: BehaviorSubject<Block[]> = new BehaviorSubject([]);
  constructor(private HS: HttpService, public UserId: Number) {}
  async fetchDetails() {
    let res = await this.HS.get("block/fetch/" + this.UserId + "/");
    // console.log(chain);
    if (res.error) {
      console.log(console.log(res));
      return;
    }
    this.data = res.result;
    this.$updates.next(this.data);
  }
  async update(data: UserVals) {
    let fields = [
      "Gender",
      "Years_in_US",
      "Maritial_Status",
      "People_Family",
      "People_Household",
      "Family_income",
      "Household_Income",
      "GlycoHemoglobin",
      "ArmCircum",
      "SaggitalAbdominal",
      "GripStrength",
      "Breast_fed",
      "Taking_Insulin",
      "Taking_Oral_Agents",
      "Eyes_Affected",
      "Recent_BP",
      "Diabetes",
      "medication",
      "age",
      "native_country",
      "occupation",
      "race",
      "workclass",
    ];
    let params = {};
    for (let f of fields) {
      console.log("Setting", f, data[f]);
      params[f] = data[f] + "";
    }
    // params.set('UserId', this.UserId+'');
    let res = await this.HS.post("block/update/" + this.UserId + "/", params);
    this.data = res.result;
    console.log(res, this.data);
    this.$updates.next(this.data);
  }
  compile(): UserVals {
    if (this.data.length != 0) return this.data[0].data;
    return null;
  }
}
