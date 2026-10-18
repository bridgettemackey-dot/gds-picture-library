# -*- coding: utf-8 -*-
"""Week 49: Mon 19 - Wed 21 Oct 2026. Four slots over three days.
TWO COLLAGE DAYS: Mon 19 (Book World) and Tue 20 (Behind the Scenes).

Book World is the natural one - the whole point of the pillar is the world of the
book, and four beats of the story carry that where one picture cannot. Tuesday is
the second because Behind the Scenes on Going To The Regatta is not about how a
picture was drawn, it is about the real family journey the book is an account of,
and a journey is a sequence. Wednesday's two slots stay single heroes: Reader
Engagement asks one question about one picture, and a Promo/CTA wants one thing
to look at and one place to go.
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
 # Mon 19 Oct — slot 70 — pillar 0 Book World — The Girl and The Whale — COLLAGE
 dict(day='2026-10-19', base=14, board=B_READ, pad=False,
  panels=['gds/girl-whale/book-of-legends-on-the-reef-20261001',
          'gds/girl-whale/annas-dance-at-sunset-20261007b',
          'gds/girl-whale/anna-on-the-glowing-fin-20261019',
          'gds/girl-whale/light-from-the-window-20261019'],
  alts=["A thick old leather-bound book lying open on a flat sun-bleached rock at the edge of a shallow coral reef, its weathered cream pages blank. A conch shell and a sprig of dried seaweed beside it, clear turquoise water over coral and two small yellow fish below, and green volcanic mountains across the bay in late golden light.",
        "Anna, a Black girl of about thirteen with chocolate-brown skin and long black hair, dances barefoot on wet sand at the edge of the sea at sunset, arms thrown wide and head tipped back mid-spin, her reflection in the thin sheet of water beneath her. She wears a knee-length floral sundress and a white shell necklace. The low orange sun, green volcanic mountains and two seabirds are behind her.",
        'Anna, a Pacific-island girl of about thirteen with deep chocolate-brown skin and long '
        'loose jet-black hair in a hibiscus-print sundress, standing with her arms flung wide on '
        'the long outstretched fin of an enormous humpback whale, the fin glowing cosmic purple '
        'and scattered with starlight, high above dark mountains, a pale beach, the lit windows '
        'of houses and the sea.',
        'Two island women seen from behind at an open window at night, a mother and her older '
        'mother, looking out at a strange purple glow spreading over the dark sea and hills, with '
        'a lamp, a jug of red juice and a woven mat in the warm room behind them.'],
  collage='gds/girl-whale/collage-believe-20261019',
  alt='A four-panel collage from The Girl and The Whale: a book of legends open on a rock by the '
      'reef, Anna dancing at sunset, Anna carried on the glowing purple fin of an enormous humpback '
      'high above the island, and two women at a window watching the light.',
  fb=tail("Four moments, one night.\n\nThe Girl and The Whale is a story about believing something "
    "before you have any proof of it.\n\nMr. Hooker gives Anna Hawaii's Book of Legends and tells "
    "her what to do: the dance, by the rocks at the edge of the coral reef, at sunset.\n\nShe does "
    "it. The sky glows coral and gold. Nothing happens, and she gives up.\n\nThen a purple glow — "
    "and the Cosmic Theseus Finback, the largest humpback in the world, whose fins shone brighter "
    "than all the stars in the sky combined. She lifts Anna onto a glowing fin and carries her "
    "above the mountains, beaches, houses and sea, and the people of Hawaii look up and see "
    "her.\n\nAt home, Kelani and Gran Gran see the light from the window.\n\nThese are our "
    "illustrations of four moments from the story, not pages from the book.\n\nWritten by Zhané "
    "Mackey. GDS Reading Series, Level 3. Ages 6 to 12, grades 1 to 6.\n\n" + GW),
  ig=tail("Four moments, one night. 💜\n\nMr. Hooker gives Anna the book of legends and tells her "
    "what to do: dance by the rocks at the edge of the reef, at sunset.\n\nShe does. The sky glows "
    "coral and gold. Nothing happens. She gives up.\n\nThen a purple glow — the Cosmic Theseus "
    "Finback, the largest humpback in the world, whose fins shone brighter than all the stars in "
    "the sky combined. She lifts Anna onto a glowing fin and carries her above the mountains, "
    "beaches, houses and sea.\n\nAt home, her mother and grandmother see the light from the "
    "window.\n\nSwipe for all four. Our illustrations of the story, not pages from the "
    "book.\n\nBy Zhané Mackey. Ages 6–12, grades 1–6.\n\n" + GW,
    "#TheGirlAndTheWhale #BahamianAuthors #ChildrensBooks #GDSPublications #ReadingSeries "
    "#KidsBooks #BelieveInWonder"),
  pin_t='Four moments from The Girl and The Whale',
  pin=tail("The book of legends on the reef, the dance at sunset, Anna carried on the glowing fin of "
    "the Cosmic Theseus Finback, and the light seen from a window at home. Our illustrations of four "
    "moments from the story. Written by Zhané Mackey. Ages 6 to 12, grades 1 to 6.\n\n" + GW),
  pin_url=GW),

 # Tue 20 Oct — slot 71 — pillar 1 Behind the Scenes — Going To The Regatta — COLLAGE
 dict(day='2026-10-20', base=14, board=B_LI, pad=False,
  panels=['gds/regatta/writers-desk-longisland-v2-20260905',
          'gds/regatta/sunrise-over-the-atlantic-20261016',
          'gds/regatta/midnight-drive-20261020',
          'gds/regatta/rainbow-over-the-atlantic-20261020'],
  alts=["A writer’s desk at night with a hand-drawn ink map of Long Island, a conch shell and a straw fan.",
        "Sunrise over the Atlantic from the rocky Long Island shore: the sun just clear of the horizon, the sky banded apricot and gold, a low swell rolling in and small waves running up the pale sand in a thin lace of foam. Dark ironshore rock in front, casuarinas leaning, two seabirds on the wing.",
        'A car driving home late at night on a narrow Long Island road, its headlights '
        'lighting the empty road ahead, which is lined with low scrub and leaning palms, '
        'enormous field of stars.',
        'A full bright rainbow arching over the Atlantic from the Long Island shore as a shower '
        'clears, half the sky still soft grey and half opening to blue, with a low swell rolling in '
        'and small waves running up pale sand in a thin lace of foam.'],
  collage='gds/regatta/collage-the-journey-20261020',
  alt='A four-panel collage behind Going To The Regatta: a writer\'s desk with a map of Long Island, '
      'sunrise over the Atlantic, a car on a dark island road under the stars, and a rainbow over '
      'the sea after a shower.',
  fb=tail("Behind this one there is no illustrator's desk. There is a trip.\n\nGoing To The Regatta "
    "is a true family account, written by Bridgette Skeete-Mackey and illustrated with real family "
    "photographs. So \"behind the scenes\" here means the days themselves.\n\nThe map, because the "
    "account was written from a real route — Stella Maris in the north, the long drive down to Salt "
    "Pond in the centre.\n\nThe sunrise, because the house looked out over the Atlantic and the "
    "sisters walked Stella Maris at dawn.\n\nThe dark road, because the drive home after the final "
    "regatta night was after midnight, with the fuel gauge dropping. They reached the house with "
    "one bar remaining.\n\nAnd the rainbow over the Atlantic, which is one of the places in the "
    "book's photo gallery.\n\nThese four are our illustrations. The book itself carries the "
    "photographs.\n\nGoing To The Regatta. GDS Reading Series, Family Reader, ages 5 to "
    "15.\n\n" + REG),
  ig=tail("Behind this one there's no illustrator's desk. There's a trip. 🚗\n\nGoing To The Regatta "
    "is a true family account, illustrated with real family photographs — so behind the scenes means "
    "the days themselves.\n\nThe map: the account was written from a real route, Stella Maris in the "
    "north down to Salt Pond in the centre.\n\nThe sunrise: the house looked out over the Atlantic, "
    "and the sisters walked Stella Maris at dawn.\n\nThe dark road: the drive home after the final "
    "regatta night was after midnight, fuel gauge dropping. They made it with one bar left.\n\nThe "
    "rainbow over the Atlantic, from the book's photo gallery.\n\nSwipe for all four — our "
    "illustrations. The book carries the photographs.\n\nFamily Reader, ages 5–15.\n\n" + REG,
    "#GoingToTheRegatta #LongIsland #Bahamas #FamilyStories #BahamianAuthors #GDSPublications "
    "#IslandLife"),
  pin_t='Behind Going To The Regatta — the trip itself',
  pin=tail("A map of Long Island, sunrise over the Atlantic, the drive home after midnight with the "
    "fuel gauge dropping, and a rainbow over the sea. Going To The Regatta is a true family account "
    "by Bridgette Skeete-Mackey, so behind the scenes means the days themselves. Family Reader, "
    "ages 5 to 15.\n\n" + REG),
  pin_url=REG),

 # Wed 21 Oct — slot 72 — pillar 2 Reader Engagement — ATB Lower — NEW ART
 dict(day='2026-10-21', base=14, pid='gds/atb-lower/island-lighthouse-20261021',
  pad=False, board=B_CULT,
  alt='A Bahamian lighthouse on a low rocky point, a tall slender tower in broad red and white '
      'bands with a glass lantern room at the top and a small keeper\'s cottage beside it, pale '
      'limestone running down to clear turquoise shallows. A low swell rolls in and small waves '
      'break gently over the rocks in a thin lace of foam and slide back, with ripple lines '
      'travelling across the shallows.',
  fb=tail("Which section would your child open first?\n\nAll Things Bahamian is built in seven "
    "sections: Bahamian National Symbols, Our Beautiful Islands, Historic Places and Landmarks, "
    "Life in Our Bahamian Seas, Junkanoo, Fruits of The Bahamas, and My Bahamas.\n\nThe lighthouse "
    "belongs to the third. Historic Places and Landmarks runs to forts, monuments and lighthouses — "
    "the things that have stood on these islands long enough to become landmarks.\n\nSome children "
    "go straight to Junkanoo for the colour. Some go to the seas. Some start at page one and will "
    "not be moved.\n\nTell us which one yours would go to, and why — we read every reply.\n\nThis "
    "is our illustration of the subject; in the book it is a line drawing waiting for pencils.\n\n"
    "All Things Bahamian, Lower Elementary. Grades 1 to 3. 83 pages.\n\n" + ATBL),
  ig=tail("Which section would your child open first? 🗼\n\nAll Things Bahamian has seven: National "
    "Symbols · Our Beautiful Islands · Historic Places and Landmarks · Life in Our Bahamian Seas · "
    "Junkanoo · Fruits of The Bahamas · My Bahamas.\n\nThe lighthouse belongs to the third — forts, "
    "monuments and lighthouses, the things that have stood here long enough to become "
    "landmarks.\n\nSome go straight to Junkanoo for the colour. Some go to the seas. Some start at "
    "page one and will not be moved.\n\nTell us which one yours would pick 👇\n\nOur illustration of "
    "the subject — in the book it's a line drawing waiting for pencils.\n\nGrades 1–3, 83 "
    "pages.\n\n" + ATBL,
    "#AllThingsBahamian #Bahamas #ColouringBook #BahamianKids #Lighthouse #GDSPublications "
    "#HomeschoolBahamas"),
  pin_t='Seven sections — which would your child open first?',
  pin=tail("A Bahamian lighthouse, from Historic Places and Landmarks — one of the seven sections of "
    "All Things Bahamian, alongside National Symbols, Our Beautiful Islands, Life in Our Bahamian "
    "Seas, Junkanoo, Fruits of The Bahamas and My Bahamas. Our illustration of the subject; in the "
    "book it is a line drawing waiting for pencils. Grades 1 to 3, 83 pages.\n\n" + ATBL),
  pin_url=ATBL),

 # Wed 21 Oct — slot 73 — pillar 3 Promo/CTA — Girl & Whale activity book — NEW ART
 dict(day='2026-10-21', base=19, pid='gds/girl-whale-activity/design-annas-dress-20261021',
  pad=False, board=B_COLOR,
  # 'Design Anna's Celebration Dress' is an activity title; no picture here shows her.
  anna_absent=True,
  alt='A worktable seen from above with four sheets of cream paper, each carrying a '
      'hand-drawn dress design coloured differently — one patterned with hibiscus flowers, one with '
      'small shells around the hem, one with a sweep of stars, one left as a plain outline — with a '
      'jar of coloured pencils, loose pencils, scraps of bright fabric and ribbon and a dish of '
      'shells around them. Through a window behind, calm turquoise sea moves gently under palms.',
  fb=tail("The page that gets the most out of a child who says they cannot draw.\n\nDesign Anna's "
    "Celebration Dress hands the whole thing over to them. No right answer and no model to copy — "
    "hibiscus, or shells, or a sweep of stars, whatever they decide the dance deserves. Above are "
    "four our illustrator drew while thinking about it.\n\nIt sits in a forty-page book alongside Coral Reef I-Spy, Crack the Cosmic "
    "Code, Label the Humpback Whale, Design Your Own Cosmic Finback, Create Anna's Island Route, "
    "Draw the Family Under the Stars, Cosmic Bookmarks and a certificate for the end.\n\nFive "
    "colouring pages too: Anna Hears a Song, A Story at the Docks, The Dance at Sunset, The Legend "
    "Appears, and Anna's Cosmic Ride.\n\nRead the story first, then do the book. They work better "
    "that way round.\n\nThe Girl and The Whale Coloring & Activity Book. 40 pages, ages 6 to "
    "12.\n\nReader: " + GW + "\nActivity book: " + GWA),
  ig=tail("The page that gets the most out of a child who says they can't draw. ✏️\n\nDesign Anna's "
    "Celebration Dress hands the whole thing over to them. No right answer, no model to copy — "
    "hibiscus, shells, a sweep of stars, whatever they decide the dance deserves. Above: four our "
    "illustrator drew while thinking about it.\n\nForty pages, alongside Coral Reef I-Spy, Crack the Cosmic Code, Label the Humpback "
    "Whale, Design Your Own Cosmic Finback, Draw the Family Under the Stars, Cosmic Bookmarks and a "
    "certificate at the end.\n\nPlus five colouring pages, including The Dance at Sunset and Anna's "
    "Cosmic Ride.\n\nRead the story first, then do the book 📖\n\nAges 6–12.\n\nReader: " + GW +
    "\nActivity book: " + GWA,
    "#TheGirlAndTheWhale #ActivityBook #ColouringBook #KidsActivities #BahamianAuthors "
    "#GDSPublications #CreativeKids"),
  pin_t="Design Anna's Celebration Dress",
  pin=tail("No right answer and no model to copy — the child decides what the dance deserves. One of "
    "forty pages in The Girl and The Whale Coloring & Activity Book, alongside Coral Reef I-Spy, Crack the "
    "Cosmic Code, Design Your Own Cosmic Finback and five colouring pages. Ages 6 to 12.\n\n"
    "Reader: " + GW + "\nActivity book: " + GWA),
  pin_url=GWA),
]

if __name__ == '__main__':
    run(S)
