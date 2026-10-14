# -*- coding: utf-8 -*-
"""Week 47: Mon 12 - Wed 14 Oct 2026. Four slots over three days.
TWO COLLAGE DAYS (Mon 12 and Wed 14 evening), per Bridge's 11 Oct instruction.

Posting is handled by sched/post.py, which knows how to send a carousel to
Facebook and Instagram and the composited collage to Pinterest.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from post import run, STD, IGC, IGP

B_COLOR, B_READ, B_LI = '830421687481393074', '830421687481391572', '830421687481393086'
GW   = 'https://www.amazon.com/dp/B0HCB7V9C9'; GWA  = 'https://www.amazon.com/dp/B0HG8NKYV2'
REG  = 'https://www.amazon.com/dp/B0HGKNTNDD'; REGA = 'https://www.amazon.com/dp/B0HH8PVQZ9'
ATBU = 'https://www.amazon.com/dp/B0HC1PJ4DS'; ATBL = 'https://www.amazon.com/dp/B0HBNFLDQP'
GDSI = 'GDS-Images — https://pictures.gdsbahamas.com/'
tail = lambda t, tags=None: t + "\n\n" + GDSI + (("\n\n" + tags) if tags else "")

S = [
 # Mon 12 Oct — slot 60 — pillar 4 Activity Spotlight — All Things Bahamian: Upper — COLLAGE
 dict(day='2026-10-12', base=14, board=B_COLOR, pad=False,
  panels=['gds/atb-upper/bahamian-flag-20261012c',
          'gds/atb-upper/glass-window-bridge-20261008-v2',
          'gds/atb-upper/junkanoo-detail-20260902',
          'gds/atb-upper/sugar-loaf-pineapple-20261012c'],
  alts=['The flag of The Bahamas snapping in a strong breeze — aquamarine, gold and aquamarine '
        'bands with a black triangle at the hoist — above a beach where waves break white.',
        'The Glass Window Bridge in Eleuthera: a road bridge crossing a narrow gap, with the '
        'rough navy Atlantic breaking against the rock beyond it and the calm clear turquoise '
        'Bight in the foreground on the near side.',
        'A Junkanoo costume in close-up: layered crepe fringing in pink, orange and turquoise, '
        'with a goatskin drum and a cowbell resting beside it.',
        'Sugar Loaf pineapples growing in red-brown Eleuthera earth, one whole and one cut in '
        'half, their spiky leaves bending in the wind.'],
  collage='gds/atb-upper/collage-seven-sections-20261012c',
  alt='A four-panel collage from All Things Bahamian: the national flag snapping in the wind, the '
      'Glass Window Bridge with rough Atlantic on one side and calm Bight on the other, a Junkanoo '
      'costume in close-up, and Sugar Loaf pineapples growing in Eleuthera.',
  fb=tail("Four corners of one book.\n\nAll Things Bahamian is built in seven sections, "
    "and the point of them is range. Swipe through our illustrations of four of them \u2014 in "
    "the book each is a line drawing waiting for colouring pencils. The flag, with its aquamarine, gold and "
    "black. The Glass Window in Eleuthera, where the open Atlantic and the calm Bight sit on "
    "opposite sides of a narrow strip of rock. A Junkanoo costume up close. Sugar Loaf "
    "pineapples in the Eleuthera earth.\n\nNational symbols, our islands, historic places, life "
    "in our seas, Junkanoo, the fruits of The Bahamas, and a closing make-your-own section. A "
    "child who finishes this book has not coloured one thing forty times — they have been "
    "somewhere.\n\nAll Things Bahamian: Upper Elementary. Ages 9 to 12, grades 4 to 6. 109 "
    "pages.\n\n" + ATBU),
  ig=tail("Four corners of one book. 🇧🇸\n\nSwipe our illustrations of four of its subjects — in the book each is a line drawing waiting for pencils. The flag — aquamarine, gold and "
    "black. The Glass Window, where the open Atlantic and the calm Bight meet at one narrow "
    "strip of rock. Junkanoo, close up. Sugar Loaf pineapples in Eleuthera earth.\n\nSeven "
    "sections in all: national symbols, our islands, historic places, life in our seas, "
    "Junkanoo, fruits, and make-your-own.\n\nA child who finishes this book has been "
    "somewhere. ✏️\n\nUpper Elementary: ages 9–12, grades 4–6, 109 pages.\n\n" + ATBU,
    "#AllThingsBahamian #Bahamas #ColouringBook #BahamianKids #Junkanoo #Eleuthera #IslandLife"),
  pin_t='Four corners of one book — All Things Bahamian',
  pin=tail("The flag, the Glass Window Bridge, Junkanoo close up, and Sugar Loaf pineapples — our "
    "illustrations of subjects from four of the seven sections in All Things Bahamian. Upper Elementary: ages 9 to 12, grades 4 to 6, "
    "109 pages.\n\n" + ATBU),
  pin_url=ATBU),

 # Tue 13 Oct — slot 61 — pillar 5 Bahamian Culture — Going To The Regatta — NEW ART
 dict(day='2026-10-13', base=14, pid='gds/regatta/vendor-buildings-salt-pond-20261013c',
  pad=False, board=B_LI,
  alt='A row of small wooden vendor stalls at the Long Island regatta grounds at Salt Pond, '
      'painted pink, turquoise, yellow and lime green, with bunting strung between their roofs '
      'and people walking between them carrying plates and drinks. Racing sloops are under sail '
      'on the choppy water behind.',
  fb=tail("The regatta is not only the boats.\n\nGoing To The Regatta takes the family down to "
    "Salt Pond in Central Long Island, and what is waiting there is a small painted town that "
    "appears for the week: food vendors, craft and merchandise stalls, racing sloops on the "
    "water, private boats carrying spectators out to watch, and Bahamian artists on stage in the "
    "evening.\n\nThat is the part a child remembers. Not the finishing order — the walk between "
    "the stalls with a plate in your hand.\n\nGoing To The Regatta is a true family account. Ages "
    "5 to 15.\n\n" + REG),
  ig=tail("The regatta is not only the boats. 🎪⛵\n\nAt Salt Pond a small painted town appears for "
    "the week: food vendors, craft and merchandise stalls, sloops racing, private boats carrying "
    "spectators out to watch, Bahamian artists on stage in the evening.\n\nThat's the part a "
    "child remembers — the walk between the stalls with a plate in your hand.\n\nA true family "
    "account. Ages 5–15.\n\n" + REG,
    "#GoingToTheRegatta #SaltPond #LongIsland #Bahamas #BahamianCulture #Regatta"),
  pin_t='The stalls at Salt Pond — Going To The Regatta',
  pin=tail("At Salt Pond the regatta brings food vendors, craft and merchandise stalls, racing "
    "sloops and Bahamian artists on stage in the evening. A true Long Island family account. "
    "Ages 5 to 15.\n\n" + REG),
  pin_url=REG),

 # Wed 14 Oct — slot 62 — pillar 6 Classroom & Library — The Girl and The Whale — CATALOGUED
 dict(day='2026-10-14', base=14, pid='gds/girl-whale/anna-meets-the-whale-20260907',
  pad=False, board=B_READ,
  alt='Anna, a girl of about thirteen with chocolate-brown skin and long black hair in a floral '
      'sundress, underwater at a coral reef reaching to touch the nose of an enormous whale whose '
      'body is deep blue-black scattered with cosmic purple starlight, among turtles and fish.',
  fb=tail("Six words worth a whole lesson.\n\nThe Girl and The Whale carries its own Words to "
    "Know list, and it is not a soft one: legend, cosmic, comet, hallucinating, mesmerised, "
    "sacrifice.\n\nThat last pair is why the book works in a classroom. Mr. Hooker tells Anna she "
    "is HALLUCINATING when she says she heard whale song — a real word, used the way an adult "
    "would really use it with a child who insists on something. And the whale of the legend took "
    "a comet strike to save every creature in the sea: SACRIFICE, shown rather than "
    "defined.\n\nRead it aloud, stop at those two, and the discussion writes itself.\n\nThe Girl "
    "and The Whale, by Zhané Mackey. Ages 6 to 12, grades 1 to 6.\n\n" + GW),
  ig=tail("Six words worth a whole lesson. 📖\n\nThe Girl and The Whale brings its own Words to "
    "Know: legend, cosmic, comet, hallucinating, mesmerised, sacrifice.\n\nMr. Hooker tells Anna "
    "she's HALLUCINATING when she says she heard whale song — a real word used the way an adult "
    "really would. And the whale of the legend took a comet strike to save every creature in the "
    "sea: SACRIFICE, shown rather than defined. 🐋\n\nRead it aloud, stop at those two, and the "
    "discussion writes itself.\n\nBy Zhané Mackey. Ages 6–12.\n\n" + GW,
    "#TheGirlAndTheWhale #ReadAloud #TeacherResources #Vocabulary #ChildrensBooks #Bahamas"),
  pin_t='Six words worth a whole lesson — The Girl and The Whale',
  pin=tail("The Girl and The Whale carries its own Words to Know: legend, cosmic, comet, "
    "hallucinating, mesmerised, sacrifice. Read it aloud and stop at the last two. By Zhané "
    "Mackey. Ages 6 to 12.\n\n" + GW),
  pin_url=GW),

 # Wed 14 Oct — slot 63 — pillar 0 Book World — Regatta Coloring & Activity Book — COLLAGE
 dict(day='2026-10-14', base=19, board=B_COLOR, pad=False,
  panels=['gds/regatta-activity/regatta-i-spy-20261014',
          'gds/regatta-activity/deans-blue-hole-20261014',
          'gds/regatta-activity/pink-sand-at-deals-beach-20261004',
          'gds/regatta-activity/design-a-regatta-flag-20261014d'],
  alts=['Looking down into clear shallow turquoise water over rippled sand: shells, orange '
        'starfish and small striped fish mid-dart, with the hulls of three small sloops on the '
        'moving surface above.',
        'Dean’s Blue Hole on Long Island, a deep dark circle of water ringed by pale turquoise '
        'shallows and white sand, with surf breaking hard against the headland beyond it and the '
        'casuarinas bent in the wind.',
        'The pink sand at Deals Beach, Long Island, with a turquoise wave curling over and breaking '
        'into thick white foam along the shore and the trees above bending in the wind.',
        'A wooden table at the regatta set up for designing flags — blank pennants, coloured '
        'pencils, scissors and string, with bunting snapping between two poles behind.'],
  collage='gds/regatta-activity/collage-activity-world-20261014d',
  alt='A four-panel collage from the Going To The Regatta Coloring & Activity Book: a seek-and-find '
      'view down into clear shallow water, Dean’s Blue Hole, the pink sand at Deals Beach, and a '
      'table set up for designing regatta flags with bunting snapping behind it.',
  fb=tail("Forty pages, and almost none of them are just colouring.\n\nSwipe through the world of "
    "the Going To The Regatta Coloring & Activity Book. Regatta I-Spy \u2014 the page in the book "
    "asks a child to find six shells, five stars, four fish and three small sloops. Dean's Blue Hole — the second "
    "deepest in the world — which the family never reached, so the book hands the trip to the "
    "reader instead. The pink sand at Deals Beach. And Design a Regatta Flag, which is exactly "
    "what it sounds like.\n\nThere is also Parts of a C1 Racing Sloop, a Long Island word search, "
    "Crack the Regatta Code, Family Roots and Roles, and Plan an Island Meal.\n\nGoing To The "
    "Regatta Coloring & Activity Book. 40 pages, ages 6 to 12.\n\nReader: " + REG +
    "\nActivity book: " + REGA),
  ig=tail("Forty pages, and almost none of them are just colouring. 🎨\n\nSwipe: Regatta I-Spy — the page in the book asks for "
    "six shells, five stars, four fish, three small sloops. Dean's Blue Hole, the second deepest "
    "in the world, which the family never reached, so the book hands the trip to you. The pink "
    "sand at Deals Beach. Design a Regatta Flag.\n\nPlus Parts of a C1 Racing Sloop, a Long "
    "Island word search, Crack the Regatta Code, Family Roots and Roles, Plan an Island "
    "Meal.\n\n40 pages, ages 6–12.\n\nReader: " + REG + "\nActivity book: " + REGA,
    "#GoingToTheRegatta #ActivityBook #KidsActivities #LongIsland #Bahamas #ColouringBook"),
  pin_t='Forty pages, almost none of them just colouring',
  pin=tail("Regatta I-Spy, Dean's Blue Hole — the second deepest in the world — the pink sand at "
    "Deals Beach, and Design a Regatta Flag. The Going To The Regatta Coloring & Activity Book. "
    "40 pages, ages 6 to 12.\n\nReader: " + REG + "\nActivity book: " + REGA),
  pin_url=REGA),
]

if __name__ == '__main__':
    run(S)
