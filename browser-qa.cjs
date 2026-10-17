const {chromium}=require('C:/Users/adamh/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const fs=require('node:fs');const assert=require('node:assert/strict');
(async()=>{const browser=await chromium.launch({executablePath:'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe',headless:true});
fs.mkdirSync('../review',{recursive:true});const results=[];
for(const width of [1440,390,320]){const page=await browser.newPage({viewport:{width,height:1000},javaScriptEnabled:false});await page.goto('file:///'+process.cwd().replaceAll('\\','/')+'/index.html');
assert(await page.locator('#find-food').isVisible());assert.equal(await page.locator('.location').count(),4);
const overflow=await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth);assert(!overflow,`overflow at ${width}`);
const broken=await page.locator('a[href^="#"]').evaluateAll(as=>as.filter(a=>a.hash && !document.getElementById(a.hash.slice(1))).map(a=>a.hash));assert.deepEqual(broken,[]);
await page.getByRole('link',{name:'Find food',exact:true}).first().click();assert(page.url().endsWith('#find-food'));
const disclosure=page.locator('summary').filter({hasText:'Questions to settle before listing a host'});assert(await disclosure.isVisible());
await disclosure.click();assert(await page.locator('details').getAttribute('open')!==null);
const mail=await page.getByRole('link',{name:'Email a correction'}).getAttribute('href');assert(mail.startsWith('mailto:adam.hind005@gmail.com?subject=Food%20Share%20Correction&body='));
await disclosure.click();await page.evaluate(()=>scrollTo(0,0));
await page.screenshot({path:`../review/${width}-viewport.png`});
await page.screenshot({path:`../review/${width===1440?'desktop':width===390?'mobile':'small-mobile'}.png`,fullPage:true});
results.push({width,jsDisabled:true,overflow,locationCards:4,anchors:'passed',hostDisclosure:'passed',correctionURI:'passed (not sent)'});await page.close();}
await browser.close();fs.writeFileSync('../review/browser-results.json',JSON.stringify(results,null,2));console.log(results);
})().catch(e=>{console.error(e);process.exit(1)});
