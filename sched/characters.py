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
# MOTION. This took three passes with Bridge on 11-14 Oct 2026 and the THIRD is
# the live one. The two earlier readings were both over-corrections, so they are
# written out here to stop anyone swinging back to either.
#
#   1. "all images that contain water shows movement in the water"  -> read as
#      ROUGH. Rearing surf, flying spray, trees bent double. Wrong.
#   2. "Let the waters remain calm"                                 -> read as
#      FLAT. Glassy, mirror-smooth, dead. Also wrong.
#   3. "any single frame image that includes water should have movement in the
#      water. Most should be calm movement."                        <- THIS ONE.
#
# So: water ALWAYS moves, and the movement is almost always GENTLE. Calm is not
# the same as still. A quiet sea still swells, laps, ripples and shifts the light;
# that is what she wants, and a mirror finish is as wrong as a storm.
#
# The one place rough water belongs is the Atlantic side of the Glass Window
# Bridge, where calm Bight against open ocean IS the subject. Name it in the scene
# text. "Most should be calm" leaves room for a genuinely energetic subject, but
# treat that as the rare exception, not a licence.
#
# She also asked for real animation, through a tool called Claude Motion. It is not
# reachable here and Sora 404s on our key, so this is movement rendered into a
# still. Buffer would take a video (VideoAssetInput) if a generator ever appears.
MOTION = (
 "\n\nMOVEMENT - THIS APPLIES TO EVERY PICTURE:\n"
 "- THE WATER IS ALWAYS MOVING, AND THE MOVEMENT IS GENTLE. Never a mirror, never "
 "glassy, never dead flat - but never rough either. A low swell rolling slowly in; "
 "small waves tipping over and running up the sand in a thin lace of white foam, "
 "with the last wash sliding back; ripple lines travelling across the shallows; "
 "light shifting and flickering in bands over the sand below; a soft wake "
 "spreading behind a boat. Calm, clear Bahamian turquoise - alive, not agitated. "
 "NO storm sea, NO rearing or crashing waves, NO whitecaps across open water, NO "
 "churning foam, NO spray thrown into the air.\n"
 "- THE AIR IS MOVING, GENTLY. A light breeze: hair and a dress stirring, palm "
 "fronds and leaves swaying, a flag or bunting lifting and rippling, birds on the "
 "wing, steam drifting off hot food, a leaf or petal falling. Trees lean a little; "
 "they are never bent over.\n"
 "- PEOPLE ARE MID-ACTION. Mid-step, mid-turn, mid-reach or mid-laugh, weight a "
 "little off-centre - never standing squarely facing the viewer.\n"
 "Clean flat picture-book colour. A quiet moment that is plainly in motion - not "
 "motion blur, not speed lines, not a photograph."
)

CHARACTERS = {'anna': ANNA, 'finback': FINBACK}



# A queen conch is NOT a garden snail. The 18 Oct render gave it a broad gliding
# sole, thin curved antennae and black beady eyes, because the prompt said only
# "its foot and two eyestalks are out of the shell" and the model filled in the
# only snail it knew. Paste this whenever a LIVE conch appears.
CONCH = (
 "\n\nTHE QUEEN CONCH IS NOT A SNAIL. DRAW IT FROM LIFE:\n"
 "- EYES: this is the thing that matters most. Two LARGE, BRIGHT GOLDEN-YELLOW eyes, each with a "
 "small round black pupil, like two little yellow lamps. Each eye sits on the end of a THICK, "
 "STOUT, FLESHY eyestalk held UP and FORWARD, and a slender sensory tentacle branches off the "
 "side of each stalk. NOT black beady dots, NOT long thin curved antennae, NOT a snail's "
 "tentacles sweeping backwards.\n"
 "- PROBOSCIS: a long flexible snout reaches forward and down from between the eyestalks to the "
 "sand. A snail has no snout; a conch does. It must be there.\n"
 "- FOOT: NARROW, muscular and tucked, not a broad flat sole. A conch does NOT glide or creep. It "
 "VAULTS - it digs a hard, dark, claw-shaped sickle of an operculum into the sand at the end of "
 "the foot and pole-vaults forward. Show that narrow foot and the dark claw-like operculum. NO "
 "wide creeping snail-foot spread out on the sand.\n"
 "- BODY: mottled grey-brown speckled with dark flecks. NOT golden, NOT a snail's soft tan.\n"
 "- SHELL: heavy and solid, carried TILTED with the aperture turned down and sideways towards the "
 "sand - never sitting upright on the animal's back like a garden snail's shell. A short conical "
 "spire with a row of blunt knob-like spines along the shoulder of the big last whorl. The "
 "OUTSIDE is dull sandy cream and tan, weathered, dusted with sand and a little algae - it is "
 "camouflage. The glossy DEEP PINK is ONLY inside the aperture and on the inner face of the "
 "flared lip. That lip is THICK and ROLLED, like a heavy wave of shell - not a thin fan.\n")

CHARACTERS['conch'] = CONCH

if __name__ == '__main__':
    for k, v in CHARACTERS.items():
        print('=== %s ===\n%s' % (k, v))
    print('=== motion ===%s' % MOTION)
