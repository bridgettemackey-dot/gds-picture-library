# -*- coding: utf-8 -*-
"""Week 54: Thu 5 - Sun 8 Nov 2026. Six slots over four days.
TWO COLLAGE DAYS: Fri 6 (Activity Spotlight) and Sun 8 (Book World).

These are the two the runbook calls the natural pair, and both earn it here.
Activity Spotlight, because the point being made is that several of the Regatta
activity book's pages send a child OUTSIDE, and one picture of one activity
cannot show a range. Book World, because the point is the story's OPENING - four
moments in sequence - and a sequence needs more than one frame. The other four
slots are single heroes.

All six books appear exactly once.
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
 # Thu 5 Nov — slot 94 — pillar 3 Promo/CTA — ATB Upper — HERO (catalogued, the real cover)
 dict(day='2026-11-05', base=14, pid='gds/atb-upper/cover-20260915', pad=False, board=B_COLOR,
  alt='The cover of All Things Bahamian: Upper Elementary — four Bahamian children with binoculars, '
      'an open map, a notebook and a cup of coloured pencils, in front of turquoise water, small '
      'cays, a lighthouse and a flamingo.',
  fb=tail("Choosing between the two All Things Bahamian editions? Here is the honest answer.\n\n"
    "The two books share their colouring artwork. The Glass Window Bridge, the queen conch, the "
    "Boxing Day Junkanoo parade — same drawings, different page numbers. What actually differs is "
    "the written work around the pictures.\n\nThe Upper edition adds Key Settlements and "
    "Communities, which gives five named communities per island with a line of description each, "
    "and EXPLORE MORE pages carrying three written-response questions.\n\nSo it is not a different "
    "book of pictures. It is the same pictures asked to do more work.\n\nSeven sections: Bahamian "
    "National Symbols, Our Beautiful Islands, Historic Places and Landmarks, Life in Our Bahamian "
    "Seas, Junkanoo, Fruits of The Bahamas, and My Bahamas to close.\n\nAbove is the cover "
    "itself.\n\nAll Things Bahamian: Upper Elementary. Ages 9 to 12, grades 4 to 6. 109 "
    "pages.\n\n" + ATBU),
  ig=tail("Choosing between the two All Things Bahamian editions? Here's the honest answer. 📖\n\n"
    "Both books share their colouring artwork — the Glass Window Bridge, the queen conch, the "
    "Boxing Day Junkanoo parade. Same drawings, different page numbers.\n\nWhat differs is the "
    "written work around them. The Upper edition adds Key Settlements and Communities (five named "
    "communities per island, a line each) and EXPLORE MORE pages of written-response "
    "questions.\n\nIt isn't a different book of pictures. It's the same pictures asked to do more "
    "work.\n\nSeven sections, National Symbols through to My Bahamas.\n\nAbove is the cover "
    "itself.\n\nAges 9–12, grades 4–6, 109 pages.\n\n" + ATBU,
    "#AllThingsBahamian #ColouringBook #Bahamas #BahamianKids #HomeschoolBahamas #TeacherResources "
    "#GDSPublications"),
  pin_t='Which All Things Bahamian edition?',
  pin=tail("Both editions share their colouring artwork — the same drawings, different page "
    "numbers. What differs is the written work: the Upper edition adds Key Settlements and "
    "Communities, five named communities per island with a line each, and EXPLORE MORE pages of "
    "written-response questions. Seven sections. Ages 9 to 12, grades 4 to 6, 109 pages.\n\n"
    + ATBU),
  pin_url=ATBU),

 # Fri 6 Nov — slot 95 — pillar 4 Activity Spotlight — Regatta Activity Book — COLLAGE
 dict(day='2026-11-06', base=14, board=B_LI, pad=False,
  panels=['gds/regatta-activity/nature-pool-observer-20261018',
          'gds/regatta-activity/the-compass-on-the-rock-20261106',
          'gds/regatta-activity/a-future-blue-hole-adventure-20261106',
          'gds/regatta-activity/pink-sand-at-deals-beach-20261004'],
  alts=['A clear natural rock pool on the Long Island shore, with pale sand and stones on the '
        'bottom, a few tiny fish, a small crab and green weed moving slowly. Fine ripple rings '
        'spread across the surface. An open blank notebook with a pencil and a magnifying glass '
        'rest on the rock at the near edge.',
        'An old brass pocket compass lying open on warm pale limestone at the edge of a Long '
        'Island shore, its plain dial carrying a red-and-white needle and a simple star, with a '
        'knotted cord, two small shells and a sprig of sea grape leaves beside it. Beyond the '
        'rock, clear turquoise shallows where a low swell rolls in and ripple lines travel across '
        'the sand.',
        "Dean's Blue Hole on Long Island seen from the rock above: a near-circular pool of deep "
        'navy water set into pale turquoise shallows, a tall limestone cliff curving round one '
        'side and a crescent of white sand on the other. In the foreground a snorkel mask, swim '
        'fins and a closed notebook with a pencil across it, laid out and waiting, with nobody '
        'there yet. The shallows move gently while the deep blue circle stays calm.',
        'The pink sand at Deals Beach, Long Island, with clear calm shallow water washing quietly '
        'up over it.'],
  collage='gds/regatta-activity/collage-out-of-the-book-20261106',
  alt='Four Long Island scenes: a clear natural rock pool with a notebook and magnifying glass on '
      "the rock beside it, a brass compass open on warm limestone, Dean's Blue Hole with snorkel "
      'gear laid out at the edge, and the pink sand at Deals Beach with shallow water washing over '
      'it.',
  fb=tail("Some of these pages cannot be done at a table.\n\nThe Going To The Regatta Coloring & "
    "Activity Book has the usual indoor pages — word search, acrostic, bookmarks, a certificate. "
    "But read three of its activity names and you can tell where they point.\n\nNature Pool "
    "Observer. In the reader, the family's house at Stella Maris has a rocky path past the "
    "backyard leading down to the nature bath, a clear natural pool.\n\nIsland Compass "
    "Challenge.\n\nA Future Dean's Blue Hole Adventure — and this one is the cleverest "
    "page in the book. The family never reached Dean's Blue Hole, the second deepest in the world. "
    "So the reader hands the job to the activity book, and asks what Nicholas \"might notice, "
    "learn, and remember when he finally gets there\".\n\nThe fourth picture is Deals Beach, whose "
    "pink sand the reader's own photo gallery names.\n\nThese are our illustrations, not pages "
    "from the book.\n\n40 pages, ages 6 to 12.\n\nReader: " + REG + "\nActivity book: " + REGA),
  ig=tail("Some of these pages can't be done at a table. 🧭\n\nThe Going To The Regatta activity "
    "book has the usual indoor pages — word search, acrostic, bookmarks, a certificate. But read "
    "three of its activity names and you can tell where they point.\n\nNature Pool Observer. In "
    "the reader, the family's house at Stella Maris has a rocky path leading down to the nature "
    "bath, a clear natural pool.\n\nIsland Compass Challenge.\n\nA Future Dean's Blue Hole Adventure — the "
    "cleverest page in the book. The family never reached Dean's Blue Hole, the second deepest in "
    "the world. So the reader hands the job over and asks what Nicholas \"might notice, learn, and "
    "remember when he finally gets there\".\n\nSwipe for all four — the last is Deals Beach, whose "
    "pink sand the reader's photo gallery names.\n\nOur illustrations, not pages from the "
    "book.\n\n40 pages, ages 6–12.\n\nReader: " + REG + "\nActivity book: " + REGA,
    "#GoingToTheRegatta #LongIsland #Bahamas #ActivityBook #KidsActivities #BahamianKids "
    "#GDSPublications"),
  pin_t='Activity pages you cannot do at a table',
  pin=tail("Nature Pool Observer, Island Compass Challenge and A Future Dean's Blue Hole "
    "Adventure — three activity names in the Going To The Regatta activity book that tell you "
    "where they point. The family never reached Dean's Blue Hole, the second deepest in the "
    "world. Our illustrations, not pages from the book.\n\n" + REGA),
  pin_url=REGA),

 # Fri 6 Nov — slot 96 — pillar 5 Bahamian Culture — ATB Lower — HERO (new)
 dict(day='2026-11-06', base=19, pid='gds/atb-lower/where-the-fruit-grows-20261106',
  pad=False, board=B_CULT,
  alt='A sunny Bahamian garden plot seen from low down: a pineapple ripening at the centre of its '
      'spiky-leaved plant, rooted close to the ground, with a leaning coconut palm carrying a '
      'cluster of green coconuts behind it. A low drystone wall, crotons and scrub beyond, a '
      'wooden bucket on its side, and a glimpse of calm turquoise sea between the trees.',
  fb=tail("A pineapple does not grow on a tree.\n\nIt grows low down, one fruit at a time, sitting "
    "in the middle of its own spiky rosette of leaves, close enough to the ground that you could "
    "put your hand on it without reaching.\n\nPlenty of grown-ups do not know that, which is why "
    "it is worth a child knowing it.\n\nFruits of The Bahamas is the sixth of the seven sections "
    "in All Things Bahamian, and it is not just a parade of fruit to colour in. The section is "
    "about where each fruit grows and when it is in season — which turns a colouring page into a "
    "small piece of geography.\n\nThe coconuts behind are doing the opposite thing: high up, in a "
    "cluster, where the fronds meet the trunk.\n\nThis is our illustration; in the book the fruits "
    "are line drawings waiting for pencils.\n\nAll Things Bahamian, Lower Elementary. Ages 5 to 9, "
    "grades 1 to 3. 83 pages, with a Colouring Tips page.\n\n" + ATBL),
  ig=tail("A pineapple doesn't grow on a tree. 🍍\n\nIt grows low down, one fruit at a time, "
    "sitting in the middle of its own spiky rosette of leaves — close enough to the ground that "
    "you could put your hand on it without reaching.\n\nPlenty of grown-ups don't know that, which "
    "is why it's worth a child knowing it.\n\nFruits of The Bahamas is the sixth of the seven "
    "sections in All Things Bahamian, and it isn't just a parade of fruit to colour. The section "
    "is about where each fruit grows and when it's in season — which turns a colouring page into a "
    "small piece of geography.\n\nThe coconuts behind do the opposite: high up, in a cluster, "
    "where the fronds meet the trunk.\n\nOur illustration; in the book these are line drawings "
    "waiting for pencils.\n\nAges 5–9, grades 1–3, 83 pages.\n\n" + ATBL,
    "#AllThingsBahamian #Bahamas #BahamianKids #ColouringBook #Pineapple #KidsLearning "
    "#GDSPublications"),
  pin_t='A pineapple does not grow on a tree',
  pin=tail("It grows low down, one fruit at a time, in the middle of its own spiky rosette of "
    "leaves. Fruits of The Bahamas is the sixth section of All Things Bahamian, and it is about "
    "where each fruit grows and when it is in season — which turns a colouring page into a small "
    "piece of geography. Our illustration; in the book these are line drawings waiting for "
    "pencils. Lower Elementary, ages 5 to 9, 83 pages.\n\n" + ATBL),
  pin_url=ATBL),

 # Sat 7 Nov — slot 97 — pillar 6 Classroom & Library — Girl & Whale Activity Book — HERO
 # Anna is named in the caption but appears in NO picture in this slot: the reading corner
 # holds a mat, a pencil tin, books, a whale bookmark and a jar of shells, and no people at
 # all. Checked at w_700 before setting this.
 dict(day='2026-11-07', base=14, pid='gds/girl-whale-activity/reading-corner-20260902',
  pad=False, board=B_COLOR, anna_absent=True,
  alt='A reading corner with a woven mat, coloured pencils, a whale bookmark and a jar of '
      'seashells.',
  fb=tail("A quiet corner, and one minute of silence. That is a whole activity.\n\nListen Like "
    "Anna asks a child to sit quietly for one minute and write down four sounds they can hear. "
    "It is the one we would start a class with.\n\nIt works because it is what Anna does. The "
    "story begins with her hearing something, and not being believed.\n\nThe rest of the book earns its place in a classroom on firmer "
    "ground. Label the Humpback Whale. Connect the Cosmic Finback, 1 to 30. Legend and Reality "
    "sorting. Coral Reef I-Spy, which asks for 6 shells, 5 starfish, 4 fish, 3 crabs, 2 sea "
    "turtles and 1 tiny legend book.\n\nAnd the facts it teaches are real ones. Humpbacks are "
    "mammals, not fish. They breathe air through a blowhole, not gills. The tail is called a "
    "fluke. Whale song travels through water.\n\n40 pages, ages 6 to 12, grades 1 to 6.\n\n"
    "Reader: " + GW + "\nActivity book: " + GWA),
  ig=tail("A quiet corner and one minute of silence. That's a whole activity. 🐋\n\nListen Like "
    "Anna asks a child to sit quietly for one minute and write down four sounds they can hear. "
    "It's the one we'd start a class with.\n\nIt works because it's what Anna does. The story "
    "begins with her hearing something, and not being believed.\n\nThe rest earns its place on firmer ground: Label the Humpback Whale, Connect "
    "the Cosmic Finback 1–30, Legend and Reality sorting, and Coral Reef I-Spy — 6 shells, 5 "
    "starfish, 4 fish, 3 crabs, 2 sea turtles, 1 tiny legend book.\n\nThe facts are real ones. "
    "Humpbacks are mammals, not fish. They breathe through a blowhole, not gills. The tail is a "
    "fluke. Whale song travels through water.\n\n40 pages, ages 6–12.\n\nReader: " + GW
    + "\nActivity book: " + GWA,
    "#TheGirlAndTheWhale #ClassroomIdeas #TeacherResources #ActivityBook #Humpback #ReadingCorner "
    "#GDSPublications"),
  pin_t='One minute of silence is a whole activity',
  pin=tail("Listen Like Anna asks a child to sit quietly for one minute and write down four "
    "sounds they can hear. The Girl and The Whale Coloring & Activity Book also teaches real "
    "facts: humpbacks are mammals not fish, they breathe through a blowhole, the tail is a "
    "fluke, and whale song travels through water. 40 pages, ages 6 to 12.\n\n" + GWA),
  pin_url=GWA),

 # Sun 8 Nov — slot 98 — pillar 0 Book World — The Girl and The Whale — COLLAGE
 dict(day='2026-11-08', base=14, board=B_READ, pad=False,
  panels=['gds/girl-whale/empty-docks-at-dawn-20261108',
          'gds/girl-whale/anna-follows-the-song-20261108',
          'gds/girl-whale/mr-hooker-tells-the-legend-20260925',
          'gds/girl-whale/book-of-legends-on-the-reef-20261001'],
  alts=['A small Hawaiian fishing dock at first light with nobody on it: weathered grey planks and '
        'pilings running out over the water, a coil of rope and a folded net, and two tied-up '
        'skiffs rocking slowly against their lines. Green mountains stand behind under a pale gold '
        'and rose sky, and the sea is plainly moving — a low swell lifting the boats and a thin '
        'lace of foam running up the sand.',
        'Anna walking a Hawaiian shoreline early in the morning, mid-stride and turned away from '
        'the viewer with her head tilted, listening. She has deep chocolate-brown skin and long '
        'black hair loose past her shoulders with a braid across the crown, a white cowrie '
        'necklace and a hibiscus sundress, and she is barefoot on black volcanic rock and pale '
        'sand. The sea rolls in low with a lace of foam.',
        'An older fisherman in a straw hat and faded blue floral shirt sits on the edge of a '
        'weathered wooden dock at sunset, one hand raised mid-story. Beside him a coil of rope, a '
        'folded green net and a battered tackle box; a small boat is tied below. Green volcanic '
        'mountains and a low golden sun behind.',
        'A thick old leather-bound book lying open on a flat sun-bleached rock at the edge of a '
        'shallow coral reef, its weathered cream pages blank. A conch shell and a sprig of dried '
        'seaweed beside it, clear turquoise water over coral and two small yellow fish below, and '
        'green volcanic mountains across the bay in late golden light.'],
  collage='gds/girl-whale/collage-where-the-story-starts-20261108',
  alt='Four moments from the opening of The Girl and The Whale: an empty fishing dock at first '
      'light, Anna walking a shoreline with her head tilted to listen, an older fisherman on a '
      'dock at sunset with one hand raised mid-story, and a thick leather-bound book lying open on '
      'a rock at the edge of a reef.',
  fb=tail("Four pictures, and you have the beginning of the story.\n\nAnna hears whale song on the "
    "beach and follows it to the docks. At the docks is Mr. Hooker — \"one of the greatest "
    "fishermen in Hawaii\", a man who knows many island stories. He tells her the legend. He gives "
    "her the book.\n\nThat is the opening, and what makes it work is the order. She does not find "
    "a whale. She finds a sound, then a person, then a book — and only then does anything "
    "happen.\n\nBelief is the thing the story keeps turning on. Her mother is sceptical. "
    "\"You do not think anything is real,\" Gran Gran tells Kelani.\n\nThe Girl and The Whale was "
    "written by Zhané Mackey, and is published from Nassau by GDS Publications.\n\nThese are our "
    "illustrations of four moments from the story, not pages from the book.\n\nGDS Reading Series, "
    "Level 3. Ages 6 to 12, grades 1 to 6.\n\n" + GW),
  ig=tail("Four pictures, and you have the beginning of the story. 🐋\n\nAnna hears whale song on "
    "the beach and follows it to the docks. At the docks is Mr. Hooker — \"one of the greatest "
    "fishermen in Hawaii\", a man who knows many island stories. He tells her the legend. He gives "
    "her the book.\n\nWhat makes the opening work is the order. She doesn't find a whale. She "
    "finds a sound, then a person, then a book — and only then does anything happen.\n\nEverything "
    "after keeps turning on belief. Her mother is sceptical.\n\nWritten by Zhané Mackey, "
    "published from Nassau by GDS Publications.\n\nSwipe for all four — our illustrations of "
    "moments from the story, not pages from the book.\n\nAges 6–12, grades 1–6.\n\n" + GW,
    "#TheGirlAndTheWhale #ChildrensBooks #BahamianAuthors #ReadingSeries #IslandStory #Humpback "
    "#GDSPublications"),
  pin_t='Four pictures and you have the beginning',
  pin=tail("Anna hears whale song on the beach and follows it to the docks. There she meets Mr. "
    "Hooker, \"one of the greatest fishermen in Hawaii\", who tells her the legend and gives her "
    "the book. She does not find a whale — she finds a sound, then a person, then a book. Written "
    "by Zhané Mackey, published from Nassau by GDS Publications. Our illustrations of moments from "
    "the story, not pages from the book. Ages 6 to 12.\n\n" + GW),
  pin_url=GW),

 # Sun 8 Nov — slot 99 — pillar 1 Behind the Scenes — Going To The Regatta — HERO
 dict(day='2026-11-08', base=19, pid='gds/regatta/writers-desk-longisland-v2-20260905',
  pad=False, board=B_LI,
  alt='A writer’s desk at night with a hand-drawn ink map of Long Island, a conch shell and a '
      'straw fan.',
  fb=tail("Going To The Regatta had a harder job than most of our books: everything in it "
    "happened.\n\nIt is a true family account, written by Bridgette Skeete-Mackey and illustrated "
    "with real family photographs rather than drawings. So the writing could not go wherever it "
    "liked. It had five days to cover and a real island to cross.\n\nThursday lands at Stella "
    "Maris in North Long Island, then the long drive south to Salt Pond in Central Long Island. "
    "Friday, Saturday and Sunday stay around the regatta and the settlements. Monday goes home "
    "from Stella Maris airport — the only one operating, because Deadman's Cay airport was being "
    "renovated.\n\nThat is the kind of detail a true account has to carry, and it is why the "
    "activity book's route page lists real places in order: Cape Santa Maria, Stella Maris, Simms, "
    "Salt Pond, Deadman's Cay, Dean's Blue Hole, South End. The page calls its own map "
    "\"simplified, not to scale\".\n\nAbove is our illustration of a writer's desk. The book "
    "itself carries the photographs.\n\nGDS Reading Series, Family Reader. Ages 5 to 15.\n\n"
    "Reader: " + REG + "\nActivity book: " + REGA),
  ig=tail("Going To The Regatta had a harder job than most of our books: everything in it "
    "happened. ✍️\n\nIt's a true family account, written by Bridgette Skeete-Mackey and "
    "illustrated with real family photographs rather than drawings. So the writing couldn't go "
    "wherever it liked. It had five days to cover and a real island to cross.\n\nThursday lands at "
    "Stella Maris in North Long Island, then the long drive south to Salt Pond. Friday, Saturday "
    "and Sunday stay around the regatta and the settlements. Monday goes home from Stella Maris "
    "airport — the only one operating, because Deadman's Cay airport was being renovated.\n\nThat "
    "kind of detail is why the activity book's route page lists real places in order: Cape Santa "
    "Maria, Stella Maris, Simms, Salt Pond, Deadman's Cay, Dean's Blue Hole, South End. The page "
    "calls its own map \"simplified, not to scale\".\n\nOur illustration of a writer's desk. The "
    "book itself carries the photographs.\n\nAges 5–15.\n\nReader: " + REG + "\nActivity book: "
    + REGA,
    "#GoingToTheRegatta #BehindTheScenes #LongIsland #Bahamas #BahamianAuthors #FamilyStories "
    "#GDSPublications"),
  pin_t='A true account has to cross a real island',
  pin=tail("Going To The Regatta is a true family account by Bridgette Skeete-Mackey, "
    "illustrated with real family photographs. Five days and a real island to cross: Thursday "
    "lands at Stella Maris, then the drive south to Salt Pond; Monday goes home from Stella "
    "Maris airport, the only one operating. Our illustration of a writer's desk; the book "
    "carries the photographs.\n\n" + REG),
  pin_url=REG),
]

if __name__ == '__main__':
    run(S)
