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

### What Meta will and will not give you

Verified against the live API on 24 September 2026, on v19 through v23:

**IMPRESSIONS AND REACH ARE GONE from the Pages API.** `post_impressions`,
`post_impressions_unique`, `post_reach`, `post_views`, `page_impressions`,
`page_reach`, `page_views` and every variant tried are rejected with
"(#100) The value must be a valid insights metric". This is a schema-level
rejection, not a permissions problem. Do not re-add them without testing.

What a Facebook Page post still reports: `post_clicks`,
`post_reactions_by_type_total`, `post_activity_by_action_type`,
`post_reactions_like_total`. Page level keeps `page_post_engagements`,
`page_follows` and `page_views_total`.

So Buffer's Facebook IMPRESSIONS figure cannot be checked against Meta - there is
nothing to check it against. Clicks and reactions can be. Instagram is the richer
side: reach, likes, comments, saved, shares and views are all still per-media.

`insights()` asks for every metric at once and, if Meta rejects the call, retries
one metric at a time and keeps whatever works. Meta retires names without notice
and rejects the whole call over a single stale one, which would otherwise cost
every other figure on the post.

## Second source: Pinterest (CSV export)

Pinterest's API needs app review, a 30-day token and a 60-day refresh the nightly job
would have to keep alive, and it is not documented whether Trial access can even read
analytics for real pins. The export route costs none of that.

    python3 dashboard/pinterest_csv.py --inspect <file.csv>   # show the column mapping, write nothing
    python3 dashboard/pinterest_csv.py <file.csv>             # -> dashboard/pinterest.json

Pinterest does not document its export headers and they differ between views, so
nothing is hard-coded to one spelling. Columns are matched by a normalised name
against an alias table, the header row is located even when buried under a title
line, and comma/semicolon/tab files and thousands separators all work. Anything it
cannot match is printed, not silently dropped.

ALWAYS run --inspect first on a new export and read the mapping before trusting it.

To line figures up against individual Buffer posts the export needs a pin id or a
pinterest.com/pin/<id> URL column. Without one the numbers still work as a period
total; the script says which case you are in.

Getting the export: Pinterest Analytics, set the date range and filters you want,
then Export at the top right. A pin-level view (Top Pins) is what carries the
per-pin rows.
