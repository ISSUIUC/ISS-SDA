import React from 'react';
import Plot from 'react-plotly.js';

export default function Chart(props) {
  return (
  <div>
        <Plot
          data={[
            {
              x: props.xdata,
              y: props.ydata,
              type: 'scatter',
              mode: 'lines+markers',
              marker: {color: 'red'},
            }
          ]}
          layout={ {width: 500, height: 375, title: props.title } }
        />
  </div>
  );
}