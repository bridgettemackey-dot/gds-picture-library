# -*- coding: utf-8 -*-
"""Week 44: Thu 1 - Sun 4 Oct 2026. Six slots.
Three on new sunburst artwork, three on catalogued assets.

Lives in the repo, not the scratchpad. The scratchpad does not survive a container
being reclaimed, which it did on 27 Sep taking every previous week's script with it.
"""
import json, os, urllib.request

K  = os.environ['BUFFER_API_KEY']; CN = os.environ['CLOUDINARY_CLOUD_NAME']
FB, IG, PIN = '6a87c738ccaf649a67e82609', '6a8bbcd7ccaf649a6704f154', '6a8bbd26ccaf649a6704f202'
B_COLOR, B_READ, B_LI = '830421687481393074', '830421687481391572', '830421687481393086'
GW   = 'https://www.amazon.com/dp/B0HCB7V9C9'; GWA  = 'https://www.amazon.com/dp/B0HG8NKYV2'
REG  = 'https://www.amazon.com/dp/B0HGKNTNDD'; REGA = 'https://www.amazon.com/dp/B0HH8PVQZ9'
ATBU = 'https://www.amazon.com/dp/B0HC1PJ4DS'; ATBL = 'https://www.amazon.com/dp/B0HBNFLDQP'
GDSI = 'GDS-Images — https://pictures.gdsbahamas.com/'

STD = lambda p: "https://res.cloudinary.com/%s/image/upload/%s.png" % (CN, p)
IGC = lambda p: "https://res.cloudinary.com/%s/image/upload/c_fill,ar_4:5,g_auto,w_1080,f_jpg,q_auto:good/%s.jpg" % (CN, p)
IGP = lambda p: "https://res.cloudinary.com/%s/image/upload/c_pad,b_rgb:fffef8,w_1080,h_1350,f_jpg,q_85/%s.jpg" % (CN, p)
cap = lambda s, n=480: s if len(s) <= n else s[:n-1].rsplit(' ', 1)[0] + '…'
tail = lambda t, tags=None: t + "\n\n" + GDSI + (("\n\n" + tags) if tags else "")

