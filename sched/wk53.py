# -*- coding: utf-8 -*-
"""Week 53: Mon 2 - Wed 4 Nov 2026. Four slots over three days.
TWO COLLAGE DAYS: Mon 2 (Classroom & Library) and Tue 3 (Book World).

Classroom & Library is a collage day here because the pitch to a teacher is
structural - seven sections, one a week - and four section subjects side by side
show that where one picture cannot. Book World is the standing case: the world of
Going To The Regatta is an actual island, and an island does not fit in one frame.
Wednesday's two stay single heroes.
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
 # Mon 2 Nov — slot 90 — pillar 6 Classroom & Library — ATB Upper — COLLAGE
 dict(day='2026-11-02', base=14, board=B_CULT, pad=False,
  panels=['gds/atb-upper/glass-window-bridge-20261008-v2',
          'gds/atb-upper/stone-monument-20261102',
          'gds/atb-upper/green-turtle-reef-20261102-v2',
          'gds/atb-upper/junkanoo-bay-street-20261018'],
  alts=["The Glass Window Bridge in Eleuthera: a road bridge crossing a narrow gap in the rock, with the rough navy Atlantic breaking beyond it and the calm clear turquoise Bight of Eleuthera in the foreground on the near side.",
        'A plain weathered limestone column on a square stepped base standing on a grassy rise '
        'above a Bahamian harbour, with nothing carved on it. A low stone wall and worn steps lead '
        'up, bougainvillea and ferns grow at the base and two casuarinas lean in the breeze. Below, '
        'clear turquoise water where a low swell rolls in and light shifts in slow bands over the '
        'sand.',
        'A green sea turtle gliding over a Bahamian coral reef in clear shallow water, her olive '
        'and gold shell patterned and her two front flippers sweeping mid-stroke. Around and below '
        'her a spotted eagle ray glides over the sand, a queen angelfish and blue tangs move among '
        'corals in pink, orange and violet, a spiny lobster shelters under a ledge, and a starfish '
        'and a queen conch shell rest on pale sand.',
        "A Junkanoo rush on Bay Street in Nassau at night: a lead dancer mid-stride in an enormous fanned headdress of pink, orange and turquoise crepe, with drummers, cowbell shakers and horn players behind and a crowd along the balconied buildings under lit street lamps."],
  collage='gds/atb-upper/collage-a-term-of-work-20261102-v2',
  alt='A four-panel collage from All Things Bahamian: the Glass Window Bridge in Eleuthera, a stone '
      'monument above a harbour, a green sea turtle over a busy coral reef, and a Junkanoo rush on Bay '
      'Street at night.',
  fb=tail("One section a week, and you have a term.\n\nThat is the practical case for All Things "
    "Bahamian in a classroom. It is built in seven sections, and they are not arbitrary — each one "
    "is a body of work with a shape.\n\nOur Beautiful Islands runs pages 9 to 49 in the Upper "
    "edition. Historic Places and Landmarks, 50 to 59 — forts, monuments and lighthouses. Life in "
    "Our Bahamian Seas, 60 to 75 — reefs, conch, turtles, sharks, fish. Junkanoo: Music, Movement "
    "and Mas, 76 to 87. Then Bahamian National Symbols at the front, Fruits of The Bahamas, and My "
    "Bahamas to close.\n\nEvery section opens with four thumbnails of its own artwork and an ABOUT "
    "THIS SECTION box, so a child knows what the next stretch of pages is about before they "
    "start.\n\nThe Upper edition adds EXPLORE MORE pages of written-response questions and Key "
    "Settlements and Communities — five named communities per island with a line each.\n\nThese "
    "are our illustrations of four of those subjects; in the book each is a line drawing waiting "
    "for pencils.\n\nAll Things Bahamian: Upper Elementary. Ages 9 to 12, grades 4 to 6. 109 "
    "pages.\n\n" + ATBU),
  ig=tail("One section a week, and you have a term. 📚\n\nAll Things Bahamian is built in seven "
    "sections, and each is a body of work with a shape.\n\nOur Beautiful Islands, pages 9–49. "
    "Historic Places and Landmarks, 50–59 — forts, monuments, lighthouses. Life in Our Bahamian "
    "Seas, 60–75 — reefs, conch, turtles, sharks, fish. Junkanoo, 76–87. Plus National Symbols, "
    "Fruits of The Bahamas, and My Bahamas to close.\n\nEvery section opens with four thumbnails "
    "of its own artwork and an ABOUT THIS SECTION box, so a child knows what's coming.\n\nThe "
    "Upper edition adds EXPLORE MORE questions and Key Settlements and Communities.\n\nSwipe for "
    "four of those subjects — our illustrations. In the book each is a line drawing waiting for "
    "pencils.\n\nAges 9–12, grades 4–6, 109 pages.\n\n" + ATBU,
    "#AllThingsBahamian #TeacherResources #ClassroomIdeas #Bahamas #HomeschoolBahamas "
    "#ColouringBook #GDSPublications"),
  pin_t='One section a week, and you have a term',
  pin=tail("All Things Bahamian is built in seven sections — National Symbols, Our Beautiful "
    "Islands, Historic Places and Landmarks, Life in Our Bahamian Seas, Junkanoo, Fruits of The "
    "Bahamas and My Bahamas — each opening with four thumbnails of its own artwork. Our "
    "illustrations of four of those subjects; in the book each is a line drawing waiting for "
    "pencils. Upper Elementary, ages 9 to 12, 109 pages.\n\n" + ATBU),
  pin_url=ATBU),

 # Tue 3 Nov — slot 91 — pillar 0 Book World — Going To The Regatta — COLLAGE
 dict(day='2026-11-03', base=14, board=B_LI, pad=False,
  panels=['gds/regatta/cape-santa-maria-20260930',
          'gds/regatta/the-nature-bath-20261103',
          'gds/regatta/long-island-church-20261103',
          'gds/regatta/sloops-at-salt-pond-20260830'],
  alts=["A long curve of pale sand at Cape Santa Maria, Long Island, with water grading from clear turquoise shallows to deep blue. Sea grape bushes along the dune, three coconut palms leaning in the wind, a weathered wooden dinghy pulled up on the sand and conch shells at the tideline in late afternoon light.",
        'A nature bath on the Long Island shore early in the morning: a clear natural pool in worn '
        'limestone with pale sand and stones on the bottom, a few small fish and rough stone steps '
        'cut down into it, fine ripple rings spreading across the surface and light flickering '
        'below. Beyond the rock the open sea, a low swell rolling in and small waves breaking '
        'gently over the ironshore.',
        'A small white clapboard island church with a steep red roof, a short square bell tower and '
        'arched windows with pale blue shutters, three worn steps up to an open door. A low stone '
        'wall runs around a swept sandy yard, with a flowering poinciana and casuarinas beside it '
        'and two bicycles leaned against the wall in bright early light.',
        "Three Bahamian sloops under full sail racing past a line of festival tents."],
  collage='gds/regatta/collage-the-island-itself-20261103',
  alt='A four-panel collage of Long Island from Going To The Regatta: the long curve of sand at Cape '
      'Santa Maria, a clear natural rock pool by the sea, a small white island church on a Sunday '
      'morning, and three sloops racing past the festival tents.',
  fb=tail("The world of this book is a real place, and you can drive the length of it.\n\nGoing To "
    "The Regatta is a true family account of five days on Long Island, written by Bridgette "
    "Skeete-Mackey.\n\nThey land at Stella Maris in the north on the Thursday. A rocky path past "
    "the backyard leads down to the nature bath, a clear natural pool. Lunch at Green Leaf, run by "
    "a husband-and-wife team. Then the long drive south to Salt Pond in the centre — food vendors, "
    "craft stalls, racing sloops, private boats carrying spectators, Bahamian artists on stage in "
    "the evening.\n\nSunday is worship at Beulah Baptist Church in Simms. The church above is our "
    "illustration of an island church, not that building.\n\nAnd Cape Santa Maria, which the book's "
    "photo gallery names alongside pink sand at Deals Beach, a rainbow over the Atlantic and "
    "colourful vendor buildings.\n\nA regatta is more than a race. It is a homecoming where "
    "history, family and island life meet.\n\nThese are our illustrations; the book itself carries "
    "the photographs.\n\nGDS Reading Series, Family Reader, ages 5 to 15.\n\n" + REG),
  ig=tail("The world of this book is a real place, and you can drive the length of it. 🏝️\n\nThey "
    "land at Stella Maris in the north on the Thursday. A rocky path past the backyard leads down "
    "to the nature bath, a clear natural pool. Lunch at Green Leaf. Then the long drive south to "
    "Salt Pond — vendors, craft stalls, racing sloops, artists on stage in the evening.\n\nSunday "
    "is worship at Beulah Baptist Church in Simms. The church here is our illustration of an "
    "island church, not that building.\n\nAnd Cape Santa Maria, which the book's photo gallery "
    "names alongside pink sand at Deals Beach and a rainbow over the Atlantic.\n\n\"A regatta is "
    "more than a race. It is a homecoming where history, family, and island life meet.\"\n\nSwipe "
    "for all four — our illustrations. The book carries the photographs.\n\nFamily Reader, ages "
    "5–15.\n\n" + REG,
    "#GoingToTheRegatta #LongIsland #Bahamas #FamilyStories #IslandLife #BahamianAuthors "
    "#GDSPublications"),
  pin_t='The world of this book is a real place',
  pin=tail("Cape Santa Maria, a clear natural rock pool, an island church on a Sunday morning and "
    "sloops racing past the festival tents. Going To The Regatta is a true family account of five "
    "days on Long Island by Bridgette Skeete-Mackey. Our illustrations; the book carries the family "
    "photographs. Family Reader, ages 5 to 15.\n\n" + REG),
  pin_url=REG),

 # Wed 4 Nov — slot 92 — pillar 1 Behind the Scenes — Girl & Whale activity book — NEW ART
 dict(day='2026-11-04', base=14, pid='gds/girl-whale-activity/choosing-the-pages-20261104',
  pad=False, board=B_COLOR,
  alt='An illustrator\'s desk with five small pencil sketches of Anna — a girl with chocolate-brown '
      'skin and long black hair in the finished art, here in uncoloured pencil outline: listening on '
      'a beach, on a dock with a seated fisherman, dancing at the water\'s edge, watching a whale '
      'rise, and riding high on its fin. A pencil, an eraser, a jar of coloured pencils and a conch '
      'shell around them.',
  fb=tail("Forty pages, and only five of them are colouring pages. Choosing which five is the "
    "whole job.\n\nThe Girl and The Whale Coloring & Activity Book gives five: Anna Hears a Song, "
    "A Story at the Docks, The Dance at Sunset, The Legend Appears, and Anna's Cosmic Ride.\n\nRead "
    "them in a row and you have the story's spine — she hears something nobody believes, she is "
    "told the legend, she does the dance, the whale comes, she flies. Five pictures and a child who "
    "has not read the book still knows what happened.\n\nThe other thirty-five pages do different "
    "work: Coral Reef I-Spy, Crack the Cosmic Code, Label the Humpback Whale, Design Your Own "
    "Cosmic Finback, Create Anna's Island Route, Anna's Feelings, Legend and Reality sorting, "
    "Create Your Own Island Legend, Draw the Family Under the Stars, Postcard from Hawaii, Cosmic "
    "Bookmarks and a certificate.\n\nAbove is our illustration of that choosing, not a page from "
    "the book.\n\n40 pages, ages 6 to 12.\n\nReader: " + GW + "\nActivity book: " + GWA),
  ig=tail("Forty pages, and only five are colouring pages. Choosing which five is the whole job. "
    "✏️\n\nThe five: Anna Hears a Song, A Story at the Docks, The Dance at Sunset, The Legend "
    "Appears, and Anna's Cosmic Ride.\n\nRead them in a row and you have the story's spine — she "
    "hears something nobody believes, she's told the legend, she does the dance, the whale comes, "
    "she flies. Five pictures and a child who hasn't read the book still knows what "
    "happened.\n\nThe other thirty-five do different work: Coral Reef I-Spy, Crack the Cosmic Code, "
    "Design Your Own Cosmic Finback, Anna's Feelings, Draw the Family Under the Stars, Cosmic "
    "Bookmarks, a certificate.\n\nOur illustration of that choosing, not a page from the "
    "book.\n\n40 pages, ages 6–12.\n\nReader: " + GW + "\nActivity book: " + GWA,
    "#TheGirlAndTheWhale #BehindTheScenes #ActivityBook #ColouringBook #ChildrensBooks "
    "#BahamianAuthors #GDSPublications"),
  pin_t='Only five of the forty pages are colouring pages',
  pin=tail("Anna Hears a Song, A Story at the Docks, The Dance at Sunset, The Legend Appears and "
    "Anna's Cosmic Ride — the five colouring pages in The Girl and The Whale Coloring & Activity "
    "Book. Read them in a row and you have the story's spine. Our illustration of that choosing, "
    "not a page from the book. Ages 6 to 12.\n\nReader: " + GW + "\nActivity book: " + GWA),
  pin_url=GWA),

 # Wed 4 Nov — slot 93 — pillar 2 Reader Engagement — ATB Lower — NEW ART
 dict(day='2026-11-04', base=19, pid='gds/atb-lower/the-crayon-tin-20261104',
  pad=False, board=B_COLOR,
  alt='An open tin of well-used crayons on a wooden table seen from above. Some are worn down to '
      'stubs with their paper peeled back — the turquoise, the gold and the pink are the shortest — '
      'while others are nearly full length. Loose crayons lie beside the tin, one broken in two, '
      'with crayon shavings scattered and a cream sheet at the edge carrying a half-coloured '
      'drawing of a conch shell.',
  fb=tail("Which colour runs out first in your house?\n\nWith this book the answer is rarely a "
    "surprise. Turquoise goes first, because every page has water in it. Then gold, because of the "
    "sand and the flag and the pineapples. Then pink, for the conch and the hibiscus and the "
    "flamingo.\n\nAll Things Bahamian is a book about a place with a very particular palette, and "
    "a well-used copy tells you so before you open it.\n\nThe Lower edition adds a Colouring Tips "
    "page and simpler design activities, including Design Your Own Junkanoo Costume — which comes "
    "with the tip that Junkanoo artists build costumes from cardboard, paste and colourful crepe "
    "paper.\n\nTell us which stub is shortest in your tin. We read every reply.\n\nAll Things "
    "Bahamian, Lower Elementary. Ages 5 to 9, grades 1 to 3. 83 pages.\n\n" + ATBL),
  ig=tail("Which colour runs out first in your house? 🖍️\n\nWith this book it's rarely a surprise. "
    "Turquoise goes first, because every page has water in it. Then gold — the sand, the flag, the "
    "pineapples. Then pink, for the conch and the hibiscus and the flamingo.\n\nAll Things Bahamian "
    "is a book about a place with a very particular palette, and a well-used copy tells you so "
    "before you open it.\n\nThe Lower edition adds a Colouring Tips page and simpler design "
    "activities, including Design Your Own Junkanoo Costume.\n\nWhich stub is shortest in your "
    "tin? 👇\n\nAges 5–9, grades 1–3, 83 pages.\n\n" + ATBL,
    "#AllThingsBahamian #ColouringBook #BahamianKids #Bahamas #KidsActivities #Crayons "
    "#GDSPublications"),
  pin_t='Which colour runs out first in your house?',
  pin=tail("Turquoise goes first, because every page has water in it. Then gold, for the sand and "
    "the flag and the pineapples. Then pink, for the conch and the hibiscus and the flamingo. All "
    "Things Bahamian is a book about a place with a very particular palette. Lower Elementary, ages "
    "5 to 9, grades 1 to 3, 83 pages.\n\n" + ATBL),
  pin_url=ATBL),
]

if __name__ == '__main__':
    run(S)
