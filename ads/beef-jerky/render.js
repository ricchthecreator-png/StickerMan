// Renders ad.html frame-by-frame to PNGs: node render.js <outDir> [fps]
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
(async () => {
  const out = process.argv[2] || 'frames', fps = +(process.argv[3] || 30);
  const only = process.argv[4]; // optional comma list of seconds for stills
  fs.mkdirSync(out, { recursive: true });
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1920 } });
  await page.goto('file://' + path.resolve(__dirname, 'ad.html') + '?render');
  await page.evaluate(() => window.ready);
  console.log('Anton loaded:', await page.evaluate(() => document.fonts.check('100px Anton')));
  const times = only ? only.split(',').map(Number) : Array.from({ length: 10 * fps }, (_, i) => i / fps);
  for (let i = 0; i < times.length; i++) {
    const data = await page.evaluate(t => { drawFrame(t); return document.getElementById('c').toDataURL('image/png'); }, times[i]);
    const name = only ? `still_${times[i]}.png` : `f_${String(i).padStart(4, '0')}.png`;
    fs.writeFileSync(path.join(out, name), Buffer.from(data.split(',')[1], 'base64'));
  }
  await browser.close();
})();