S = [
 # Thu 1 Oct — slot 44 — pillar 2 Reader Engagement — The Girl and The Whale — NEW ART
 dict(day='2026-10-01', base=14, pid='gds/girl-whale/book-of-legends-on-the-reef-20261001', pad=False, board=B_READ,
  alt='A thick old leather-bound book lying open on a flat sun-bleached rock at the edge of a '
      'shallow coral reef, its weathered cream pages blank. A conch shell and a sprig of dried '
      'seaweed beside it, clear turquoise water over coral and two small yellow fish below, and '
      'green volcanic mountains across the bay in late golden light.',
  fb=tail("Mr. Hooker does not tell Anna she is right. He hands her a book.\n\n"
    "Hawaii's Book of Legends is where she finds the Cosmic Theseus Finback — the largest humpback "
    "in the world, whose fins shone brighter than all the stars combined, and who took a comet "
    "strike to save every creature in the sea.\n\nWhich is what we want to ask you. Every island "
    "has stories that get passed down rather than written down. Which one were you told as a "
    "child?\n\nWe would genuinely like to know. Tell us in the comments — we are collecting "
    "them.\n\nThe Girl and The Whale, by Zhané Mackey. Ages 6 to 12.\n\n"+GW),
  ig=tail("Mr. Hooker doesn't tell Anna she's right. He hands her a book. 📖\n\nHawaii's Book of "
    "Legends is where she finds the Cosmic Theseus Finback — the largest humpback in the world, "
    "whose fins shone brighter than all the stars combined, and who took a comet strike to save "
    "every creature in the sea. ✨🐋\n\nSo: every island has stories that get passed down rather "
    "than written down. Which one were you told as a child?\n\nTell us below — we're collecting "
    "them. 👇\n\nBy Zhané Mackey. Ages 6–12.\n\n"+GW,
    "#IslandLegends #TheGirlAndTheWhale #ChildrensBooks #Bahamas #ReaderQuestion #Folklore"),
  pin_t='Hawaii’s Book of Legends — The Girl and The Whale',
  pin=tail("Mr. Hooker does not tell Anna she is right. He hands her a book — and in it she finds "
    "the Cosmic Theseus Finback, who took a comet strike to save every creature in the sea. By "
    "Zhané Mackey. Ages 6 to 12.\n\n"+GW),
  pin_url=GW),

 # Fri 2 Oct — slot 45 — pillar 3 Promo/CTA — All Things Bahamian: Lower Elementary — CATALOGUED
 dict(day='2026-10-02', base=14, pid='gds/atb-lower/conch-and-starfish-20260909', pad=False, board=B_COLOR,
  alt='A bright illustration of a queen conch shell and a starfish on pale sand, in flat clear '
      'colour with simple bold shapes.',
  fb=tail("If you are buying one book for a Bahamian five year old, buy this one.\n\n"
    "All Things Bahamian: My First Cultural Coloring Book is the entry point to the whole series. "
    "Big shapes. Outlines thick enough for small hands. The conch, the flamingo, the hibiscus, the "
    "sloop — the things a Bahamian child sees before they can read about them.\n\nAnd when they "
    "outgrow it, the Upper Elementary edition is waiting: 109 pages, seven sections, real written "
    "work. The two are built to be a sequence, not alternatives.\n\n"
    "All Things Bahamian: My First Cultural Coloring Book. Ages 5 to 9.\n\n"+ATBL),
  ig=tail("Buying one book for a Bahamian five year old? Start here. 🐚\n\nAll Things Bahamian: My "
    "First Cultural Coloring Book is the entry point to the series. Big shapes, outlines thick "
    "enough for small hands, and the things a Bahamian child sees before they can read about them "
    "— conch, flamingo, hibiscus, sloop.\n\nWhen they outgrow it, the Upper Elementary edition is "
    "waiting. Built as a sequence, not alternatives. 📚\n\nAges 5–9.\n\n"+ATBL,
    "#BahamianKids #ColoringBook #EarlyYears #GiftForKids #Bahamas #QueenConch"),
  pin_t='The first one to buy — All Things Bahamian, Ages 5 to 9',
  pin=tail("The entry point to the series: big shapes, thick outlines for small hands, and the "
    "things a Bahamian child sees before they can read about them. The Upper Elementary edition "
    "waits for when they outgrow it. Ages 5 to 9.\n\n"+ATBL),
  pin_url=ATBL),

 # Sat 3 Oct — slot 46 — pillar 4 Activity Spotlight — GW Activity Book — NEW ART
 dict(day='2026-10-03', base=14, pid='gds/girl-whale-activity/the-comet-strikes-cosmic-20261003', pad=False, board=B_READ,
  alt='A vast humpback whale rising through deep night ocean water, her long pectoral fins glowing '
      'cosmic purple and scattered with starlight. A white-gold comet streaks down towards her '
      'raised back. Turtles, rays and shoals of small fish look up from the water below her, safe '
      'in her shadow, under a sky full of stars.',
  fb=tail("The moment the whole legend turns on, and the activity it became.\n\n"
    "Cosmic did not dodge the comet. She took it, and every creature in the sea lived because she "
    "did.\n\nInside the Coloring & Activity Book there is a page called Design Your Own Cosmic "
    "Finback. A child decides what their whale's fins are made of — and children do not choose "
    "purple. They choose reef fish, or hurricane clouds, or their grandmother's church dress.\n\n"
    "It is the page teachers tell us about most.\n\nThe Girl and The Whale Coloring & Activity "
    "Book. Ages 6 to 12.\n\n"+GWA),
  ig=tail("The moment the whole legend turns on. ☄️🐋\n\nCosmic didn't dodge the comet. She took it, "
    "and every creature in the sea lived because she did.\n\nInside the activity book there's a "
    "page called Design Your Own Cosmic Finback — the child decides what their whale's fins are "
    "made of. And children never choose purple. They choose reef fish, hurricane clouds, their "
    "grandmother's church dress. ✨\n\nThe page teachers tell us about most.\n\nAges 6–12.\n\n"+GWA,
    "#ActivityBook #TheGirlAndTheWhale #CreativeKids #ChildrensBooks #Bahamas #Whales"),
  pin_t='Design your own Cosmic Finback — the activity book page',
  pin=tail("Cosmic did not dodge the comet. She took it, and every creature in the sea lived. The "
    "activity book asks a child to design their own — and they never choose purple. Ages 6 to "
    "12.\n\n"+GWA),
  pin_url=GWA),

 # Sat 3 Oct — slot 47 — pillar 5 — All Things Bahamian: Upper Elementary — CATALOGUED
 dict(day='2026-10-03', base=19, pid='gds/atb-upper/junkanoo-detail-20260902', pad=False, board=B_COLOR,
  alt='A Junkanoo costume photographed close: layers of finely cut crepe paper fringing in hot '
      'pink, orange and turquoise, built up in overlapping rows.',
  fb=tail("Look at how a Junkanoo costume is actually built.\n\nNot painted. Fringed — thousands of "
    "strips of crepe paper cut by hand and laid in overlapping rows, so the whole thing moves when "
    "the wearer does. A single costume can take most of a year.\n\nAll Things Bahamian: Upper "
    "Elementary gives Junkanoo a full section, because a child who only ever sees it on parade day "
    "never learns that the work happens in a shack in July.\n\nAges 9 to 12.\n\n"+ATBU),
  ig=tail("How a Junkanoo costume is actually built. 🎭\n\nNot painted — fringed. Thousands of "
    "strips of crepe paper cut by hand, laid in overlapping rows so the whole thing moves when the "
    "wearer does. One costume can take most of a year.\n\nAll Things Bahamian: Upper Elementary "
    "gives Junkanoo a full section, because a child who only sees parade day never learns the work "
    "happens in a shack in July. 🥁\n\nAges 9–12.\n\n"+ATBU,
    "#Junkanoo #BahamianCulture #AllThingsBahamian #ClassroomResources #Bahamas"),
  pin_t='How a Junkanoo costume is built — All Things Bahamian',
  pin=tail("Not painted, fringed: thousands of strips of crepe paper cut by hand and laid in "
    "overlapping rows so the costume moves with the wearer. One can take most of a year. Ages 9 to "
    "12.\n\n"+ATBU),
  pin_url=ATBU),

 # Sun 4 Oct — slot 48 — pillar 6 Classroom & Library — Regatta Activity Book — NEW ART
 dict(day='2026-10-04', base=14, pid='gds/regatta-activity/pink-sand-at-deals-beach-20261004', pad=False, board=B_LI,
  alt='A wide sweep of pink-tinged sand at Deals Beach, Long Island, palest rose where dry and '
      'deeper coral where the water has washed it, meeting clear turquoise shallows. Broken shells '
      'and pieces of pink coral across the sand, sea grape and silver-green scrub on the dune and '
      'casuarina trees leaning under a bright sky.',
  fb=tail("Why is the sand pink? It is a better science lesson than it looks.\n\n"
    "The pink comes from foraminifera — single-celled creatures with reddish shells that live on "
    "the reef, die, wash ashore and mix in with the white coral sand. No pink rock. No dye. A beach "
    "coloured by something too small to see.\n\nDeals Beach on Long Island is one of the places you "
    "can see it, and it is one of the observation pages in the Going To The Regatta Coloring & "
    "Activity Book — the sort of question that sends a class outside with a magnifying glass "
    "instead of a worksheet.\n\nAges 6 to 12.\n\n"+REGA),
  ig=tail("Why is the sand pink? Better science than it looks. 🔬\n\nIt comes from foraminifera — "
    "single-celled creatures with reddish shells that live on the reef, die, wash ashore and mix "
    "into the white coral sand. No pink rock. No dye. A whole beach coloured by something too small "
    "to see. 🐚\n\nDeals Beach on Long Island is one of the places you can see it, and it's an "
    "observation page in the Regatta activity book.\n\nAges 6–12.\n\n"+REGA,
    "#PinkSand #LongIslandBahamas #ScienceForKids #ActivityBook #Bahamas #DealsBeach"),
  pin_t='Why the sand is pink — Going To The Regatta activity book',
  pin=tail("The pink comes from foraminifera, single-celled creatures with reddish shells that wash "
    "ashore from the reef and mix into the white coral sand. A beach coloured by something too "
    "small to see. An observation page for ages 6 to 12.\n\n"+REGA),
  pin_url=REGA),

 # Sun 4 Oct — slot 49 — pillar 0 Book World — The Girl and The Whale — CATALOGUED
 # CORRECTED 30 Sep: the first draft said Zhané wrote the book "after living there".
 # She has NEVER been to Hawaii; the story is fiction. See the no-invented-biography
 # rule in SOCIAL-RUNBOOK.md.
 dict(day='2026-10-04', base=19, pid='gds/girl-whale/on-the-outrigger-20260907', pad=False, board=B_READ,
  alt='An outrigger canoe on calm open water at golden hour, its float arm cutting a line across '
      'the surface, green island headland behind.',
  fb=tail("The book is set in Hawaii. The author has never been there.\n\n"
    "Zhané built the island out of reading, looking and imagining — the outrigger, the reef, the "
    "volcanic mountains, Mr. Hooker and his boat — and published it from Nassau.\n\nPeople ask why "
    "a Bahamian publisher's first reader is a Hawaiian story. Partly because a child raised around "
    "reef and boat and legend can recognise another island from a long way off. Mostly because it "
    "is a story about believing a child who says she heard something, and that belongs to no one "
    "island.\n\nOne day we hope she gets to stand on that beach and see how close she came.\n\n"
    "The Girl and The Whale, by Zhané Mackey. Ages 6 to 12.\n\n"+GW),
  ig=tail("The book is set in Hawaii. The author has never been there. 🛶\n\nZhané built the island "
    "out of reading, looking and imagining — the outrigger, the reef, the volcanic mountains, Mr. "
    "Hooker and his boat — and published it from Nassau. 🇧🇸\n\nWhy a Hawaiian story from a "
    "Bahamian publisher? Partly because a child raised around reef and boat and legend can "
    "recognise another island from a long way off. Mostly because it's a story about believing a "
    "child who says she heard something.\n\nOne day we hope she gets to stand on that beach. ✨\n\n"
    "By Zhané Mackey. Ages 6–12.\n\n"+GW,
    "#TheGirlAndTheWhale #ChildrensBooks #IslandStories #Bahamas #YoungAuthor #Imagination"),
  pin_t='Set in Hawaii, written from Nassau — The Girl and The Whale',
  pin=tail("Set in Hawaii, by a Bahamian author who has never been there — an island built out of "
    "reading, looking and imagining, and published from Nassau. A story about believing a child who "
    "says she heard something. By Zhané Mackey. Ages 6 to 12.\n\n"+GW),
  pin_url=GW),
]

