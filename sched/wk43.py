# -*- coding: utf-8 -*-
"""Week 43: Mon 28 - Wed 30 Sep 2026. Four slots.
Two on new sunburst artwork, two on catalogued assets.

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
 # Mon 28 — slot 40 — All Things Bahamian: Upper Elementary — NEW ART
 dict(day='2026-09-28', base=14, pid='gds/atb-upper/fruits-of-the-bahamas-20260928', pad=False, board=B_COLOR,
  alt='A roadside fruit stall under a faded blue awning: sapodillas, guavas halved to show pink '
      'flesh, knobbly green sugar apples, a bunch of small bananas, tamarind pods in a shallow '
      'basket and two halved papayas. A straw basket at one end, pink and yellow wooden houses, a '
      'coconut palm and turquoise sea behind.',
  fb=tail("Ask a Bahamian child to name a fruit and you will hear mango. Ask for five and it gets "
    "interesting.\n\nSapodilla. Guava. Sugar apple. Tamarind. Sea grape. Gooseberry. Dilly. These "
    "are the ones that grow in the yard, that children eat walking home, and that almost never "
    "appear in an imported school book.\n\nAll Things Bahamian: Upper Elementary gives them a "
    "section of their own, and it does not stop at naming them. One question asks the child to "
    "explain how rainfall, soil and island location might affect a fruit harvest. That is a "
    "geography lesson wearing a colouring page.\n\nAll Things Bahamian: Upper Elementary. Ages 9 to "
    "12.\n\n"+ATBU),
  ig=tail("Name five Bahamian fruits. 🥭\n\nMango is easy. Then it gets interesting: sapodilla, "
    "guava, sugar apple, tamarind, sea grape, gooseberry, dilly.\n\nThe ones that grow in the yard, "
    "that children eat walking home — and that almost never turn up in an imported school book.\n\n"
    "All Things Bahamian: Upper Elementary gives them a whole section, and asks the child to work "
    "out how rainfall and soil affect a harvest. 🌱\n\nAges 9–12.\n\n"+ATBU,
    "#BahamianFruit #AllThingsBahamian #BahamianCulture #ClassroomResources #Bahamas #Sapodilla"),
  pin_t='The fruits of The Bahamas — All Things Bahamian, Ages 9 to 12',
  pin=tail("Sapodilla, guava, sugar apple, tamarind, sea grape, dilly. The fruits that grow in a "
    "Bahamian yard and almost never appear in an imported school book. A whole section of All "
    "Things Bahamian: Upper Elementary. Ages 9 to 12.\n\n"+ATBU),
  pin_url=ATBU),

 # Tue 29 — slot 41 — pillar 6 Classroom & Library — Regatta Activity Book — CATALOGUED
 dict(day='2026-09-29', base=14, pid='gds/regatta-activity/nature-study-desk-20260906', pad=False, board=B_COLOR,
  alt='A nature study table laid out with shells, a piece of coral, a magnifying glass, a notebook '
      'and coloured pencils, beside an open activity book.',
  fb=tail("What a Bahamian nature table actually holds.\n\nNot acorns and conkers. Conch shell, "
    "sea fan, a piece of brain coral, a sand dollar, a length of sea grape leaf gone leathery.\n\n"
    "The Going To The Regatta Coloring & Activity Book was built for that table. It pairs with the "
    "reader so a child can read about Long Island in one sitting and then spend a week drawing, "
    "labelling and looking closely at what the story described.\n\nIf you run a classroom nature "
    "corner, this is the one that matches what your children can actually go outside and find.\n\n"
    "Going To The Regatta Coloring & Activity Book. Ages 6 to 12.\n\n"+REGA),
  ig=tail("What a Bahamian nature table actually holds. 🐚\n\nNot acorns and conkers. Conch shell, "
    "sea fan, brain coral, a sand dollar, a sea grape leaf gone leathery.\n\nThe Going To The "
    "Regatta activity book was made for that table — read about Long Island in one sitting, then "
    "spend a week drawing and labelling what the story described. 🔍\n\nAges 6–12.\n\n"+REGA,
    "#NatureTable #ClassroomLibrary #BahamianKids #ActivityBook #Bahamas #LongIsland"),
  pin_t='A Bahamian nature table — Going To The Regatta activity book',
  pin=tail("Conch shell, sea fan, brain coral, a sand dollar. Not acorns and conkers. The Going To "
    "The Regatta Coloring & Activity Book was built for the Bahamian nature corner. Ages 6 to 12.\n\n"+REGA),
  pin_url=REGA),

 # Wed 30 — slot 42 — pillar 0 Book World — Going To The Regatta reader — NEW ART — BUNDLE DAY
 dict(day='2026-09-30', base=14, pid='gds/regatta/cape-santa-maria-20260930', pad=False, board=B_LI,
  alt='A long curve of pale sand at Cape Santa Maria, Long Island, with water grading from clear '
      'turquoise shallows to deep blue. Sea grape bushes along the dune, three coconut palms '
      'leaning in the wind, a weathered wooden dinghy pulled up on the sand and conch shells at the '
      'tideline in late afternoon light.',
  fb=tail("Cape Santa Maria. If you have been, you already know why it is in the book.\n\n"
    "Going To The Regatta follows Nicholas and his family the length of Long Island — Cape Santa "
    "Maria, Stella Maris, Simms, Salt Pond, Deadman's Cay. It is a real route, in order, the way "
    "the drive actually happens.\n\nThat is the difference between a book set in The Bahamas and a "
    "book about somewhere in The Bahamas. A Long Island child reading this recognises the order of "
    "the settlements.\n\nToday is bundle day — the reader and its Coloring & Activity Book, "
    "below.\n\nGoing To The Regatta. Ages 6 to 12.\n\nReader: "+REG+"\nActivity book: "+REGA),
  ig=tail("Cape Santa Maria. If you've been, you know why it's in the book. 🏝️\n\nGoing To The "
    "Regatta follows Nicholas and his family the length of Long Island — Cape Santa Maria, Stella "
    "Maris, Simms, Salt Pond, Deadman's Cay. A real route, in order, the way the drive actually "
    "happens.\n\nA Long Island child reading this recognises the order of the settlements. 🚗\n\n"
    "Bundle day: reader + activity book.\n\nAges 6–12.\n\nReader: "+REG+"\nActivity book: "+REGA,
    "#CapeSantaMaria #LongIslandBahamas #GoingToTheRegatta #ChildrensBooks #Bahamas"),
  pin_t='Cape Santa Maria — Going To The Regatta, a real Long Island route',
  pin=tail("Cape Santa Maria, Stella Maris, Simms, Salt Pond, Deadman's Cay — a real route, in "
    "order, the way the drive actually happens. Reader and activity book. Ages 6 to 12.\n\n"
    "Reader: "+REG+"\nActivity book: "+REGA),
  pin_url=REG),

 # Wed 30 — slot 43 — pillar 1 Behind the Scenes — Regatta Activity Book — CATALOGUED
 dict(day='2026-09-30', base=19, pid='gds/regatta/writers-desk-longisland-v2-20260905', pad=False, board=B_LI,
  alt='A writer\'s desk with a hand-drawn map of Long Island, a notebook of handwritten notes, a '
      'pencil, a coffee cup and a small conch shell, lit by a window.',
  fb=tail("The second half of bundle day, and a look at how the book got made.\n\n"
    "Going To The Regatta started as a family drive, not a plot. The map came first — the "
    "settlements in the order you pass them — and the story was fitted to the road, rather than the "
    "road invented for the story.\n\nThat is why the activity book works the way it does. It follows "
    "the same route, so a child colours and labels the island in the order they read about it.\n\n"
    "Going To The Regatta. Ages 6 to 12.\n\nReader: "+REG+"\nActivity book: "+REGA),
  ig=tail("How the book actually got made. 🗺️✏️\n\nGoing To The Regatta started as a family drive, "
    "not a plot. The map came first — settlements in the order you pass them — and the story was "
    "fitted to the road, not the road invented for the story.\n\nThat's why the activity book "
    "follows the same route: colour and label the island in the order you read about it.\n\n"
    "Ages 6–12.\n\nReader: "+REG+"\nActivity book: "+REGA,
    "#BehindTheScenes #GoingToTheRegatta #LongIslandBahamas #ChildrensBooks #Bahamas"),
  pin_t='The map came first — making Going To The Regatta',
  pin=tail("The book started as a family drive, not a plot. The map came first, settlements in the "
    "order you pass them, and the story was fitted to the road. Reader and activity book, ages 6 "
    "to 12.\n\nReader: "+REG+"\nActivity book: "+REGA),
  pin_url=REGA),
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
