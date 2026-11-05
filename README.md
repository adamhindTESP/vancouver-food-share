# Vancouver Food Share

An independent guide to community fridges, food-support directories and donation options.

Website: https://adamhindtesp.github.io/vancouver-food-share/

## Find or give food

The two primary routes are “I need food” and “I have food to give”. Eight organizer-listed fridge cards keep their address, hours, entrance, pickup/donation caveats and map link visible. “More details” opens storage, longer rules and source notes. Neighbourhood links help readers jump around without granting location access.

Directories, registration and eligible paid delivery are labelled separately. This is not a live-stock service or a complete citywide list. Check each operator's current information before travelling or donating. Source-check dates record source-page reviews, not on-site inspections or guarantees.

Project contact: Vancouverfoodshare.contact@gmail.com. Correction and hosting links open an email app; nothing is sent automatically. Hosting interest is exploratory, with no promised box, placement or date.

## Start a guide for another city

Open [the city editor](https://adamhindtesp.github.io/vancouver-food-share/starter.html).

1. Enter a city/community and country, plus an optional public maintainer email you are authorized to publish.
2. Add up to 25 local locations or resources. Choose pickup, donation, both, support/directory or delivery. Enter a public address where relevant, access instructions, separate pickup/donation hours, food rules, eligibility/fees, source and actual check date.
3. Add each entry, then edit or remove it from the saved-entry list. Clear unfinished fields if you want to discard them.
4. Update the preview and download the website ZIP or editable project JSON. Reopen that JSON in the editor to continue later without writing HTML.

Generated websites use compact cards. All entered hours, access instructions, food rules and eligibility/fees stay visible because they may contain essential restrictions. Contact and source history open under More details. A long essential note can make a card taller. Both-purpose entries appear in both find/give sections.

The ZIP contains index.html, README.md, LICENSE.md and food-share-project.json. The exported website does not include the editor. City projects start blank and never inherit Vancouver listings, contact details or QR codes. They remain explicitly unverified until their maintainer checks them. The tool does not research, translate, certify, host or publish a site.

Save before leaving: work stays in page memory until downloaded. Closing/reloading can lose unsaved edits. Inputs are not uploaded or stored in browser storage. Downloaded files contain entered details. Loading a hosted editor still makes ordinary web requests. Do not enter visitors' private information.

Read [ADAPT_FOR_YOUR_CITY.md](ADAPT_FOR_YOUR_CITY.md) before separately publishing. Verify local facts, consent, safety requirements and your contact. Create a new QR only after confirming your own URL. Preserve the MIT license and copyright notice.

## Run locally and maintain

Open index.html after downloading/extracting this repository. For the editor, keep starter.html and starter.js together; browsers that restrict local scripts need a local static server. A computer browser is recommended for editing. Physical iPhone/local-file behavior has not been certified.

The main directory and exported city websites work without JavaScript. The optional editor uses a local script and protected preview; there is no backend, account, analytics or live inventory feed.

Run:

- `python draft-checks.py` (content and release checks)
- `node verify.cjs`
- `node --test editor-checks.cjs starter-checks.cjs`

See TEST_REPORT.md, SOURCES.md and SECURITY.md. Historical Windows-specific browser scripts remain for reference but were not used to validate this release. CHECKSUMS.json records the release's main source/document hashes.

Review changes before publishing to main, which can update GitHub Pages. Preserve the existing public URL, qr-code.png and posters unless deliberately replacing them. Repository history retains earlier versions; rollback should use a reviewed revert rather than rewriting shared history.
