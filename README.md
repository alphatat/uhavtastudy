# My YouTube Links — iOS 12-friendly static site

This is a dependency-free static webpage for the unlisted YouTube links supplied in `links.txt`.

## Preview locally
Open `index.html` in a browser. Thumbnails need an internet connection; video links open YouTube.

## Publish with GitHub Pages
1. Create a new GitHub repository (public is simplest for GitHub Pages).
2. Upload `index.html` to the repository root and commit it.
3. Open **Settings → Pages**.
4. Under **Build and deployment**, select **Deploy from a branch**.
5. Select branch `main` and folder `/ (root)`, then save.
6. Open the URL GitHub Pages provides, usually `https://YOUR-USERNAME.github.io/REPOSITORY/`, on the iPad.

## Notes
- The page uses plain HTML, CSS, and older JavaScript syntax; no framework or build step is required.
- The links are unlisted, not private. Anyone who can access this page can see the URLs.
- YouTube may still have playback limitations on iOS 12. If an embedded player is unreliable, this page deliberately opens the regular YouTube link instead.
