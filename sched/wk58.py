# -*- coding: utf-8 -*-
"""Week 58: Thu 19 - Sun 22 Nov 2026. Six slots over four days.
TWO COLLAGE DAYS: Fri 20 (Activity Spotlight) and Sun 22 (Book World).

Activity Spotlight takes one because the point is a CONTRAST - the activity book
asks a child to learn a real humpback and to invent a cosmic one, and a contrast
needs both halves in view. Book World takes the other because the world of All
Things Bahamian is an archipelago, and no single frame is an archipelago.

All six books appear exactly once. ATB Upper and the Regatta reader were due.

Every catalogued alt below was emitted from images.json rather than retyped.
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
 # Thu 19 Nov — slot 114 — pillar 2 Reader Engagement — The Girl and The Whale — HERO
 # No Anna anywhere in this picture: it is the whale alone over a moonlit island.
 dict(day='2026-11-19', base=14, pid='gds/girl-whale/cosmic-whale-night-20260906',
  pad=False, board=B_READ, anna_absent=True,
  alt='A humpback whale made of purple starfield swimming through the night sky above a moonlit '
      'island.',
  fb=tail("If she came past your window tonight, what would you ask her?\n\nThat is a real "
    "question and we would genuinely like the answers, because it is the question we are "
    "left holding.\n\nHere is what we know about her. She is the Cosmic Theseus "
    "Finback. She is the largest humpback in the world — humpback, not whale, and the book is "
    "careful about that. Her fins glowed a cosmic purple and shone brighter than all the stars "
    "in the sky combined. And she took a comet strike to save every sea creature.\n\nSo she has "
    "been somewhere, and she has done something, and she is not telling.\n\nWhat would you "
    "ask?\n\nThe Girl and The Whale was written by Zhané Mackey and is published from Nassau by "
    "GDS Publications. This is our illustration, not a page from the book.\n\nGDS Reading "
    "Series, Level 3. Ages 6 to 12, grades 1 to 6.\n\n" + GW),
  ig=tail("If she came past your window tonight, what would you ask her? 🐋✨\n\nIt's a real "
    "question and we'd genuinely like the answers, because it's the one the book leaves a child "
    "holding.\n\nWhat we know: she is the Cosmic Theseus Finback. She is the largest humpback in "
    "the world — humpback, not whale, and the book is careful about that. Her fins glowed a "
    "cosmic purple and shone brighter than all the stars in the sky combined. And she took a "
    "comet strike to save every sea creature.\n\nSo she's been somewhere, she's done something, "
    "and she isn't telling.\n\nWhat would you ask? 👇\n\nWritten by Zhané Mackey, published from "
    "Nassau by GDS Publications. Our illustration, not a page from the book.\n\nAges 6–12.\n\n"
    + GW,
    "#TheGirlAndTheWhale #ChildrensBooks #BahamianAuthors #Humpback #ReadingSeries #IslandStory "
    "#GDSPublications"),
  pin_t='What would you ask her?',
  pin=tail("She is the Cosmic Theseus Finback: the largest humpback in the world, her fins "
    "glowing a cosmic purple and shining brighter than all the stars in the sky combined, and "
    "she took a comet strike to save every sea creature. Written by Zhané Mackey, published "
    "from Nassau by GDS Publications. Our illustration, not a page from the book.\n\n" + GW),
  pin_url=GW),

 # Fri 20 Nov — slot 115 — pillar 3 Promo/CTA — Going To The Regatta — HERO (catalogued)
 dict(day='2026-11-20', base=14, pid='gds/regatta/rainbow-over-the-atlantic-20261020',
  pad=False, board=B_LI, anna_absent=True,
  alt='A full bright rainbow arching over the Atlantic from the Long Island shore as a shower '
      'clears, half the sky still soft grey and half opening to blue, with a low swell rolling in '
      'and small waves running up pale sand in a thin lace of foam.',
  fb=tail("The best argument for this book is that nobody made any of it up.\n\nGoing To The "
    "Regatta is a true family account of five days on Long Island, written by Bridgette "
    "Skeete-Mackey and illustrated with the family's own photographs. That changes what the book "
    "can do.\n\nA made-up story would not bother telling you that the family never reached "
    "Dean's Blue Hole. It would not mention that they drove home after midnight with the fuel "
    "gauge dropping and got back with one bar remaining. It would not record that they flew out "
    "of Stella Maris airport because Deadman's Cay airport was being renovated.\n\nThose are the "
    "details that make a child believe the rest of it.\n\nAnd it carries real history: the first "
    "recorded organised race was at Deadman's Cay in 1868, racing near Salt Pond began in 1967, "
    "and the Long Islanders Association formed in August 1973.\n\nAbove is our illustration of "
    "the Atlantic shore. The book itself carries the photographs.\n\nGDS Reading Series, Family "
    "Reader. Ages 5 to 15.\n\nReader: " + REG + "\nActivity book: " + REGA),
  ig=tail("The best argument for this book is that nobody made any of it up. 🌈\n\nGoing To The "
    "Regatta is a true family account of five days on Long Island, written by Bridgette "
    "Skeete-Mackey and illustrated with the family's own photographs.\n\nA made-up story "
    "wouldn't bother telling you the family never reached Dean's Blue Hole. It wouldn't mention "
    "driving home after midnight with the fuel gauge dropping and getting back with one bar "
    "remaining. It wouldn't record flying out of Stella Maris airport because Deadman's Cay "
    "airport was being renovated.\n\nThose are the details that make a child believe the "
    "rest.\n\nReal history too: first recorded organised race at Deadman's Cay, 1868; racing "
    "near Salt Pond from 1967; the Long Islanders Association formed August 1973.\n\nOur "
    "illustration of the Atlantic shore. The book carries the photographs.\n\nAges 5–15.\n\n"
    "Reader: " + REG + "\nActivity book: " + REGA,
    "#GoingToTheRegatta #LongIsland #Bahamas #FamilyStories #BahamianAuthors #TrueStory "
    "#GDSPublications"),
  pin_t='Nobody made any of it up',
  pin=tail("Going To The Regatta is a true family account of five days on Long Island by "
    "Bridgette Skeete-Mackey, illustrated with the family's own photographs. A made-up story "
    "would not tell you they never reached Dean's Blue Hole, or that they drove home after "
    "midnight and got back with one bar of fuel remaining. Our illustration; the book carries "
    "the photographs.\n\n" + REG),
  pin_url=REG),

 # Fri 20 Nov — slot 116 — pillar 4 Activity Spotlight — Girl & Whale Activity Book — COLLAGE
 dict(day='2026-11-20', base=19, board=B_COLOR, pad=False, anna_absent=True,
  panels=['gds/girl-whale-activity/label-the-humpback-whale-20261120',
          'gds/girl-whale-activity/designing-the-finback-20261010',
          'gds/girl-whale-activity/the-fluke-going-down-20261120',
          'gds/girl-whale-activity/the-comet-strikes-cosmic-20261003'],
  alts=['A single humpback whale swimming slowly through clear open blue water, seen from the '
        'side and slightly below so the whole animal shows from snout to fluke: two very long '
        'pectoral fins, white underneath and knobbly along the front edge, a small stubby dorsal '
        'fin set well back on a low hump, a broad notched tail fluke, rounded knobs across the '
        'head and jaw and long pleated grooves along the throat. Sunlight comes down in shifting '
        'bands.',
        'An illustrator’s worktable seen from above, scattered with pencil sketches of a humpback '
        'whale — a tail fluke, a long pectoral fin, a whole whale in outline. On one sheet a fin '
        'has been coloured deep purple and scattered with starlight. A purple and a graphite '
        'pencil, a sharpener with shavings, an eraser, a jar of coloured pencils and a conch '
        'shell lie around them.',
        "A humpback whale's tail fluke lifted clear of the sea as she dives, seen from behind: "
        'broad, dark on top and patterned pale underneath, with a clear notch at the centre and a '
        'ragged trailing edge, water running off it in bright ribbons and falling back as spray. '
        'The rest of the whale is already under. Open blue-green ocean with a low swell rolling '
        'through and a soft wake spreading, a low green island far off in late afternoon light.',
        'A vast humpback whale rising through deep night ocean water, her long pectoral fins '
        'glowing cosmic purple and scattered with starlight. A white-gold comet streaks down '
        'towards her raised back. Turtles, rays and shoals of small fish look up from the water '
        'below her, safe in her shadow, under a sky full of stars.'],
  collage='gds/girl-whale-activity/collage-one-whale-two-jobs-20261120',
  alt='Four whale pictures: a humpback swimming in clear blue water with its long pectoral fins '
      'and notched fluke plainly shown, a worktable of pencil sketches of whale parts with one '
      'fin coloured purple, a fluke lifted clear of the sea as the whale dives, and a cosmic '
      'purple whale rising under a comet.',
  fb=tail("The same book asks a child to get a whale right, and then to make one up.\n\nThose "
    "are two different jobs and The Girl and The Whale Coloring & Activity Book wants "
    "both.\n\nLabel the Humpback Whale is the first job. It is about a real animal, and the "
    "facts the book teaches are real ones: humpbacks are mammals, not fish; they breathe air "
    "through a blowhole, not gills; the tail is called a fluke; whale song travels through "
    "water; and humpbacks are much larger than dolphins.\n\nDesign Your Own Cosmic Finback is "
    "the second.\n\nOur guess is that a child who has done the first one invents a better "
    "second one, because by then they know what a pectoral fin is for and roughly how long "
    "it ought to be.\n\nSwipe for both halves — these are our illustrations, not pages from the "
    "book.\n\n40 pages, ages 6 to 12, grades 1 to 6.\n\nReader: " + GW + "\nActivity book: "
    + GWA),
  ig=tail("The same book asks a child to get a whale right, and then to make one up. 🐋\n\nTwo "
    "different jobs, and The Girl and The Whale activity book wants both.\n\nLabel the Humpback "
    "Whale is the first. Real animal, real facts: humpbacks are mammals, not fish; they breathe "
    "air through a blowhole, not gills; the tail is called a fluke; whale song travels through "
    "water; humpbacks are much larger than dolphins.\n\nDesign Your Own Cosmic Finback is the "
    "second.\n\nOur guess is that a child who's done the first invents a "
    "better second one, because now they know what a pectoral fin is for and how long it ought "
    "to be.\n\nSwipe for both halves — our illustrations, not pages from the book.\n\n40 pages, "
    "ages 6–12.\n\nReader: " + GW + "\nActivity book: " + GWA,
    "#TheGirlAndTheWhale #ActivityBook #Humpback #KidsLearning #ClassroomIdeas #ColouringBook "
    "#GDSPublications"),
  pin_t='Get a whale right, then make one up',
  pin=tail("The Girl and The Whale activity book wants both jobs. Label the Humpback Whale is "
    "the real animal — mammals not fish, a blowhole not gills, the tail is a fluke. Design Your "
    "Own Cosmic Finback asks them to invent one. Our illustrations, not pages from the book. "
    "40 pages, ages 6 to 12.\n\n" + GWA),
  pin_url=GWA),

 # Sat 21 Nov — slot 117 — pillar 5 Bahamian Culture — ATB Lower — HERO (new)
 dict(day='2026-11-21', base=14, pid='gds/atb-lower/the-old-fort-20261121',
  pad=False, board=B_CULT, anna_absent=True,
  alt='An old stone fort above a Bahamian harbour seen from the grass below, its pale limestone '
      'walls weathered to cream and grey with rounded corner sentry turrets, a low arched gateway '
      'and narrow slit openings. Two black cannons on wooden carriages stand on the grass '
      'pointing out to sea, with bougainvillea and ferns at the foot of the wall and casuarinas '
      'leaning above. Beyond, clear turquoise water with a low swell rolling in.',
  fb=tail("Forts, monuments and lighthouses — that is one of the seven sections, and it is the "
    "one we would reach for first.\n\nHistoric Places and Landmarks runs pages 29 to 37 in All "
    "Things Bahamian, Lower Elementary. A fort gives a young child a great deal to colour: "
    "cannons, stonework, an arched gate, a turret, and the sea it was all pointed at.\n\nIt also "
    "gives them a question worth asking at that age — who was it watching for, and why "
    "here?\n\nAbove is our illustration of an island fort. It does not stand for any one of the "
    "real forts, and we have left it without flags or crests for that reason.\n\nThe artwork is "
    "shared with the Upper edition — same drawings, different page numbers. What differs is the "
    "written work around them.\n\nAll Things Bahamian, Lower Elementary. Ages 5 to 9, grades 1 "
    "to 3. 83 pages.\n\n" + ATBL),
  ig=tail("Forts, monuments and lighthouses — one of the seven sections, and the one children "
    "race to. 🏰\n\nHistoric Places and Landmarks runs pages 29–37 in All Things Bahamian, Lower "
    "Elementary. A fort gives a young child a lot to colour: cannons, stonework, an arched gate, "
    "a turret, and the sea it was all pointed at.\n\nIt also gives them a question worth asking "
    "at that age — who was it watching for, and why here?\n\nOur illustration of an island fort. "
    "It doesn't stand for any one of the real forts, which is why we've left it without flags or "
    "crests.\n\nThe artwork is shared with the Upper edition — same drawings, different page "
    "numbers.\n\nAges 5–9, grades 1–3, 83 pages.\n\n" + ATBL,
    "#AllThingsBahamian #Bahamas #BahamianHistory #ColouringBook #BahamianKids #IslandLife "
    "#GDSPublications"),
  pin_t='Forts, monuments and lighthouses',
  pin=tail("Historic Places and Landmarks runs pages 29 to 37 in All Things Bahamian, Lower "
    "Elementary. A fort gives a young child cannons, stonework, an arched gate, a turret and the "
    "sea it was pointed at. Our illustration of an island fort — it does not stand for any one "
    "of the real forts. Ages 5 to 9, 83 pages.\n\n" + ATBL),
  pin_url=ATBL),

 # Sun 22 Nov — slot 118 — pillar 6 Classroom & Library — Regatta Activity Book — HERO
 dict(day='2026-11-22', base=14, pid='gds/regatta-activity/family-connections-page-20261101',
  pad=False, board=B_COLOR, anna_absent=True,
  alt='A worktable seen from above where a family tree is being made: a large cream sheet with '
      'blank oval and rectangular frames joined by hand-drawn branching lines, every frame still '
      'empty, with small blank cards cut ready to stick in, a glue stick, scissors, a pencil, a '
      'jar of coloured pencils and a shell holding one corner down.',
  fb=tail("The page that goes home with the child.\n\nMy Family Connections and Family Roots and "
    "Roles are two of the activities in the Going To The Regatta Coloring & Activity Book, and "
    "of all the pages in it those are the two we would send home. A family tree wants "
    "somebody to ask.\n\nThat suits the book they came from. Going To The Regatta is a true family "
    "account by Bridgette Skeete-Mackey, and it is full of who is related to whom — "
    "the lesson it states is that a regatta is \"a homecoming where history, family, and island "
    "life meet\".\n\nIt also pairs with the reader's Words to Know list, which includes "
    "archipelago, descendant, hospitality, regatta, sloop and tradition. Descendant is not an "
    "abstract word once you are filling in the frames.\n\nAbove is our illustration of a family "
    "tree being made, not a page from the book.\n\n40 pages, ages 6 to 12.\n\nReader: " + REG
    + "\nActivity book: " + REGA),
  ig=tail("The page that goes home with the child. 🌴\n\nMy Family Connections and Family Roots "
    "and Roles are two of the activities in the Going To The Regatta activity book, and they're "
    "they're the two we'd send home. A family tree wants somebody to ask.\n\nThat "
    "suits the book they came from. Going To The Regatta is a true family account by Bridgette "
    "Skeete-Mackey, and the lesson it states is that a regatta is \"a homecoming where history, "
    "family, and island life meet\".\n\nIt pairs with the reader's Words to Know list, which "
    "includes archipelago, descendant, hospitality, regatta, sloop and tradition. Descendant "
    "isn't an abstract word once you're filling in the frames.\n\nOur illustration of a family "
    "tree being made, not a page from the book.\n\n40 pages, ages 6–12.\n\nReader: " + REG
    + "\nActivity book: " + REGA,
    "#GoingToTheRegatta #ClassroomIdeas #TeacherResources #FamilyTree #Bahamas #LongIsland "
    "#GDSPublications"),
  pin_t='The page that goes home with the child',
  pin=tail("My Family Connections and Family Roots and Roles are two of the activities in the "
    "Going To The Regatta activity book, and of all its pages those are the two we would send "
    "home: a family tree wants somebody to ask. Our illustration of a family tree being made, not a page "
    "from the book. 40 pages, ages 6 to 12.\n\n" + REGA),
  pin_url=REGA),

 # Sun 22 Nov — slot 119 — pillar 0 Book World — ATB Upper — COLLAGE
 dict(day='2026-11-22', base=19, board=B_COLOR, pad=False, anna_absent=True,
  panels=['gds/atb-upper/glass-window-bridge-20261008-v2',
          'gds/atb-upper/mangrove-creek-20261122',
          'gds/atb-upper/island-settlement-harbour-20261023',
          'gds/atb-upper/sandbar-at-low-tide-20261122'],
  alts=['The Glass Window Bridge in Eleuthera: a road bridge crossing a narrow gap in the rock, '
        'with the rough navy Atlantic breaking beyond it and the calm clear turquoise Bight of '
        'Eleuthera in the foreground on the near side.',
        'A quiet mangrove creek on a Bahamian island, looking along the channel from just above '
        'the water. Red mangroves crowd both banks, their arching tangles of pale prop roots '
        'standing out of shallow clear water under dark glossy leaves. The water runs shallow and '
        'very clear over pale sand and patches of turtle grass, with small fish in the shadows, a '
        'slow current, fine ripple lines and light shifting across the sand.',
        'A small Bahamian island settlement around a quiet harbour: pastel clapboard houses in '
        'pink, mint, yellow and pale blue stepping down a low hill, a wooden dock running out '
        'into clear turquoise water with two small boats alongside and a sailing boat moored '
        'beyond, palms and sea grape between the houses and a church spire on the rise. Ripple '
        'lines travel across the shallows and light flickers in bands over the sand below.',
        'A wide Bahamian sandbar at low tide seen from low down: a long pale bar curving out into '
        'shallow water, ribbed all over with ripple marks left by the tide, with scattered shells '
        'and an orange starfish on it and warm shallow pools lying in the dips. The water runs '
        'out in bands of near-white, jade, turquoise and deeper blue, with a low swell rolling in '
        'and thin lines of foam sliding across the flats. A low green cay on the horizon.'],
  collage='gds/atb-upper/collage-our-beautiful-islands-20261122',
  alt='Four Bahamian island scenes: the Glass Window Bridge with the navy Atlantic on one side '
      'and turquoise shallows on the other, a mangrove creek with arching prop roots over clear '
      'water, a pastel settlement around a quiet harbour, and a rippled sandbar at low tide with '
      'a starfish on it.',
  fb=tail("You cannot put an archipelago on one page, which is the whole problem the book is "
    "solving.\n\nOur Beautiful Islands is the longest section in All Things Bahamian by a "
    "distance — pages 9 to 49 in the Upper edition — and it is maps and island scenes. It has to "
    "be long, because the country is not one place.\n\nThe Glass Window Bridge is the clearest "
    "case. The book's own caption puts it plainly: \"At the Glass Window Bridge, the Atlantic "
    "Ocean and the calm Bight of Eleuthera lie on opposite sides of a narrow strip of rock.\" "
    "Two completely different seas, a road's width apart.\n\nThe Upper edition also carries Key "
    "Settlements and Communities — five named communities per island with a line of description "
    "each — which is the same idea in writing.\n\nThese are four island scenes of ours. In that "
    "section of the book, the pages are line drawings waiting for pencils.\n\nAll Things Bahamian: "
    "Upper Elementary. Ages 9 to 12, grades 4 to 6. 109 pages.\n\n" + ATBU),
  ig=tail("You can't put an archipelago on one page, which is the whole problem the book is "
    "solving. 🏝️\n\nOur Beautiful Islands is the longest section in All Things Bahamian by a "
    "distance — pages 9–49 in the Upper edition — maps and island scenes. It has to be long, "
    "because the country isn't one place.\n\nThe Glass Window Bridge is the clearest case. The "
    "book's own caption: \"At the Glass Window Bridge, the Atlantic Ocean and the calm Bight of "
    "Eleuthera lie on opposite sides of a narrow strip of rock.\" Two completely different seas, "
    "a road's width apart.\n\nThe Upper edition also carries Key Settlements and Communities — "
    "five named communities per island, a line each.\n\nSwipe for four island scenes of ours. In "
    "that section of the book, the pages are line drawings waiting for pencils.\n\nAges 9–12, grades 4–6, 109 pages.\n\n"
    + ATBU,
    "#AllThingsBahamian #Bahamas #Eleuthera #IslandLife #ColouringBook #BahamianKids "
    "#GDSPublications"),
  pin_t='You cannot put an archipelago on one page',
  pin=tail("Our Beautiful Islands is the longest section in All Things Bahamian — pages 9 to 49 "
    "in the Upper edition, maps and island scenes. The book's own caption on Eleuthera: \"At the "
    "Glass Window Bridge, the Atlantic Ocean and the calm Bight of Eleuthera lie on opposite "
    "sides of a narrow strip of rock.\" Our illustrations, not pages from the book.\n\n" + ATBU),
  pin_url=ATBU),
]

if __name__ == '__main__':
    run(S)