M = """mutation($input: CreatePostInput!){ createPost(input:$input){
  ... on PostActionSuccess { post { id status dueAt channelService } }
  ... on InvalidInputError { message } ... on RestProxyError { message code }
  ... on LimitReachedError { message } ... on NotFoundError { message }
  ... on UnauthorizedError { message } ... on UnexpectedError { message } } }"""


def call(q, v):
    r = urllib.request.Request('https://api.buffer.com/graphql',
        data=json.dumps({'query': q, 'variables': v}).encode(),
        headers={'Authorization': 'Bearer ' + K, 'Content-Type': 'application/json'})
    return json.loads(urllib.request.urlopen(r, timeout=90).read())


def post(ch, text, due, url, alt, meta):
    v = {'input': {'channelId': ch, 'text': text, 'mode': 'customScheduled',
        'schedulingType': 'automatic', 'dueAt': due,
        'assets': [{'image': {'url': url, 'thumbnailUrl': url, 'metadata': {'altText': cap(alt)}}}],
        'metadata': meta}}
    d = call(M, v)
    node = d.get('data', {}).get('createPost', {})
    if 'post' in node:
        p = node['post']; print('  ok  %s %s' % (p['dueAt'][:16], p['channelService'])); return True
    print('  FAIL', json.dumps(d)[:260]); return False


if __name__ == '__main__':
    ok = fail = 0
    for s in S:
        d, b = s['day'], s['base']
        ig_url = (IGP if s['pad'] else IGC)(s['pid']); std = STD(s['pid'])
        for ch, due, text, url, meta in (
            (FB,  '%sT%02d:00:00Z' % (d, b), s['fb'],  std,    {'facebook': {'type': 'post'}}),
            (IG,  '%sT%02d:20:00Z' % (d, b), s['ig'],  ig_url, {'instagram': {'type': 'post', 'shouldShareToFeed': True}}),
            (PIN, '%sT%02d:40:00Z' % (d, b), s['pin'], std,    {'pinterest': {'boardServiceId': s['board'],
                                                                'title': s['pin_t'], 'url': s['pin_url']}}),
        ):
            if post(ch, text, due, url, s['alt'], meta): ok += 1
            else: fail += 1
    print('\ncreated %d, failed %d' % (ok, fail))
