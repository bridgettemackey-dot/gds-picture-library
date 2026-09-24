# Post-activity dashboard

Live page: https://claude.ai/artifact/JybswuGRdkDb1V3chFezs2 (private to Bridge until shared)

Every post Buffer has published for GDS, with the activity each network reported back, plus
a plain-language note on what each of the nine activity types actually counts.

## Rebuilding it

    python3 dashboard/build.py            # pulls Buffer, writes dashboard/index.html
    python3 dashboard/build.py --check    # pulls and reports, writes nothing

Needs `BUFFER_API_KEY` in the environment; the script refuses to run without it rather than
writing a half-empty page. Thumbnails are cached in `thumbs.json`, so a daily run only
downloads pictures it has not seen before.

Then publish the result to the EXISTING artifact, passing its url:

    Artifact(url="https://claude.ai/artifact/JybswuGRdkDb1V3chFezs2",
             file_path="dashboard/index.html")

Publishing without `url` creates a second, orphaned dashboard. Read the artifact first if
this conversation has not already published it — the tool refuses a blind overwrite.

## How it is put together

- `build.py` — pulls every sent post from Buffer's GraphQL API, caches thumbnails, computes
  the reporting-health runs, and inlines everything into the template as one JSON blob.
- `template.html` — the page. `__DATA__` is the only placeholder.
- `thumbs.json` — cached 120px thumbnails as data URIs. Committed on purpose: the artifact
  sandbox blocks external images, so every picture has to ship inside the page.

## Two things the page is careful about

**A zero is not always a zero.** Buffer's API fills in `0` both when nobody did the thing and
when the network never reported it. The two are indistinguishable from outside.

**Engagement rate is noise at these volumes.** It is interactions over people reached, so a post
seen by one person with five interactions reads as 500%. Only the Pinterest rates, computed over
hundreds of impressions, mean anything.

## Reporting health

`build.py` counts each channel's run of consecutive posts that reported nothing at all and prints
an ALERT line. The page shows the same runs and flags a channel at 8 or more. This exists because
Pinterest went to exactly zero on every pin from 11 September 2026 onward while Facebook and
Instagram kept reporting normally — see the note in `SOCIAL-RUNBOOK.md`.

## Second source: Meta (Facebook Page + Instagram)

`meta_pull.py` reads Page and Instagram insights straight from Meta, so Buffer can be
checked rather than trusted. It needs `META_PAGE_TOKEN` in the environment — a long-lived
Facebook **Page** access token. Page tokens derived from a long-lived user token do not
expire, so this is set once and left alone.

    python3 dashboard/meta_pull.py --probe   # check the token, print what it can see
    python3 dashboard/meta_pull.py           # pull insights -> dashboard/meta.json

The probe names the missing permission when a call is refused, rather than failing
generically. Run it first after any token change.

Accounts, confirmed from Buffer on 24 Sep 2026:
  Facebook Page  "The GDS Group of Companies"  id 106614211138659   (type: page)
  Instagram      @gdsgroupofcompanies          id 17841444276794297 (type: business)

Because both accounts belong to GDS, these insights are Standard Access and need no App
Review. The permissions are `pages_show_list`, `pages_read_engagement`, `instagram_basic`
and `instagram_manage_insights`.

The script never prints the token and never writes it to disk.
