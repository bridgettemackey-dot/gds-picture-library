# -*- coding: utf-8 -*-
"""Week 52: Thu 29 Oct - Sun 1 Nov 2026. Six slots over four days.
TWO COLLAGE DAYS: Thu 29 (Book World) and Sun 1 Nov 14:00 (Activity Spotlight).

Book World is the pillar about the world of the book, and the thread this one
takes - the family around Anna rather than the whale - only exists across several
moments. Activity Spotlight is the standing case: a forty page activity book is
more than colouring and it takes more than one page to show that. The other four
slots are single heroes, each with one thing to look at and one thought.
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
 # Thu 29 Oct — slot 84 — pillar 0 Book World — The Girl and The Whale — COLLAGE
 dict(day='2026-10-29', base=14, board=B_READ, pad=False,
  panels=['gds/girl-whale/mr-hooker-tells-the-legend-20260925',
          'gds/girl-whale/gran-gran-covers-for-anna-20261029',
          'gds/girl-whale/turning-into-stardust-20261029',
          'gds/girl-whale/under-the-stars-20261024'],
  alts=["An older fisherman in a straw hat and faded blue floral shirt sits on the edge of a weathered wooden dock at sunset, one hand raised mid-story. Beside him a coil of rope, a folded green net and a battered tackle box; a small boat is tied below. Green volcanic mountains and a low golden sun behind.",
        'A kitchen in a small island house in the evening. Anna, a girl of about thirteen with '
        'chocolate-brown skin and long black hair in a hibiscus-print sundress, stands in the '
        'doorway with her hands behind her back. Her mother stands with a hand on her hip, and at '
        'the table her grandmother looks up mid-sentence with an easy smile and a raised hand, a '
        'large silvery-green mahi-mahi on a board in front of her. Warm lamplight.',
        'An enormous humpback whale high above a dark island, coming apart from the tail forward '
        'into drifting motes of silver and violet light that rise among the stars, her head still '
        'solid and her long fins still glowing cosmic purple. On the pale beach far below, Anna — a '
        'girl with chocolate-brown skin and long black hair in a floral sundress — stands alone '
        'looking up, with a low swell running up the sand.',
        "Anna, a girl of about thirteen with chocolate-brown skin and long black hair, sitting close on the sand at night between her mother and her grandmother, all three seen from behind and looking up at a sky full of stars, one arm around her shoulders. Beyond them the dark sea moves gently, small waves running up the sand in a thin lace of pale foam, with green mountains behind."],
  collage='gds/girl-whale/collage-the-people-around-her-20261029',
  alt='A four-panel collage from The Girl and The Whale: Mr. Hooker telling the legend on the dock, '
      'Gran Gran covering for Anna in the kitchen, the whale turning into stardust above the island, '
      'and Anna sitting with her mother and grandmother under the stars.',
  fb=tail("The whale gets the cover. The people get the story.\n\nIt is easy to read The Girl and "
    "The Whale as a book about a whale. Look at who is actually in it.\n\nMr. Hooker, one of the "
    "greatest fishermen in Hawaii, who knows many island stories — he is the one who tells Anna the "
    "legend and puts Hawaii's Book of Legends in her hands.\n\nGran Gran, who covers for Anna with "
    "the mahi-mahi story when Kelani asks where she has been. \"You do not think anything is real,\" "
    "she tells her own daughter.\n\nKelani, who does not believe any of it, and who shouts Anna "
    "Lelani Mahoe — the full name, the one used when Anna is in trouble.\n\nAnd at the end, after "
    "the Cosmic Theseus Finback has turned into stardust and floated into the sky, the three of them "
    "sitting on the sand looking up.\n\nAnna wanted her mother to be proud of her. That is the "
    "engine of the whole book.\n\nThese are our illustrations of four moments from the story, not "
    "pages from the book.\n\nBy Zhané Mackey. GDS Reading Series, Level 3. Ages 6 to 12, grades 1 "
    "to 6.\n\n" + GW),
  ig=tail("The whale gets the cover. The people get the story. 💜\n\nMr. Hooker, one of the greatest "
    "fishermen in Hawaii, who tells Anna the legend and hands her the book.\n\nGran Gran, who covers "
    "for her with the mahi-mahi story. \"You do not think anything is real,\" she tells her own "
    "daughter.\n\nKelani, who believes none of it, and who shouts Anna Lelani Mahoe — the full name, "
    "the one used when she's in trouble.\n\nAnd at the end, after the whale turns to stardust, the "
    "three of them on the sand looking up.\n\nAnna wanted her mother to be proud of her. That's the "
    "engine of the whole book.\n\nSwipe for all four — our illustrations of the story, not pages "
    "from the book.\n\nBy Zhané Mackey. Ages 6–12, grades 1–6.\n\n" + GW,
    "#TheGirlAndTheWhale #BahamianAuthors #ChildrensBooks #ReadingSeries #FamilyStories "
    "#GDSPublications #BelieveInWonder"),
  pin_t='The whale gets the cover — the people get the story',
  pin=tail("Mr. Hooker telling the legend, Gran Gran covering for Anna with the mahi-mahi story, the "
    "Cosmic Theseus Finback turning into stardust, and Anna with her mother and grandmother under "
    "the stars. Our illustrations of four moments from The Girl and The Whale, not pages from the "
    "book. By Zhané Mackey. Ages 6 to 12, grades 1 to 6.\n\n" + GW),
  pin_url=GW),

 # Fri 30 Oct — slot 85 — pillar 1 Behind the Scenes — ATB Upper — NEW ART
 dict(day='2026-10-30', base=14, pid='gds/atb-upper/section-opener-thumbnails-20261030',
  pad=False, board=B_CULT,
  alt='A designer\'s desk where a book\'s section opener is being planned, seen from above. Four '
      'small square thumbnail sketches — a conch, a sea turtle, a reef fish and a ray — are pinned '
      'in a row on a cork board at the back. On the desk a larger cream sheet with an empty '
      'rectangle ruled on it, a ruler, a pencil, a kneaded eraser and a jar of coloured pencils.',
  fb=tail("Every section of All Things Bahamian opens the same way, and it is a deliberate "
    "choice.\n\nA section opener shows four thumbnails of that section's artwork, with an ABOUT "
    "THIS SECTION box beside them. Four small pictures and a short paragraph, before a single "
    "colouring page.\n\nIt is there so a child knows where they are. Life in Our Bahamian Seas runs "
    "from page 60 to 75 in the Upper edition — reefs, conch, turtles, sharks, fish. Opening it with "
    "four small drawings tells them what the next sixteen pages are about before they start, which "
    "is the same thing a good chapter heading does.\n\nSeven sections, seven openers: National "
    "Symbols, Our Beautiful Islands, Historic Places and Landmarks, Life in Our Bahamian Seas, "
    "Junkanoo, Fruits of The Bahamas, My Bahamas.\n\nAbove is our illustration of that planning "
    "stage, not a page from the book.\n\nAll Things Bahamian: Upper Elementary. Ages 9 to 12, "
    "grades 4 to 6. 109 pages.\n\n" + ATBU),
  ig=tail("Every section of All Things Bahamian opens the same way, and it's deliberate. 📐\n\nA "
    "section opener shows four thumbnails of that section's artwork with an ABOUT THIS SECTION box "
    "beside them. Four small pictures and a short paragraph, before a single colouring "
    "page.\n\nIt's there so a child knows where they are. Life in Our Bahamian Seas runs pages "
    "60–75 in the Upper edition — reefs, conch, turtles, sharks, fish. Four small drawings tell "
    "them what's coming before they start.\n\nSeven sections, seven openers.\n\nOur illustration of "
    "that planning stage, not a page from the book.\n\nAges 9–12, grades 4–6, 109 pages.\n\n" + ATBU,
    "#AllThingsBahamian #BehindTheScenes #BookDesign #Bahamas #ColouringBook #GDSPublications "
    "#HomeschoolBahamas"),
  pin_t='Why every section opens with four small pictures',
  pin=tail("A section opener in All Things Bahamian shows four thumbnails of that section's artwork "
    "with an ABOUT THIS SECTION box beside them — so a child knows where they are before they "
    "start. Seven sections, seven openers. Our illustration of that planning stage, not a page from "
    "the book. Upper Elementary, ages 9 to 12, 109 pages.\n\n" + ATBU),
  pin_url=ATBU),

 # Fri 30 Oct — slot 86 — pillar 2 Reader Engagement — Going To The Regatta — NEW ART
 dict(day='2026-10-30', base=19, pid='gds/regatta/stella-maris-airport-20261030',
  pad=False, board=B_LI,
  alt='A tiny Bahamian island airstrip on the morning a family flies home: a small single-storey '
      'terminal with a shaded porch and louvred windows, a low fence, and a small twin-propeller '
      'plane waiting on the apron. Travellers with bags and a cooler stand in the shade saying '
      'goodbye, two women hugging, a boy with a backpack almost as big as he is. Turquoise sea past '
      'the end of the runway, a low swell rolling in.',
  fb=tail("The last page of the trip is the hardest one.\n\nGoing To The Regatta ends on the "
    "Monday, flying home from Stella Maris airport — the only one operating, because Deadman's Cay "
    "airport was being renovated.\n\nThat is all the summary I have of it. But anyone who has left an island after a week with family knows what that morning "
    "actually is: the bags by the door, the last look at the water, the aunt who walks you all the "
    "way to the fence.\n\nThe book is a true family account by Bridgette Skeete-Mackey, so it keeps "
    "the small true things — the fuel gauge on one bar after midnight, the empty pan at breakfast, "
    "which airport was open.\n\nWhat does leaving look like in your family? Tell us below.\n\nThis "
    "is our illustration; the book itself carries the photographs.\n\nGDS Reading Series, Family "
    "Reader, ages 5 to 15.\n\n" + REG),
  ig=tail("The last page of the trip is the hardest one. ✈️\n\nGoing To The Regatta ends on the "
    "Monday, flying home from Stella Maris airport — the only one operating, because Deadman's Cay "
    "was being renovated.\n\nThat's all the summary I have of it. But anyone who's left an island after a week with family knows what that morning is: the bags by "
    "the door, the last look at the water, the aunt who walks you to the fence.\n\nIt's a true "
    "family account, so it keeps the small true things — the fuel gauge on one bar after midnight, "
    "the empty pan at breakfast, which airport was open.\n\nWhat does leaving look like in your "
    "family? 👇\n\nOur illustration; the book carries the photographs.\n\nFamily Reader, ages "
    "5–15.\n\n" + REG,
    "#GoingToTheRegatta #LongIsland #Bahamas #FamilyStories #IslandLife #BahamianAuthors "
    "#GDSPublications"),
  pin_t='The last page of the trip is the hardest one',
  pin=tail("Going To The Regatta ends flying home from Stella Maris airport — the only one "
    "operating, because Deadman's Cay was being renovated. Anyone who has left an island after a week "
    "with family knows what that morning is. A true family account by "
    "Bridgette Skeete-Mackey. Family Reader, ages 5 to 15.\n\n" + REG),
  pin_url=REG),

 # Sat 31 Oct — slot 87 — pillar 3 Promo/CTA — Girl & Whale activity book — NEW ART
 dict(day='2026-10-31', base=14, pid='gds/girl-whale-activity/draw-the-family-under-the-stars-20261031',
  pad=False, board=B_COLOR,
  # 'Draw the Family Under the Stars' is an activity title; the drawing is a child's own family.
  anna_absent=True,
  alt='A child\'s finished crayon drawing lying on a wooden desk: three figures seen from behind '
      'sitting close together on a beach at night — a tall one, a small one in the middle and a '
      'grandmotherly one — under a sky scribbled deep blue and covered in yellow stars, with a '
      'crayoned sea behind them. A jar of crayons, three loose crayons, a soft eraser and a small '
      'shell around the sheet, in warm lamplight.',
  fb=tail("The book ends with three people on the sand looking up. Then it asks the child to draw "
    "their own.\n\nDraw the Family Under the Stars is one of the forty pages in The Girl and The "
    "Whale Coloring & Activity Book, and it is the one that turns the story outward. Anna's night "
    "ends with her mother and her grandmother beside her. The page asks who would be beside "
    "you.\n\nAbove is a child's answer, not Anna's family.\n\nThe book also holds Coral Reef "
    "I-Spy, Crack the Cosmic Code, Label the Humpback Whale, Design Your Own Cosmic Finback, Create "
    "Anna's Island Route, Anna's Feelings, Legend and Reality sorting, Create Your Own Island "
    "Legend, Postcard from Hawaii, Cosmic Bookmarks and a certificate — plus five colouring pages: "
    "Anna Hears a Song, A Story at the Docks, The Dance at Sunset, The Legend Appears and Anna's "
    "Cosmic Ride.\n\nRead the story first. The book works better that way round.\n\n40 pages, ages "
    "6 to 12.\n\nReader: " + GW + "\nActivity book: " + GWA),
  ig=tail("The book ends with three people on the sand looking up. Then it asks the child to draw "
    "their own. ⭐\n\nDraw the Family Under the Stars is the page that turns the story outward. "
    "Anna's night ends with her mother and grandmother beside her. The page asks who'd be beside "
    "you.\n\nAbove is a child's answer — not Anna's family.\n\nAlso inside: Coral Reef I-Spy, Crack "
    "the Cosmic Code, Design Your Own Cosmic Finback, Anna's Feelings, Legend and Reality sorting, "
    "Create Your Own Island Legend, Cosmic Bookmarks, a certificate, and five colouring "
    "pages.\n\nRead the story first 📖\n\n40 pages, ages 6–12.\n\nReader: " + GW +
    "\nActivity book: " + GWA,
    "#TheGirlAndTheWhale #ActivityBook #KidsActivities #ColouringBook #FamilyStories "
    "#BahamianAuthors #GDSPublications"),
  pin_t='Draw the Family Under the Stars',
  pin=tail("The story ends with Anna, her mother and her grandmother on the sand looking up. Then "
    "the activity book asks the child who would be beside them. One of forty pages in The Girl and "
    "The Whale Coloring & Activity Book. Ages 6 to 12.\n\nReader: " + GW + "\nActivity book: " + GWA),
  pin_url=GWA),

 # Sun 1 Nov — slot 88 — pillar 4 Activity Spotlight — Regatta activity book — COLLAGE
 dict(day='2026-11-01', base=14, board=B_COLOR, pad=False,
  panels=['gds/regatta-activity/nature-pool-observer-20261018',
          'gds/regatta-activity/family-connections-page-20261101',
          'gds/regatta-activity/island-food-scramble-20261101',
          'gds/regatta-activity/deans-blue-hole-20261014'],
  alts=["A clear natural rock pool on the Long Island shore, with pale sand and stones on the bottom, a few tiny fish, a small crab and green weed moving slowly. Fine ripple rings spread across the surface. An open blank notebook with a pencil and a magnifying glass rest on the rock at the near edge.",
        'A worktable seen from above where a family tree is being made: a large cream sheet with '
        'blank oval and rectangular frames joined by hand-drawn branching lines, every frame still '
        'empty, with small blank cards cut ready to stick in, a glue stick, scissors, a pencil, a '
        'jar of coloured pencils and a shell holding one corner down.',
        'Five Bahamian foods laid out apart from each other on a scrubbed wooden table, each on its '
        'own small square of cream paper: a whole silver fish on a board, a green coconut cut open '
        'at the top, a few pears, a bowl of white rice and a bowl of pigeon peas, with a pencil and '
        'a jar of coloured pencils at one edge under dappled light.',
        "Dean’s Blue Hole on Long Island, a deep dark circle of water ringed by pale turquoise shallows and a curve of white sand, with a low swell rolling in, small waves running up the sand in a thin lace of foam and ripple lines crossing the shallows."],
  collage='gds/regatta-activity/collage-not-a-quiz-20261101',
  alt='A four-panel collage from the Going To The Regatta Coloring & Activity Book: a clear rock '
      'pool to sit and watch, a blank family tree waiting to be filled in, five Bahamian foods laid '
      'out as a puzzle, and Dean\'s Blue Hole.',
  fb=tail("Four pages, and three of them have no right answer at all.\n\nNature Pool "
    "Observer sends a child to sit beside water and write down what is actually there.\n\nMy Family "
    "Connections gives them an empty tree and asks who goes in it. Family Roots and Roles sits "
    "beside it.\n\nIsland Food Scramble works with fish, coconut, pears, rice and peas — the food "
    "that was actually on the table.\n\nAnd A Future Dean's Blue Hole Adventure asks them to "
    "imagine a place the family never reached. That is the book's own cross-sell: the reader sends "
    "readers here to imagine what Nicholas might notice, learn and remember when he finally gets "
    "there.\n\nAlso inside: Parts of a C1 Racing Sloop, Decorate the C1 Mainsail, Nicholas's Long "
    "Island Route, Regatta I-Spy, Design a Regatta Flag, Island Compass Challenge, Plan an Island "
    "Meal, a postcard, an acrostic, bookmarks and a certificate — plus four colouring pages.\n\n"
    "These are our illustrations of what those pages are about; in the book each is a line drawing "
    "waiting for pencils.\n\n40 pages, ages 6 to 12, grades 1 to 6.\n\nReader: " + REG +
    "\nActivity book: " + REGA),
  ig=tail("Four pages, and three of them have no right answer at all. 🔍\n\nNature Pool "
    "Observer sends a child to sit beside water and write down what's actually there.\n\nMy Family "
    "Connections gives them an empty tree and asks who goes in it.\n\nIsland Food Scramble works "
    "with fish, coconut, pears, rice and peas — the food that was actually on the table.\n\nAnd A "
    "Future Dean's Blue Hole Adventure asks them to imagine a place the family never reached. "
    "That's the book's own cross-sell.\n\nAlso inside: Parts of a C1 Racing Sloop, Decorate the C1 "
    "Mainsail, Regatta I-Spy, Design a Regatta Flag, Plan an Island Meal, and four colouring "
    "pages.\n\nSwipe for all four — our illustrations of what the pages are about.\n\n40 pages, "
    "ages 6–12.\n\nReader: " + REG + "\nActivity book: " + REGA,
    "#GoingToTheRegatta #ActivityBook #TeacherResources #Bahamas #LongIsland #KidsActivities "
    "#GDSPublications"),
  pin_t='Four pages from the activity book',
  pin=tail("Nature Pool Observer, My Family Connections, Island Food Scramble and A Future Dean's "
    "Blue Hole Adventure — four of the forty pages in the Going To The Regatta Coloring & Activity "
    "Book. Our illustrations of what those pages are about; in the book each is a line drawing "
    "waiting for pencils. Ages 6 to 12.\n\nReader: " + REG + "\nActivity book: " + REGA),
  pin_url=REGA),

 # Sun 1 Nov — slot 89 — pillar 5 Bahamian Culture — ATB Lower — NEW ART
 dict(day='2026-11-01', base=19, pid='gds/atb-lower/fruits-opener-basket-20261101',
  pad=False, board=B_CULT,
  alt='Two Bahamian children standing behind a big woven basket piled with fruit, smiling and '
      'holding up a mango, a pineapple, a soursop, a halved coconut, a sugar apple and a bunch of '
      'grapes. They stand on a shaded porch with bougainvillea along the rail, with a glimpse of '
      'turquoise sea beyond where a low swell rolls in.',
  fb=tail("A whole section about fruit, and it is not really about fruit.\n\nThe Fruits of The "
    "Bahamas is the sixth of the seven sections in All Things Bahamian. It runs from page 64 to 79 "
    "in the Lower edition, and what it teaches is where each fruit grows and when it is in "
    "season.\n\nSo the Eleuthera pineapple page does not just show a pineapple. It says Eleuthera "
    "is famous for its sweet Sugar Loaf pineapples, that they grow in sunny rocky red-soil fields, "
    "and that the season is late spring to early summer.\n\nThat is geography and agriculture "
    "arriving through a colouring page, which is the whole trick of the book.\n\nThe Upper edition "
    "pushes it further with EXPLORE MORE questions — \"Explain how rainfall, soil and island "
    "location might affect a fruit harvest.\"\n\nThis is our illustration of the section's opening "
    "subject; in the book it is a line drawing waiting for pencils.\n\nAll Things Bahamian, Lower "
    "Elementary. Ages 5 to 9, grades 1 to 3. 83 pages.\n\n" + ATBL),
  ig=tail("A whole section about fruit, and it's not really about fruit. 🍍\n\nThe Fruits of The "
    "Bahamas is the sixth of seven sections, pages 64–79 in the Lower edition, and what it teaches "
    "is where each fruit grows and when it's in season.\n\nSo the Eleuthera pineapple page doesn't "
    "just show a pineapple. It says Eleuthera is famous for its sweet Sugar Loaf pineapples, that "
    "they grow in sunny rocky red-soil fields, and that the season is late spring to early "
    "summer.\n\nGeography and agriculture arriving through a colouring page. That's the whole trick "
    "of the book.\n\nOur illustration of the section's opening subject — in the book it's a line "
    "drawing waiting for pencils.\n\nAges 5–9, grades 1–3, 83 pages.\n\n" + ATBL,
    "#AllThingsBahamian #BahamianCulture #Bahamas #ColouringBook #BahamianKids #Eleuthera "
    "#GDSPublications"),
  pin_t='A whole section about fruit — and not really about fruit',
  pin=tail("The Fruits of The Bahamas is the sixth of the seven sections in All Things Bahamian, "
    "pages 64 to 79 in the Lower edition, and it teaches where each fruit grows and when it is in "
    "season. Our illustration of the section's opening subject; in the book it is a line drawing "
    "waiting for pencils. Ages 5 to 9, grades 1 to 3, 83 pages.\n\n" + ATBL),
  pin_url=ATBL),
]

if __name__ == '__main__':
    run(S)
