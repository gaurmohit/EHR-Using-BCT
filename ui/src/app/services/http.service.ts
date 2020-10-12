import { Injectable } from "@angular/core";
import { HttpClient, HttpHeaders, HttpParams } from "@angular/common/http";
import { environment as env } from "../../environments/environment";

@Injectable({
  providedIn: "root",
})
export class HttpService {
  public env = env;
  constructor(private http: HttpClient) {
    // this.post("block/add-process/", { user: "all", type: "k" });
  }
  async get(url) {
    let result = await this.http
      .get<any>(this.env.server.base + url)
      .toPromise();
    if (result.error) {
      console.log("Some error occurred", result);
      return result;
    } else return result;
  }
  async post(url, data) {
    // console.log(data);
    // let options = new RequestOptions();
    let result: any = await this.http
      .post(this.env.server.base + url, data, {
        headers: new HttpHeaders({ "Content-Type": "application/json" }),
        observe: "body",
        params: data,
      })
      .toPromise();
    if (result.error) {
      console.log("Some error occurred", result);
      return result;
    } else return result;
  }
}
