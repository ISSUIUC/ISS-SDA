import React from 'react';
import Plot from 'react-plotly.js';

const create_vline = (x, color) => {
  return {
      type: 'line',
      x0: x,
      y0: 0,
      x1: x,
      y1: 1,
      xref: 'x',
      yref: 'paper',
      line: {
        color: color,
        width: 1,
        dash: 'dash',
      }
    }
}

const create_hline = (y, color) => {
  return {
      type: 'line',
      x0: 0,
      y0: y,
      x1: 1,
      y1: y,
      xref: 'paper',
      yref: 'y',
      line: {
        color: color,
        width: 2,
        dash: 'dash',
      }
    }
}

export default function Chart(props) {

  let shapes = [];
  if(props.ssalt != 0) {
    shapes.push(create_vline(props.ssalt, "blue"))
  }

  if(props.sialt != 0) {
    shapes.push(create_vline(props.sialt, "green"))
  }

  if(props.wc != 0) {
    shapes.push(create_hline(props.wc, "red"))
  }
  

  return (
  <div>
        <Plot
          data={[
            {
              x: props.xdata,
              y: props.ydata,
              type: 'scatter',
              mode: 'lines+markers',
              marker: {color: 'black', size: 1},
            }
          ]}
          layout={ {shapes: shapes, width: 500, height: 375, title: props.title, xaxis: {title: "Altitude (ft)"}, yaxis: {title: "Wind speed (mph)"} } }
        />
  </div>
  );
}