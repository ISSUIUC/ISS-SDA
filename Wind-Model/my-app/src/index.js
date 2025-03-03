import React, { useState } from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import Plot from 'react-plotly.js';
import Helmet from 'react-helmet';
import Chart from './chart.js'
import main_data from './main_data.json' 

const Datarow = ({stat, label, value}) => {
  return <div className={`wm-datarow wm-datarow-${stat}`}>
    <div className='wm-datarow-label'>{label}</div>
    <div className='wm-datarow-value'>{value}</div>
  </div>
}

const WindAnalysisText = ({alts, windspeeds, cutoffs}) => {
  let [ssalt, sialt, wc] = cutoffs;

  if(ssalt == "") {
    ssalt = 0;
  }

  if(sialt == "") {
    sialt = 0;
  }
  if(wc == "") {
    wc = 0;
  }

  const ground_speed = windspeeds[0]
  const gs_stat = (ground_speed < wc) ? (ground_speed < wc*0.85 ? "OK" : "MED") : "BAD"
  const MAX_ALT = Math.max(...alts)

  const get_val_at_alt = (alt) => {
    if(alt > MAX_ALT || alt < 0) {
      return 0;
    }

    const key = Math.floor(alt/100)
    return windspeeds[key]
  }

  const ssalt_value = get_val_at_alt(ssalt);
  const sialt_value = get_val_at_alt(sialt);

  return (<>
  <div className='wm-datarows'>
    <b>Wind data for critical altitudes:</b>
    <Datarow stat={gs_stat} label={"GROUND (x = 0ft)"} value={ground_speed.toFixed(2) + " mph"} />
    <Datarow stat={"NONE"} label={`STAGE SEPERATION (x = ${ssalt.toFixed(0)}ft)`} value={ssalt_value.toFixed(2) + " mph"} />
    <Datarow stat={"NONE"} label={`SUSTAINER IGNITION (x = ${sialt.toFixed(0)}ft)`} value={sialt_value.toFixed(2) + " mph"} />
  </div>

  </>);
}

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
            <Chart key={title+"-1"} xdata={x} ydata={y} title={title} ssalt={stagesepalt} sialt={susignalt} wc={windcutoff} />
            <WindAnalysisText key={title} alts={x} windspeeds={y} cutoffs={[Number(stagesepalt), Number(susignalt), Number(windcutoff)]} />
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
