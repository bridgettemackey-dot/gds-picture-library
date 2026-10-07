# -*- coding: utf-8 -*-
"""Week 46: Thu 8 - Sun 11 Oct 2026. Six slots.
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
 # Thu 8 Oct — slot 54 — pillar 5 Bahamian Culture — All Things Bahamian: Upper — NEW ART
 dict(day='2026-10-08', base=14, pid='gds/atb-upper/glass-window-bridge-20261008', pad=False, board=B_COLOR,
  alt='The Glass Window Bridge in Eleuthera: a short road bridge spanning a narrow gap between '
      'two rocky headlands, with one car crossing. The deep navy Atlantic breaks white against '
      'the rock on one side; the calm pale turquoise Bight lies on the other.',
  fb=tail("Two oceans, one road, one narrow strip of rock.\n\nAt the Glass Window Bridge in "
    "Eleuthera the open Atlantic is on one side and the calm Bight of Eleuthera is on the other, "
    "separated by a narrow strip of rock. Navy and rough on the left. Pale turquoise and still on "
    "the right. One strip of rock between them.\n\nIt has a page in All Things "
    "Bahamian, in the Our Beautiful Islands section — one of seven, alongside national symbols, "
    "historic places, life in our seas, Junkanoo, the fruits of The Bahamas, and a closing "
    "make-your-own section.\n\nAll Things Bahamian: Upper Elementary. Ages 9 to 12, grades 4 to 6. "
    "109 pages.\n\n" + ATBU),
  ig=tail("Two oceans. One road. 🌊\n\nThe Atlantic on one side, the calm Bight of Eleuthera on "
    "the other, and a narrow strip of rock between them. Navy and rough. Pale turquoise and "
    "still.\n\nThe Glass Window has a page in All Things Bahamian, in Our Beautiful Islands — "
    "one of the book's seven sections.\n\nUpper Elementary: ages 9–12, grades 4–6, 109 pages.\n\n"
    + ATBU, "#AllThingsBahamian #Eleuthera #GlassWindowBridge #Bahamas #BahamianKids #IslandLife"),
  pin_t='The Glass Window Bridge — All Things Bahamian',
  pin=tail("At the Glass Window Bridge in Eleuthera the rough Atlantic and the calm Bight lie on "
    "opposite sides of a narrow strip of rock. It has a page in All Things Bahamian, in the Our "
    "Beautiful Islands section. Upper Elementary: ages 9 to 12, grades 4 to 6.\n\n" + ATBU),
  pin_url=ATBU),

 # Fri 9 Oct — slot 55 — pillar 6 Classroom & Library — Going To The Regatta — CATALOGUED
 dict(day='2026-10-09', base=14, pid='gds/regatta/sloops-at-salt-pond-20260830', pad=False, board=B_LI,
  alt='Three Bahamian C1 sloops under full sail racing past a line of festival tents, crews out '
      'on the pry boards, bunting and vendor stalls along the shore behind them.',
  fb=tail("A reader that doubles as a social studies lesson.\n\nGoing To The Regatta is a true "
    "family account, but the history sits inside it for any teacher who wants it. The first "
    "recorded organised race was at Deadman's Cay in 1868. Racing near Salt Pond began in 1967, "
    "when a schools inspector and others started racing and a visiting American businessman "
    "offered a trophy — a three-day event followed. From 1969, Long Island descendants living in "
    "New Providence raised money for the prizes. In August 1973 the Long Islanders Association "
    "formed, working on education, recreation, medical assistance and support for Long Island "
    "families.\n\nThat is a century of island history a class can follow in one sitting, attached "
    "to a family they have already met.\n\nAges 5 to 15. A family reader — one book the whole "
    "class range can share.\n\n" + REG),
  ig=tail("A reader that doubles as a social studies lesson. 📚⛵\n\nFirst recorded organised race: "
    "Deadman's Cay, 1868. Racing near Salt Pond from 1967. From 1969 Long Island descendants in "
    "New Providence raised the prize money. August 1973: the Long Islanders Association forms — "
    "education, recreation, medical assistance, support for Long Island families.\n\nA century of "
    "island history, attached to a family a child has already met.\n\nAges 5–15.\n\n" + REG,
    "#GoingToTheRegatta #LongIsland #Bahamas #SocialStudies #TeacherResources #BahamianHistory"),
  pin_t='A Bahamian reader that doubles as a social studies lesson',
  pin=tail("Going To The Regatta carries real Long Island history: the first recorded organised "
    "race at Deadman's Cay in 1868, racing near Salt Pond from 1967, and the Long Islanders "
    "Association formed in August 1973. Ages 5 to 15.\n\n" + REG),
  pin_url=REG),

 # Sat 10 Oct — slot 56 — pillar 0 Book World — All Things Bahamian: Lower — NEW ART
 dict(day='2026-10-10', base=14, pid='gds/atb-lower/queens-staircase-20261010', pad=False, board=B_COLOR,
  alt='The Queen’s Staircase in Nassau: a long flight of worn limestone steps cut down through a '
      'narrow gorge, with tall pale stone walls draped in ferns and vines either side and '
      'dappled sunlight falling across the steps.',
  fb=tail("Sixty-six steps, cut down through solid limestone.\n\nThe Queen's Staircase in "
    "Nassau is also called the 66 Steps, and it has a page in All Things Bahamian — in Historic "
    "Places and Landmarks, the third of the book's seven sections, alongside the forts, the "
    "monuments and the lighthouses.\n\nOur illustration above is how we picture the walk up: "
    "cool green shade, ferns in the stone, light coming down through the trees. The page in the "
    "book is a line drawing waiting for a child's colouring pencils.\n\nAll Things Bahamian: "
    "Lower Elementary. Grades 1 to 3. 83 pages.\n\n" + ATBL),
  ig=tail("Sixty-six steps, cut down through solid limestone. 🪜\n\nThe Queen's Staircase — the "
    "66 Steps — has a page in All Things Bahamian, in Historic Places and Landmarks, one of the "
    "book's seven sections.\n\nThis is our illustration of the place. The page in the book is a "
    "line drawing waiting for colouring pencils. ✏️\n\nLower Elementary: grades 1–3, 83 pages.\n\n"
    + ATBL, "#AllThingsBahamian #QueensStaircase #Nassau #Bahamas #ColouringBook #BahamianKids"),
  pin_t='The Queen’s Staircase — All Things Bahamian',
  pin=tail("The Queen's Staircase in Nassau, also called the 66 Steps, has a page in All Things "
    "Bahamian — in Historic Places and Landmarks, one of the book's seven sections. Lower "
    "Elementary: grades 1 to 3.\n\n" + ATBL),
  pin_url=ATBL),

 # Sat 10 Oct — slot 57 — pillar 1 Behind the Scenes — Girl & Whale activity book — NEW ART
 dict(day='2026-10-10', base=19, pid='gds/girl-whale-activity/designing-the-finback-20261010', pad=False, board=B_COLOR,
  alt='An illustrator’s worktable seen from above, scattered with pencil sketches of a humpback '
      'whale — a tail fluke, a long pectoral fin, a whole whale in outline. On one sheet a fin '
      'has been coloured deep purple and scattered with starlight. A purple and a graphite '
      'pencil, a sharpener with shavings, an eraser, a jar of coloured pencils and a conch shell '
      'lie around them.',
  fb=tail("Before a child can design their own, somebody has to draw the real one.\n\nThe Girl and "
    "The Whale Coloring & Activity Book has a page called Design Your Own Cosmic Finback. For "
    "that page to work, the book also teaches the anatomy: Label the Humpback Whale, and "
    "Connect the Cosmic Finback 1 to 30.\n\nSo the drawing starts with the real animal. A "
    "humpback is a mammal, not a fish. It breathes air through a blowhole, not gills. That tail "
    "is a fluke. Get those right, and only then does the fin turn cosmic purple.\n\nThis is the "
    "worktable, not a page from the book — but it is where the pages come from.\n\nThe Girl and "
    "The Whale Coloring & Activity Book. 40 pages, ages 6 to 12.\n\nReader: " + GW +
    "\nActivity book: " + GWA),
  ig=tail("Before a child designs their own, somebody draws the real one. 🐋✏️\n\nDesign Your Own "
    "Cosmic Finback only works if the book teaches the anatomy too — Label the Humpback Whale, "
    "Connect the Cosmic Finback 1 to 30.\n\nSo it starts with the real animal. A humpback is a "
    "mammal, not a fish. It breathes through a blowhole, not gills. That tail is a fluke.\n\nThen "
    "the fin turns cosmic purple. 💜\n\nThis is the worktable, not a page from the book.\n\n"
    "40 pages, ages 6–12.\n\nReader: " + GW + "\nActivity book: " + GWA,
    "#BehindTheScenes #TheGirlAndTheWhale #ActivityBook #Humpback #ChildrensBooks #Bahamas"),
  pin_t='Designing the Cosmic Finback — behind the activity book',
  pin=tail("Design Your Own Cosmic Finback only works if the book teaches the anatomy too. A "
    "humpback is a mammal, not a fish; it breathes through a blowhole; the tail is a fluke. Then "
    "the fin turns cosmic purple. 40 pages, ages 6 to 12.\n\nReader: " + GW +
    "\nActivity book: " + GWA),
  pin_url=GWA),

 # Sun 11 Oct — slot 58 — pillar 2 Reader Engagement — Regatta activity book — CATALOGUED
 dict(day='2026-10-11', base=14, pid='gds/regatta-activity/deans-blue-hole-20260831', pad=False, board=B_COLOR,
  alt='Dean’s Blue Hole, a deep circle of dark water inside a pale turquoise bay ringed by '
      'limestone and low green trees, with the open sea beyond.',
  fb=tail("The family never got there. That is the point.\n\nGoing To The Regatta is a true "
    "account, and in five days on Long Island they did not reach Dean's Blue Hole — the second "
    "deepest in the world. So the reader hands the question to you instead, and the activity "
    "book has a page for it: A Future Dean's Blue Hole Adventure.\n\nWhat would Nicholas notice "
    "first? What would he want to learn before he went? What would he remember afterwards?\n\n"
    "Tell us in the comments — and if a child in your house has an answer, that is the page "
    "waiting for them.\n\nGoing To The Regatta Coloring & Activity Book. 40 pages, ages 6 to "
    "12.\n\nReader: " + REG + "\nActivity book: " + REGA),
  ig=tail("The family never got there. That's the point. 🌊\n\nFive days on Long Island and they "
    "never reached Dean's Blue Hole — the second deepest in the world. So the book hands the "
    "question over: A Future Dean's Blue Hole Adventure.\n\nWhat would Nicholas notice first? "
    "What would he want to learn before going? What would he remember after?\n\nTell us below. 👇"
    "\n\n40 pages, ages 6–12.\n\nReader: " + REG + "\nActivity book: " + REGA,
    "#DeansBlueHole #LongIsland #Bahamas #ActivityBook #KidsActivities #GoingToTheRegatta"),
  pin_t='A future Dean’s Blue Hole adventure — activity book page',
  pin=tail("In five days on Long Island the family never reached Dean's Blue Hole, the second "
    "deepest in the world. So the activity book hands the trip to the reader: what would you "
    "notice, learn and remember? 40 pages, ages 6 to 12.\n\nReader: " + REG +
    "\nActivity book: " + REGA),
  pin_url=REGA),

 # Sun 11 Oct — slot 59 — pillar 3 Promo/CTA — The Girl and The Whale — CATALOGUED (real page 20)
 dict(day='2026-10-11', base=19, pid='gds/girl-whale/page20-riding-the-whale-20260826', pad=True, board=B_READ,
  alt='Page 20 of The Girl and The Whale: Anna, a girl with chocolate-brown skin and long black '
      'hair in a floral sundress, sits astride an enormous whale made of purple starfield, flying '
      'through the night sky above a lit island and the sea.',
  fb=tail("Page 20. The whole book has been building to this.\n\nThe whale lifts Anna onto a "
    "glowing fin and carries her above the mountains, the beaches, the houses and the sea. Below "
    "her, the people of Hawaii look up and see her go.\n\nShe had done the dance and nothing had "
    "happened. She had given up. This is what came after.\n\nThe Girl and The Whale, by Zhané "
    "Mackey. Ages 6 to 12, grades 1 to 6.\n\nThe reader and its Coloring & Activity Book are "
    "below — the pair is how most families buy it.\n\nReader: " + GW + "\nActivity book: " + GWA),
  ig=tail("Page 20. The whole book has been building to this. ✨🐋\n\nThe whale lifts Anna onto a "
    "glowing fin and carries her above the mountains, the beaches, the houses and the sea. Below, "
    "the people of Hawaii look up and watch her go.\n\nShe had done the dance. Nothing had "
    "happened. She had given up.\n\nThis is what came after.\n\nBy Zhané Mackey. Ages 6–12.\n\n"
    "Reader: " + GW + "\nActivity book: " + GWA,
    "#TheGirlAndTheWhale #ChildrensBooks #ReadingForKids #Bahamas #BelieveInWonder #PictureBooks"),
  pin_t='Page 20 — The Girl and The Whale',
  pin=tail("The whale lifts Anna onto a glowing fin and carries her above the mountains, beaches, "
    "houses and sea, while the people of Hawaii look up and watch her go. By Zhané Mackey. Ages "
    "6 to 12.\n\nReader: " + GW + "\nActivity book: " + GWA),
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
