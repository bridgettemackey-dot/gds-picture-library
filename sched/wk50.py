# -*- coding: utf-8 -*-
"""Week 50: Thu 22 - Sun 25 Oct 2026. Six slots over four days.
TWO COLLAGE DAYS: Thu 22 (Activity Spotlight) and Sun 25 14:00 (Behind the Scenes).

Activity Spotlight is the clearest case there is - the whole claim is that a forty
page activity book is more than colouring, and four different kinds of page prove
it where one cannot. Sunday is the second because Behind the Scenes on the activity
book is a sequence by nature: sketch, ink, colour test, finished illustration. The
other four slots stay single heroes - Bahamian Culture, Classroom & Library, Book
World and Reader Engagement each want one picture and one thought.
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
 # Thu 22 Oct — slot 74 — pillar 4 Activity Spotlight — Regatta activity book — COLLAGE
 dict(day='2026-10-22', base=14, board=B_COLOR, pad=False,
  panels=['gds/regatta-activity/regatta-i-spy-20261014',
          'gds/regatta-activity/design-a-regatta-flag-20261014d',
          'gds/regatta-activity/decorate-the-c1-mainsail-20261022',
          'gds/regatta-activity/plan-an-island-meal-20261022'],
  alts=["Looking down into clear shallow turquoise water over rippled sand: conch and scallop shells, orange starfish and small striped fish mid-dart, with the hulls of three small sloops on the moving surface above and light flickering in bands across the sand.", "A wooden table at the regatta set up for designing flags — blank pennants, coloured pencils, scissors and string, one pennant lifting at the corner — with bunting rippling between two poles and a gentle swell running up the sand beyond, a sloop leaving a soft wake.",
        'A Bahamian C1 racing sloop sailing on clear turquoise water, its single enormous '
        'triangular mainsail decorated with bold hand-drawn stripes, zigzags, stars and shells in '
        'aquamarine, gold and coral, two crew sitting out on the pry board, a low swell rolling '
        'under the hull and light shifting in bands through the shallows.',
        'A Bahamian family meal laid out on a wooden table outdoors, seen from above: a whole '
        'fried fish, peas and rice, baked chicken, fried plantains, potato salad, a halved coconut '
        'and a jug of juice with cut limes, with enamel plates, forks and hibiscus flowers between '
        'the dishes under dappled afternoon light.'],
  collage='gds/regatta-activity/collage-more-than-colouring-20261022',
  alt='A four-panel collage from the Going To The Regatta Coloring & Activity Book: a seek-and-find '
      'in clear shallow water, a table set up for designing flags, a C1 sloop with a decorated '
      'mainsail, and a Bahamian family meal laid out on a table.',
  fb=tail("Forty pages, and four of them look like this.\n\nGoing To The Regatta Coloring & Activity "
    "Book is not forty pages of colouring. Regatta I-Spy asks for six shells, five stars, four fish "
    "and three small sloops. Design a Regatta Flag hands over the pennant and the pencils. Decorate "
    "the C1 Mainsail does the same with the biggest sail on the water. Plan an Island Meal asks "
    "what you would actually put on the table.\n\nAlongside them: Parts of a C1 Racing Sloop, "
    "Nicholas's Long Island Route, My Family Connections, Family Roots and Roles, Island Compass "
    "Challenge, Nature Pool Observer, Island Food Scramble, A Future Dean's Blue Hole Adventure, "
    "and four colouring pages — Nicholas Sees the Sloops, The C1 Sloop Race, Family at the Regatta "
    "and The Nature Bath.\n\nThese are our illustrations of what those pages are about; in the book "
    "each is a line drawing waiting for pencils.\n\n40 pages, ages 6 to 12, grades 1 to "
    "6.\n\nReader: " + REG + "\nActivity book: " + REGA),
  ig=tail("Forty pages, and four of them look like this. ⛵\n\nRegatta I-Spy asks for six shells, "
    "five stars, four fish and three small sloops. Design a Regatta Flag hands over the pennant and "
    "the pencils. Decorate the C1 Mainsail does the same with the biggest sail on the water. Plan "
    "an Island Meal asks what you'd actually put on the table.\n\nAlso inside: Parts of a C1 Racing "
    "Sloop, Nicholas's Long Island Route, Family Roots and Roles, Island Compass Challenge, Nature "
    "Pool Observer, and four colouring pages.\n\nSwipe for all four — our illustrations of what the "
    "pages are about. In the book each is a line drawing waiting for pencils.\n\n40 pages, ages "
    "6–12.\n\nReader: " + REG + "\nActivity book: " + REGA,
    "#GoingToTheRegatta #ActivityBook #ColouringBook #Bahamas #LongIsland #KidsActivities "
    "#GDSPublications"),
  pin_t='Forty pages, and four of them look like this',
  pin=tail("Regatta I-Spy, Design a Regatta Flag, Decorate the C1 Mainsail and Plan an Island Meal "
    "— four of the forty pages in the Going To The Regatta Coloring & Activity Book. Our "
    "illustrations of what those pages are about; in the book each is a line drawing waiting for "
    "pencils. Ages 6 to 12.\n\nReader: " + REG + "\nActivity book: " + REGA),
  pin_url=REGA),

 # Fri 23 Oct — slot 75 — pillar 5 Bahamian Culture — ATB Upper — NEW ART
 dict(day='2026-10-23', base=14, pid='gds/atb-upper/island-settlement-harbour-20261023',
  pad=False, board=B_CULT,
  alt='A small Bahamian island settlement around a quiet harbour: pastel clapboard houses in pink, '
      'mint, yellow and pale blue stepping down a low hill, a wooden dock running out into clear '
      'turquoise water with two small boats alongside and a sailing boat moored beyond, palms and sea '
      'grape between the houses and a church spire on the rise. Ripple lines travel across the '
      'shallows and light flickers in bands over the sand below.',
  fb=tail("A settlement is not a town, and that distinction is the whole chapter.\n\nOur Beautiful "
    "Islands is the second of the seven sections in All Things Bahamian, and the largest. It runs "
    "to maps and island scenes across the archipelago.\n\nThe Upper edition goes further. It adds "
    "Key Settlements and Communities: five named communities per island with a line of description "
    "each. Eleuthera alone gives Governor's Harbour for its administrative role and historic homes, "
    "Gregory Town for pineapple farming and its annual Pineapple Festival, Rock Sound for the Ocean "
    "Hole, Tarpum Bay for fishing traditions, and Hatchet Bay for its protected harbour.\n\nThat is "
    "the part children rarely get taught — that the places they drive through have names for "
    "reasons, and the reasons are specific.\n\nThis is our illustration of the subject; in the book "
    "it is a line drawing waiting for pencils.\n\nAll Things Bahamian: Upper Elementary. Ages 9 to "
    "12, grades 4 to 6. 109 pages.\n\n" + ATBU),
  ig=tail("A settlement is not a town, and that difference is the whole chapter. 🏘️\n\nOur Beautiful "
    "Islands is the second and largest of the book's seven sections — maps and island scenes across "
    "the archipelago.\n\nThe Upper edition adds Key Settlements and Communities: five named "
    "communities per island, a line each. Eleuthera alone gives Governor's Harbour, Gregory Town "
    "and its Pineapple Festival, Rock Sound and the Ocean Hole, Tarpum Bay, Hatchet Bay.\n\nThe "
    "part children rarely get taught: the places they drive through have names for reasons, and "
    "the reasons are specific.\n\nOur illustration of the subject — in the book it's a line drawing "
    "waiting for pencils.\n\nAges 9–12, grades 4–6, 109 pages.\n\n" + ATBU,
    "#AllThingsBahamian #Bahamas #BahamianCulture #ColouringBook #IslandLife #GDSPublications "
    "#HomeschoolBahamas"),
  pin_t='A settlement is not a town — Our Beautiful Islands',
  pin=tail("The second and largest of the seven sections in All Things Bahamian. The Upper edition "
    "adds Key Settlements and Communities — five named communities per island with a line each. Our "
    "illustration of the subject; in the book it is a line drawing waiting for pencils. Upper "
    "Elementary, ages 9 to 12, 109 pages.\n\n" + ATBU),
  pin_url=ATBU),

 # Fri 23 Oct — slot 76 — pillar 6 Classroom & Library — ATB Lower — NEW ART
 dict(day='2026-10-23', base=19, pid='gds/atb-lower/classroom-display-wall-20261023',
  pad=False, board=B_CULT,
  alt='A primary classroom noticeboard with about twelve sheets of cream paper pinned up, each a '
      'child\'s coloured-in drawing of a Bahamian subject — a conch, a flamingo, a sailing boat, a '
      'pineapple, a lighthouse, a Junkanoo headdress, a fish, a palm — all in bright uneven crayon '
      'and pencil. Below the board a low shelf holds a jar of crayons, a stack of paper and a small '
      'potted plant.',
  fb=tail("The display wall is the point.\n\nA colouring book used well in a classroom does not end "
    "at the page. Thirty children colour the same conch and produce thirty different conchs, and "
    "pinning them up side by side is the lesson: this is ours, we all know it, and no two of us see "
    "it the same way.\n\nAll Things Bahamian is built for that. Seven sections — National Symbols, "
    "Our Beautiful Islands, Historic Places and Landmarks, Life in Our Bahamian Seas, Junkanoo, "
    "Fruits of The Bahamas, My Bahamas — so a teacher can take one section a week and have a term "
    "of work with a wall to show for it.\n\nThe Lower edition adds a Colouring Tips page and "
    "simpler design activities, including Design Your Own Junkanoo Costume.\n\nTeachers and "
    "librarians: tell us how you would run it, and how long you would give each section.\n\nAll "
    "Things Bahamian, Lower Elementary. Grades 1 to 3. 83 pages.\n\n" + ATBL),
  ig=tail("The display wall is the point. 📌\n\nThirty children colour the same conch and produce "
    "thirty different conchs. Pinning them up side by side is the lesson: this is ours, we all know "
    "it, and no two of us see it the same way.\n\nSeven sections — National Symbols, Our Beautiful "
    "Islands, Historic Places and Landmarks, Life in Our Bahamian Seas, Junkanoo, Fruits of The "
    "Bahamas, My Bahamas. One section a week is a term of work with a wall to show for it.\n\nThe "
    "Lower edition adds a Colouring Tips page and simpler design activities.\n\nTeachers and "
    "librarians — how would you run it? 👇\n\nGrades 1–3, 83 pages.\n\n" + ATBL,
    "#AllThingsBahamian #TeacherResources #ClassroomIdeas #Bahamas #BahamianKids #ColouringBook "
    "#GDSPublications"),
  pin_t='The display wall is the point',
  pin=tail("Thirty children colour the same conch and produce thirty different conchs. All Things "
    "Bahamian is built in seven sections, so a teacher can take one a week and have a term of work "
    "with a wall to show for it. The Lower edition adds a Colouring Tips page and simpler design "
    "activities. Grades 1 to 3, 83 pages.\n\n" + ATBL),
  pin_url=ATBL),

 # Sat 24 Oct — slot 77 — pillar 0 Book World — The Girl and The Whale — NEW ART
 dict(day='2026-10-24', base=14, pid='gds/girl-whale/under-the-stars-20261024',
  pad=False, board=B_READ,
  alt='Anna, a girl of about thirteen with chocolate-brown skin and long black hair, sitting close '
      'on the sand at night between her mother and her grandmother, all three seen from behind and '
      'looking up at a sky full of stars, one arm around her shoulders. Beyond them the dark sea '
      'moves gently, small waves running up the sand in a thin lace of pale foam, with green '
      'mountains behind.',
  fb=tail("The whale is gone by the last page, and that is not the ending.\n\nThe Cosmic Theseus "
    "Finback lands Anna, turns into stardust and floats into the sky. Kelani shouts her daughter's "
    "full name — Anna Lelani Mahoe, the one she uses when Anna is in trouble. Anna admits what the "
    "whole night was for: she wanted her mother to be proud of her.\n\nAnd then the three of them "
    "sit and look at the stars.\n\nThat is the book's last beat, and it is a quiet one. Not the "
    "flight, not the glow — a girl, her mother and her grandmother on the sand, with nothing left "
    "to prove.\n\n\"If you believe in something enough, it will come true!\"\n\nOur illustration of "
    "that moment, not a page from the book.\n\nThe Girl and The Whale, written by Zhané Mackey. GDS "
    "Reading Series, Level 3. Ages 6 to 12, grades 1 to 6.\n\n" + GW),
  ig=tail("The whale is gone by the last page, and that is not the ending. ✨\n\nThe Cosmic Theseus "
    "Finback lands Anna, turns into stardust and floats into the sky. Her mother shouts her full "
    "name — Anna Lelani Mahoe, the one used when she's in trouble. Anna admits what the whole night "
    "was for: she wanted her mother to be proud of her.\n\nThen the three of them sit and look at "
    "the stars.\n\nThat's the last beat, and it's a quiet one. Not the flight, not the glow — a "
    "girl, her mother and her grandmother on the sand, with nothing left to prove.\n\n\"If you "
    "believe in something enough, it will come true!\"\n\nOur illustration of that moment, not a "
    "page from the book.\n\nBy Zhané Mackey. Ages 6–12.\n\n" + GW,
    "#TheGirlAndTheWhale #BahamianAuthors #ChildrensBooks #ReadingSeries #KidsBooks "
    "#GDSPublications #BelieveInWonder"),
  pin_t='The whale is gone by the last page — and that is not the ending',
  pin=tail("The Cosmic Theseus Finback turns into stardust and floats into the sky, and the book "
    "ends with Anna, her mother and her grandmother sitting on the sand looking up. Our "
    "illustration of that moment, not a page from the book. Written by Zhané Mackey. Ages 6 to 12, "
    "grades 1 to 6.\n\n" + GW),
  pin_url=GW),

 # Sun 25 Oct — slot 78 — pillar 1 Behind the Scenes — Girl & Whale activity book — COLLAGE
 dict(day='2026-10-25', base=14, board=B_COLOR, pad=False,
  # The collage is about how a page is made; no picture in it shows Anna.
  anna_absent=True,
  panels=['gds/girl-whale-activity/designing-the-finback-20261010',
          'gds/girl-whale-activity/inking-the-line-art-20261025',
          'gds/girl-whale-activity/colour-tests-for-cosmic-20261025',
          'gds/girl-whale-activity/the-comet-strikes-cosmic-20261003'],
  alts=["An illustrator’s worktable seen from above, scattered with pencil sketches of a humpback whale — a tail fluke, a long pectoral fin, a whole whale in outline. On one sheet a fin has been coloured deep purple and scattered with starlight. A purple and a graphite pencil, a sharpener with shavings, an eraser, a jar of coloured pencils and a conch shell lie around them.",
        'A colouring page being inked at an illustrator\'s desk, seen from above: a sheet of cream '
        'paper carrying a clean black line drawing of a humpback whale breaching over water, '
        'outlines only and completely uncoloured, with a fine black pen laid across one corner, a '
        'pencil, an eraser and a jar of pens beside it, and the edge of a rougher pencil sketch of '
        'the same whale showing underneath.',
        'Colour tests on an illustrator\'s desk: a sheet of cream paper with two rows of painted '
        'swatches working through deep violet, indigo, lilac and blue-purple, beside a pencil '
        'sketch of a whale\'s long pectoral fin with three versions coloured in different purples '
        'to compare, one scattered with tiny stars, with a brush, a jar of water, a palette and '
        'coloured pencils around them.',
        "A vast humpback whale rising through deep night ocean water, her long pectoral fins glowing cosmic purple and scattered with starlight. A white-gold comet streaks down towards her raised back. Turtles, rays and shoals of small fish look up from the water below her, safe in her shadow, under a sky full of stars."],
  collage='gds/girl-whale-activity/collage-how-a-page-is-made-20261025',
  alt='A four-panel collage of how a colouring page is made: pencil sketches of a humpback whale, '
      'a clean uncoloured line drawing being inked, purple colour swatches tested against a fin, '
      'and the finished full-colour illustration of the whale under a falling comet.',
  fb=tail("Before a whale can be a line drawing, somebody has to decide what shape it is.\n\nSwipe "
    "through four stages of drawing the Cosmic Theseus Finback: loose pencil sketches working out "
    "the fluke and the set of the long pectoral fin; a clean inked outline with no colour in it at "
    "all; swatch after swatch of purple tested against that fin, because getting a glow wrong "
    "makes a whole picture go flat; and the finished illustration, the comet coming down.\n\nA "
    "colouring page is the quietest-looking thing in a book and rarely the quickest.\n\nThese are "
    "our illustrations; in the book the pages are line drawings waiting for pencils.\n\nThe Girl and The Whale Coloring & Activity Book. 40 pages, "
    "ages 6 to 12.\n\nReader: " + GW + "\nActivity book: " + GWA),
  ig=tail("Before a whale can be a line drawing, somebody has to decide what shape it is. 🎨\n\nFour "
    "stages of drawing the Cosmic Theseus Finback: loose pencil sketches working out the fluke and "
    "the long pectoral fin; a clean inked outline with no colour in it at all; swatch after swatch "
    "of purple tested against that fin, because getting a glow wrong makes a whole picture go "
    "flat; and the finished illustration, the comet coming down.\n\nSwipe through all four. Our "
    "illustrations — in the book the pages are line drawings waiting for pencils.\n\n40 pages, "
    "ages 6–12.\n\nReader: " + GW + "\nActivity book: " + GWA,
    "#TheGirlAndTheWhale #BehindTheScenes #Illustration #ColouringBook #ActivityBook "
    "#BahamianAuthors #GDSPublications"),
  pin_t='How a colouring page is made',
  pin=tail("Pencil sketches, a clean inked line drawing with no colour in it, swatches of purple "
    "tested against the Cosmic Theseus Finback's fin, and the finished illustration. Our "
    "illustrations of four stages of drawing her. 40 pages, ages 6 to 12.\n\nReader: " + GW + "\nActivity book: " + GWA),
  pin_url=GWA),

 # Sun 25 Oct — slot 79 — pillar 2 Reader Engagement — Going To The Regatta — NEW ART
 dict(day='2026-10-25', base=19, pid='gds/regatta/stella-maris-at-dawn-20261025',
  pad=False, board=B_LI,
  alt='Three Bahamian sisters walking barefoot together along the shore at Stella Maris, Long '
      'Island, early in the morning, seen from behind at a little distance, one carrying her '
      'sandals. The sky is soft apricot and pale gold just after sunrise. A low swell rolls in and '
      'small waves run up the wet sand in a thin lace of foam around their feet, with ironshore '
      'rock and casuarinas at the edge.',
  fb=tail("What does your family do on the first morning?\n\nIn Going To The Regatta it is this. "
    "They land at Stella Maris on the Thursday. By Friday morning Nicole and her sisters are "
    "walking Stella Maris at dawn, before the day starts making demands.\n\nIt is not in the book because anything happens. Nothing happens. It is in the book "
    "because that walk is the thing they do, and a family account that left it out would be "
    "wrong.\n\nEvery family has one. The early walk, the first swim, the drive past the old house, "
    "the particular shop. Tell us yours — we read every reply.\n\nGoing To The Regatta is a true "
    "family account by Bridgette Skeete-Mackey, illustrated with real family photographs. This is "
    "our illustration; the book itself carries the photographs.\n\nGDS Reading Series, Family "
    "Reader, ages 5 to 15.\n\n" + REG),
  ig=tail("What does your family do on the first morning? 🌅\n\nIn Going To The Regatta it's this. "
    "They land at Stella Maris on the Thursday. By Friday morning Nicole and her sisters are "
    "walking Stella Maris at dawn.\n\nIt's not in the book because "
    "anything happens. Nothing happens. It's in the book because that walk is the thing they do, "
    "and a family account that left it out would be wrong.\n\nEvery family has one. The early walk, "
    "the first swim, the drive past the old house, the particular shop.\n\nTell us yours 👇\n\nA "
    "true family account by Bridgette Skeete-Mackey. This is our illustration; the book carries the "
    "photographs.\n\nFamily Reader, ages 5–15.\n\n" + REG,
    "#GoingToTheRegatta #LongIsland #Bahamas #FamilyTraditions #BahamianAuthors #FamilyStories "
    "#GDSPublications"),
  pin_t='What does your family do on the first morning?',
  pin=tail("In Going To The Regatta the family land at Stella Maris on the Thursday, and by Friday "
    "morning Nicole and her sisters are walking the shore at dawn. Nothing happens. It is in the "
    "book because that walk is the thing they do. A true family account by Bridgette "
    "Skeete-Mackey. Family Reader, ages 5 to 15.\n\n" + REG),
  pin_url=REG),
]

if __name__ == '__main__':
    run(S)
