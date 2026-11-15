# -*- coding: utf-8 -*-
"""Week 57: Mon 16 - Wed 18 Nov 2026. Four slots over three days.
TWO COLLAGE DAYS: Mon 16 (Bahamian Culture) and Tue 17 (Book World).

Bahamian Culture takes one because the point is a JOURNEY - where fruit grows,
and what it looks like by the time it reaches a basket - and that is three or
four frames or it is nothing. Book World takes the other because the subject is
a sequence: the whale arrives, Anna rides, the whale goes, and the sea is left.
The two single-hero slots each make one point, so they show one picture.

Four books this week. ATB Upper and the Regatta reader both ran last week.
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
 # Mon 16 Nov — slot 110 — pillar 5 Bahamian Culture — ATB Lower — COLLAGE
 dict(day='2026-11-16', base=14, board=B_CULT, pad=False,
  panels=['gds/atb-lower/where-the-fruit-grows-20261106',
          'gds/atb-lower/bahamian-pears-on-the-tree-20261116',
          'gds/atb-lower/coconuts-at-the-roadside-20261116',
          'gds/atb-lower/fruits-opener-basket-20261101'],
  alts=['A sunny Bahamian garden plot seen from low down: a pineapple ripening at the centre of '
        'its spiky-leaved plant, rooted close to the ground, with a leaning coconut palm carrying '
        'a cluster of green coconuts behind it. A low drystone wall, crotons and scrub beyond, a '
        'wooden bucket on its side, and a glimpse of calm turquoise sea between the trees.',
        'Four large avocados ripening on a branch in a sunny Bahamian yard, seen from below and '
        'close: deep green, smooth-skinned and pear-shaped, widest at the bottom, hanging among '
        'big glossy dark-green leaves that stir in the breeze. Behind them a low drystone wall, '
        'bright crotons, red hibiscus and the corner of a pastel pink house under a wide blue sky.',
        'A small roadside coconut stand with nobody there: a weathered wooden table and a crate '
        'heaped with big green drinking coconuts, two of them opened at the top, a cutlass laid '
        'flat beside them and a blue cooler box on the ground. A leaning coconut palm above, sea '
        'grape and dry grass at the edge of the tarmac, and clear turquoise water beyond with a '
        'low swell and a line of foam along the sand.',
        'Two Bahamian children standing behind a big woven basket piled with fruit, smiling and holding '
        'up a mango, a pineapple, a soursop, a halved coconut, a sugar apple and a bunch of grapes. '
        'They stand on a shaded porch with bougainvillea along the rail, with a glimpse of turquoise '
        'sea beyond where a low swell rolls in.'],
  collage='gds/atb-lower/collage-where-it-comes-from-20261116',
  alt='Four Bahamian fruit scenes: a pineapple ripening low at the centre of its spiky-leaved '
      'plant, avocados hanging on a branch, a roadside stand with a crate of green drinking '
      'coconuts and a cutlass, and two children behind a woven basket piled with fruit.',
  fb=tail("Ask a child where a pineapple grows and watch them point up.\n\nIt grows down. One "
    "fruit at a time, sitting in the middle of its own spiky rosette of leaves, close enough to "
    "the ground to put your hand on without reaching. The coconuts are the ones doing the "
    "opposite, high up where the fronds meet the trunk.\n\nAnd the second picture is a Bahamian "
    "pear. If you expected something else, that is the point — in Bahamian usage a pear is an "
    "AVOCADO. \"Alligator pear\" and \"avocado pear\" are documented Bahamian names for the same "
    "thing.\n\nFruits of The Bahamas is the sixth of the seven sections in All Things Bahamian, "
    "pages 64 to 79 in the Lower edition, and it is about where each fruit grows and when it is "
    "in season. That is what turns a page of fruit into a piece of geography.\n\nThese are our "
    "illustrations; in the book the fruits are line drawings waiting for pencils.\n\nAll Things "
    "Bahamian, Lower Elementary. Ages 5 to 9, grades 1 to 3. 83 pages.\n\n" + ATBL),
  ig=tail("Ask a child where a pineapple grows and watch them point up. 🍍\n\nIt grows DOWN. One "
    "fruit at a time, in the middle of its own spiky rosette of leaves, close enough to the "
    "ground to put your hand on. The coconuts are the ones doing the opposite, high up where the "
    "fronds meet the trunk.\n\nAnd swipe to the second picture — that's a Bahamian pear. If you "
    "expected something else, that's the point: in Bahamian usage a pear is an AVOCADO. "
    "\"Alligator pear\" and \"avocado pear\" are documented Bahamian names for it.\n\nFruits of The "
    "Bahamas is the sixth of seven sections in All Things Bahamian, pages 64–79 in the Lower "
    "edition, and it's about where each fruit grows and when it's in season.\n\nOur "
    "illustrations; in the book these are line drawings waiting for pencils.\n\nAges 5–9, grades "
    "1–3, 83 pages.\n\n" + ATBL,
    "#AllThingsBahamian #Bahamas #BahamianKids #ColouringBook #Avocado #IslandLife "
    "#GDSPublications"),
  pin_t='A Bahamian pear is an avocado',
  pin=tail("Ask a child where a pineapple grows and watch them point up — it grows down, in the "
    "middle of its own spiky rosette. Fruits of The Bahamas is the sixth of seven sections in "
    "All Things Bahamian, pages 64 to 79 in the Lower edition, about where each fruit grows and "
    "when it is in season. Our illustrations, not pages from the book.\n\n" + ATBL),
  pin_url=ATBL),

 # Tue 17 Nov — slot 111 — pillar 6 Classroom & Library — Regatta Activity Book — HERO
 dict(day='2026-11-17', base=14, pid='gds/regatta-activity/nature-study-desk-20260906',
  pad=False, board=B_COLOR, anna_absent=True,
  alt='A school desk with blank drawing paper, coloured pencils, a conch shell and a magnifying '
      'glass.',
  fb=tail("A whole term can sit on one island.\n\nGoing To The Regatta and its activity book work "
    "as a pair, and between them they cover more ground than a single subject. The reader is a "
    "true family account of five days on Long Island, written by Bridgette Skeete-Mackey. Its "
    "Words to Know list includes archipelago, descendant, hospitality, regatta, sloop and "
    "tradition.\n\nThat is vocabulary, geography, history and social studies in one list.\n\nThe "
    "activity book then turns it into work. Parts of a C1 Racing Sloop. Nicholas's Long Island "
    "Route, which names Cape Santa Maria, Stella Maris, Simms, Salt Pond, Deadman's Cay, Dean's "
    "Blue Hole and South End, and calls its own map \"simplified, not to scale\". My Family "
    "Connections. Family Roots and Roles. Nature Pool Observer. Island Compass Challenge.\n\n"
    "Above is our illustration of a desk, not a page from the book.\n\nActivity book: 40 pages, "
    "ages 6 to 12. Reader: ages 5 to 15.\n\nReader: " + REG + "\nActivity book: " + REGA),
  ig=tail("A whole term can sit on one island. 🏝️\n\nGoing To The Regatta and its activity book "
    "work as a pair. The reader is a true family account of five days on Long Island by "
    "Bridgette Skeete-Mackey, and its Words to Know list includes archipelago, "
    "descendant, hospitality, regatta, sloop, tradition.\n\nVocabulary, geography, history and "
    "social studies in one list.\n\nThe activity book turns it into work: Parts of a C1 Racing "
    "Sloop. Nicholas's Long Island Route, which names Cape Santa Maria, Stella Maris, Simms, "
    "Salt Pond, Deadman's Cay, Dean's Blue Hole and South End, and calls its own map "
    "\"simplified, not to scale\". My Family Connections. Family Roots and Roles. Nature Pool "
    "Observer. Island Compass Challenge.\n\nOur illustration of a desk, not a page from the "
    "book.\n\nActivity book 40 pages, ages 6–12.\n\nReader: " + REG + "\nActivity book: " + REGA,
    "#GoingToTheRegatta #TeacherResources #ClassroomIdeas #LongIsland #Bahamas "
    "#HomeschoolBahamas #GDSPublications"),
  pin_t='A whole term can sit on one island',
  pin=tail("The Going To The Regatta reader's Words to Know list includes archipelago, "
    "descendant, hospitality, regatta, sloop, tradition. The activity book turns it into work — "
    "Parts of a C1 Racing Sloop, Nicholas's Long Island Route, My Family Connections, Nature "
    "Pool Observer. Our illustration of a desk, not a page from the book.\n\n" + REGA),
  pin_url=REGA),

 # Tue 17 Nov — slot 112 — pillar 0 Book World — The Girl and The Whale — COLLAGE
 dict(day='2026-11-17', base=19, board=B_READ, pad=False,
  panels=['gds/girl-whale/anna-meets-the-whale-20260907',
          'gds/girl-whale/annas-cosmic-ride-20261117',
          'gds/girl-whale/turning-into-stardust-20261029',
          'gds/girl-whale/the-sea-after-she-is-gone-20261117'],
  alts=['Anna underwater at a bright coral reef, reaching up with one hand to touch the nose of '
        'an enormous whale made of deep purple starfield. She has deep chocolate-brown skin and '
        'long black hair drifting out around her with a braid across the crown, a hibiscus '
        'sundress and a white cowrie necklace. Two green sea turtles glide past, small yellow '
        'fish dart over pink and orange coral, and sunlight comes down through the surface in '
        'shifting bands.',
        "An enormous cosmic humpback whale flying through a star-filled night sky high above a "
        "moonlit island, her body deep purple starfield and her long fins glowing violet. Anna "
        "rides small and high on the whale's back near the shoulders, leaning forward with one "
        "hand down and her hair and dress streaming back — deep chocolate-brown skin, long black "
        "hair, a hibiscus sundress and a cowrie necklace, lit warm by the whale's glow.",
        'An enormous humpback whale high above a dark island, coming apart from the tail forward '
        'into drifting motes of silver and violet light that rise among the stars, her head '
        'still solid and her long fins still glowing cosmic purple. On the pale beach far below, '
        'Anna — a girl with chocolate-brown skin and long black hair in a floral sundress — '
        'stands alone looking up, with a low swell running up the sand.',
        'A Hawaiian coral reef at night with nobody there: dark volcanic rock in the foreground, '
        'clear shallow water over the reef flat, the silhouette of green mountains along the '
        'coast and a low full moon laying a pale gold road of light across the sea. The water is '
        'moving quietly — a low swell rolling in, a lace of white foam running over the reef and '
        'ripple lines crossing the shallows — under a deep blue sky thick with stars.'],
  collage='gds/girl-whale/collage-after-the-whale-comes-20261117',
  alt='Four moments with the cosmic whale: Anna underwater reaching to touch the nose of an '
      'enormous purple starfield whale, Anna riding small and high on its back through a starry '
      'sky above a moonlit island, the whale coming apart into drifting motes of light with Anna '
      'watching from the beach, and the empty moonlit reef afterwards.',
  fb=tail("She is called the Cosmic Theseus Finback, and the book is careful about her.\n\nShe is "
    "a she. She is the largest HUMPBACK in the world — the book says humpback, not whale, and "
    "that precision is worth keeping. Her fins glowed a cosmic purple, and shone brighter than "
    "all the stars in the sky combined.\n\nAnd she took a comet strike to save every sea "
    "creature. That is what the book says she did, and Mr. Hooker is the one who knows the "
    "happens.\n\nAnna's Cosmic Ride is one of the five colouring pages in the activity book, "
    "which is where we would start a child who asks what happens.\n\nThese are our illustrations of "
    "four moments, not pages from the book.\n\nThe Girl and The Whale was written by Zhané "
    "Mackey and is published from Nassau by GDS Publications. GDS Reading Series, Level 3. Ages "
    "6 to 12, grades 1 to 6.\n\nReader: " + GW + "\nActivity book: " + GWA),
  ig=tail("She's called the Cosmic Theseus Finback, and the book is careful about her. 🐋✨\n\nShe "
    "is a she. She's the largest HUMPBACK in the world — the book says humpback, not whale, and "
    "that precision is worth keeping. Her fins glowed a cosmic purple, and shone brighter than "
    "all the stars in the sky combined.\n\nAnd she took a comet strike to save every sea "
    "creature. That's what the book says she did, and Mr. Hooker is the one who knows the "
    "happens.\n\nAnna's Cosmic Ride is one of the five colouring pages in the activity book, "
    "which is where we'd start a child who asks what happens.\n\nSwipe for four moments — our illustrations, "
    "not pages from the book.\n\nWritten by Zhané Mackey, published from Nassau by GDS "
    "Publications. Ages 6–12.\n\nReader: " + GW + "\nActivity book: " + GWA,
    "#TheGirlAndTheWhale #ChildrensBooks #BahamianAuthors #Humpback #IslandStory #ReadingSeries "
    "#GDSPublications"),
  pin_t='The Cosmic Theseus Finback',
  pin=tail("She is a she. She is the largest HUMPBACK in the world — the book says humpback, not "
    "whale. Her fins glowed a cosmic purple and shone brighter than all the stars in the sky "
    "combined, and she took a comet strike to save every sea creature. Our illustrations of four "
    "moments, not pages from the book. Written by Zhané Mackey.\n\n" + GW),
  pin_url=GW),

 # Wed 18 Nov — slot 113 — pillar 1 Behind the Scenes — Girl & Whale Activity Book — HERO
 dict(day='2026-11-18', base=14, pid='gds/girl-whale-activity/inking-the-line-art-20261025',
  pad=False, board=B_COLOR, anna_absent=True,
  alt="A colouring page being inked at an illustrator's desk, seen from above: a sheet of cream "
      "paper carrying a clean black line drawing of a humpback whale breaching over water, "
      "outlines only and completely uncoloured, with a fine black pen laid across one corner, a "
      "pencil, an eraser and a jar of pens beside it, and the edge of a rougher pencil sketch of "
      "the same whale showing underneath.",
  fb=tail("A colouring page has to survive losing all its colour.\n\nThat is the awkward thing "
    "about the form. Whatever the subject is, by the time it reaches a child it is outlines on "
    "white paper — and it still has to be recognisable, and the shapes still have to be big "
    "enough for a six-year-old to stay inside.\n\nA humpback is a good test. Take the colour "
    "away and what is left to recognise her by? The long pectoral fins, the knobbly head, the "
    "shape of the fluke.\n\nThe activity book has a page called Label the Humpback "
    "Whale, and the facts it teaches are real ones: "
    "humpbacks are mammals, not fish; they breathe air through a blowhole, not gills; the tail "
    "is called a fluke; whale song travels through water; and humpbacks are much larger than "
    "dolphins.\n\nAbove is our illustration of a page being inked, not a page from the "
    "book.\n\n40 pages, ages 6 to 12, grades 1 to 6.\n\nReader: " + GW + "\nActivity book: "
    + GWA),
  ig=tail("A colouring page has to survive losing all its colour. 🖊️\n\nThat's the awkward thing "
    "about the form. Whatever the subject is, by the time it reaches a child it's outlines on "
    "white paper — and it still has to be recognisable, with shapes big enough for a six-year-"
    "old to stay inside.\n\nA humpback is a good test. Take the colour away and what's left to "
    "recognise her by? The long pectoral fins, the knobbly head, the shape of the fluke.\n\nThe "
    "activity book has a page called Label the Humpback Whale, and the facts are real "
    "ones: humpbacks are mammals, not fish; they breathe through a "
    "blowhole, not gills; the tail is a fluke; whale song travels through water; and humpbacks "
    "are much larger than dolphins.\n\nOur illustration of a page being inked, not a page from "
    "the book.\n\n40 pages, ages 6–12.\n\nReader: " + GW + "\nActivity book: " + GWA,
    "#TheGirlAndTheWhale #BehindTheScenes #ActivityBook #Humpback #ColouringBook #KidsLearning "
    "#GDSPublications"),
  pin_t='A colouring page survives losing its colour',
  pin=tail("By the time a page reaches a child it is outlines on white paper, and it still has "
    "to be recognisable. A humpback is a good test: the long pectoral fins, the knobbly head, "
    "the fluke. Label the Humpback Whale is one of the activity book's pages. Our illustration "
    "of a page being inked, not a page from the book. 40 pages, ages 6 to 12.\n\n" + GWA),
  pin_url=GWA),
]

if __name__ == '__main__':
    run(S)
