# -*- coding: utf-8 -*-
"""Week 56: Thu 12 - Sun 15 Nov 2026. Six slots over four days.
TWO COLLAGE DAYS: Fri 13 (Book World) and Sun 15 (Activity Spotlight).

Book World takes one because the subject is the SHAPE OF THE TRIP - five days
with a beginning and an end - and a sequence needs more than one frame. Activity
Spotlight takes the other because the subject is one boat seen four ways, which
is a comparison, and a comparison needs them side by side. The other four slots
each make a single point, so they keep a single hero.

All six books appear exactly once. ATB Lower and the Regatta activity book were
both due after last week.
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
 # Thu 12 Nov — slot 104 — pillar 6 Classroom & Library — ATB Lower — HERO (catalogued)
 dict(day='2026-11-12', base=14, pid='gds/atb-lower/colouring-tips-desk-20261015',
  pad=False, board=B_COLOR, anna_absent=True,
  alt='A worktable seen from above with practice patches of pencil shading — light, medium, '
      'pressed dark and a blend — beside a line drawing of a flamingo half coloured in. A jar of '
      'coloured pencils, loose pencils, a sharpener with shavings and an eraser around them, and '
      'a leafy plant stirring by the window.',
  fb=tail("Teaching a child to colour is teaching a child to press harder.\n\nAll Things Bahamian, "
    "Lower Elementary carries a Colouring Tips page — one of the things the Lower edition adds "
    "over the Upper, along with simpler design activities such as Design Your Own Junkanoo "
    "Costume.\n\nAnd shading is a real thing to teach. It is one of the first places a "
    "young child meets the idea that how you do something changes what you get: the same "
    "pencil and the same colour give you something different depending on how hard you lean "
    "and whether you go back over it.\n\nThat is worth a classroom ten minutes before anyone opens to a full "
    "page.\n\nThe artwork is shared with the Upper edition — same drawings, different page "
    "numbers. What the Lower edition changes is the written work around them, and who it is "
    "pitched at.\n\nAbove is our illustration of a practice sheet, not a page from the "
    "book.\n\nAll Things Bahamian, Lower Elementary. Ages 5 to 9, grades 1 to 3. 83 "
    "pages.\n\n" + ATBL),
  ig=tail("Teaching a child to colour is teaching a child to press harder. ✏️\n\nAll Things "
    "Bahamian, Lower Elementary carries a Colouring Tips page — one of the things the Lower "
    "edition adds over the Upper, along with simpler design activities like Design Your Own "
    "Junkanoo Costume.\n\nAnd shading is a real thing to teach. It's one of the first places "
    "a young child meets the idea that HOW you do something changes what you get: same pencil, "
    "same colour, something different depending on how hard you lean.\n\nWorth ten minutes "
    "before anyone opens to a full page.\n\nThe artwork is shared with the Upper edition — same "
    "drawings, different page numbers. What changes is the written work around them.\n\nOur "
    "illustration of a practice sheet, not a page from the book.\n\nAges 5–9, grades 1–3, 83 "
    "pages.\n\n" + ATBL,
    "#AllThingsBahamian #ColouringBook #TeacherResources #ClassroomIdeas #Bahamas "
    "#HomeschoolBahamas #GDSPublications"),
  pin_t='Colouring is learning to press harder',
  pin=tail("All Things Bahamian, Lower Elementary carries a Colouring Tips page — one of the "
    "things the Lower edition adds over the Upper. Shading is where a young child meets the idea "
    "that how you do something changes what you get. Our illustration of a practice sheet, not a "
    "page from the book. Ages 5 to 9, 83 pages.\n\n" + ATBL),
  pin_url=ATBL),

 # Fri 13 Nov — slot 105 — pillar 0 Book World — Going To The Regatta — COLLAGE
 dict(day='2026-11-13', base=14, board=B_LI, pad=False,
  panels=['gds/regatta/the-drive-south-20261113',
          'gds/regatta/the-hoop-la-table-20261113',
          'gds/regatta/final-regatta-night-20261026',
          'gds/regatta/stella-maris-airport-20261030'],
  alts=['A long afternoon drive down a narrow two-lane Long Island road, seen from the verge as a '
        'single car passes. Low scrub, leaning casuarinas and sea grape line the road, telephone '
        'poles run along it and a few pastel houses sit back from the tarmac. Clear turquoise '
        'water shows between the trees, moving gently with a low swell and a thin line of foam '
        'along the shore.',
        'A hoop-la stall at a Bahamian regatta with nobody standing at it: a wooden trestle table '
        'under a striped awning, its top marked out in painted squares with small prizes on them '
        '— a tin whistle, a little carved boat, a bag of sweets, a green bangle and a conch shell '
        '— and a stack of wooden hoops at the near edge. Bunting above, other stalls on the grass '
        'behind, and the sea beyond.',
        'The last night of a Bahamian regatta at Salt Pond: a lit stage with a band playing, '
        'people of all ages dancing on the grass in front of it, families watching from folding '
        'chairs, strings of lights between poles and food and craft stalls glowing at the side, '
        'with the dark harbour and moored boats beyond.',
        'A tiny Bahamian island airstrip on the morning a family flies home: a small '
        'single-storey terminal with a shaded porch and louvred windows, a low fence, and a small '
        'twin-propeller plane waiting on the apron. Travellers with bags and a cooler stand in '
        'the shade saying goodbye, two women hugging, a boy with a backpack almost as big as he '
        'is. Turquoise sea past the end of the runway, a low swell rolling in.'],
  collage='gds/regatta/collage-four-of-the-five-days-20261113',
  alt='Four moments from a Long Island trip: a single car on a narrow road running south between '
      'scrub and sea grape, a hoop-la stall with nobody at it, a lit stage and dancing on the '
      'grass at the last night of the regatta, and a tiny island airstrip with a twin-propeller '
      'plane waiting.',
  fb=tail("The trip is five days long, and the book keeps all five.\n\nThursday the family lands "
    "at Stella Maris in North Long Island, and then there is the long drive south to Salt Pond "
    "in Central Long Island — food vendors, craft and merchandise stalls, racing sloops, private "
    "boats carrying spectators, Bahamian artists on stage in the evening.\n\nFriday a cousin runs "
    "a hoop-la table at the regatta. Nicholas wins nothing. That detail is in the book, and it is "
    "the kind of thing a made-up story leaves out.\n\nSaturday is the final regatta night: "
    "results and prizes, music and dancing.\n\nMonday they fly home from Stella Maris airport — "
    "the only one operating, because Deadman's Cay airport was being renovated.\n\nFour of the "
    "five days are above. Sunday is the one missing: worship at Beulah Baptist Church in "
    "Simms.\n\nThese are our illustrations. The book itself carries the family's "
    "photographs.\n\nGDS Reading Series, Family Reader. Ages 5 to 15.\n\nReader: " + REG
    + "\nActivity book: " + REGA),
  ig=tail("The trip is five days long, and the book keeps all five. 🛬\n\nThursday: land at Stella "
    "Maris in North Long Island, then the long drive south to Salt Pond — food vendors, craft "
    "stalls, racing sloops, Bahamian artists on stage in the evening.\n\nFriday: a cousin runs a "
    "hoop-la table at the regatta. Nicholas wins nothing. That's in the book, and it's the kind "
    "of thing a made-up story leaves out.\n\nSaturday: the final regatta night — results and "
    "prizes, music and dancing.\n\nMonday: home from Stella Maris airport, the only one "
    "operating, because Deadman's Cay airport was being renovated.\n\nSwipe for four of the five "
    "days. Sunday is the one missing — worship at Beulah Baptist Church in Simms.\n\nOur "
    "illustrations. The book itself carries the family's photographs.\n\nAges 5–15.\n\nReader: "
    + REG + "\nActivity book: " + REGA,
    "#GoingToTheRegatta #LongIsland #Bahamas #FamilyStories #BahamianAuthors #Regatta "
    "#GDSPublications"),
  pin_t='Five days, and the book keeps all five',
  pin=tail("Thursday lands at Stella Maris, then the long drive south to Salt Pond. Friday a "
    "cousin runs a hoop-la table and Nicholas wins nothing. Saturday is the final regatta night. "
    "Monday they fly home from Stella Maris airport, the only one operating. Our illustrations of "
    "four of the five days; the book carries the family's photographs.\n\n" + REG),
  pin_url=REG),

 # Fri 13 Nov — slot 106 — pillar 1 Behind the Scenes — ATB Upper — HERO (catalogued)
 dict(day='2026-11-13', base=19, pid='gds/atb-upper/worktable-sketches-20260830',
  pad=False, board=B_COLOR, anna_absent=True,
  alt='A work table of Bahamian pencil sketches, a Junkanoo headdress, a conch shell and a model '
      'sloop.',
  fb=tail("Everything on this table is a decision waiting to be made.\n\nAll Things Bahamian has "
    "seven sections, and each one opens with four thumbnails of its own artwork and an ABOUT THIS "
    "SECTION box — so before a child colours anything, they are shown what the next stretch of "
    "pages is about.\n\nWhich four? That is a real question, and not an obvious one. "
    "Life in Our Bahamian Seas runs pages 60 to 75 in the Upper edition and covers reefs, conch, "
    "turtles, sharks and fish. Four of those have to stand for all of it.\n\nThe Upper edition "
    "also carries Key Settlements and Communities — five named communities per island, a line of "
    "description each — which is a different kind of choosing altogether, and a harder one.\n\n"
    "Above is our illustration of a worktable, not a page from the book.\n\nAll Things Bahamian: "
    "Upper Elementary. Ages 9 to 12, grades 4 to 6. 109 pages.\n\n" + ATBU),
  ig=tail("Everything on this table is a decision waiting to be made. 🐚\n\nAll Things Bahamian "
    "has seven sections, and each opens with four thumbnails of its own artwork and an ABOUT THIS "
    "SECTION box — so before a child colours anything, they're shown what's coming.\n\nWhich four "
    "thumbnails? That's the question. Life in Our Bahamian Seas runs pages 60–75 in the Upper "
    "edition and covers reefs, conch, turtles, sharks and fish. Four of those have to stand for "
    "all of it.\n\nThe Upper edition also carries Key Settlements and Communities — five named "
    "communities per island, a line each — which is a harder kind of choosing "
    "altogether.\n\nOur illustration of a worktable, not a page from the book.\n\nAges 9–12, "
    "grades 4–6, 109 pages.\n\n" + ATBU,
    "#AllThingsBahamian #BehindTheScenes #Bahamas #ColouringBook #BookDesign #BahamianCulture "
    "#GDSPublications"),
  pin_t='Everything here is a decision waiting',
  pin=tail("Each of the seven sections in All Things Bahamian opens with four thumbnails of its "
    "own artwork and an ABOUT THIS SECTION box. Life in Our Bahamian Seas runs pages 60 to 75 in "
    "the Upper edition and covers reefs, conch, turtles, sharks and fish — four of those have to "
    "stand for all of it. Our illustration of a worktable, not a page from the book.\n\n" + ATBU),
  pin_url=ATBU),

 # Sat 14 Nov — slot 107 — pillar 2 Reader Engagement — Girl & Whale Activity Book — HERO
 dict(day='2026-11-14', base=14, pid='gds/girl-whale-activity/cosmic-bookmarks-20261017',
  pad=False, board=B_COLOR, anna_absent=True,
  alt='Four finished paper bookmarks laid out on a pale wooden desk, decorated by hand with a '
      'whale tail, a starry night sky, a pattern of small waves and a ribbon of starlight, with '
      'scissors, a ball of twine and a jar of coloured pencils beside them.',
  fb=tail("A bookmark is the only craft that proves a child went back to the book.\n\nCosmic "
    "Bookmarks is one of the activities in The Girl and The Whale Coloring & Activity Book. You "
    "make it, and then it has a job — which is more than most things a child cuts out ever "
    "get.\n\nSo here is our question, and we are genuinely curious about the "
    "answer:\n\nWhat does your child actually use as a bookmark?\n\nOur money is on a receipt, a "
    "folded corner, or whatever was within reach.\n\nTell us. We read every reply, and the honest answers are the best "
    "ones.\n\n40 pages, ages 6 to 12, grades 1 to 6.\n\nReader: " + GW + "\nActivity book: "
    + GWA),
  ig=tail("A bookmark is the only craft that proves a child went back to the book. 🔖\n\nCosmic "
    "Bookmarks is one of the activities in The Girl and The Whale Coloring & Activity Book. You "
    "make it, and then it has a job — which is more than most things a child cuts out ever "
    "get.\n\nSo, genuinely curious:\n\nWhat does your child actually use as a bookmark?\n\nOur "
    "money is on a receipt, a folded corner, or whatever was within reach.\n\nTell us 👇 the "
    "honest answers are the best ones.\n\n40 pages, ages 6–12.\n\nReader: " + GW
    + "\nActivity book: " + GWA,
    "#TheGirlAndTheWhale #ActivityBook #KidsCrafts #Bookmarks #ReadingWithKids #ChildrensBooks "
    "#GDSPublications"),
  pin_t='What does your child use as a bookmark?',
  pin=tail("Cosmic Bookmarks is one of the activities in The Girl and The Whale Coloring & "
    "Activity Book — a craft that ends up with a job, which is more than most things a child "
    "cuts out ever get. Our illustration of four finished bookmarks, not a page from the book. "
    "40 pages, ages 6 to 12.\n\n" + GWA),
  pin_url=GWA),

 # Sun 15 Nov — slot 108 — pillar 3 Promo/CTA — The Girl and The Whale — HERO (new)
 dict(day='2026-11-15', base=14, pid='gds/girl-whale/the-dance-at-sunset-20261115',
  pad=False, board=B_READ,
  alt='A Hawaiian reef flat at sunset with the sky glowing coral and gold and a long road of '
      'light over the water. Anna dances in the middle distance, mid-turn with both arms lifted '
      'and one bare foot off the ground, her dress and hair swinging out — deep chocolate-brown '
      'skin, long black hair past her shoulders, a hibiscus sundress and a cowrie necklace. The '
      'sea rolls in low with a lace of foam and the gold light shifts on the surface.',
  fb=tail("Before anything happens, she dances.\n\nIt is the hinge of The Girl and The Whale and "
    "it is easy to read past. Anna has heard a sound nobody believes. She has been told a legend "
    "by Mr. Hooker, one of the greatest fishermen in Hawaii. And then, at the reef, as the sun "
    "goes down — the sky, in the book's words, glowed coral and gold — she dances.\n\nAnd it is "
    "the dance the story turns on: what comes next in the book is the purple glow.\n\nThat is a good shape for a "
    "children's story: the quiet choice first, the enormous consequence after.\n\nThe Girl and "
    "The Whale was written by Zhané Mackey and is published from Nassau by GDS "
    "Publications.\n\nThis is our illustration of that moment, not a page from the book.\n\nGDS "
    "Reading Series, Level 3. Ages 6 to 12, grades 1 to 6.\n\n" + GW),
  ig=tail("Before anything happens, she dances. 🌅\n\nIt's the hinge of The Girl and The Whale and "
    "it's easy to read past. Anna has heard a sound nobody believes. She's been told a legend by "
    "Mr. Hooker, one of the greatest fishermen in Hawaii. And then, at the reef, as the sun goes "
    "down — the sky, in the book's words, glowed coral and gold — she dances.\n\nAnd it's the "
    "dance the story turns on: what comes next in the book is the purple glow.\n\nA good shape for a children's story: the quiet choice "
    "first, the enormous consequence after.\n\nWritten by Zhané Mackey, published from Nassau by "
    "GDS Publications. Our illustration of that moment, not a page from the book.\n\nAges 6–12, "
    "grades 1–6.\n\n" + GW,
    "#TheGirlAndTheWhale #ChildrensBooks #BahamianAuthors #ReadingSeries #IslandStory #Sunset "
    "#GDSPublications"),
  pin_t='Before anything happens, she dances',
  pin=tail("Anna has heard a sound nobody believes and been told a legend by Mr. Hooker. Then, at "
    "the reef as the sun goes down, she dances — and it is the dance the story turns on, because "
    "what comes next in the book is the purple glow. Written by Zhané Mackey, published from Nassau by GDS "
    "Publications. Our illustration, not a page from the book.\n\n" + GW),
  pin_url=GW),

 # Sun 15 Nov — slot 109 — pillar 4 Activity Spotlight — Regatta Activity Book — COLLAGE
 dict(day='2026-11-15', base=19, board=B_LI, pad=False,
  panels=['gds/regatta-activity/parts-of-a-c1-sloop-20261115',
          'gds/regatta-activity/decorate-the-c1-mainsail-20261022',
          'gds/regatta-activity/the-c1-sloop-race-20261115',
          'gds/regatta-activity/regatta-i-spy-20261014-v2'],
  alts=['A single Bahamian C1 racing sloop at rest in clear shallow turquoise water, side on and '
        'close so the whole boat shows from bow to the end of the boom: one mast set well '
        'forward, one large triangular mainsail and no jib, a long boom running past the stern, a '
        'shallow open wooden hull and a pry board out over the side. The water is calm but '
        'moving, with ripple lines and light shifting over the sand.',
        'A Bahamian C1 racing sloop sailing on clear turquoise water, its single enormous '
        'triangular mainsail decorated with bold hand-drawn stripes, zigzags, stars and shells in '
        'aquamarine, gold and coral, two crew sitting out on the pry board, a low swell rolling '
        'under the hull and light shifting in bands through the shallows.',
        'Three Bahamian C1 racing sloops racing across clear turquoise water on a bright regatta '
        'day, seen from the side and slightly below so the sails tower. Each carries one mast and '
        'one large triangular mainsail with no jib, and the boats are heeled over with crew '
        'sitting out on the pry boards as counterweight. A low green shore behind, a soft white '
        'wake spreading from each hull and a low swell rolling through.',
        'Looking down into clear shallow turquoise water over rippled sand: six shells, three '
        'fluted scallops and three pink-mouthed conch, five orange starfish and four small '
        'striped fish mid-dart, with three Bahamian C1 racing sloops on the calm surface beyond — '
        'each with one mast, one large triangular mainsail and no jib. A low swell rolls in and '
        'light flickers in bands across the sand.'],
  collage='gds/regatta-activity/collage-one-boat-four-pages-20261115',
  alt='Four views of a Bahamian C1 racing sloop: one at rest with the whole boat showing, one '
      'with its mainsail decorated in stripes, stars and shells, three racing with crew sitting '
      'out on the pry boards, and three more seen from below the surface beyond a sandy sea floor '
      'of shells and starfish.',
  fb=tail("One boat, four pages.\n\nThe Going To The Regatta Coloring & Activity Book keeps coming "
    "back to the same vessel, and it is worth knowing why: the C1 is a class with rules, and the "
    "rig is fixed.\n\nOne mast, set well forward. One enormous triangular mainsail and no jib — "
    "nothing at all forward of the mast. A long boom running well past the stern. A shallow open "
    "wooden hull. And a pry board sticking out over the windward side for the crew to sit on, "
    "which is how a boat that size carries that much sail without going over.\n\nFour pages that "
    "use it: Parts of a C1 Racing Sloop. Decorate the C1 Mainsail. The C1 Sloop Race. And Regatta "
    "I-Spy, which asks for 6 shells, 5 stars, 4 fish and 3 small sloops.\n\nOnce you know the "
    "rig, you cannot unsee it — and neither can a child who has met the same boat four times.\n\nThese "
    "are our illustrations, not pages from the book.\n\n40 pages, ages 6 to 12.\n\nReader: "
    + REG + "\nActivity book: " + REGA),
  ig=tail("One boat, four pages. ⛵\n\nThe Going To The Regatta activity book keeps coming back to "
    "the same vessel, and it's worth knowing why: the C1 is a class with rules, and the rig is "
    "fixed.\n\nOne mast, set well forward. One enormous triangular mainsail and NO jib — nothing "
    "forward of the mast. A long boom running well past the stern. A shallow open wooden hull. "
    "And a pry board out over the windward side for the crew to sit on, which is how a boat that "
    "size carries that much sail without going over.\n\nSwipe for the four pages that use it: "
    "Parts of a C1 Racing Sloop, Decorate the C1 Mainsail, The C1 Sloop Race, and Regatta I-Spy — "
    "6 shells, 5 stars, 4 fish, 3 small sloops.\n\nOnce you know the rig you can't unsee "
    "it.\n\nOur illustrations, not pages from the book.\n\n40 pages, ages 6–12.\n\nReader: "
    + REG + "\nActivity book: " + REGA,
    "#GoingToTheRegatta #C1Sloop #Bahamas #LongIsland #ActivityBook #BahamianCulture "
    "#GDSPublications"),
  pin_t='One boat, four pages',
  pin=tail("The C1 is a class with rules and the rig is fixed: one mast set well forward, one "
    "enormous triangular mainsail and no jib, a long boom past the stern, a shallow wooden hull "
    "and a pry board for the crew to sit out on. Four pages of the Going To The Regatta activity "
    "book use it. Our illustrations, not pages from the book.\n\n" + REGA),
  pin_url=REGA),
]

if __name__ == '__main__':
    run(S)
