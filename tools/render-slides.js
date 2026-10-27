// Render every <section class="slide" id="..."> in an HTML file to <id>.png (1080x1350).
// usage: node tools/render-slides.js channels/instagram/posts/001-intro/slides.html
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const html = path.resolve(process.argv[2]);
  const outdir = path.dirname(html);
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1350 } });
  await page.goto('file://' + html);
  await page.evaluate(() => document.fonts.ready);
  for (const id of await page.$$eval('section.slide', els => els.map(e => e.id))) {
    await page.locator('#' + id).screenshot({ path: path.join(outdir, id + '.png') });
    console.log(id + '.png');
  }
  await browser.close();
})();
