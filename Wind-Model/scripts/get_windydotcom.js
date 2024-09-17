/**
 * Good luck finding out how this works! 😂
 */
import puppeteer from 'puppeteer';
import fs from 'fs';



let _GBL_IND_AMT = 1;
let p_queue = []
let p_queue_len = 10;
let _last_text = ""

let OUTPUT = []


const clear_and_print = (text) => { 
  console.log(`\x1b[2J`)
  console.log(text)
  _last_text = text;
}


const clear_queue = () => {
  p_queue = []
}

const sub_print = (text) => {
  let out = " ".repeat(_GBL_IND_AMT*2) + "└── " + text
  console.log(out);
}

const sub_inc = () => {
  _GBL_IND_AMT++;
}

const sub_reset = () => {
  _GBL_IND_AMT = 1;
}

const rewrite_line = (text) => {
  process.stdout.write(text);
}

const ISS_SDA = "\x1b[1m\x1b[31mISS-SDA   \x1b[0m"
const PUPPETEER = "\x1b[1m\x1b[33mPUPPETEER   \x1b[0m"

const zoomed_uri = "https://www.windy.com/-Menu/menu?37.119,-99.844,4,m:"
const pin_key = 'eD4acSO'; // get this by clicking :)

const uri = zoomed_uri + pin_key;

const read_label = async (page) => {
  return new Promise(async function(myResolve, myReject) {
    // "Producing Code" (May take some time)
      const searchResultSelector = '.picker-content > span:nth-child(1) > big:nth-child(2)';
      let inner_text = await page.$eval(searchResultSelector, (element) => {
        return element.innerHTML
      });

      // extract knots
      const extract_num = /^[^<]*/g;
      const extract_rot = /[0-9]*(?=deg)/;

      let ws_num = Number(inner_text.match(extract_num)[0].trim());
      let wd_rot = (Number(inner_text.match(extract_rot)[0].trim()) + 180) % 360;

      myResolve([ws_num, wd_rot]);
    });
}

const read_hover_label = async (page) => {

  return new Promise(async function(myResolve, myReject) {
    // "Producing Code" (May take some time)
    const selector = "div.timecode:nth-child(2) > div:nth-child(1)"
      let inner_text = await page.$eval(selector, (element) => {
        return element.innerHTML
      });

      myResolve(inner_text);
    });
}

const read_alt_label = async (page) => {

  return new Promise(async function(myResolve, myReject) {
    // "Producing Code" (May take some time)
    const selector = "#menu-levels > div:nth-child(1)"
      let inner_text = await page.$eval(selector, (element) => {
        return element.innerHTML
      });

      myResolve(inner_text);
    });
}

const unselect = async (page) => {

  return new Promise(async function(myResolve, myReject) {
    // "Producing Code" (May take some time)
    const selector = "#menu-levels"
    let elem = await page.waitForSelector(selector)
    elem.click();

    myResolve();
    });
}

const read_time_label = async (page) => {

  return new Promise(async function(myResolve, myReject) {
    // "Producing Code" (May take some time)
    const selector = "div.timecode:nth-child(3) > div:nth-child(1)"
      let inner_text = await page.$eval(selector, (element) => {
        return element.innerHTML
      });


      myResolve(inner_text);
    });


}

const increment_slider = async (page, selector) => {
  return new Promise(async function(myResolve, myReject) {
    // more elegant way of incrementing a slider.
    await page.focus(selector)
    await page.keyboard.press('ArrowRight');
    await page.$eval(selector, e => e.blur());

    myResolve();
  });
}

const drag_slider = async (page, selector, percentage) => {
  return new Promise(async function(myResolve, myReject) {

      const sliderElement = await page.$(selector);
      const pos = await sliderElement.asElement().boundingBox();

      await page.mouse.click(
        pos.x + percentage * pos.width,
        pos.y
      );


      await page.$eval(selector, e => e.blur());


      myResolve();
    });
}

(async () => {
  // Launch the browser and open a new blank page
  clear_and_print(`${ISS_SDA} Spinning up weather scraper backend`);
  const browser = await puppeteer.launch({headless: false});
  sub_print(`${PUPPETEER} Navigating..`);
  const page = await browser.newPage();

  // Navigate the page to a URL
  await page.goto(uri);
  await page.setViewport({width: 4000, height: 2000}); // comically large so we can click the damn timestamps
  sub_print(`${PUPPETEER} Awaiting page load..`);
  await new Promise(r => setTimeout(r, 10000));
  await read_label(page); // test that label has loaded
  clear_and_print(`${ISS_SDA} Scraping...\n\n`);

  // READY TO SCRAPE!

  const TOTAL_DAYS = 10

  const DAYS = 1 // days to forecast
  const IND_PER_DAY = 3
  const TIME_INDICES = DAYS * IND_PER_DAY;
  const TIME_WIDTH = TOTAL_DAYS * IND_PER_DAY;
  const ALT_INDICES = 16;
  const time_bar_selector = ".avbl";
  const altitude_bar_selector = "input.noselect"

  const pct = 0
  drag_slider(page, time_bar_selector, pct);
  await page.keyboard.press('ArrowLeft');
  await new Promise(r => setTimeout(r, 2000));

  // For every time..
  for(let time_ind = 0; time_ind < TIME_INDICES; time_ind++) {

    let cur_time = await read_time_label(page);
    console.log(`${ISS_SDA} Updated scraper timestamp to "${cur_time}"`);

    let TIME_OUTPUT = {altitudes: [], speeds: [], directions: [], time: cur_time}


    // For every altitude...
    for(let alt_ind = 0; alt_ind < ALT_INDICES; alt_ind++) {
      console.log(`${ISS_SDA} Scraping datapoint (${1 + alt_ind + (time_ind*ALT_INDICES)}/${ALT_INDICES*TIME_INDICES})`);
      console.log(`${PUPPETEER} Edit element ${altitude_bar_selector} to value ${alt_ind}`);

      const percentage = (alt_ind/ALT_INDICES); // adjust slider percentage;

      drag_slider(page, altitude_bar_selector, percentage);

      await new Promise(r => setTimeout(r, 2500));
      let [ws, wd] = await read_label(page);
      let alt = await read_alt_label(page);

      console.log(`${ISS_SDA} [Altitude ${alt}] Logged ${ws} knots @ ${wd} degrees (Timestamp "${cur_time}") (${alt_ind+1}/${ALT_INDICES})`);

      TIME_OUTPUT.altitudes.push(alt);
      TIME_OUTPUT.speeds.push(ws);
      TIME_OUTPUT.directions.push(wd);

    }

    OUTPUT.push(TIME_OUTPUT)

    console.log(`${PUPPETEER} Press (->) (Index ${time_ind}/${TIME_INDICES})`);

    await page.keyboard.press('ArrowRight');
    await new Promise(r => setTimeout(r, 2000));


  }

  console.log(`${ISS_SDA} Writing output..`);

  let filename = "output_" + Date.now() + "_FAR" + ".json" 
  fs.writeFileSync("../extern/" + filename, JSON.stringify(OUTPUT))


  // STOP SCRAPING, CLEANUP

  console.log(`${ISS_SDA} Done! Data written to '${filename}'`);
  await new Promise(r => setTimeout(r, 1000));


  await browser.close();
})();
