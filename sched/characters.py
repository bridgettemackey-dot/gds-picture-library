# -*- coding: utf-8 -*-
"""Prompt blocks pasted verbatim into image prompts: characters, and motion.

PASTE THESE INTO EVERY IMAGE PROMPT THAT CONTAINS THE CHARACTER. Do not
paraphrase them, do not summarise them, and do not write your own from memory.

Why this file exists: on 4 Oct 2026 a picture of Anna went into the Buffer queue
with fair skin and two brown pigtail braids. The prompt that produced it spent
its whole length on her AGE and never mentioned her appearance at all, even
though BOOK-CONTEXT.md and SOCIAL-RUNBOOK.md both carried the description.
Knowing the rule was not enough; the prompt has to carry it. So it lives here as
a string a script imports, not as prose a future run has to remember to re-derive.

    from characters import ANNA, MOTION
    prompt = "A children's picture-book illustration of ...\n\n" + ANNA + MOTION
"""

# The Girl and The Whale. The book says: "Chocolate-brown skin. Her hair was
# darker than the stripes on a zebra." Canonical references in Cloudinary:
#   gds/girl-whale/page12-anna-20260828   (her character portrait, page 12)
#   gds/girl-whale/cover-20260825         (the cover)
ANNA = (
 "ANNA'S APPEARANCE IS FIXED BY THE BOOK AND MUST NOT BE CHANGED:\n"
 "- SKIN: deep chocolate-brown skin. She is a Black Pacific-island girl. Her skin is "
 "rich warm dark brown, NOT fair, NOT light, NOT olive, NOT tan.\n"
 "- HAIR: jet black with a blue-black sheen, darker than the stripes on a zebra. It is "
 "LONG and falls loose past her shoulders, thick and softly wavy, parted in the middle, "
 "with a single braid running back across the crown of her head like a headband. NOT "
 "brown hair, NOT two pigtails, NOT twin braids, NOT short hair, NOT tight coils, NOT a puff.\n"
 "- EYES: large warm dark brown eyes. Round soft face, full lips, a few freckles across "
 "the nose.\n"
 "- CLOTHES: a knee-length sundress with thin spaghetti straps in a bright hibiscus and "
 "plumeria print - coral, pink and white flowers with green leaves on a cream ground - "
 "and a white cowrie shell necklace at her throat. Barefoot.\n"
 "- AGE: she is THIRTEEN. Halfway between a child and a teenager and neither extreme. "
 "Not a little girl: no toddler proportions, no oversized head, no baby face. Not "
 "fifteen or older: no long slender legs, no tall elegant silhouette, no defined waist, "
 "no curves, no make-up, nothing fashion-illustration-like. A shortish, straight, "
 "flat-built girl with slightly knobbly knees and elbows and an unselfconscious grin - "
 "a first-year secondary school pupil.\n")

# The Girl and The Whale. FEMALE. "Her fins glowed a cosmic purple."
FINBACK = (
 "THE COSMIC THESEUS FINBACK IS FIXED BY THE BOOK: an enormous humpback whale, the "
 "largest in the world, SHE not he. Her body is deep ocean blue-black and her long "
 "pectoral fins glow a cosmic purple scattered with starlight, brighter than all the "
 "stars in the sky combined. She carries the scar of a comet strike.\n")

# ---------------------------------------------------------------------------
# MOTION. Bridge asked on 11 Oct 2026 for movement in every picture, and for
# water in particular to show movement. She REVISED THAT THE SAME DAY, after
# seeing the result: "Let the waters remain calm. Only the rough side of the
# Glass Window Bridge should be choppy."
#
# So the rule now has two halves pulling opposite ways, and the water half is the
# one that changed:
#   WATER  -> CALM. Serene, clear, glassy Bahamian turquoise. This is the look of
#             the books and of the islands, and rough sea is off-brand.
#   EVERYTHING ELSE -> still alive, but in a LIGHT BREEZE, not a gale. Big bent
#             trees and flying spray were the over-correction; they are gone.
#
# The one exception is a subject that IS rough water: the Atlantic side of the
# Glass Window Bridge, where the whole point is calm Bight against open ocean.
# Name that explicitly in the scene text when you want it.
#
# She also asked for actual animation, through a tool called Claude Motion. It is
# not reachable here and Sora 404s on our key, so this is movement rendered into a
# still. Buffer would take a video (VideoAssetInput) if a generator ever appears.
MOTION = (
 "\n\nSTILLNESS AND MOVEMENT - THIS APPLIES TO EVERY PICTURE:\n"
 "- WATER IS CALM. Bahamian water is serene, clear and glassy: smooth turquoise "
 "shallows you can see the sand through, a quiet sea, at most a soft lapping edge "
 "at the shore and a gentle sheen of light on the surface. NO rough or stormy sea, "
 "NO rearing or breaking waves, NO whitecaps, NO churning white foam, NO spray in "
 "the air. If the scene has open ocean in it, that ocean is calm too.\n"
 "- THE AIR IS MOVING, GENTLY. A light breeze, not a gale: hair and a dress "
 "stirring, palm fronds and leaves swaying, a flag or bunting lifting and rippling, "
 "birds on the wing, steam drifting off hot food, a petal or a leaf falling. Trees "
 "lean slightly; they are never bent over.\n"
 "- PEOPLE ARE MID-ACTION. Mid-step, mid-turn, mid-reach or mid-laugh, weight "
 "a little off-centre - never standing squarely facing the viewer.\n"
 "Clean flat picture-book colour. Calm water, light air, a moment in progress - "
 "not motion blur, not speed lines, not a photograph."
)

CHARACTERS = {'anna': ANNA, 'finback': FINBACK}

if __name__ == '__main__':
    for k, v in CHARACTERS.items():
        print('=== %s ===\n%s' % (k, v))
    print('=== motion ===%s' % MOTION)
