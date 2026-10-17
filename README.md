# Vancouver Food Share

A static, independent directory connecting people with existing community fridges in Vancouver. No backend, accounts, inventory feed or activity submission. Food availability varies.

## Use this in your city

[Fork this repository](https://github.com/adamhindTESP/vancouver-food-share/fork) into your GitHub account, or choose **Code > Download ZIP** on the [repository page](https://github.com/adamhindTESP/vancouver-food-share). You can also [download the main-branch ZIP](https://github.com/adamhindTESP/vancouver-food-share/archive/refs/heads/main.zip).

Follow [Adapt for your city](ADAPT_FOR_YOUR_CITY.md) to replace the city, locations, guidelines and contact details, then publish your own copy with GitHub Pages. No build tool is needed. Keep the [MIT license](LICENSE.md) and copyright notice with your copy.

## Preview locally

Open `index.html` in a browser. `preview.html` is an identical compatibility copy. The page needs no dependency installation to work.

## Maintaining listings

Edit `index.html`, then copy it to `preview.html`. Each location needs a public organizer source, the date actually checked, pickup/donation distinction, entrance and hours, storage details, and explicit unknowns. A source check is not an on-site inspection or a guarantee that a fridge is stocked or operating right now. Do not automatically refresh dates.

Keep prospective hosts separate. Obtain consent before listing a new host or private address. Do not imply a partnership from an acknowledgment, silence, or a directory listing. Do not impose pickup limits on mutual-aid fridges.

Corrections use the intentionally published contact email via `mailto`; a configured mail app or manually composed email is required. The site sends and stores nothing. The maintainer reviews changes manually.

See the [source register](SOURCES.md) for Vancouver location evidence and gaps. Replace those facts with checked local sources when adapting the site.

## Developer checks

With Node.js installed, run `node verify.cjs` for content checks. `flow-qa.cjs` checks keyboard/link/accessibility flows; `browser-qa.cjs` checks mobile layout and creates screenshots. Both browser scripts require Playwright and Edge and currently use explicit Windows paths; adjust those paths for your machine. These tools are optional for viewing or hosting the site. Browser evidence is generated in a sibling review folder when the scripts run.

Update city-specific test expectations when adapting the content. Keep `index.html` and `preview.html` identical.

## License

[MIT License](LICENSE.md), copyright 2026 Adam Hind. Preserve the copyright and permission notice when copying or adapting the software.

## Security maintenance

Read [SECURITY.md](SECURITY.md) before accepting corrections, changing code, or publishing a fork. Preserve the browser policy and review links and permissions. Run `node security-qa.cjs` for local browser-policy regression checks. Account and publishing protections need a separate owner review.
