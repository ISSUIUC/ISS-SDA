import React, { useState } from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import Plot from 'react-plotly.js';
import Helmet from 'react-helmet';
import Chart from './chart.js'
import main_data from './main_data.json' 

const WindModel = () => {
  const [stagesepalt, setStageSepAlt] = useState(0);
  const [susignalt, setSusIgnAlt] = useState(0);
  const [windcutoff, setWindCutoff] = useState(0);


  const rows = [];

  for (let i = 0; i <= 11; i += 3) {
    // CHANGE THIS LINE TO USE THE DATA YOU WANT
    const rowData = main_data.slice(i, i + 3); 

    rows.push(
      <tr>
        {rowData.map(({ x, y, title }) => (
          <td>
            <Chart xdata={x} ydata={y} title={title} ssalt={stagesepalt} sialt={susignalt} wc={windcutoff} />
          </td>
        ))}
      </tr>
    );
  }

  return (
    <div>
      <div>

        <div className='top-flex'>
          <div className='top-flex-title'>
            <div>
              <img src={require("./spaceshot_logo_highres_720.png")} alt="spaceshot logo" width="139" height="180"></img>
            </div>
            <div className='top-flex-title-elem'>
              <div>Illinois Space Society Spaceshot</div>
              <div className='big-title'>SDA Wind Model</div>
            </div>
          </div>
          <div className='data-entry-wrap'>
            <div className='data-entry'>
              <b>Data inputs</b>
              <div className='data-entry-row'>
                <div>Stage Sep Altitude: </div>
                <div><input type='number' value={stagesepalt} onChange={(v) => {setStageSepAlt(v.target.value)}}/></div>
              </div>
              <div className='data-entry-row'>
                <div>Sustainer Ignition Altitude: </div>
                <div><input type='number' value={susignalt} onChange={(v) => {setSusIgnAlt(v.target.value)}}/></div>
              </div>
              <div className='data-entry-row'>
                <div>Wind speed cutoff: </div>
                <div><input type='number' value={windcutoff} onChange={(v) => {setWindCutoff(v.target.value)}}/></div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
        <table border="5">
          <tbody>
            {rows}
          </tbody>
        </table>
      </div>
    </div>
  );
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <WindModel />
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
