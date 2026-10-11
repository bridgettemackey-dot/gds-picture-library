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
# MOTION. Bridge, 11 Oct 2026: "all images that contain water shows movement in
# the water. Where you are able to add movement to any other picture elements I
# want you to do so."
#
# She asked for this through a tool called Claude Motion, which this session
# cannot reach - there is no such tool here, and the Sora models on our OpenAI
# key report a shutdown date of 2026-09-24 and 404 on POST /v1/videos. Buffer
# itself WOULD take a video (VideoAssetInput: url, thumbnailUrl,
# metadata{title, thumbnailOffset}), so if a generator ever becomes reachable
# the publishing half is already in place.
#
# Until then this is the substitute, and it is a substitute: motion rendered
# INTO the still. Paste it into every prompt. It is deliberately last in the
# prompt, after the scene and the characters, because trailing instructions
# survive best.
MOTION = (
 "\n\nMOVEMENT - THIS APPLIES TO EVERY PICTURE:\n"
 "Nothing in this picture is still or posed. Catch it one moment into an action "
 "already happening.\n"
 "- WATER IS NEVER FLAT OR GLASSY unless the scene is explicitly a calm bank or "
 "pool, and even then it carries fine ripples and a moving light-sparkle. "
 "Open sea: waves mid-roll, crests tipping over, white foam actually breaking "
 "and spray thrown into the air. Shallows: ripple rings spreading, water sliding "
 "up and drawing back over sand, a wet sheen running off. Around a boat or a "
 "swimmer: a wake peeling away, bow spray, disturbed water.\n"
 "- EVERYTHING ELSE THAT CAN MOVE, MOVES: hair and clothing lifting and "
 "streaming, leaves, palm fronds, bougainvillea and grass bending in the wind, "
 "flags, bunting and sails filling and snapping, clouds stretched by wind, birds "
 "mid-wingbeat, sand or dust kicked up, steam rising off hot food, loose paper, "
 "shavings or petals caught mid-fall.\n"
 "- A person is mid-step, mid-turn, mid-reach or mid-laugh, with their weight "
 "off-centre - never standing squarely facing the viewer.\n"
 "Keep the clean flat picture-book colour. This is energy and direction, not "
 "motion blur, not speed lines, and not a photograph."
)

CHARACTERS = {'anna': ANNA, 'finback': FINBACK}

if __name__ == '__main__':
    for k, v in CHARACTERS.items():
        print('=== %s ===\n%s' % (k, v))
    print('=== motion ===%s' % MOTION)
