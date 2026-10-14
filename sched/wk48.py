# -*- coding: utf-8 -*-
"""Week 48: Thu 15 - Sun 18 Oct 2026. Six slots over four days.
TWO COLLAGE DAYS: Sat 17 (Activity Spotlight) and Sun 18 14:00 (Bahamian Culture)
- the two pillars where showing a book's RANGE beats a single hero.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from post import run, STD, IGC, IGP

B_COLOR, B_READ, B_LI, B_CULT = ('830421687481393074','830421687481391572',
                                 '830421687481393086','830421687481393085')
GW   = 'https://www.amazon.com/dp/B0HCB7V9C9'; GWA  = 'https://www.amazon.com/dp/B0HG8NKYV2'
REG  = 'https://www.amazon.com/dp/B0HGKNTNDD'; REGA = 'https://www.amazon.com/dp/B0HH8PVQZ9'
ATBU = 'https://www.amazon.com/dp/B0HC1PJ4DS'; ATBL = 'https://www.amazon.com/dp/B0HBNFLDQP'
GDSI = 'GDS-Images — https://pictures.gdsbahamas.com/'
tail = lambda t, tags=None: t + "\n\n" + GDSI + (("\n\n" + tags) if tags else "")

S = [
 # Thu 15 Oct — slot 64 — pillar 1 Behind the Scenes — ATB Lower — NEW ART
 dict(day='2026-10-15', base=14, pid='gds/atb-lower/colouring-tips-desk-20261015',
  pad=False, board=B_COLOR,
  alt='A worktable seen from above with practice patches of pencil shading — light, medium, pressed '
      'dark and a blend — beside a line drawing of a flamingo half coloured in. A jar of coloured '
      'pencils, a sharpener with shavings and an eraser around them, and a leafy plant stirring by '
      'the window.',
  fb=tail("The younger book gets a page the older one does not.\n\nAll Things Bahamian comes in two "
    "editions that share their artwork — the same drawings, page for page. What differs is the "
    "written work around them, and one of the things the Lower Elementary edition adds is a "
    "Colouring Tips page.\n\nThat is what the page covers, and above is how we picture it being worked out \u2014 how hard to press, how to "
    "build a light wash into a deep one, how to blend one into the other. A nine-year-old does not "
    "need it. A six-year-old does, and without it the first page they open can be the last one they "
    "finish.\n\nThe Lower edition also adds simpler design activities — Design Your Own Junkanoo "
    "Costume among them.\n\nAll Things Bahamian: Lower Elementary. Grades 1 to 3. 83 pages.\n\n" + ATBL),
  ig=tail("The younger book gets a page the older one doesn't. ✏️\n\nBoth editions of All Things "
    "Bahamian share the same artwork. What changes is the written work around it — and the Lower "
    "edition adds a Colouring Tips page.\n\nHow hard to press. How to build a light wash into a deep "
    "one. How to blend.\n\nA nine-year-old doesn't need that. A six-year-old does, and without it "
    "the first page they open can be the last one they finish.\n\nGrades 1–3, 83 pages.\n\n" + ATBL,
    "#AllThingsBahamian #ColouringBook #BahamianKids #Bahamas #EarlyYears #ColouringTips"),
  pin_t='The page the younger edition adds — All Things Bahamian',
  pin=tail("Both editions of All Things Bahamian share the same artwork; the written work around it "
    "is what differs. The Lower Elementary edition adds a Colouring Tips page — how hard to press, "
    "how to blend. Grades 1 to 3, 83 pages.\n\n" + ATBL),
  pin_url=ATBL),

 # Fri 16 Oct — slot 65 — pillar 2 Reader Engagement — The Girl and The Whale — CATALOGUED
 dict(day='2026-10-16', base=14, pid='gds/girl-whale/reef-at-sunset-20260907',
  pad=False, board=B_READ,
  alt='Anna, a girl of about thirteen with chocolate-brown skin and long black hair in a floral '
      'sundress, stands in calm shallow water over a coral reef at sunset with one hand raised as an '
      'enormous whale scattered with cosmic purple starlight rises out of the water in front of her.',
  fb=tail("What would you have said?\n\nAnna has done everything the legend asked. She danced at the "
    "reef at sunset. Nothing happened, and she gave up. Then the water turned purple and the largest "
    "humpback in the world came up in front of her.\n\nShe screams and falls backwards. That is the "
    "honest answer, and it is what the book gives her.\n\nBut we want yours. If the Cosmic Theseus "
    "Finback surfaced an arm's length away and waited — what would you say to her? Tell us in the "
    "comments, and if there is a child in the house, ask them first. Their answer will be better than "
    "ours.\n\nThe Girl and The Whale, by Zhané Mackey. Ages 6 to 12.\n\n" + GW),
  ig=tail("What would you have said? 🐋💜\n\nAnna danced at the reef at sunset, exactly as the legend "
    "asked. Nothing happened. She gave up.\n\nThen the water turned purple and the largest humpback in "
    "the world came up in front of her.\n\nIn the book she screams and falls backwards — the honest "
    "answer. But if she surfaced an arm's length from YOU and waited, what would you say?\n\nTell us "
    "below 👇 and ask a child first. Their answer will be better.\n\nBy Zhané Mackey. Ages 6–12.\n\n"
    + GW, "#TheGirlAndTheWhale #ReadingForKids #ChildrensBooks #Bahamas #BelieveInWonder"),
  pin_t='What would you have said? — The Girl and The Whale',
  pin=tail("Anna danced at the reef at sunset as the legend asked, nothing happened, and she gave up. "
    "Then the largest humpback in the world rose in front of her. In the book she screams and falls "
    "backwards. What would you have said? By Zhané Mackey. Ages 6 to 12.\n\n" + GW),
  pin_url=GW),

 # Fri 16 Oct — slot 66 — pillar 3 Promo/CTA — Going To The Regatta — NEW ART
 dict(day='2026-10-16', base=19, pid='gds/regatta/sunrise-over-the-atlantic-20261016',
  pad=False, board=B_LI,
  alt='Sunrise over the Atlantic from the rocky Long Island shore: the sun just clear of the horizon, '
      'the sky banded apricot and gold, a low swell rolling in and small waves running up the pale '
      'sand in a thin lace of foam, with casuarinas leaning and two seabirds on the wing.',
  fb=tail("One book the whole family can read.\n\nMost children's books pick an age and stay there. "
    "Going To The Regatta is a family reader, ages 5 to 15, and it works across that whole range "
    "because it is a true account rather than a plot — five days on Long Island, told as they "
    "happened.\n\nA five-year-old follows the trip: the plane, the house above the Atlantic, the "
    "soup, the boats. A fifteen-year-old reads the other layer — a homecoming, a family spread "
    "between islands and Florida, a regatta whose first recorded organised race was in 1868.\n\nSame pages. Same "
    "evening. Nobody is being read down to.\n\nGoing To The Regatta, by Bridgette Skeete-Mackey. "
    "Illustrated with real family photographs.\n\n" + REG),
  ig=tail("One book the whole family can read. 🌅\n\nGoing To The Regatta is a family reader, ages "
    "5–15, and it works across that range because it's a true account rather than a plot — five days "
    "on Long Island, told as they happened.\n\nA five-year-old follows the trip. A fifteen-year-old "
    "reads the other layer: a homecoming, a family spread between islands and Florida, a regatta whose "
    "first recorded organised race was in 1868.\n\nSame pages. Same evening. Nobody read down to.\n\nBy Bridgette Skeete-Mackey.\n\n"
    + REG, "#GoingToTheRegatta #FamilyReading #LongIsland #Bahamas #ChildrensBooks #ReadTogether"),
  pin_t='One book the whole family can read — Going To The Regatta',
  pin=tail("A family reader for ages 5 to 15: five days on Long Island, told as they happened. The "
    "youngest follow the trip; the oldest read the homecoming underneath it. By Bridgette "
    "Skeete-Mackey.\n\n" + REG),
  pin_url=REG),

 # Sat 17 Oct — slot 67 — pillar 4 Activity Spotlight — Girl & Whale activity book — COLLAGE
 dict(day='2026-10-17', base=14, board=B_COLOR, pad=False,
  # 'Listen Like Anna' is an activity title; none of these four panels show her.
  anna_absent=True,
  panels=['gds/girl-whale-activity/coral-reef-i-spy-20261017',
          'gds/girl-whale-activity/the-comet-strikes-cosmic-20261003',
          'gds/girl-whale-activity/designing-the-finback-20261010',
          'gds/girl-whale-activity/cosmic-bookmarks-20261017'],
  alts=['A bright coral reef underwater with shells, orange starfish, striped fish, two crabs and two '
        'green turtles, and a small leather-bound book resting half hidden on the sand, sunlight '
        'flickering down in slow bands.',
        'An enormous humpback whale rising through deep night water, her long pectoral fins glowing '
        'cosmic purple and scattered with starlight, as a comet streaks down towards the sea.',
        'An illustrator’s worktable scattered with pencil sketches of a humpback whale — a tail '
        'fluke, a pectoral fin, a whole whale in outline — with one fin coloured deep purple and '
        'scattered with starlight.',
        'Four finished paper bookmarks on a pale wooden desk, decorated by hand with a whale tail, a '
        'starry night sky, small waves and a ribbon of starlight, with scissors, twine and a jar of '
        'coloured pencils beside them.'],
  collage='gds/girl-whale-activity/collage-make-and-find-20261017',
  alt='A four-panel collage from The Girl and The Whale Coloring & Activity Book: a coral reef '
      'seek-and-find, the Cosmic Theseus Finback rising as a comet falls, an illustrator’s table of '
      'whale sketches, and four hand-decorated bookmarks.',
  fb=tail("Forty pages, and the colouring is the smallest part of it.\n\nSwipe our illustrations of what is in it \u2014 in the book these are line drawings waiting for pencils. "
    "Coral Reef I-Spy, where the page "
    "asks a child to find six shells, five starfish, four fish, three crabs, two sea turtles and one "
    "tiny legend book. The Cosmic Theseus Finback, who took a comet strike to save every creature in "
    "the sea. The whale anatomy the book teaches alongside Design Your Own Cosmic Finback. And "
    "Cosmic Bookmarks, to cut out and keep.\n\nThere is also Crack the Cosmic Code — the answer is "
    "BELIEVE IN WONDER — Listen Like Anna, Create Your Own Island Legend, and a certificate at the "
    "end.\n\nThe Girl and The Whale Coloring & Activity Book. 40 pages, ages 6 to 12.\n\nReader: "
    + GW + "\nActivity book: " + GWA),
  ig=tail("Forty pages, and the colouring is the smallest part. 🐋✂️\n\nSwipe: Coral Reef I-Spy — the "
    "page asks for six shells, five starfish, four fish, three crabs, two sea turtles and one tiny "
    "legend book. The Cosmic Theseus Finback, who took a comet strike to save every creature in the "
    "sea. The whale anatomy the book teaches alongside Design Your Own Cosmic Finback. Bookmarks to cut out and "
    "keep.\n\nPlus Crack the Cosmic Code (the answer is BELIEVE IN WONDER), Listen Like Anna, Create "
    "Your Own Island Legend.\n\n40 pages, ages 6–12.\n\nReader: " + GW + "\nActivity book: " + GWA,
    "#TheGirlAndTheWhale #ActivityBook #KidsActivities #ChildrensBooks #Bahamas #SeekAndFind"),
  pin_t='Forty pages, and the colouring is the smallest part',
  pin=tail("Coral Reef I-Spy, the Cosmic Theseus Finback, the whale anatomy behind Design Your Own "
    "Cosmic Finback, and bookmarks to cut out and keep. The Girl and The Whale Coloring & Activity "
    "Book. 40 pages, ages 6 to 12.\n\nReader: " + GW + "\nActivity book: " + GWA),
  pin_url=GWA),

 # Sun 18 Oct — slot 68 — pillar 5 Bahamian Culture — ATB Upper — COLLAGE
 dict(day='2026-10-18', base=14, board=B_CULT, pad=False,
  panels=['gds/atb-upper/queen-conch-20261018-v5',
          'gds/atb-upper/junkanoo-bay-street-20261018',
          'gds/atb-upper/fruits-of-the-bahamas-20260928',
          'gds/atb-upper/glass-window-bridge-20261008-v2'],
  alts=['A live queen conch on pale rippled sand in clear shallow turquoise water, seen looking down '
        'into the shell. The broad flared lip is spread wide and glossy deep pink, and the animal '
        'is nestled inside it: a dark claw-shaped operculum, a mottled speckled foot, and a short '
        'blunt snout with two golden eyes looking out.',
        'A Junkanoo rush on Bay Street in Nassau at night: a lead dancer mid-stride in an enormous '
        'fanned headdress of pink, orange and turquoise crepe, drummers and cowbell shakers behind, '
        'and a crowd under lit street lamps.',
        'A roadside table piled with Bahamian fruit — guavas, sugar apples, bananas, papaya and '
        'sapodilla — with a pink clapboard house, palms and calm turquoise water behind.',
        'The Glass Window Bridge in Eleuthera: a road bridge crossing a narrow gap, the rough navy '
        'Atlantic beyond it and the calm clear turquoise Bight in the foreground.'],
  collage='gds/atb-upper/collage-island-culture-20261018-v5',
  alt='A four-panel collage from All Things Bahamian: a live queen conch looking out from inside its pink shell, a Junkanoo rush '
      'on Bay Street at night, a roadside table of Bahamian fruit, and the Glass Window Bridge with '
      'the Atlantic on one side and the calm Bight on the other.',
  fb=tail("Four sections, one country.\n\nAll Things Bahamian is built in seven sections, and these "
    "are four of them. Life in Our Bahamian Seas: the queen conch, which carries its strong shell "
    "wherever it goes. Junkanoo, which fills Bay Street with music, movement and colour. The Fruits "
    "of The Bahamas, where each one grows and when it is in season. And Our Beautiful Islands — the "
    "Glass Window in Eleuthera, where the open Atlantic and the calm Bight lie on opposite sides of "
    "a narrow strip of rock.\n\nThese are our illustrations of those subjects; in the book each one "
    "is a line drawing waiting for a child's colouring pencils.\n\nThe other three sections: "
    "national symbols, historic places and landmarks, and a closing make-your-own.\n\nAll Things "
    "Bahamian: Upper Elementary. Ages 9 to 12, grades 4 to 6. 109 pages.\n\n" + ATBU),
  ig=tail("Four sections, one country. 🇧🇸\n\nSwipe our illustrations of four of the book's seven "
    "sections — in the book each is a line drawing waiting for pencils.\n\nLife in Our Bahamian "
    "Seas: the queen conch, which carries its strong shell wherever it goes. Junkanoo, which fills "
    "Bay Street with music, movement and colour. The Fruits of The Bahamas. And Our Beautiful "
    "Islands — the Glass Window, where the Atlantic and the calm Bight sit either side of one narrow "
    "strip of rock.\n\nUpper Elementary: ages 9–12, grades 4–6, 109 pages.\n\n" + ATBU,
    "#AllThingsBahamian #Bahamas #Junkanoo #QueenConch #Eleuthera #BahamianKids #ColouringBook"),
  pin_t='Four sections, one country — All Things Bahamian',
  pin=tail("The queen conch, Junkanoo on Bay Street, the fruits of The Bahamas and the Glass Window "
    "Bridge — our illustrations of subjects from four of the book's seven sections. Upper "
    "Elementary: ages 9 to 12, 109 pages.\n\n" + ATBU),
  pin_url=ATBU),

 # Sun 18 Oct — slot 69 — pillar 6 Classroom & Library — Regatta activity book — NEW ART
 dict(day='2026-10-18', base=19, pid='gds/regatta-activity/nature-pool-observer-20261018',
  pad=False, board=B_COLOR,
  alt='A clear natural rock pool on the Long Island shore with pale sand and stones on the bottom, a '
      'few tiny fish, a small crab and green weed moving slowly, fine ripple rings spreading across '
      'the surface, and an open blank notebook, a pencil and a magnifying glass on the rock at the '
      'near edge.',
  fb=tail("A page that sends the class outside.\n\nIn Going To The Regatta the family walk a rocky "
    "path past the backyard down to the nature bath, a clear natural pool. The activity book turns "
    "that into Nature Pool Observer: sit beside water, watch, and write down what is actually "
    "there.\n\nIt needs no reef and no trip. A rock pool works. So does a puddle after rain, a "
    "drainage channel, a bucket left out overnight. The skill being taught is the same one every "
    "science lesson from here on will ask for — look first, record what you saw, not what you "
    "expected.\n\nIt sits alongside Parts of a C1 Racing Sloop, the Island Compass Challenge, Family "
    "Roots and Roles and Plan an Island Meal.\n\nGoing To The Regatta Coloring & Activity Book. 40 "
    "pages, ages 6 to 12.\n\nReader: " + REG + "\nActivity book: " + REGA),
  ig=tail("A page that sends the class outside. 🔍\n\nIn the reader the family walk down to the "
    "nature bath, a clear natural pool. The activity book turns it into Nature Pool Observer: sit "
    "beside water, watch, write down what's actually there.\n\nNo reef needed. A rock pool works. So "
    "does a puddle after rain.\n\nThe skill is the one every science lesson from here on will ask "
    "for — look first, record what you saw, not what you expected.\n\n40 pages, ages 6–12.\n\n"
    "Reader: " + REG + "\nActivity book: " + REGA,
    "#GoingToTheRegatta #ActivityBook #TeacherResources #NatureStudy #Bahamas #ClassroomIdeas"),
  pin_t='Nature Pool Observer — a page that sends the class outside',
  pin=tail("The reader walks the family down to the nature bath, a clear natural pool. The activity "
    "book turns it into Nature Pool Observer: sit beside water, watch, record what is actually "
    "there. A rock pool works; so does a puddle. 40 pages, ages 6 to 12.\n\nReader: " + REG +
    "\nActivity book: " + REGA),
  pin_url=REGA),
]

if __name__ == '__main__':
    run(S)
