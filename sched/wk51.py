# -*- coding: utf-8 -*-
"""Week 51: Mon 26 - Wed 28 Oct 2026. Four slots over three days.
TWO COLLAGE DAYS: Mon 26 (Promo/CTA) and Tue 27 (Activity Spotlight).

A Promo/CTA is the one pillar whose whole job is "here is what you get", and a
reader about five days on an island cannot be sold on one picture. Activity
Spotlight is the standing case: the claim is that a colouring book is more than
colouring, which takes more than one page to show. Wednesday's two slots stay
single heroes - Bahamian Culture wants one subject looked at properly, and
Classroom & Library wants one thing a teacher can hold up.
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
 # Mon 26 Oct — slot 80 — pillar 3 Promo/CTA — Going To The Regatta — COLLAGE
 dict(day='2026-10-26', base=14, board=B_LI, pad=False,
  panels=['gds/regatta/sloops-at-salt-pond-20260830',
          'gds/regatta/flags-over-the-regatta-20260927',
          'gds/regatta/final-regatta-night-20261026',
          'gds/regatta/green-leaf-coconut-20261026'],
  alts=["Three Bahamian sloops under full sail racing past a line of festival tents.", "Rows of plain coloured bunting strung above a grassy waterfront at a Bahamian regatta. Three wooden sloops with tall masts and white sails race on turquoise water beyond. Coral-pink and yellow vendor stalls stacked with pineapples, coconuts and papaya, a crowd in straw hats watching from the grass.",
        'The last night of a Bahamian regatta at Salt Pond: a lit stage with a band playing, people '
        'of all ages dancing on the grass in front of it, families watching from folding chairs, '
        'strings of lights between poles and food and craft stalls glowing at the side, with the '
        'dark harbour and moored boats beyond.',
        'A table outside a small Bahamian restaurant at lunchtime: a bowl of soup with a spoon on a '
        'folded napkin, a plate of bread, and a fresh green coconut opened at the top with a straw '
        'in it, beads of water on its skin, with more coconuts in a basket, painted shutters and '
        'bougainvillea behind.'],
  collage='gds/regatta/collage-five-days-20261026',
  alt='A four-panel collage from Going To The Regatta: three sloops racing past the festival tents, '
      'bunting and sails over the regatta grounds, the last night with a band and '
      'dancing, and a lunch table with a freshly opened coconut.',
  fb=tail("Five days, and the racing is only part of it.\n\nGoing To The Regatta is a true family "
    "account of a trip to Long Island, written by Bridgette Skeete-Mackey and illustrated with real "
    "family photographs.\n\nThey land at Stella Maris on the Thursday and drive down to Salt Pond — "
    "food vendors, craft stalls, racing sloops, private boats carrying spectators, and Bahamian "
    "artists on stage in the evening.\n\nFriday is soup at Green Leaf and a freshly opened "
    "coconut.\n\nSaturday brings chicken souse with pepper, lime and allspice, and johnny cake, "
    "crisp outside and soft inside and spread with butter. The pan is empty before breakfast "
    "ends.\n\nThen the final regatta night: results and prizes, music and dancing.\n\nA regatta is "
    "more than a race. It is a homecoming where history, family and island life meet.\n\nThese are "
    "our illustrations; the book itself carries the photographs.\n\nGDS Reading Series, Family "
    "Reader, ages 5 to 15.\n\nReader: " + REG + "\nActivity book: " + REGA),
  ig=tail("Five days, and the racing is only part of it. 🇧🇸\n\nThey land at Stella Maris on the "
    "Thursday and drive down to Salt Pond — food vendors, craft stalls, racing sloops, and "
    "Bahamian artists on stage in the evening.\n\nFriday is soup at Green Leaf and a freshly opened "
    "coconut.\n\nSaturday brings chicken souse with pepper, lime and allspice, and johnny cake — "
    "crisp outside, soft inside, spread with butter. The pan is empty before breakfast "
    "ends.\n\nThen the final regatta night: results and prizes, music and dancing.\n\n\"A regatta "
    "is more than a race. It is a homecoming where history, family, and island life meet.\"\n\n"
    "Swipe for all four. Our illustrations — the book carries the photographs.\n\nFamily Reader, "
    "ages 5–15.\n\nReader: " + REG + "\nActivity book: " + REGA,
    "#GoingToTheRegatta #LongIsland #Bahamas #BahamianFood #FamilyStories #BahamianAuthors "
    "#GDSPublications"),
  pin_t='Five days on Long Island — Going To The Regatta',
  pin=tail("Sloops racing past the festival tents, chicken souse and johnny cake, the last night of "
    "the regatta, and lunch with a freshly opened coconut. A true family account of five days on "
    "Long Island by Bridgette Skeete-Mackey. Our illustrations; the book carries the family "
    "photographs. Family Reader, ages 5 to 15.\n\nReader: " + REG + "\nActivity book: " + REGA),
  pin_url=REG),

 # Tue 27 Oct — slot 81 — pillar 4 Activity Spotlight — ATB Lower — COLLAGE
 dict(day='2026-10-27', base=14, board=B_COLOR, pad=False,
  panels=['gds/atb-lower/colouring-tips-desk-20261015',
          'gds/atb-lower/junkanoo-costume-design-20261027',
          'gds/atb-lower/classroom-display-wall-20261023',
          'gds/atb-lower/proud-to-be-bahamian-20261027'],
  alts=["A worktable seen from above with practice patches of pencil shading — light, medium, pressed dark and a blend — beside a line drawing of a flamingo half coloured in. A jar of coloured pencils, loose pencils, a sharpener with shavings and an eraser around them, and a leafy plant stirring by the window.",
        'A table where a Junkanoo costume is being designed and built, seen from above: sheets of '
        'cream paper with hand-drawn costume designs coloured in bright crepe-paper colours, a '
        'part-built cardboard headdress base with strips of pink, orange and turquoise crepe paper '
        'being pasted on, a pot of paste with a brush, scissors, string and loose fringing.',
        "A primary classroom noticeboard with about twelve sheets of cream paper pinned up, each a child's coloured-in drawing of a Bahamian subject — a conch, a flamingo, a sailing boat, a pineapple, a lighthouse, a Junkanoo headdress, a fish, a palm — all in bright uneven crayon and pencil. Below the board a low shelf holds a jar of crayons, a stack of paper and a small potted plant.",
        'Nine Bahamian children of mixed ages standing together on a beach, all waving and smiling, '
        'two of them holding Bahamian flags lifting in the breeze. Palms lean behind them and clear '
        'turquoise sea beyond, where a low swell rolls in and small waves run up the pale sand in a '
        'thin lace of foam.'],
  collage='gds/atb-lower/collage-more-than-colouring-20261027',
  alt='A four-panel collage from All Things Bahamian, Lower Elementary: a desk working out colouring '
      'technique, a table where a Junkanoo costume is being designed and built, a classroom wall of '
      'finished work pinned up, and nine children waving on a beach with Bahamian flags.',
  fb=tail("It opens with a page on colouring itself and ends with nine children on a beach.\n\nThe "
    "Lower edition of All Things Bahamian adds two things the Upper edition does not: a Colouring "
    "Tips page, and simpler design activities — including Design Your Own Junkanoo "
    "Costume, which comes with the tip that Junkanoo artists build costumes from cardboard, paste "
    "and colourful crepe paper.\n\nSo it is not only colouring. It is technique, then design, then "
    "a wall of work no two children did the same way, and then the closing page: Proud to be "
    "Bahamian.\n\nSeven sections in between — National Symbols, Our Beautiful Islands, Historic "
    "Places and Landmarks, Life in Our Bahamian Seas, Junkanoo, Fruits of The Bahamas, My "
    "Bahamas.\n\nThese are our illustrations of those subjects; in the book each is a line drawing "
    "waiting for pencils.\n\nAll Things Bahamian, Lower Elementary. Ages 5 to 9, grades 1 to 3. 83 "
    "pages.\n\n" + ATBL),
  ig=tail("It opens with a page on colouring itself and ends with nine children on a beach. 🖍️\n\nThe "
    "Lower edition adds two things the Upper one doesn't: a Colouring Tips page, and simpler "
    "design activities — including Design Your Own Junkanoo Costume, with the tip that "
    "Junkanoo artists build costumes from cardboard, paste and colourful crepe paper.\n\nSo it's "
    "not only colouring. Technique, then design, then a wall of work no two children did the same "
    "way, then the closing page: Proud to be Bahamian.\n\nSeven sections in between.\n\nSwipe for "
    "all four — our illustrations of those subjects. In the book each is a line drawing waiting for "
    "pencils.\n\nAges 5–9, grades 1–3, 83 pages.\n\n" + ATBL,
    "#AllThingsBahamian #ColouringBook #BahamianKids #Junkanoo #Bahamas #KidsActivities "
    "#GDSPublications"),
  pin_t='Not only colouring — All Things Bahamian, Lower',
  pin=tail("A Colouring Tips page, Design Your Own Junkanoo Costume among the design "
    "activities, a wall of finished work where no two children did it the same way, and the closing "
    "Proud to be Bahamian page. Our illustrations of those subjects; in the book each is a line "
    "drawing waiting for pencils. Ages 5 to 9, grades 1 to 3, 83 pages.\n\n" + ATBL),
  pin_url=ATBL),

 # Wed 28 Oct — slot 82 — pillar 5 Bahamian Culture — ATB Upper — NEW ART
 dict(day='2026-10-28', base=14, pid='gds/atb-upper/old-stone-fort-20261028',
  pad=False, board=B_CULT,
  alt='An old colonial stone fort on a rise above a Bahamian harbour: thick pale limestone walls '
      'with a rounded bastion, narrow slit windows, worn steps climbing to the top and two old iron '
      'cannons on wooden carriages pointing out over the water. Ferns and bougainvillea grow from '
      'gaps in the stonework. Below, clear turquoise water where a low swell rolls in and light '
      'shifts in slow bands over the sand.',
  fb=tail("Forts, monuments and lighthouses — the third section.\n\nHistoric Places and Landmarks "
    "runs from page 50 to 59 in the Upper edition. It is the section about the things that have "
    "stood on these islands long enough that everyone navigates by them.\n\nA fort is a good one to "
    "give a child, because it carries its own question. Who built it, who were they expecting, and "
    "what were they watching for out there?\n\nThe same section holds the Queen's Staircase in "
    "Nassau, also called the 66 Steps.\n\nThe Upper edition adds EXPLORE MORE pages of written "
    "questions to work through, and Key Settlements and Communities — five named communities per "
    "island with a line of description each.\n\nThis is our illustration of the subject; in the "
    "book it is a line drawing waiting for pencils.\n\nAll Things Bahamian: Upper Elementary. Ages "
    "9 to 12, grades 4 to 6. 109 pages.\n\n" + ATBU),
  ig=tail("Forts, monuments and lighthouses — the third section. 🏰\n\nHistoric Places and Landmarks "
    "is the section about things that have stood here long enough that everyone navigates by "
    "them.\n\nA fort is a good one to give a child, because it carries its own question. Who built "
    "it, who were they expecting, and what were they watching for out there?\n\nThe same section "
    "holds the Queen's Staircase in Nassau — also called the 66 Steps.\n\nThe Upper edition adds "
    "EXPLORE MORE written questions and Key Settlements and Communities, five named communities per "
    "island.\n\nOur illustration of the subject — in the book it's a line drawing waiting for "
    "pencils.\n\nAges 9–12, grades 4–6, 109 pages.\n\n" + ATBU,
    "#AllThingsBahamian #BahamianHistory #Bahamas #ColouringBook #HomeschoolBahamas "
    "#GDSPublications #HistoricPlaces"),
  pin_t='Forts, monuments and lighthouses — the third section',
  pin=tail("Historic Places and Landmarks runs from page 50 to 59 in the Upper edition — the things "
    "that have stood on these islands long enough that everyone navigates by them, the Queen's "
    "Staircase among them. Our illustration of the subject; in the book it is a line drawing "
    "waiting for pencils. Ages 9 to 12, grades 4 to 6, 109 pages.\n\n" + ATBU),
  pin_url=ATBU),

 # Wed 28 Oct — slot 83 — pillar 6 Classroom & Library — The Girl and The Whale — NEW ART
 dict(day='2026-10-28', base=19, pid='gds/girl-whale/people-of-hawaii-looking-up-20261028-v2',
  pad=False, board=B_READ,
  alt="A Pacific-island village at night as everyone comes outside to look up: villagers of all ages in the lane between lit houses, heads tipped back, faces lit from above by a cosmic purple glow. Low overhead an enormous humpback whale passes, her long fins glowing purple and scattered with starlight, with Anna — a girl with chocolate-brown skin and long black hair in a floral sundress — standing on one fin, arms wide. The sea beyond moves gently under the glow.",
  fb=tail("The page to stop on when you read it aloud.\n\nNear the end of The Girl and The Whale, "
    "the Cosmic Theseus Finback lifts Anna onto a glowing fin and carries her above the mountains, "
    "beaches, houses and sea — and the people of Hawaii look up and see her.\n\nIt is one moment in "
    "the book. It is also the moment a class goes quiet, because it moves the camera. For the whole "
    "story so far nobody has believed Anna. Here, everybody sees it.\n\nSo stop there "
    "and ask: what would you do if you looked up and saw that? Who would you tell? Would they "
    "believe you?\n\nThe activity book carries the discussion further — Anna's Feelings, Legend and "
    "Reality sorting, Create Your Own Island Legend, and Draw the Family Under the Stars.\n\nOur "
    "illustration of that moment, not a page from the book.\n\nThe Girl and The Whale by Zhané "
    "Mackey. GDS Reading Series, Level 3. Ages 6 to 12, grades 1 to 6.\n\nReader: " + GW +
    "\nActivity book: " + GWA),
  ig=tail("The page to stop on when you read it aloud. 💜\n\nNear the end, the Cosmic Theseus "
    "Finback lifts Anna onto a glowing fin and carries her above the mountains, beaches, houses and "
    "sea — and the people of Hawaii look up and see her.\n\nIt's one moment in the book. It's also "
    "the moment a class goes quiet, because it moves the camera. For the whole story so far nobody "
    "has believed Anna. Here, everybody sees it.\n\nStop there and ask: what would you "
    "do if you looked up and saw that? Who would you tell? Would they believe you?\n\nThe activity "
    "book carries it further — Anna's Feelings, Legend and Reality sorting, Create Your Own Island "
    "Legend.\n\nOur illustration of that moment, not a page from the book.\n\nBy Zhané Mackey. Ages "
    "6–12.\n\nReader: " + GW + "\nActivity book: " + GWA,
    "#TheGirlAndTheWhale #ReadAloud #TeacherResources #ClassroomIdeas #ChildrensBooks "
    "#BahamianAuthors #GDSPublications"),
  pin_t='The page to stop on when you read it aloud',
  pin=tail("The Cosmic Theseus Finback carries Anna above the mountains, beaches, houses and sea, "
    "and the people of Hawaii look up and see her. One moment in the book, and the moment a class "
    "goes quiet — for the whole story so far nobody has believed her. Our illustration of that "
    "moment, not a page from the book. Ages 6 to 12.\n\nReader: " + GW + "\nActivity book: " + GWA),
  pin_url=GW),
]

if __name__ == '__main__':
    run(S)
