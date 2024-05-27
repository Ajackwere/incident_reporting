import * as React from "react";
import { BarChart } from "@mui/x-charts/BarChart";

const chartSetting = {
  xAxis: [
    {
      label: "Units",
    },
  ],
};

const valueFormatter = (value) => `${value}units`;

export default function HorizontalBars({ dataset, label }) {
  return (
    <BarChart
      dataset={dataset}
      yAxis={[{ scaleType: "band", dataKey: "title" }]}
      series={[{ dataKey: "amount", label: label, valueFormatter }]}
      layout="horizontal"
      {...chartSetting}
    />
  );
}
