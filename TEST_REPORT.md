# Food Share release validation

Original source-page checks: 4 November 2026. Additional operator and donation sources: 5 November 2026 UTC. Code/release checks: 5 November 2026 UTC. This release is based on the approved 14-file source bundle (14 files plus a checksum manifest), with publication wording adjusted and the main review banner removed. Newly generated city websites remain unverified drafts.

## Passed locally

- 24 Python content checks: ten cards in separate VCFP/operator groups, visible trip essentials, accessible native disclosures, neighbourhood links, registration/delivery/geography distinctions, donation and host caveats, project email, source dates, safe link schemes, static main-page policy and index/preview parity.
- Node verify.cjs: content honesty, correction route, sources and parity.
- 28 Node editor checks: four-file output, project roundtrip, escaping, unsafe URL rejection, field/date/import limits, clear/cancel behavior, overwrite guard, map context, Unicode project capacity, responsive layout rules, compact disclosures, no inherited Vancouver contact, all five service types and preservation of every entered essential field.
- ZIP CRC, fixed filenames and file checksums verified. The test that writes a sample ZIP creates its own evidence directory so it works in a fresh checkout.
- Actual editor reopened a saved local project and generated compact cards. Preview iframe HTML matched generated export HTML byte-for-byte.
- All eight Vancouver card disclosures opened with Enter and closed with Space. Visible keyboard focus remained. The Kitsilano jump focused its target; the two Kitsilano cards are adjacent.
- Closed/expanded cards, neighbourhood jumps, editor fields and project contact were visually inspected in 320px/390px CSS frames. The narrow main page and generated cards had matching client/scroll widths with no horizontal overflow. These are browser-frame tests, not physical-device tests.
- Independent review covered original location facts/source URLs, access and donation caveats, compact mobile views, injected text, invalid URLs/email/dates/imports, prototype keys, JSON roundtrip, ZIP UTF-8/CRC, mixed service fields and edit/remove index safety. Confirmed defects were repaired and regression checks rerun.

## Responsible limits

This is not a penetration-test, screen-reader, physical-device, 200% text-zoom or legal-compliance certification. Historical Windows/Edge browser scripts were not rerun and do not validate this release. The local preview service adds development tooling not present in shipped main HTML.

No live food stock, on-site accessibility, temporary closures or complete location-specific donation rules were independently verified. Source pages can change. Eight organizer listings do not mean complete citywide coverage. HTTPS source validation does not establish that an operator or entered fact is trustworthy.

The English-language editor supports up to 25 entries and has no automatic research, translation, storage, hosting or publication. Entered rules and eligibility may be lengthy because potentially essential restrictions must not be hidden. Missing relevant facts remain unknown. All exported city websites remain labelled unverified.

The contact address is maintainer-provided; no test email was sent and no mailbox was created. MIT attribution is retained. Account security, collaborators, branch protections and hosting settings require separate owner review and are not guaranteed by HTML or these tests.

## Publication checks

Before declaring deployment complete, verify the exact release commit on main, the corresponding GitHub Pages build, served index/starter content and the unchanged QR/poster objects. Preserve the prior commit as a rollback point. This report records local validation, not an assertion that a future deployment or account setting has been verified.

## Operator-resource addition — 5 November 2026 UTC

Added Collingwood Neighbourhood House and Boundless as a separate operator-sourced group, and Food Bank on Wheels only as a donation route. CNH fridge hours and both operators' donation policies remain explicitly unconfirmed. Boundless has its actual weekday schedule, with weekends unconfirmed. The existing eight cards, 211 resource, city editor, contact, QR and posters are unchanged.

Three new content regression checks were first run against the previous release and failed as expected, then passed after the additions. The full current checks pass: 24 Python, verify.cjs, and 28 Node. No operational claims were inferred from unrelated programs or donation drop-off sites. Source dates for older entries were not advanced.
