# -*- coding: utf-8 -*-
"""Week 60: Thu 26 - Sun 29 Nov 2026. Six slots over four days.
TWO COLLAGE DAYS: Fri 27 (Book World) and Sun 29 (Promo/CTA).

Book World takes one because the world of a story is not one frame. Promo/CTA takes
the other because the argument for the activity book is BREADTH - forty pages doing
several different kinds of work - and breadth needs more than one example in view.
The other four pillars each make a single point, so they get a single picture.

All six books appear exactly once. Both readers were due; week 59 had only four slots
and used neither.

Fri 27 is Black Friday. The gift angle sits on Book World, and names no discount:
GDS does not set Amazon's prices and no promotion has been agreed.

Thu 26 and Fri 27 both involve a real page or a real rig, and both say which is which:
Friday's map IS an actual page of the book; Thursday's sloops are ours.

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
 # Thu 26 Nov — slot 124 — pillar 5 Bahamian Culture — Going To The Regatta (reader) — HERO (new)
 # No child in this picture: the crews are grown men, in the middle distance.
 dict(day='2026-11-26', base=14, pid='gds/regatta/the-start-of-the-race-20261126',
  pad=False, board=B_LI, anna_absent=True,
  alt='Three wooden Bahamian racing sloops just after the start of a race off Long Island, seen '
      'from the shore. Each carries one tall triangular mainsail on a single mast set well forward, '
      'with no second sail, and each is heeled over with its crew of grown men sitting right out on '
      'the long pry board over the windward side. Bright turquoise water with a short chop, spray '
      'off the bows and white wake behind. Rocks, a pale beach and casuarinas in the foreground.',
  fb=tail("Sloop racing in The Bahamas is older than the aeroplane.\n\nThe first recorded organised "
    "race was at Deadman's Cay in 1868. Racing near Salt Pond began in 1967, when the schools "
    "inspector and others started racing; an American businessman watching offered a trophy, and "
    "a three-day event followed. From 1969, Long Island descendants living in New Providence "
    "raised money for the prizes. In August 1973 the Long Islanders Association was formed, "
    "working on education, recreation, medical assistance and support for Long Island "
    "families.\n\nThat last line is the part worth sitting with. The thing that grew out of the "
    "racing was not a bigger race. It was a body of people looking after an island's "
    "families.\n\nGoing To The Regatta puts it this way: \"A regatta is more than a race. It is a "
    "homecoming where history, family, and island life meet.\"\n\nThe boats above are C1 class, "
    "and the book is strict about the rig: one mast, ONE large mainsail, no jib, and the crew out "
    "on the pry board to hold her down.\n\nThis is our illustration. The book itself carries the "
    "family's own photographs.\n\nGDS Reading Series, Family Reader. Ages 5 to 15.\n\n" + REG),
  ig=tail("Sloop racing in The Bahamas is older than the aeroplane. ⛵\n\nFirst recorded organised "
    "race: Deadman's Cay, 1868. Racing near Salt Pond from 1967, when the schools inspector and "
    "others began racing — an American businessman watching offered a trophy, and a three-day "
    "event followed. From 1969, Long Island descendants in New Providence raised money for the "
    "prizes. August 1973: the Long Islanders Association formed, working on education, "
    "recreation, medical assistance and support for Long Island families.\n\nThat last line is "
    "the part worth sitting with. What grew out of the racing wasn't a bigger race. It was a body "
    "of people looking after an island's families.\n\nThe book's own words: \"A regatta is more "
    "than a race. It is a homecoming where history, family, and island life meet.\"\n\nThese are "
    "C1 sloops — one mast, ONE mainsail, no jib, crew out on the pry board.\n\nOur illustration; "
    "the book carries the family's photographs.\n\nAges 5–15.\n\n" + REG,
    "#GoingToTheRegatta #LongIsland #Bahamas #SloopRacing #BahamianCulture #FamilyStories "
    "#GDSPublications"),
  pin_t='Older than the aeroplane',
  pin=tail("The first recorded organised sloop race in The Bahamas was at Deadman's Cay in 1868. "
    "Racing near Salt Pond began in 1967, and in August 1973 the Long Islanders Association "
    "formed — education, recreation, medical assistance and support for Long Island families. "
    "Going To The Regatta is a true family account by Bridgette Skeete-Mackey. Our illustration; "
    "the book carries the photographs.\n\n" + REG),
  pin_url=REG),

 # Fri 27 Nov — slot 125 — pillar 6 Classroom & Library — ATB Upper — HERO (REAL book page)
 dict(day='2026-11-27', base=14, pid='gds/atb-upper/map-of-the-bahamas-20260915',
  pad=True, board=B_COLOR, anna_absent=True,
  alt='A colouring page: an outline map of the whole Bahamian archipelago with every island and cay '
      'named, from Grand Bahama and Abaco down to Inagua, with a north arrow and a scale bar.',
  fb=tail("A colouring book stops being only a colouring book at the point where it asks a child "
    "to write something down.\n\nThis is an actual page from All Things Bahamian, Upper "
    "Elementary: the archipelago with every island and cay named, a north arrow and a scale "
    "bar.\n\nFor a classroom or a library that page does two jobs at once. A child colours it, "
    "and a child has to find Inagua.\n\nThe Upper edition carries written work the Lower one does "
    "not. Key Settlements and Communities gives five named communities per island with a line of "
    "description each. The EXPLORE MORE! pages ask three written-response questions. That is the "
    "part a teacher can build a lesson on, and it is why this edition is the one we would hand to "
    "a librarian.\n\nOur Beautiful Islands is the longest section in the book — pages 9 to 49, "
    "maps and island scenes.\n\nAll Things Bahamian, Upper Elementary. Ages 9 to 12, grades 4 to "
    "6. 109 pages.\n\n" + ATBU),
  ig=tail("A colouring book stops being only a colouring book the moment it asks a child to write "
    "something down. 🗺️\n\nThis is an actual page from All Things Bahamian, Upper Elementary: the "
    "archipelago with every island and cay named, a north arrow, a scale bar.\n\nIn a classroom "
    "that page does two jobs at once. A child colours it, and a child has to find "
    "Inagua.\n\nThe Upper edition carries written work the Lower one doesn't. Key Settlements and "
    "Communities gives five named communities per island with a line each. The EXPLORE MORE! "
    "pages ask three written-response questions. That's what a teacher can build a lesson "
    "on.\n\nOur Beautiful Islands is the longest section — pages 9 to 49.\n\nAges 9–12, grades "
    "4–6, 109 pages.\n\n" + ATBU,
    "#AllThingsBahamian #Bahamas #ClassroomIdeas #Teachers #Homeschool #BahamianKids "
    "#GDSPublications"),
  pin_t='Colour it, then find Inagua',
  pin=tail("An actual page from All Things Bahamian, Upper Elementary: the whole archipelago with "
    "every island and cay named, a north arrow and a scale bar. The Upper edition also carries "
    "Key Settlements and Communities — five named communities per island — and EXPLORE MORE! "
    "pages of three written-response questions. Ages 9 to 12, 109 pages.\n\n" + ATBU),
  pin_url=ATBU),

 # Fri 27 Nov — slot 126 — pillar 0 Book World — The Girl and The Whale (reader) — COLLAGE
 # Black Friday. A gift angle, no discount claimed. Anna is in two of the four panels.
 dict(day='2026-11-27', base=19, board=B_READ, pad=False,
  panels=['gds/girl-whale/the-dance-at-sunset-20261115',
          'gds/girl-whale/turning-into-stardust-20261029',
          'gds/girl-whale/the-song-over-the-water-20261127',
          'gds/girl-whale/the-whale-far-offshore-20261127'],
  alts=['A Hawaiian reef flat at sunset with the sky glowing coral and gold and a long road of light '
        'over the water. Anna dances in the middle distance, mid-turn with both arms lifted and one '
        'bare foot off the ground, her dress and hair swinging out — deep chocolate-brown skin, long '
        'black hair past her shoulders, a hibiscus sundress and a cowrie necklace. The sea rolls in '
        'low with a lace of foam and the gold light shifts on the surface.',
        'An enormous humpback whale high above a dark island, coming apart from the tail forward into '
        'drifting motes of silver and violet light that rise among the stars, her head still solid '
        'and her long fins still glowing cosmic purple. On the pale beach far below, Anna — a girl '
        'with chocolate-brown skin and long black hair in a floral sundress — stands alone looking '
        'up, with a low swell running up the sand.',
        'The open sea at first light seen from a low rocky shore, with nobody in the picture. The sun '
        'sits just above the horizon laying a road of gold across the water, and the sea runs in '
        'bands of deep blue, jade and turquoise with a long swell rolling through it and small waves '
        'breaking white over the rocks in the foreground. Out in the middle distance a soft '
        'violet-purple glow shows under the surface, diffuse and low, as though something luminous '
        'were passing below.',
        'An enormous humpback whale in deep blue water offshore, seen from an empty pale beach. Her '
        'broad dark back and knobbly head are clear of the surface and one long pectoral fin is '
        'raised high out of the water with water streaming off it, its edge glowing cosmic purple and '
        'scattered with points of starlight. A low green cay lies on the horizon behind her, small '
        'against her. Calm water with a long swell, and small waves running up the sand in a lace of '
        'foam.'],
  collage='gds/girl-whale/collage-one-story-four-pictures-20261127',
  alt='Four pictures from the world of The Girl and The Whale: Anna dancing on a reef flat at '
      'sunset, an enormous cosmic whale breaking apart into stardust above a dark island while Anna '
      'watches from the beach, the open sea at first light with a violet glow under the surface, and '
      'the whale offshore with one long glowing fin raised out of the water.',
  fb=tail("If you are buying books for a child this weekend, here is what is actually inside this "
    "one.\n\nThe Girl and The Whale was written by Zhané Mackey and is published from Nassau by "
    "GDS Publications. It is a story about Anna and the Cosmic Theseus Finback — the largest "
    "humpback in the world, whose fins glowed a cosmic purple and shone brighter than all the "
    "stars in the sky combined, and who took a comet strike to save every sea "
    "creature.\n\nMr. Hooker tells Anna the legend. What she does with it is the book.\n\nNo sale, "
    "no code, no countdown — we would just rather you knew what was in it before you chose. What "
    "a child gets is a Bahamian-published story with a Bahamian author's name on the cover, and "
    "a whale worth being frightened of and glad about at the same "
    "time.\n\nSwipe for four pictures of that world. These are our illustrations of moments from "
    "the story, not pages from the book.\n\nGDS Reading Series, Level 3. Ages 6 to 12, grades 1 "
    "to 6.\n\nReader: " + GW + "\nActivity book: " + GWA),
  ig=tail("Buying books for a child this weekend? Here's what's actually inside this one. "
    "🐋✨\n\nThe Girl and The Whale was written by Zhané Mackey and published from Nassau by GDS "
    "Publications. Anna, and the Cosmic Theseus Finback — the largest humpback in the world, her "
    "fins glowing cosmic purple and shining brighter than all the stars in the sky combined, who "
    "took a comet strike to save every sea creature.\n\nMr. Hooker tells Anna the legend. What "
    "she does with it is the book.\n\nNo sale, no code, no countdown — we'd just rather you knew "
    "what was in it before you chose. What a child gets is a Bahamian-published story with a "
    "Bahamian author's name on the cover.\n\nSwipe for four pictures of that "
    "world — our illustrations of moments from the story, not pages from the book.\n\nAges "
    "6–12.\n\nReader: " + GW + "\nActivity book: " + GWA,
    "#TheGirlAndTheWhale #BahamianAuthors #ChildrensBooks #GiftIdeas #IslandStory #Humpback "
    "#GDSPublications"),
  pin_t='What is actually inside this one',
  pin=tail("The Girl and The Whale, written by Zhané Mackey and published from Nassau by GDS "
    "Publications: Anna, and the Cosmic Theseus Finback — the largest humpback in the world, her "
    "fins glowing cosmic purple and brighter than all the stars combined, who took a comet strike "
    "to save every sea creature. Our illustrations of moments from the story, not pages from the "
    "book. Ages 6 to 12.\n\n" + GW),
  pin_url=GW),

 # Sat 28 Nov — slot 127 — pillar 1 Behind the Scenes — ATB Lower — HERO (new)
 dict(day='2026-11-28', base=14, pid='gds/atb-lower/the-same-page-in-both-books-20261128',
  pad=False, board=B_CULT, anna_absent=True,
  alt='Two paperback colouring books lying open side by side on a wooden table, seen from above, '
      'both open at the same line drawing — a flamingo standing in shallow water among sea grape '
      'leaves, in clean black outline on white. One book is a little larger than the other; both '
      'covers are plain. An open tin of crayons, a pink crayon, three coloured pencils and a shell '
      'lie around them, with warm afternoon light falling across the table.',
  fb=tail("People ask us which All Things Bahamian to buy, and the honest answer starts with "
    "something that surprises them: the drawings are the same in both.\n\nThe Upper and Lower "
    "editions share their artwork. Same flamingo, same fort, same Junkanoo rush — different page "
    "numbers, because the books are different lengths.\n\nWhat differs is the written work "
    "around the pictures.\n\nUpper adds Key Settlements and Communities, five named communities "
    "per island with a line each, and EXPLORE MORE! pages of three written-response questions. "
    "Lower adds a Colouring Tips page and simpler design activities — Design Your Own Junkanoo "
    "Costume is one.\n\nSo it is not a question of which book has the better pictures. It is a "
    "question of how much writing you want a child doing beside them.\n\nUpper: 109 pages, ages "
    "9 to 12, grades 4 to 6.\nLower: 83 pages, ages 5 to 9, grades 1 to 3.\n\nAbove is our "
    "illustration of the two books open at the same page, not a photograph of them.\n\nLower: "
    + ATBL + "\nUpper: " + ATBU),
  ig=tail("People ask which All Things Bahamian to buy, and the honest answer starts with "
    "something that surprises them: the drawings are the same in both. 🦩\n\nUpper and Lower share "
    "their artwork. Same flamingo, same fort, same Junkanoo rush — different page numbers, "
    "because the books are different lengths.\n\nWhat differs is the written work around the "
    "pictures.\n\nUpper adds Key Settlements and Communities — five named communities per island "
    "with a line each — and EXPLORE MORE! pages of three written-response questions. Lower adds a "
    "Colouring Tips page and simpler design activities, like Design Your Own Junkanoo "
    "Costume.\n\nSo it isn't which book has the better pictures. It's how much writing you want a "
    "child doing beside them.\n\nUpper: 109 pages, ages 9–12. Lower: 83 pages, ages "
    "5–9.\n\nOur illustration of the two books, not a photograph.\n\nLower: " + ATBL + "\nUpper: "
    + ATBU,
    "#AllThingsBahamian #Bahamas #ColouringBook #BehindTheScenes #Teachers #BahamianKids "
    "#GDSPublications"),
  pin_t='The drawings are the same in both',
  pin=tail("The Upper and Lower editions of All Things Bahamian share their artwork — same "
    "drawings, different page numbers. What differs is the written work: Upper adds Key "
    "Settlements and Communities and EXPLORE MORE! questions; Lower adds Colouring Tips and "
    "simpler design activities. Upper 109 pages, ages 9 to 12. Lower 83 pages, ages 5 to 9. Our "
    "illustration, not a photograph.\n\n" + ATBL),
  pin_url=ATBL),

 # Sat 28 Nov — slot 128 — pillar 2 Reader Engagement — Regatta Activity Book — HERO (catalogued)
 dict(day='2026-11-28', base=19, pid='gds/regatta-activity/a-future-blue-hole-adventure-20261106',
  pad=False, board=B_LI, anna_absent=True,
  alt='Dean\'s Blue Hole on Long Island seen from the rock above: a near-circular pool of deep navy '
      'water set into pale turquoise shallows, a tall limestone cliff curving round one side and a '
      'crescent of white sand on the other. In the foreground a snorkel mask, swim fins and a '
      'closed notebook with a pencil across it, laid out and waiting, with nobody there yet. The '
      'shallows move gently while the deep blue circle stays calm.',
  fb=tail("The family in this book never got to Dean's Blue Hole.\n\nFive days on Long Island, and "
    "the second deepest blue hole in the world was the one thing they did not reach. A true "
    "account has to say so, and Going To The Regatta does.\n\nWhat the reader does next is the "
    "interesting part: it sends you to the activity book to imagine what Nicholas \"might notice, "
    "learn, and remember when he finally gets there\".\n\nThat is the page called A Future Dean's "
    "Blue Hole Adventure, and it is a blank one.\n\nSo we will ask you the same thing. If you "
    "were standing on that rock tomorrow morning with a mask and a notebook — what would you want "
    "to see?\n\nTell us below. We will read them.\n\nAbove is our illustration of the blue hole "
    "waiting, not a page from the book.\n\n40 pages, ages 6 to 12, grades 1 to 6.\n\nActivity "
    "book: " + REGA + "\nReader: " + REG),
  ig=tail("The family in this book never got to Dean's Blue Hole. 🌊\n\nFive days on Long Island, "
    "and the second deepest blue hole in the world was the one thing they didn't reach. A true "
    "account has to say so, and Going To The Regatta does.\n\nWhat the reader does next is the "
    "interesting part: it sends you to the activity book to imagine what Nicholas \"might notice, "
    "learn, and remember when he finally gets there\".\n\nThat's the page called A Future Dean's "
    "Blue Hole Adventure — and it's a blank one.\n\nSo, same question to you. If you were "
    "standing on that rock tomorrow morning with a mask and a notebook, what would you want to "
    "see? 👇\n\nOur illustration of the blue hole waiting, not a page from the book.\n\n40 pages, "
    "ages 6–12.\n\nActivity book: " + REGA + "\nReader: " + REG,
    "#GoingToTheRegatta #DeansBlueHole #LongIsland #Bahamas #ActivityBook #KidsWriting "
    "#GDSPublications"),
  pin_t='The one place they never reached',
  pin=tail("Five days on Long Island, and the second deepest blue hole in the world was the one "
    "thing the family never reached. Going To The Regatta says so, then sends readers to the "
    "activity book to imagine what Nicholas \"might notice, learn, and remember when he finally "
    "gets there\". That page is a blank one. Our illustration, not a page from the book.\n\n"
    + REGA),
  pin_url=REGA),

 # Sun 29 Nov — slot 129 — pillar 3 Promo/CTA — Girl & Whale Activity Book — COLLAGE
 dict(day='2026-11-29', base=14, board=B_COLOR, pad=False, anna_absent=True,
  panels=['gds/girl-whale-activity/coral-reef-i-spy-20261017',
          'gds/girl-whale-activity/design-annas-dress-20261021',
          'gds/girl-whale-activity/a-childs-cosmic-finback-20261129',
          'gds/girl-whale-activity/the-worn-down-pencils-20261129'],
  alts=['A bright coral reef underwater: shells, orange starfish, small striped fish, two crabs among '
        'the rocks and two green sea turtles gliding, with a small leather-bound book resting half '
        'hidden on the sand. Sunlight flickers down in slow shifting bands.',
        'A worktable seen from above with four sheets of cream paper, each carrying a hand-drawn '
        'dress design coloured differently — one patterned with hibiscus flowers, one with small '
        'shells around the hem, one with a sweep of stars, one left as a plain outline — with a jar '
        'of coloured pencils, loose pencils, scraps of bright fabric and ribbon and a dish of shells '
        'around them. Through a window behind, calm turquoise sea moves gently under palms.',
        'A child\'s own wax-crayon drawing taped up crooked on a pale wall: a big purple whale with '
        'long fins, drawn in bold waxy strokes with the paper showing through, surrounded by yellow '
        'stars and blue scribbled water. Two smaller crayon drawings are taped below it, one of a sun '
        'and flowers and one of a rainbow. A corner of a wooden shelf with building blocks and a soft '
        'toy shows at the bottom, in soft daylight.',
        'An open blue tin of coloured pencils on a wooden table after a long afternoon\'s colouring, '
        'most of them worn down short and blunt and two still sharp. A metal sharpener and a small '
        'heap of curled shavings lie beside the tin, a sheet of paper rests face down nearby so only '
        'its blank back shows, and a conch shell sits at the edge of the table. Warm low light comes '
        'through a window behind.'],
  collage='gds/girl-whale-activity/collage-forty-pages-of-work-20261129',
  alt='Four scenes from the Girl and The Whale activity book: a crowded coral reef to search, four '
      'hand-coloured dress designs laid out on a worktable, a child\'s own crayon drawing of a '
      'purple whale taped up on a wall, and a tin of coloured pencils worn down short after a long '
      'afternoon.',
  fb=tail("Forty pages, and five of them are colouring pages.\n\nThat is the thing we would want a "
    "parent to know about The Girl and The Whale Coloring & Activity Book before buying it. The "
    "five are Anna Hears a Song, A Story at the Docks, The Dance at Sunset, The Legend Appears "
    "and Anna's Cosmic Ride. The rest of the book asks for something else.\n\nSome of it is "
    "looking: Coral Reef I-Spy asks for six shells, five starfish, four fish, three crabs, two "
    "sea turtles and one tiny legend book. Some of it is designing: Design Anna's Celebration "
    "Dress, Design Your Own Cosmic Finback. Some of it is writing: Create Your Own Island Legend, "
    "Believe Acrostic, Postcard from Hawaii. Some of it is learning a real animal properly — "
    "Label the Humpback Whale teaches that humpbacks are mammals and not fish, that they breathe "
    "through a blowhole and not gills, and that the tail is called a fluke.\n\nAnd then there is "
    "Crack the Cosmic Code, where the answer is BELIEVE IN WONDER.\n\nSwipe for four of ours. "
    "These are our illustrations of what the activities produce, not pages from the book.\n\n40 "
    "pages, ages 6 to 12, grades 1 to 6.\n\nActivity book: " + GWA + "\nReader: " + GW),
  ig=tail("Forty pages, and five of them are colouring pages. 🖍️\n\nThat's what we'd want a parent "
    "to know about The Girl and The Whale Coloring & Activity Book. The five: Anna Hears a Song, "
    "A Story at the Docks, The Dance at Sunset, The Legend Appears, Anna's Cosmic Ride. The rest "
    "of the book asks for something else.\n\nLooking: Coral Reef I-Spy wants six shells, five "
    "starfish, four fish, three crabs, two sea turtles and one tiny legend book. Designing: "
    "Design Anna's Celebration Dress, Design Your Own Cosmic Finback. Writing: Create Your Own "
    "Island Legend, Believe Acrostic, Postcard from Hawaii. Learning a real animal properly: "
    "Label the Humpback Whale — mammals not fish, a blowhole not gills, the tail is a "
    "fluke.\n\nAnd Crack the Cosmic Code, where the answer is BELIEVE IN WONDER.\n\nSwipe for "
    "four of ours — our illustrations of what the activities produce, not pages from the "
    "book.\n\n40 pages, ages 6–12.\n\nActivity book: " + GWA + "\nReader: " + GW,
    "#TheGirlAndTheWhale #ActivityBook #ColouringBook #KidsLearning #GiftIdeas #BahamianAuthors "
    "#GDSPublications"),
  pin_t='Forty pages, five of them colouring',
  pin=tail("The Girl and The Whale Coloring & Activity Book has five colouring pages. The rest of "
    "the book asks for something else: Coral Reef I-Spy, Design Anna's Celebration Dress, "
    "Create Your Own Island Legend, Label the Humpback Whale, Crack the Cosmic Code. Our "
    "illustrations of what the activities produce, not pages from the book. 40 pages, ages 6 to "
    "12.\n\n" + GWA),
  pin_url=GWA),
]

if __name__ == '__main__':
    run(S)
