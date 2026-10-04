# -*- coding: utf-8 -*-
"""Week 45: Mon 5 - Wed 7 Oct 2026. Four slots.
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
 # Mon 5 Oct — slot 50 — pillar 1 Behind the Scenes — Going To The Regatta — NEW ART
 dict(day='2026-10-05', base=14, pid='gds/regatta/friday-soup-at-green-leaf-20261005b', pad=False, board=B_LI,
  alt='A deep white enamel bowl of thick Bahamian soup with chunks of root vegetable, a wedge of '
      'lime on the rim, beside a fresh green coconut cut open with a straw in it, a folded paper '
      'napkin with a spoon resting on it, and a scattering of pigeon peas on a worn wooden table. '
      'Behind, the open serving window of a mint green and coral building with bougainvillea '
      'against the wall.',
  fb=tail("The detail people always ask about.\n\nGoing To The Regatta stops for lunch, because the "
    "drive down Long Island does. Soup on a Friday, a coconut cut open at the top, a table in the "
    "shade outside a little painted takeaway.\n\nWe could have skipped it. A plot does not need "
    "lunch. But a Bahamian child reading it needs to recognise their own Friday, and the recognising "
    "is most of what makes a child keep turning pages.\n\nThat is the whole approach to this book: "
    "the ordinary bits are not filler. They are the point.\n\n"
    "Going To The Regatta. Ages 6 to 12.\n\n"+REG),
  ig=tail("The detail people always ask about. 🥥\n\nGoing To The Regatta stops for lunch, because "
    "the drive down Long Island does. Soup on a Friday, a coconut cut open at the top, a table in "
    "the shade outside a little painted takeaway.\n\nA plot doesn't need lunch. But a Bahamian "
    "child needs to recognise their own Friday — and the recognising is most of what keeps a child "
    "turning pages. 📖\n\nThe ordinary bits aren't filler. They're the point.\n\nAges 6–12.\n\n"+REG,
    "#BahamianFood #LongIslandBahamas #GoingToTheRegatta #ChildrensBooks #Bahamas #FridaySoup"),
  pin_t='Friday soup and a coconut — Going To The Regatta',
  pin=tail("The book stops for lunch, because the drive down Long Island does. Soup on a Friday, a "
    "coconut cut open at the top. The ordinary bits are not filler — they are what a Bahamian child "
    "recognises. Ages 6 to 12.\n\n"+REG),
  pin_url=REG),

 # Tue 6 Oct — slot 51 — pillar 2 Reader Engagement — ATB Lower — CATALOGUED
 dict(day='2026-10-06', base=14, pid='gds/atb-lower/straw-market-20260909', pad=False, board=B_COLOR,
  alt='A bright illustration of a Bahamian straw market stall hung with woven baskets, bags and '
      'hats, in flat clear colour with simple bold shapes.',
  fb=tail("A question for anyone who learned to plait.\n\nStraw work is one of the few Bahamian "
    "crafts a child can still watch being made — the palm strips, the plaiting, the long patient "
    "coiling. It is the kind of thing All Things Bahamian was made for: the ordinary Bahamian "
    "world a child already half knows, put in front of them properly.\n\nSo: who taught you? A "
    "grandmother, an aunt, a neighbour on a porch? And did you keep it up?\n\nTell us in the "
    "comments. We ask because we suspect the answer is mostly no, and that is worth "
    "knowing.\n\nAll Things Bahamian: My First Cultural Coloring Book. Ages 5 to 9.\n\n"+ATBL),
  ig=tail("A question for anyone who learned to plait. 🧺\n\nStraw work is one of the few Bahamian "
    "crafts most children still see being made — the palm strips, the plaiting, the long patient "
    "coiling.\n\nSo: who taught you? A grandmother, an aunt, a neighbour on a porch? And did you "
    "keep it up?\n\nTell us below. We ask because we suspect the answer is mostly no. 👇\n\n"
    "All Things Bahamian: My First Cultural Coloring Book. Ages 5–9.\n\n"+ATBL,
    "#StrawWork #BahamianCulture #BahamianKids #ColoringBook #Bahamas #ReaderQuestion"),
  pin_t='Who taught you to plait? — All Things Bahamian, Ages 5 to 9',
  pin=tail("Straw work is one of the few Bahamian crafts a child can still watch being made — the "
    "palm strips, the plaiting, the patient coiling. The ordinary Bahamian world a child already "
    "half knows. All Things Bahamian: My First Cultural Coloring Book, ages 5 to 9.\n\n"+ATBL),
  pin_url=ATBL),

 # Wed 7 Oct — slot 52 — pillar 3 Promo/CTA — The Girl and The Whale — NEW ART — BUNDLE DAY
 dict(day='2026-10-07', base=14, pid='gds/girl-whale/annas-dance-at-sunset-20261007b', pad=False, board=B_READ,
  alt='Anna, a Black girl of about thirteen with chocolate-brown skin and long black hair, dances '
      'barefoot on wet sand at the edge of the sea at sunset, arms thrown wide and head tipped back '
      'mid-spin, her reflection in the thin sheet of water beneath her. She wears a knee-length '
      'floral sundress and a white shell necklace. The low orange sun, green volcanic mountains and '
      'two seabirds are behind her.',
  fb=tail("She does the dance. Nothing happens.\n\nThe legend gave Anna an instruction: dance at "
    "sunset, at the edge of the water. So she does — and the sky goes coral and gold and the sea "
    "stays empty, and she gives up.\n\nThat is the page we are proudest of. Most children's books "
    "would have the whale arrive on cue. This one makes her stand there in the dark feeling "
    "foolish first, because every child who has ever believed something has had that exact "
    "minute.\n\nWhat happens next is worth the wait.\n\nToday is bundle day: the reader and its "
    "Coloring & Activity Book, below.\n\nThe Girl and The Whale, by Zhané Mackey. Ages 6 to "
    "12.\n\nReader: "+GW+"\nActivity book: "+GWA),
  ig=tail("She does the dance. Nothing happens. 🌅\n\nThe legend gave Anna an instruction: dance "
    "at sunset, at the edge of the water. So she does — the sky goes coral and gold, the sea stays "
    "empty, and she gives up.\n\nThat's the page we're proudest of. Most books would have the "
    "whale arrive on cue. This one makes her stand there feeling foolish first, because every "
    "child who has believed something has had that exact minute. ✨\n\nWhat happens next is worth "
    "the wait.\n\nBundle day: reader + activity book.\n\nBy Zhané Mackey. Ages 6–12.\n\n"
    "Reader: "+GW+"\nActivity book: "+GWA,
    "#TheGirlAndTheWhale #ChildrensBooks #ReadingForKids #Bahamas #BelieveInWonder"),
  pin_t='She does the dance. Nothing happens. — The Girl and The Whale',
  pin=tail("The legend told Anna to dance at sunset. She does, the sea stays empty, and she gives "
    "up — because every child who has believed something has had that exact minute. What happens "
    "next is worth the wait. Ages 6 to 12.\n\nReader: "+GW+"\nActivity book: "+GWA),
  pin_url=GW),

 # Wed 7 Oct — slot 53 — pillar 4 Activity Spotlight — GW Activity Book — CATALOGUED
 dict(day='2026-10-07', base=19, pid='gds/girl-whale-activity/title-page-20260826', pad=True, board=B_READ,
  alt='The title page of The Girl and The Whale Coloring and Activity Book, a black and white line '
      'drawing of the whale and the title lettering ready to be coloured in.',
  fb=tail("The other half of bundle day, and the page children colour first.\n\nIt is the title "
    "page, and it is deliberately the simplest thing in the book. A child who has just finished the "
    "reader opens the activity book and is immediately able to do something — before any question, "
    "any puzzle, any writing line.\n\nAfter that come the harder pages: Crack the Cosmic Code, the "
    "word search, Design Your Own Cosmic Finback, the sorting of legend from reality.\n\nEasy first "
    "is not a small decision. It is the difference between a book a child opens twice and one they "
    "finish.\n\nThe Girl and The Whale Coloring & Activity Book. Ages 6 to 12.\n\n"
    "Reader: "+GW+"\nActivity book: "+GWA),
  ig=tail("The page children colour first. 🐋\n\nIt's the title page, and it's deliberately the "
    "simplest thing in the book. A child who's just finished the reader opens this and can "
    "immediately do something — before any question, puzzle or writing line.\n\nThen come the "
    "harder pages: Crack the Cosmic Code, the word search, Design Your Own Cosmic Finback.\n\n"
    "Easy first isn't a small decision. It's the difference between a book opened twice and one "
    "that gets finished. ✏️\n\nAges 6–12.\n\nReader: "+GW+"\nActivity book: "+GWA,
    "#ActivityBook #TheGirlAndTheWhale #ColoringPages #ReadingForKids #Bahamas"),
  pin_t='The page children colour first — The Girl and The Whale activity book',
  pin=tail("The title page is deliberately the simplest thing in the book: a child who has just "
    "finished the reader can immediately do something. The harder pages come after. Ages 6 to "
    "12.\n\nReader: "+GW+"\nActivity book: "+GWA),
  pin_url=GWA),
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
