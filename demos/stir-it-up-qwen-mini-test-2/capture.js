const puppeteer = require('puppeteer');
const path = require('path');

async function captureScreenshot() {
  const outputPath = path.join(__dirname, 'screenshot-final.png');
  
  const browser = await puppeteer.launch({
    headless: 'new',
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });
  
  const page = await browser.newPage();
  
  // Set viewport
  await page.setViewport({ width: 1200, height: 1600 });
  
  // Navigate to the HTML file
  const htmlPath = path.join(__dirname, 'index.html');
  await page.goto(`file://${htmlPath}`, {
    waitUntil: 'networkidle0',
    timeout: 30000
  });
  
  // Wait for fonts and images
  await new Promise(r => setTimeout(r, 2000));
  
  // Take full page screenshot
  await page.screenshot({
    path: outputPath,
    fullPage: true
  });
  
  console.log(`Screenshot saved to: ${outputPath}`);
  
  await browser.close();
}

captureScreenshot().catch(err => {
  console.error('Error:', err);
  process.exit(1);
});
