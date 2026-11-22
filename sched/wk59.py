# -*- coding: utf-8 -*-
"""Week 59: Mon 23 - Wed 25 Nov 2026. Four slots over three days.
TWO COLLAGE DAYS: Tue 24 (Promo/CTA) and Wed 25 (Activity Spotlight).

Promo/CTA takes one because the argument for All Things Bahamian is breadth -
seven sections, and a single picture only ever shows one of them. Activity
Spotlight takes the other because the point being made is that the Regatta
activity book is not only a colouring book, and "not only" needs more than one
example in view.

Four slots, so not all six books fit. The two readers sat out; both ran last week.

Mon 23 posts an ACTUAL PAGE from All Things Bahamian - rare, and the Behind the
Scenes slot is the right place to say so. pad=True: it is line art.

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
 # Mon 23 Nov — slot 120 — pillar 1 Behind the Scenes — ATB Upper — HERO (real book page)
 dict(day='2026-11-23', base=14, pid='gds/atb-upper/page-junkanoo-rush-rgb-20260915',
  pad=True, board=B_CULT, anna_absent=True,
  alt='A colouring page: a Junkanoo rush out on Bay Street, Nassau, with drummers and a feathered '
      'costume.',
  fb=tail("Almost everything we post is our own illustration. This one is not. This is an actual "
    "page out of the book, and getting it onto a screen took more work than drawing a new "
    "picture would have.\n\nA flat scan of a colouring page looks fine on paper and poor "
    "everywhere else. The line goes soft, the whites go grey, and what was a crisp outline a "
    "child could colour inside becomes a smudge.\n\nSo this one is not a scan. It is rendered "
    "straight out of the book's own file at 220 dots per inch, which is why the drum rims and "
    "the feather edges still have an edge on them.\n\nThe honest part: two of our older page "
    "images are still upscaled scans, because we do not hold a page file for those two books. "
    "We know which ones they are and we would like to fix them.\n\nThe page is the Boxing Day "
    "Junkanoo Parade — page 86 in the Upper edition, page 63 in the Lower. The book's own line "
    "is that Junkanoo fills Bay Street with music, movement and colour.\n\nJunkanoo: Music, "
    "Movement and Mas runs pages 76 to 87 in the Upper edition.\n\nAll Things Bahamian, Upper "
    "Elementary. Ages 9 to 12, grades 4 to 6. 109 pages.\n\n" + ATBU),
  ig=tail("Almost everything we post is our own illustration. This one isn't — this is an actual "
    "page out of the book. 🥁\n\nAnd getting it onto a screen took more work than drawing "
    "something new would have.\n\nA flat scan of a colouring page looks fine on paper and poor "
    "everywhere else. The line goes soft, the whites go grey, and a crisp outline a child could "
    "colour inside turns into a smudge.\n\nSo this isn't a scan. It's rendered straight out of "
    "the book's own file at 220 dots per inch — which is why the drum rims and the feather "
    "edges still have an edge on them.\n\nThe honest part: two of our older page images are "
    "still upscaled scans, because we don't hold a page file for those two books. We know which "
    "ones, and we'd like to fix them.\n\nThis is the Boxing Day Junkanoo Parade — p86 Upper, "
    "p63 Lower. The book's own line: Junkanoo fills Bay Street with music, movement and "
    "colour.\n\nAges 9–12, grades 4–6, 109 pages.\n\n" + ATBU,
    "#AllThingsBahamian #Junkanoo #Bahamas #ColouringBook #BahamianKids #BehindTheScenes "
    "#GDSPublications"),
  pin_t='An actual page, not an illustration',
  pin=tail("Almost everything we post is our own illustration. This is an actual page from All "
    "Things Bahamian: the Boxing Day Junkanoo Parade, page 86 in the Upper edition and page 63 "
    "in the Lower. Not a scan — rendered from the book's own file at 220 dots per inch, so the "
    "drum rims and feather edges keep their edge. Ages 9 to 12, 109 pages.\n\n" + ATBU),
  pin_url=ATBU),

 # Tue 24 Nov — slot 121 — pillar 2 Reader Engagement — Girl & Whale Activity Book — HERO (new)
 dict(day='2026-11-24', base=14, pid='gds/girl-whale-activity/create-your-own-island-legend-20261124',
  pad=False, board=B_READ, anna_absent=True,
  alt='A wooden desk by an open window at night, lit by a brass lamp. A large sheet of cream paper '
      'lies blank in the middle of the desk with a yellow pencil beside it, waiting to be written '
      'on. A queen conch shell with a glossy pink mouth, a few small shells and a sand dollar sit '
      'to one side, a jar of coloured pencils and a bowl of coral to the other, and a stack of '
      'books at the edge. Through the window a full moon lays a path of light across a calm sea, '
      'with a dark cay on the horizon.',
  fb=tail("Create Your Own Island Legend is one of the activities in The Girl and The Whale "
    "Coloring & Activity Book, and it is the one we would most like to read the answers "
    "to.\n\nSo: what is the legend where you are from?\n\nEvery island has one. A light nobody "
    "can account for. A reef that takes something and gives something back. A sound off the "
    "water that the older people in the settlement will tell you about and the younger ones "
    "will not.\n\nThe activity hands a child a blank page and asks them to write theirs down. "
    "That is a harder page than it looks, which is also why it is worth doing — a child who "
    "writes one has to decide what makes a story stay in a place for a hundred years.\n\nTell "
    "us yours in the comments. We will read every one.\n\nThe reader behind the activity book "
    "is The Girl and The Whale, written by Zhané Mackey and published from Nassau by GDS "
    "Publications. The picture above is our illustration of a page waiting to be filled, not a "
    "page from the book.\n\n40 pages, ages 6 to 12, grades 1 to 6.\n\nReader: " + GW
    + "\nActivity book: " + GWA),
  ig=tail("What's the legend where you're from? 🌙\n\nCreate Your Own Island Legend is one of "
    "the activities in The Girl and The Whale Coloring & Activity Book, and it's the one we'd "
    "most like to read the answers to.\n\nEvery island has one. A light nobody can account for. "
    "A reef that takes something and gives something back. A sound off the water the older "
    "people will tell you about and the younger ones won't.\n\nThe activity hands a child a "
    "blank page and asks them to write theirs down. Harder than it looks — which is why it's "
    "worth doing. A child who writes one has to work out what makes a story stay in a place for "
    "a hundred years.\n\nTell us yours in the comments 👇 we'll read every one.\n\nThe reader "
    "behind it is The Girl and The Whale by Zhané Mackey, published from Nassau by GDS "
    "Publications. Our illustration of a page waiting to be filled, not a page from the "
    "book.\n\n40 pages, ages 6–12.\n\nReader: " + GW + "\nActivity book: " + GWA,
    "#TheGirlAndTheWhale #IslandLegends #BahamianAuthors #ActivityBook #KidsWriting "
    "#BahamianKids #GDSPublications"),
  pin_t='What is the legend where you are from?',
  pin=tail("Create Your Own Island Legend is one of the activities in The Girl and The Whale "
    "Coloring & Activity Book. It hands a child a blank page and asks them to write their "
    "island's legend down — a harder page than it looks, and worth doing for that reason. The "
    "reader is by Zhané Mackey, published from Nassau by GDS Publications. Our illustration, "
    "not a page from the book. 40 pages, ages 6 to 12.\n\n" + GWA),
  pin_url=GWA),

 # Tue 24 Nov — slot 122 — pillar 3 Promo/CTA — ATB Lower — COLLAGE
 dict(day='2026-11-24', base=19, board=B_COLOR, pad=False, anna_absent=True,
  panels=['gds/atb-lower/queens-staircase-20261010',
          'gds/atb-lower/island-lighthouse-20261021',
          'gds/atb-lower/a-shark-over-the-reef-20261124',
          'gds/atb-lower/a-spiny-lobster-under-the-ledge-20261124'],
  alts=['The Queen’s Staircase in Nassau: a long flight of worn limestone steps cut down through a '
        'narrow gorge, with tall pale stone walls draped in ferns and vines either side and dappled '
        'sunlight falling across the steps.',
        'A Bahamian lighthouse on a low rocky point, a tall slender tower in broad red and white '
        'bands with a glass lantern room at the top and a small keeper\'s cottage beside it, pale '
        'limestone running down to clear turquoise shallows. A low swell rolls in and small waves '
        'break gently over the rocks in a thin lace of foam and slide back, with ripple lines '
        'travelling across the shallows.',
        'A nurse shark cruising slowly through clear turquoise water above a Bahamian reef. It is '
        'tan-brown with a blunt rounded head, two short barbels hanging below its snout, small eyes, '
        'two rounded dorsal fins set far back and a long trailing tail. Below it the reef is crowded '
        'with orange and pink corals, purple sea fans and brain coral, with pale rippled sand between '
        'them and small black-and-yellow sergeant major fish swimming past. Sunlight falls in bands '
        'from the surface above.',
        'A Caribbean spiny lobster — the Bahamian crawfish — walking out from under a coral ledge '
        'onto pale rippled sand. Its shell is mottled brown, rust and olive with scattered cream '
        'spots, and it has no claws at all: two enormously long spiny antennae sweep forward into the '
        'open water, ten plain walking legs carry it along, and a broad fan tail trails behind. A '
        'purple sea fan and soft yellow corals grow on the ledge above, and small yellow fish pass in '
        'the blue beyond.'],
  collage='gds/atb-lower/collage-our-bahamian-world-20261124',
  alt='Four Bahamian scenes: the Queen’s Staircase cut down through a fern-draped limestone gorge, '
      'a red and white lighthouse on a rocky point above turquoise shallows, a nurse shark cruising '
      'over a crowded reef, and a spiny lobster walking out from under a coral ledge onto pale sand.',
  fb=tail("Two of these a child can go and stand in front of. Two of them they would need a mask "
    "and a calm day for.\n\nThat is the argument for All Things Bahamian, Lower Elementary, and "
    "it is why one picture never makes it. The book runs seven sections, and these four scenes "
    "come out of just two of them.\n\nHistoric Places and Landmarks is pages 29 to 37 — forts, "
    "monuments and lighthouses. Life in Our Bahamian Seas is pages 38 to 52 — reefs, conch, "
    "turtles, sharks and fish.\n\nThe nurse shark is worth a word, because it is the shark a "
    "Bahamian child is most likely to actually meet. Blunt head, two little barbels under the "
    "snout like whiskers, small eyes, and a habit of lying still under a ledge. And the "
    "crawfish has no claws at all — what it has is two antennae longer than the rest of "
    "it.\n\nThe other five sections are National Symbols, Our Beautiful Islands, Junkanoo, "
    "Fruits of The Bahamas, and My Bahamas.\n\nSwipe for all four. These are our illustrations "
    "of subjects the book covers, not pages from the book.\n\nAll Things Bahamian, Lower "
    "Elementary. Ages 5 to 9, grades 1 to 3. 83 pages.\n\n" + ATBL),
  ig=tail("Two of these a child can go and stand in front of. Two of them they'd need a mask and "
    "a calm day for. 🦈\n\nThat's the argument for All Things Bahamian, Lower Elementary — and "
    "why one picture never makes it. Seven sections in the book; these four scenes come out of "
    "two of them.\n\nHistoric Places and Landmarks, pages 29–37: forts, monuments, lighthouses. "
    "Life in Our Bahamian Seas, pages 38–52: reefs, conch, turtles, sharks, fish.\n\nThe nurse "
    "shark is worth a word — it's the shark a Bahamian child is most likely to actually meet. "
    "Blunt head, two little barbels under the snout like whiskers, small eyes, and a habit of "
    "lying still under a ledge. And the crawfish has no claws at all. What it has is two "
    "antennae longer than the rest of it.\n\nThe other five sections: National Symbols, Our "
    "Beautiful Islands, Junkanoo, Fruits of The Bahamas, My Bahamas.\n\nSwipe for all four — "
    "our illustrations of subjects the book covers, not pages from the book.\n\nAges 5–9, "
    "grades 1–3, 83 pages.\n\n" + ATBL,
    "#AllThingsBahamian #Bahamas #ColouringBook #BahamianKids #NurseShark #ReefLife "
    "#GDSPublications"),
  pin_t='Seven sections, and this is two of them',
  pin=tail("All Things Bahamian, Lower Elementary runs seven sections. These four scenes come "
    "out of two: Historic Places and Landmarks, pages 29 to 37, and Life in Our Bahamian Seas, "
    "pages 38 to 52. The nurse shark is the one a Bahamian child is most likely to meet, and "
    "the crawfish has no claws at all. Our illustrations of subjects the book covers, not pages "
    "from the book. Ages 5 to 9, 83 pages.\n\n" + ATBL),
  pin_url=ATBL),

 # Wed 25 Nov — slot 123 — pillar 4 Activity Spotlight — Regatta Activity Book — COLLAGE
 dict(day='2026-11-25', base=14, board=B_COLOR, pad=False, anna_absent=True,
  panels=['gds/regatta-activity/plan-an-island-meal-20261022',
          'gds/regatta-activity/island-food-scramble-20261101-v2',
          'gds/regatta-activity/regatta-bookmarks-20261125',
          'gds/regatta-activity/the-finished-flags-flying-20261125'],
  alts=['A Bahamian family meal laid out on a wooden table outdoors, seen from above: a whole fried '
        'fish, peas and rice, baked chicken, fried plantains, potato salad, a halved coconut and a '
        'jug of juice with cut limes, with enamel plates, forks and hibiscus flowers between the '
        'dishes under dappled afternoon light.',
        'Five Bahamian foods laid out apart from each other on a scrubbed wooden table, each on its '
        'own small square of cream paper: a whole silver fish on a board, a green coconut cut open at '
        'the top, three avocados with one halved to show the stone, a bowl of white rice and a bowl '
        'of pigeon peas, with a pencil and a jar of coloured pencils at one edge under dappled light.',
        'Four hand-decorated paper bookmarks laid in a row on a scrubbed wooden table, each with a '
        'twine tassel at the top. One is painted with a Bahamian sloop under a single tall triangular '
        'sail on blue water, one with a pink-mouthed conch shell among green leaves, one with a row '
        'of small coloured pennants, and one with a pattern of blue and turquoise waves. A ball of '
        'twine, a jar of coloured pencils and a pair of scissors lie beside them in warm afternoon '
        'light.',
        'Seven hand-painted triangular pennants strung on a rope between two wooden poles above a '
        'regatta ground, seen from below against a bright blue sky. Each carries a different design — '
        'turquoise stripes, a gold scallop shell, coral zigzags, a yellow sun, a coral hibiscus, '
        'white starfish on gold, and turquoise waves — and they lift in the breeze. Casuarina pines '
        'lean in behind them, and below the line the clear turquoise sea runs in to a pale beach with '
        'low surf breaking.'],
  collage='gds/regatta-activity/collage-make-it-yourself-20261125',
  alt='Four scenes from the Regatta activity book: a Bahamian family meal laid out on a table, five '
      'island foods set apart on paper squares, four finished paper bookmarks with twine tassels, '
      'and a line of hand-painted pennants flying above a regatta ground.',
  fb=tail("Only one of these four needs crayons. That is the thing people get wrong about the "
    "Going To The Regatta Coloring & Activity Book.\n\nThere are four named colouring pages in "
    "it — Nicholas Sees the Sloops, The C1 Sloop Race, Family at the Regatta, The Nature Bath. "
    "Everything else asks for something other than colour.\n\nPlan an Island Meal asks a child "
    "to build a meal. Island Food Scramble gives them five words to untangle: fish, coconut, "
    "pears, rice, peas. The bookmarks and the flag page ask them to cut, paint and make "
    "something that leaves the book and ends up on a shelf or a rope in the yard.\n\nThat last "
    "part matters more than it sounds. A regatta flag the child designed and then saw flying is "
    "a different object from a page they coloured in.\n\nThe rest of the book runs to word "
    "searches, a code to crack, Parts of a C1 Racing Sloop, My Family Connections, Regatta "
    "I-Spy, Nature Pool Observer, an island compass challenge and a certificate.\n\nSwipe for "
    "all four. These are our illustrations of what the activities produce, not pages from the "
    "book.\n\n40 pages, ages 6 to 12, grades 1 to 6.\n\nActivity book: " + REGA + "\nReader: "
    + REG),
  ig=tail("Only one of these four needs crayons. 🎏\n\nThat's the thing people get wrong about "
    "the Going To The Regatta Coloring & Activity Book.\n\nFour named colouring pages in it — "
    "Nicholas Sees the Sloops, The C1 Sloop Race, Family at the Regatta, The Nature Bath. "
    "Everything else asks for something other than colour.\n\nPlan an Island Meal asks a child "
    "to build a meal. Island Food Scramble gives them five words to untangle: fish, coconut, "
    "pears, rice, peas. The bookmarks and the flag page ask them to cut, paint and make "
    "something that leaves the book and ends up on a shelf — or on a rope in the yard.\n\nThat "
    "last part matters more than it sounds. A flag a child designed and then saw flying is a "
    "different object from a page they coloured in.\n\nAlso inside: word searches, a code to "
    "crack, Parts of a C1 Racing Sloop, My Family Connections, Regatta I-Spy, Nature Pool "
    "Observer, a compass challenge, a certificate.\n\nSwipe for all four — our illustrations of "
    "what the activities produce, not pages from the book.\n\n40 pages, ages 6–12.\n\nActivity "
    "book: " + REGA + "\nReader: " + REG,
    "#GoingToTheRegatta #ActivityBook #LongIsland #Bahamas #KidsCrafts #ClassroomIdeas "
    "#GDSPublications"),
  pin_t='Only one of these four needs crayons',
  pin=tail("The Going To The Regatta Coloring & Activity Book has four named colouring pages. "
    "Everything else asks for something other than colour: Plan an Island Meal, Island Food "
    "Scramble — fish, coconut, pears, rice, peas — and bookmarks and flags a child cuts, paints "
    "and takes out of the book. Our illustrations of what the activities produce, not pages "
    "from the book. 40 pages, ages 6 to 12.\n\n" + REGA),
  pin_url=REGA),
]

if __name__ == '__main__':
    run(S)
