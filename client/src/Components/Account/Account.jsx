import React, { useState } from "react";
import "./account.css";
import BarChart from "../Reusables.jsx/BarChart";
import SimpleLineChart from "../Reusables.jsx/LineChart";
import MultilineEditing from "../Reusables.jsx/Table";
import HorizontalBars from "../Reusables.jsx/BarChart";

function Account() {
  const [addIncident, setAddIncident] = useState(false);
  const uData = [4000, 3000, 2000, 2780, 1890, 2390, 3490];
  const pData = [2400, 1398, 9800, 3908, 4800, 3800, 4300];
  const trafficChartLabels = [
    "Jan",
    "Feb",
    "Mat",
    "Apri",
    "May",
    "June",
    "July",
    "Aug",
    "Oct",
    "Nov",
    "Dec",
  ];

  const trafficChartData = [{ data: pData, label: "Incidents" }];

  const incident = [
    { title: "No Water", amount: 20 },
    { title: "Vandalism", amount: 10 },
    { title: "Leaks and Bursts", amount: 50 },
    { title: "Meter Theft", amount: 38 },
    { title: "HR Issue", amount: 10 },
    { title: "OSH Activity", amount: 24 },
  ];

  const incidentLocation = [
    { title: " Milimani", amount: 23 },
    { title: "CBD", amount: 30 },
    { title: "Manyatta", amount: 20 },
    { title: "Meter Theft", amount: 28 },
    { title: "Kenya Re", amount: 19 },
    { title: "Kibuye", amount: 24 },
    { title: "Kisat", amount: 22 },
    { title: " Kajulu", amount: 34 },
  ];

  const AddIncident = () => {
    return (
      <div className="new-i-cnt">
        <form className="new-i">
          <div className="new-i-head">
            <h1>Add incident</h1>
            <span
              className="material-symbols-outlined"
              onClick={() => setAddIncident(false)}
            >
              close
            </span>
          </div>
          <div className="i-type-info">
            <div className="select-card">
              Incident type
              <select name="incident_type" id="">
                <option value="No Water">No Water</option>
                <option value="Vandalism">Vandalism</option>
                <option value="Leaks and Bursts">Leaks and Bursts</option>
                <option value="Meter Theft">Meter Theft</option>
                <option value="HR Issue">HR Issue</option>
                <option value=" OSH Activity"> OSH Activity</option>
              </select>
            </div>
            <div className="select-card">
              Incident location
              <select name="incident_location" id="">
                <option value="Milimani">Milimani</option>
                <option value="CBD">CBD</option>¨
                <option value="Riat"> Riat</option>
                <option value="Manyatta">Manyatta</option>
                <option value="Kenya Re">Kenya Re</option>
                <option value="Head Office">Head Office</option>
                <option value="Kibuye">Kibuye</option>
                <option value="Kisat">Kisat</option>
                <option value="Kajulu">Kajulu</option>
              </select>
            </div>
          </div>
          <textarea name="incident_type" id=""></textarea>
        </form>
      </div>
    );
  };

  return (
    <div className="account-cnt">
      {addIncident && <AddIncident />}
      <div className="account-body">
        <ul className="ab-head">
          <li>
            <h1>Reporter</h1>
          </li>
          <li>
            <div className="ac-user-info">
              John doh <span className="material-symbols-outlined">person</span>
            </div>
            <button>Log out</button>
          </li>
        </ul>
        <section className="bc-head">
          <h2>Report statistics</h2>{" "}
          <button onClick={() => setAddIncident(true)}>New report</button>
        </section>
        <section className="report-charts">
          <div className="chart-card">
            <SimpleLineChart
              data={trafficChartData}
              labels={trafficChartLabels}
            />
          </div>

          <div className="chart-card">
            <HorizontalBars dataset={incident} label={"Incident Type"} />
          </div>

          <div className="chart-card">
            <HorizontalBars
              dataset={incidentLocation}
              label={"Incident Location"}
            />
          </div>
        </section>
        <section className="incidents">
          <MultilineEditing />
        </section>
      </div>
    </div>
  );
}

export default Account;
