// Renders ad.html frame-by-frame to PNGs: node render.js <outDir> [fps]
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path'), http = require('http');
const MIME = { '.html': 'text/html', '.png': 'image/png', '.jpg': 'image/jpeg', '.js': 'text/javascript' };
(async () => {
  const out = process.argv[2] || 'frames', fps = +(process.argv[3] || 30);
  const only = process.argv[4]; // optional comma list of seconds for stills
  fs.mkdirSync(out, { recursive: true });
  // serve this folder over http so the canvas isn't tainted by file:// images
  const server = http.createServer((req, res) => {
    const f = path.join(__dirname, decodeURIComponent(req.url.split('?')[0]));
    if (!f.startsWith(__dirname) || !fs.existsSync(f)) { res.writeHead(404); return res.end(); }
    res.writeHead(200, { 'Content-Type': MIME[path.extname(f)] || 'application/octet-stream' }); fs.createReadStream(f).pipe(res);
  }).listen(0);
  const port = server.address().port;
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1920 } });
  await page.goto(`http://127.0.0.1:${port}/ad.html?render`);
  await page.evaluate(() => window.ready);
  console.log('fonts:', await page.evaluate(() => [document.fonts.check('800 100px "Baloo 2"'),document.fonts.check('100px "Kaushan Script"')]));
  const times = only ? only.split(',').map(Number) : Array.from({ length: 10 * fps }, (_, i) => i / fps);
  for (let i = 0; i < times.length; i++) {
    const data = await page.evaluate(t => { drawFrame(t); return document.getElementById('c').toDataURL('image/png'); }, times[i]);
    const name = only ? `still_${times[i]}.png` : `f_${String(i).padStart(4, '0')}.png`;
    fs.writeFileSync(path.join(out, name), Buffer.from(data.split(',')[1], 'base64'));
  }
  await browser.close(); server.close();
})();
