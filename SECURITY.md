# Security and responsible maintenance

The main directory is static: no account system, database, submission endpoint, analytics, runtime JavaScript or third-party libraries. The separate optional starter.html/starter.js editor never runs in the main directory page. Corrections open the visitor's email app; nothing is submitted automatically. External map/source sites have their own security and privacy practices.

## Reporting

Report suspected security problems privately to the project contact, Vancouverfoodshare.contact@gmail.com. Include the affected URL, browser, and a minimal description. Do not include passwords, tokens, sensitive personal information or public exploit details. This project promises no response time or bounty. Ordinary listing corrections use the site's correction link.

## Browser controls

The index.html and preview.html directory entry points include an early meta Content Security Policy. Scripts, connections, frames, objects, forms and base-URL overrides are blocked. Local images and inline CSS are permitted; inline CSS is needed by this single-file layout. The no-referrer policy limits referrer information sent when following links. There are no remote scripts requiring integrity hashes.

These are defence-in-depth controls, not proof of an exploitable injection flaw or a guarantee against compromise. A maintainer or attacker with repository write access can remove them or replace links and facts. Meta CSP cannot enforce frame-ancestors or CSP reporting; this repository does not set HTTP-only response headers such as X-Frame-Options or HSTS. Do not claim those protections were installed. GitHub Pages HTTPS and account controls must be reviewed separately in GitHub settings.

## Safe changes and forks

- Treat corrections, issues and pull requests as untrusted. Verify addresses, donation rules and source ownership independently. Obtain listing/host permissions where promised; never infer permission from silence.
- Edit text as text with proper HTML escaping. Do not paste raw submitted HTML, scripts, tracking embeds, event handlers, javascript URLs or private contact details. Query strings and fragments are currently never rendered into the page.
- Keep links to reviewed HTTPS destinations, internal fragments and the intended mailto address. Check for lookalike domains and changed redirect destinations. Browser policy does not certify linked sites.
- Keep both HTML files identical. Run the content, keyboard/layout and local security checks before release. Review any proposal adding forms, dynamic rendering, remote libraries or storage as a new security design.
- Review changes before running contributor code. Never give untrusted PR workflows secrets or write tokens. No custom Actions workflows or build dependencies are required by this site.
- In a new city, replace contact details, maps, sources and QR destination. Preserve the MIT notice, but do not imply the original maintainer operates your copy.

## Operator controls to review

Use a passkey or strong MFA, least-privilege short-lived tokens, reviewed collaborators and protected publishing branches with reviewed changes. Verify the Pages source and HTTPS setting. Keep recovery methods safe and revoke exposed tokens immediately. These account controls cannot be supplied by an HTML patch; changes require the owner's approval.

## Local tests

Current release checks use `python draft-checks.py`, `node verify.cjs` and `node --test editor-checks.cjs starter-checks.cjs`, plus managed-browser review documented in TEST_REPORT.md. The original Windows-specific security-qa.cjs, browser-qa.cjs and flow-qa.cjs scripts were not run here and remain in the repository for historical reference, unchanged. They do not validate the current release. Do not interpret the current checks as a full CSP exploit test, penetration test or account-security assessment.

References: [MDN CSP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy), [GitHub Pages HTTPS](https://docs.github.com/en/pages/getting-started-with-github-pages/securing-your-github-pages-site-with-https).



## Optional local city editor

The separate starter page permits its same-origin script and blocks network connections, form submission and object loading. A scriptless iframe with an empty sandbox renders the generated preview; it cannot run entered scripts or open external links. This is a local editing interface, not a public visitor reporting form. The main directory and exported pages block scripts entirely.

All text fields are escaped before HTML generation. Source URLs must use HTTPS with no credentials; unsafe schemes are rejected. Public maintainer email validation rejects line breaks/header injection. Map queries encode the entered public address, city and country. Contact text is plain text, not interpreted HTML.

Limits are field-specific: city/country 80 characters, name 120, public address/contact 200, service/donation hours 300, entrance 400, eligibility/fees 500, food rules 700, source URL 1,000 (including normalized URL), maintainer email 160. Up to 25 entries are supported. Imported JSON is limited to 1 MB and the supported version/schema; allowed fields are reconstructed rather than arbitrary keys merged into application state. Dates are optional, must be real and not future, and are always described as maintainer-entered rather than certified.

ZIPs contain four fixed filenames (index.html, README.md, LICENSE.md, food-share-project.json). No user-controlled archive paths, inherited local listings/contact or QR are added. The exact MIT notice is retained. The editable JSON contains all entered public details and is read locally on import. No browser storage or request API is used. Unsaved work is lost on closing/reloading; replacing an existing project asks first. Blob downloads are cleared when inputs change or the page exits.

These checks are not penetration-test certification. HTTPS alone does not establish that an operator URL or entered information is trustworthy. Independently verify facts, consent and local requirements before publication.
