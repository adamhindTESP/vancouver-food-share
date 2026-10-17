# Security and responsible maintenance

This is a static directory: no account system, database, submission endpoint, analytics, runtime JavaScript or third-party libraries. Corrections open the visitor's email app; nothing is submitted automatically. External map/source sites have their own security and privacy practices.

## Reporting

Report suspected security problems privately to the existing published contact, adam.hind005@gmail.com. Include the affected URL, browser, and a minimal description. Do not include passwords, tokens, sensitive personal information or public exploit details. This project promises no response time or bounty. Ordinary listing corrections use the site's correction link.

## Browser controls

Both HTML entry points include an early meta Content Security Policy. Scripts, connections, frames, objects, forms and base-URL overrides are blocked. Local images and inline CSS are permitted; inline CSS is needed by this single-file layout. The no-referrer policy limits referrer information sent when following links. There are no remote scripts requiring integrity hashes.

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

`node security-qa.cjs` runs harmless injection fixtures on an ephemeral loopback server using preinstalled Playwright/Edge paths (adjust for your machine). It checks script/event/javascript-URL blocking, base override, frames and forms, and confirms ordinary inline styles render. Fixtures never enter the shipped HTML. This is a limited regression check, not penetration testing, a dependency audit or an account security assessment.

References: [MDN CSP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy), [GitHub Pages HTTPS](https://docs.github.com/en/pages/getting-started-with-github-pages/securing-your-github-pages-site-with-https).
