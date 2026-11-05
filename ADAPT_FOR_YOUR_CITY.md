# Adapt for your city

Make a local guide using verified information from your community. This is a static HTML page: no backend, build tool or hosting integration is required.

## Local editor route

This repository includes starter.html and starter.js. Open [the city editor](https://adamhindtesp.github.io/vancouver-food-share/starter.html) in a compatible browser, enter your place, add local resources, preview and download. These steps do not require HTML editing or a GitHub account. Download the editable project JSON before leaving; reopen it in this editor for later revisions. The exported website ZIP has index.html, README.md, LICENSE.md and food-share-project.json, but not the editor. Keep the project JSON and reopen it in the editor to edit again.

This route starts blank and retains unverified notices. It does not look up food locations or publish them. Verify every local fact, permission and safety requirement before the separate publishing step below. It creates no QR; make your own only after confirming your new URL.

The manual fork/edit route below remains available. References to copied QR assets apply to a full repository download, not an editor-generated city kit.

## 1. Get your own copy

Choose one route:

- **Fork on GitHub:** sign in, open the [repository](https://github.com/adamhindTESP/vancouver-food-share), click **Fork**, choose your account and repository name, then **Create fork**. Edit your fork, not the original repository.
- **Download ZIP:** on the repository page choose **Code > Download ZIP**, or use the [main-branch ZIP](https://github.com/adamhindTESP/vancouver-food-share/archive/refs/heads/main.zip). Extract it on your computer. You can edit locally without a GitHub account; publishing through GitHub Pages requires an account and your own repository.

This repository is not currently configured as a GitHub template; use Fork or ZIP rather than looking for a Use this template button. Keep `LICENSE.md` with the copied files and retain Adam Hind's copyright and permission notice.

## 2. Make it local

Open `index.html` in a text editor. All page content and styling are in this file.

| What to change | What to check |
|---|---|
| Page title, description, brand, introduction and footer | Replace Vancouver references with your city and project name. |
| Location cards | Use verified local locations, public sources, dates checked, pickup/donation roles, entrance, hours and storage details. Mark unknowns explicitly. |
| Organizer and alternative-resource links | Replace Vancouver-specific maps, organizations and City resource links with appropriate local sources. |
| Donation and safety guidance | Use official guidance for your region. Do not assume one host's accepted foods apply everywhere. |
| Correction email | Replace every instance of the Vancouver Food Share project email with a contact you are authorized to publish, including both mailto links. Check the subject/body wording and manual-send explanation. |
| Reuse link and source register | Decide whether the reuse link should point to your own repository or this original; update `SOURCES.md` for your local evidence. |
| QR image | The included `qr-code.png` points to Vancouver's site. Replace it only after your own public URL is confirmed. |

You may translate the page. Preserve its meaning, source links, explicit unknowns and availability caveat. Copy your finished `index.html` to `preview.html` so the two files match.

## 3. Verify before publishing

- Obtain consent before adding a new host or publishing a private address. Keep proposed hosts out of active listings until consent and practical responsibilities are agreed.
- Verify pickup versus donation acceptance, access hours, entrances, food rules and storage against primary sources. Record the actual check date; do not automatically refresh it.
- Do not suggest unrefrigerated storage for perishables or promise hosts have no duties. Agree who checks, cleans and removes unsuitable items.
- Open `index.html` locally. Test each section, source and map link; check keyboard navigation and layout at 320px wide. The directory should work with JavaScript disabled.
- Check the correction mailto link and visible contact. Opening an email draft does not send it; no test email is required.
- Update city-specific test expectations if you use the optional developer checks described in [README.md](README.md).

This directory has no live stock feed or reporting backend. Do not add a submission form that only displays a success message. Do not imply affiliation or endorsement from a public listing or silence.

## 4. Publish your own copy with GitHub Pages

GitHub Pages supports public repositories on GitHub Free. Only publish content and contact details intended to be public.

1. In **your fork**, commit the reviewed edits to `main`. If you downloaded a ZIP, create your own public repository and upload the extracted files, with `index.html` at the repository root (not inside an extra ZIP folder), then commit them to `main`.
2. In your repository, open **Settings > Pages**.
3. Under **Build and deployment**, set **Source** to **Deploy from a branch**.
4. Select **main** and **/(root)**, then click **Save**. If you use a differently named branch, select the branch containing your reviewed `index.html`.
5. Wait for the Pages deployment to finish. Open the site URL shown in Pages settings and test the actual published page. Project-site URLs usually look like `https://your-username.github.io/your-repo-name/`.

After this setup, changes committed to the selected publishing branch can update your public site. Review future edits before committing them there. Other static hosts can also serve `index.html`.

Steps checked against [GitHub's publishing-source documentation](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site) on 16 October 2026. If GitHub's interface changes, follow that documentation.

## 5. Make a QR code for your site

After confirming your published URL, replace the copied Vancouver QR with one for your own URL. Scan a printed sample with a phone and confirm it opens the correct city and current site. Only print or distribute flyers at a host location with permission.

## Security maintenance

Read [SECURITY.md](SECURITY.md) before accepting corrections, changing code, or publishing a fork. Preserve the browser policy and review links and permissions. Use the current checks listed in README.md and TEST_REPORT.md. The legacy Windows-specific security-qa.cjs was not run here and does not validate this release. Account and publishing protections need a separate owner review.

