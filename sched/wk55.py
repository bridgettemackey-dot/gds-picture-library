# -*- coding: utf-8 -*-
"""Week 55: Mon 9 - Wed 11 Nov 2026. Four slots over three days.
TWO COLLAGE DAYS: Tue 10 (Activity Spotlight) and Wed 11 (Bahamian Culture).

Activity Spotlight is the standing case and it is the strongest one here: the
point is that only five of the activity book's forty pages are colouring pages,
and a claim about RANGE needs more than one frame. Bahamian Culture takes the
second because the subject is Junkanoo - a whole section of All Things Bahamian
- and four views of it (the street, the street from above, a costume close up,
a finished headdress) say what one picture of a dancer cannot. Reader
Engagement on Monday stays a single hero: it asks one question, so it shows one
picture.
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
 # Mon 9 Nov — slot 100 — pillar 2 Reader Engagement — The Girl and The Whale — HERO (new)
 dict(day='2026-11-09', base=14, pid='gds/girl-whale/the-purple-glow-20261109',
  pad=False, board=B_READ,
  alt='A Hawaiian coral reef at dusk with a huge cosmic purple glow rising from under the water, '
      'lighting the sea from beneath in violet and lilac; nothing that makes the glow is visible. '
      'Anna stands small on dark volcanic rock in the middle distance, seen from behind with one '
      'hand lifted — deep chocolate-brown skin, long black hair past her shoulders, a hibiscus '
      'sundress, barefoot. The sky '
      'still glows coral and gold low down and a low swell rolls in over the reef flat.',
  fb=tail("What would you do?\n\nAnna has danced at the reef as the sun went down. The sky, in the "
    "book's words, glowed coral and gold. And then the water starts to glow purple from "
    "underneath, and whatever is making the light has not surfaced yet.\n\nWe will tell you what "
    "Anna does, because it is one of our favourite things about the book: she screams, and falls "
    "backwards.\n\nNot a brave speech. Not a calm hello. Something enormous is lighting up the "
    "sea, and she screams and lands on her back.\n\nTell us honestly: scream, run, or stand still? We will read every "
    "reply.\n\nThe Girl and The Whale was written by Zhané Mackey and is published from Nassau by "
    "GDS Publications. This is our illustration of that moment, not a page from the book.\n\nGDS "
    "Reading Series, Level 3. Ages 6 to 12, grades 1 to 6.\n\n" + GW),
  ig=tail("What would you do? 💜\n\nAnna has danced at the reef as the sun went down — the sky, in "
    "the book's words, glowed coral and gold. Then the water starts to glow purple from "
    "underneath, and whatever is making the light hasn't surfaced yet.\n\nWe'll tell you what Anna "
    "does, because it's one of our favourite things about the book: she screams, and falls "
    "backwards.\n\nNot a brave speech. Not a calm hello. Something enormous is lighting up the "
    "sea, and she screams and lands on her back.\n\nScream, run, or stand still? Tell us honestly 👇\n\nWritten by "
    "Zhané Mackey, published from Nassau by GDS Publications. Our illustration of that moment, not "
    "a page from the book.\n\nAges 6–12, grades 1–6.\n\n" + GW,
    "#TheGirlAndTheWhale #ChildrensBooks #BahamianAuthors #ReadingSeries #IslandStory "
    "#ReadAloud #GDSPublications"),
  pin_t='The water starts to glow purple',
  pin=tail("Anna has danced at the reef as the sun went down. Then the sea lights up from "
    "underneath, and whatever is making the glow has not surfaced yet. What she actually does: "
    "she screams and falls backwards. Written by Zhané Mackey, published from "
    "Nassau by GDS Publications. Our illustration of that moment, not a page from the "
    "book.\n\n" + GW),
  pin_url=GW),

 # Tue 10 Nov — slot 101 — pillar 3 Promo/CTA — Going To The Regatta — HERO (catalogued)
 dict(day='2026-11-10', base=14, pid='gds/regatta/flags-over-the-regatta-20260927',
  pad=False, board=B_LI,
  alt='Rows of plain coloured bunting strung above a grassy waterfront at a Bahamian regatta. '
      'Three wooden sloops with tall masts and white sails race on turquoise water beyond. '
      'Coral-pink and yellow vendor stalls stacked with pineapples, coconuts and papaya, a crowd '
      'in straw hats watching from the grass.',
  fb=tail("\"A regatta is more than a race. It is a homecoming where history, family, and island "
    "life meet.\"\n\nThat line is the lesson Going To The Regatta is built to teach, and the book "
    "earns it by being true. It is a family account of five real days on Long Island, written by "
    "Bridgette Skeete-Mackey and illustrated with the family's own photographs.\n\nThe history is "
    "real too. The first recorded organised race was at Deadman's Cay in 1868. Racing near Salt "
    "Pond began in 1967, when the schools inspector and others started racing and an American "
    "businessman watching offered a trophy — a three-day event followed. From 1969, Long Island "
    "descendants living in New Providence raised money for prizes. In August 1973 the Long "
    "Islanders Association formed, working on education, recreation, medical assistance and "
    "support for Long Island families.\n\nAbove is our illustration of a regatta waterfront. The "
    "book itself carries the photographs.\n\nGDS Reading Series, Family Reader. Ages 5 to "
    "15.\n\nReader: " + REG + "\nActivity book: " + REGA),
  ig=tail("\"A regatta is more than a race. It is a homecoming where history, family, and island "
    "life meet.\" ⛵\n\nThat's the lesson Going To The Regatta is built to teach, and it earns it "
    "by being true — a family account of five real days on Long Island, written by Bridgette "
    "Skeete-Mackey and illustrated with the family's own photographs.\n\nThe history is real too. "
    "First recorded organised race: Deadman's Cay, 1868. Racing near Salt Pond began in 1967, when "
    "the schools inspector and others started racing and a watching American businessman offered a "
    "trophy. From 1969 Long Island descendants in New Providence raised money for prizes, and in "
    "August 1973 the Long Islanders Association formed.\n\nOur illustration of a regatta "
    "waterfront. The book itself carries the photographs.\n\nAges 5–15.\n\nReader: " + REG
    + "\nActivity book: " + REGA,
    "#GoingToTheRegatta #LongIsland #Bahamas #BahamianAuthors #FamilyStories #Regatta "
    "#GDSPublications"),
  pin_t='A regatta is more than a race',
  pin=tail("\"It is a homecoming where history, family, and island life meet.\" Going To The "
    "Regatta is a true family account of five days on Long Island by Bridgette Skeete-Mackey, "
    "illustrated with the family's own photographs. First recorded organised race: Deadman's Cay, "
    "1868. Our illustration of a regatta waterfront; the book carries the photographs.\n\n" + REG),
  pin_url=REG),

 # Tue 10 Nov — slot 102 — pillar 4 Activity Spotlight — Girl & Whale Activity Book — COLLAGE
 # Anna is named in the captions (Listen Like Anna, Design Anna's Celebration Dress) but
 # appears in NO panel here: the reef has no people, the mat on the rock has nobody there,
 # the dress sheets carry drawings of DRESSES with no figure in them, and the postcard desk
 # has no hands. All four looked at before setting this.
 dict(day='2026-11-10', base=19, board=B_COLOR, pad=False, anna_absent=True,
  panels=['gds/girl-whale-activity/coral-reef-i-spy-20261017',
          'gds/girl-whale-activity/listen-like-anna-20261110',
          'gds/girl-whale-activity/design-annas-dress-20261021',
          'gds/girl-whale-activity/postcard-from-hawaii-20261110'],
  alts=['A bright coral reef underwater: shells, orange starfish, small striped fish, two crabs '
        'among the rocks and two green sea turtles gliding, with a small leather-bound book '
        'resting half hidden on the sand. Sunlight flickers down in slow shifting bands.',
        'A quiet spot set up for sitting still and listening: a folded woven mat on a flat warm '
        'rock above a Hawaiian shoreline, with an open blank notebook, a pencil and a cup of '
        'coloured pencils on it, and nobody there. Green mountains and palms behind; below, the '
        'sea moves gently with a low swell and a thin lace of foam running up the pale sand.',
        'A worktable seen from above with four sheets of cream paper, each carrying a hand-drawn '
        'dress design coloured differently — one patterned with hibiscus flowers, one with small '
        'shells around the hem, one with a sweep of stars, one left as a plain outline — with a '
        'jar of coloured pencils, loose pencils, scraps of bright fabric and ribbon and a dish of '
        'shells around them. Through a window behind, calm turquoise sea moves gently under palms.',
        'A completely blank cream postcard with a thin printed border lying on a pale wooden desk, '
        'seen from above. A pen rests across one corner, with two small shells, a sprig of dried '
        'seaweed and a striped jar of coloured pencils around it, and warm light coming in from a '
        'window to one side.'],
  collage='gds/girl-whale-activity/collage-not-a-colouring-page-20261110',
  alt='Four things to do from the activity book: a bright coral reef to search, a woven mat on a '
      'rock with an open blank notebook and pencils, four hand-drawn dress designs on a worktable, '
      'and a blank postcard with a pen beside shells and a jar of coloured pencils.',
  fb=tail("Forty pages. Five of them are colouring pages.\n\nThat surprises people, so it is worth "
    "saying plainly: The Girl and The Whale Coloring & Activity Book has five colouring pages — "
    "Anna Hears a Song, A Story at the Docks, The Dance at Sunset, The Legend Appears and Anna's "
    "Cosmic Ride. The other thirty-five pages ask a child to do something else.\n\nFour of "
    "them:\n\nListen Like Anna — sit quietly for one minute and write down four sounds you can "
    "hear.\n\nCoral Reef I-Spy — 6 shells, 5 starfish, 4 fish, 3 crabs, 2 sea turtles and 1 tiny "
    "legend book.\n\nDesign Anna's Celebration Dress.\n\nPostcard from Hawaii.\n\nFour pages, four "
    "different kinds of asking — and the first needs nothing but a minute of "
    "quiet.\n\nThese are our illustrations, not pages from the book.\n\n40 pages, ages 6 to 12, "
    "grades 1 to 6.\n\nReader: " + GW + "\nActivity book: " + GWA),
  ig=tail("Forty pages. Five of them are colouring pages. 🐚\n\nThat surprises people, so: The "
    "Girl and The Whale Coloring & Activity Book has five colouring pages — Anna Hears a Song, A "
    "Story at the Docks, The Dance at Sunset, The Legend Appears, Anna's Cosmic Ride. The other "
    "thirty-five ask a child to do something else.\n\nSwipe for four of them:\n\nListen Like Anna "
    "— sit quietly for one minute, write down four sounds.\n\nCoral Reef I-Spy — 6 shells, 5 "
    "starfish, 4 fish, 3 crabs, 2 sea turtles, 1 tiny legend book.\n\nDesign Anna's Celebration "
    "Dress.\n\nPostcard from Hawaii.\n\nFour pages, four different kinds of asking "
    "— and the first needs nothing but a minute of quiet.\n\nOur illustrations, not pages from the book.\n\n40 "
    "pages, ages 6–12.\n\nReader: " + GW + "\nActivity book: " + GWA,
    "#TheGirlAndTheWhale #ActivityBook #KidsActivities #ClassroomIdeas #ColouringBook "
    "#BahamianAuthors #GDSPublications"),
  pin_t='Forty pages, five of them colouring pages',
  pin=tail("The Girl and The Whale Coloring & Activity Book has five colouring pages. The other "
    "thirty-five ask a child to do something else: Listen Like Anna, Coral Reef I-Spy, Design "
    "Anna's Celebration Dress, Postcard from Hawaii — four different kinds of asking. "
    "Our illustrations, not pages from the book. Ages 6 to 12.\n\n" + GWA),
  pin_url=GWA),

 # Wed 11 Nov — slot 103 — pillar 5 Bahamian Culture — ATB Upper — COLLAGE
 dict(day='2026-11-11', base=14, board=B_CULT, pad=False,
  panels=['gds/atb-upper/junkanoo-bay-street-20261018',
          'gds/atb-upper/junkanoo-from-the-balcony-20261111',
          'gds/atb-upper/junkanoo-detail-20260902',
          'gds/atb-upper/junkanoo-headdress-on-the-stand-20261111'],
  alts=['A Junkanoo rush on Bay Street in Nassau at night: a lead dancer mid-stride in an enormous '
        'fanned headdress of pink, orange and turquoise crepe, with drummers, cowbell shakers and '
        'horn players behind and a crowd along the balconied buildings under lit street lamps.',
        'A Junkanoo rush seen from a first-floor balcony on Bay Street in Nassau at night: the '
        'parade snakes away down the street as a river of colour, dancers in enormous fanned '
        'crepe-paper costumes in pink, orange and turquoise with drummers and cowbell shakers '
        'among them, all mid-stride, and crowds packed along both pavements under warm street '
        'lamps between pastel colonial buildings.',
        'A close-up of a Junkanoo costume in fringed crepe paper, beside a goatskin drum and a '
        'cowbell.',
        'A finished Junkanoo headdress standing ready on a wooden stand in a workshop, seen from '
        'the front and slightly below so it towers: an enormous fanned crown of fringed crepe '
        'paper in hot pink, orange, turquoise and white built over a cardboard frame, with '
        'scrolled and spiralled paper shapes across it. Rolls of crepe paper, a pot of paste and '
        'card offcuts on the bench behind.'],
  collage='gds/atb-upper/collage-junkanoo-20261111',
  alt='Four views of Junkanoo: a rush on Bay Street at night, the same parade seen from a balcony '
      'above as a river of colour, a close-up of a fringed crepe-paper costume beside a goatskin '
      'drum and a cowbell, and a finished headdress standing ready on a stand in a workshop.',
  fb=tail("Junkanoo is a whole section of the book, not a single page.\n\nIn All Things Bahamian "
    "it is the fifth of seven sections — Junkanoo: Music, Movement and Mas — running pages 76 to "
    "87 in the Upper edition and 53 to 63 in the Lower. The Boxing Day Junkanoo Parade has its own "
    "page: 86 in Upper, 63 in Lower. Same drawing in both books.\n\nAnd the section is not only "
    "about the parade. The Lower edition's Design Your Own Junkanoo Costume comes with the tip "
    "that Junkanoo artists build their costumes from cardboard, paste and colourful crepe paper — "
    "which is why we wanted a picture of a headdress standing finished on its stand, before "
    "anyone has carried it anywhere.\n\nFour views of one subject: the rush at street level, the "
    "rush from a balcony, a costume close up, and the work behind it.\n\nThese are our "
    "illustrations. In the book, Junkanoo is line drawings waiting for pencils.\n\nAll Things "
    "Bahamian: Upper Elementary. Ages 9 to 12, grades 4 to 6. 109 pages.\n\n" + ATBU),
  ig=tail("Junkanoo is a whole section of the book, not a single page. 🥁\n\nIn All Things "
    "Bahamian it's the fifth of seven sections — Junkanoo: Music, Movement and Mas — pages 76–87 "
    "in the Upper edition, 53–63 in the Lower. The Boxing Day Junkanoo Parade has its own page: 86 "
    "in Upper, 63 in Lower. Same drawing in both books.\n\nAnd it isn't only about the parade. The "
    "Lower edition's Design Your Own Junkanoo Costume comes with the tip that Junkanoo artists "
    "build costumes from cardboard, paste and colourful crepe paper — which is why we wanted a "
    "headdress standing finished on its stand, before anyone has carried it anywhere.\n\nSwipe for "
    "four views: the rush at street level, the rush from a balcony, a costume close up, and the "
    "work behind it.\n\nOur illustrations. In the book, Junkanoo is line drawings waiting for "
    "pencils.\n\nAges 9–12, grades 4–6, 109 pages.\n\n" + ATBU,
    "#Junkanoo #AllThingsBahamian #Bahamas #BahamianCulture #Nassau #ColouringBook "
    "#GDSPublications"),
  pin_t='Junkanoo is a whole section, not a page',
  pin=tail("In All Things Bahamian, Junkanoo: Music, Movement and Mas is the fifth of seven "
    "sections — pages 76 to 87 in the Upper edition, 53 to 63 in the Lower, with the same drawings "
    "in both. Four views of one subject: the rush at street level, the rush from a balcony, a "
    "costume close up, and the work behind it. Our illustrations, not pages from the "
    "book.\n\n" + ATBU),
  pin_url=ATBU),
]

if __name__ == '__main__':
    run(S)
