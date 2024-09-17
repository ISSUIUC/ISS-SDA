import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import Plot from 'react-plotly.js';
import Helmet from 'react-helmet';
import Chart from './chart.js'
import windData from './wind_data.json';
import farDataTest from './far_wind_data_test.json';
import farDataTestNew from './far_wind_data_test5_22.json';
import stormglassData from "./sg_wind_data.json";
import interweaved from './interweaved.json';
import far529 from './far_5.29.json';
import fartest from './manually_input_interweave.json';
import almostdone from './almost_done.json';
import justwindy from './just_windy.json';
import finalhopefully from './finalhopefully.json';
import fixedinterweave from './fixedinterweave.json';
import final from './FAR_TIME.json';
import last from './lastone.json';
import am645 from './645am.json';
import sunday2 from './sunday2.json';
import june2 from './6_2.json';
import june2_2 from './6_2_522am.json';

class WindModel extends React.Component {
  render() {

    const rows = [];

    for (let i = 0; i <= 11; i += 3) {
      // CHANGE THIS LINE TO USE THE DATA YOU WANT
      const rowData = june2_2.slice(i, i + 3); 

      rows.push(
        <tr>
          {rowData.map(({ x, y, title }) => (
            <td>
              <Chart xdata={x} ydata={y} title={title} />
            </td>
          ))}
        </tr>
      );
    }

    return (
      <div>
        <div>
          <table border="0" width="100%">
            <tr>
              <td rowspan="2" width="10%">
                <img src={require("./spaceshot_logo_highres_720.png")} alt="spaceshot logo" width="139" height="180"></img>
              </td>
              <td style={{ textAlign: 'center' }}>
                <h1 style={ {fontSize: "40px" } }>Illinois Space Society Spaceshot</h1>
              </td>
            </tr>
            <tr>
              <td style={{ textAlign: 'center' }}>
                <h1 style={ {fontSize: "35px" } }>SDA Wind Model</h1>
              </td>
            </tr>
          </table>
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
