// Local-only defence-in-depth fixtures. Never sends probes to published sites.
const fs=require('node:fs'),http=require('node:http'),assert=require('node:assert/strict');
const {chromium}=require('C:/Users/adamh/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const html=fs.readFileSync('index.html','utf8');
assert(html.includes('http-equiv="Content-Security-Policy"'),'CSP must exist');
assert(html.includes('name="referrer" content="no-referrer"'));
const fixture='<base href="http://127.0.0.1:1/"><script>window.injected=true</script><script src="/trap-script"></script><img src="/missing" onerror="window.injected=true"><iframe src="/trap-frame"></iframe><a id="attack" href="javascript:window.injected=true">fixture</a><form action="/trap-form"><button id="submit">fixture</button></form>';
const hits=[];
const server=http.createServer((req,res)=>{hits.push(req.url);res.setHeader('Content-Type','text/html; charset=utf-8');res.end(req.url.startsWith('/fixture')?html.replace('</body>',fixture+'</body>'):html)});
(async()=>{await new Promise(r=>server.listen(0,'127.0.0.1',r));let b;try{
 b=await chromium.launch({executablePath:'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe',headless:true});
 const p=await b.newPage();const origin='http://127.0.0.1:'+server.address().port;
 await p.route('**/*',r=>new URL(r.request().url()).origin===origin?r.continue():r.abort());
 await p.goto(origin+'/?q='+encodeURIComponent('<span id=fixture-query>query-marker-713</span>')+'#'+encodeURIComponent('<span id=fixture-fragment>fragment-marker-713</span>'));
 assert.equal(await p.locator('.location').count(),4);await p.evaluate(()=>new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r))));
 assert.equal(await p.evaluate(()=>window.injected),undefined);
 assert.equal(await p.locator('#fixture-query,#fixture-fragment').count(),0);assert(!(await p.locator('body').innerText()).includes('marker-713'));
 await p.goto(origin+'/fixture');await p.locator('#attack').evaluate(e=>e.click());await p.locator('#submit').evaluate(e=>e.click());
 assert.equal(await p.evaluate(()=>window.injected),undefined);
 assert.equal(await p.evaluate(()=>document.baseURI),origin+'/fixture');
 assert(!hits.some(x=>x.startsWith('/trap-')),JSON.stringify(hits));
 assert.equal(await p.evaluate(()=>getComputedStyle(document.body).backgroundColor),'rgb(247, 245, 238)');
 const result={inlineScript:'blocked',eventHandler:'blocked',javascriptURL:'blocked',externalScript:'blocked',iframe:'blocked',formSubmission:'blocked',baseOverride:'blocked',queryAndFragment:'not interpolated',inlineStyles:'rendered',scope:'local test server only; no production attacks'};
 fs.mkdirSync('../review',{recursive:true});fs.writeFileSync('../review/security-results.json',JSON.stringify(result,null,2));console.log(result);
 }finally{if(b)await b.close();server.close()}})().catch(e=>{console.error(e);process.exitCode=1});
