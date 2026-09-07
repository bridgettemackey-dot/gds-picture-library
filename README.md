# GDS Picture Library

A public download site for artwork from the GDS Publications children's books.
Live at https://bridgettemackey-dot.github.io/gds-picture-library/

Every downloadable file has a caption band added underneath the artwork carrying the
book's title and a QR code that opens that book's Amazon page. A raster image cannot
hold a clickable link, so the code is drawn into the pixels — it survives downloading,
reposting, and even a screenshot of a screen.

## How it updates

`images.json` is the bundled manifest and always works.

If Cloudinary's public resource list is enabled (Settings → Security → uncheck
"Resource list"), the page additionally fetches
`https://res.cloudinary.com/<cloud>/image/list/gdsshelf.json` on load and shows any
newly tagged picture without a redeploy. Upload branded images to
`gds-share/<book-slug>/<name>` with the tags `gdsshelf` and `book-<code>`.

## Files

| File | Purpose |
|---|---|
| `index.html` | the whole site |
| `images.json` | bundled manifest: caption, book, Amazon link, Cloudinary ids |
| `books.json` | the six titles and their ASINs |
