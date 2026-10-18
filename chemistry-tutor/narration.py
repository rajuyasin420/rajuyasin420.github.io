"""Generate a spoken tutor track for the molecular-shapes lesson."""
import asyncio
import edge_tts

SCRIPT = """
Welcome to your OCR A-level Chemistry tutorial on molecular shapes. I am your personal chemistry tutor. By the end, you should be able to predict common shapes, recall their bond angles, and explain why lone pairs change those angles.

Start with the key rule: regions of electron density repel one another. Around a central atom, they arrange themselves as far apart as possible. Count each bonding region as one region, even when the bond is a double bond. Lone pairs repel more strongly than bonding pairs. The order is lone pair against lone pair, then lone pair against bonding pair, then bonding pair against bonding pair.

First, carbon dioxide is linear. There are two bonding regions around carbon and no lone pairs on that central atom. They point in opposite directions, giving an angle of one hundred and eighty degrees.

Next, boron trifluoride is trigonal planar. Three bonding regions spread out in one plane, each separated by one hundred and twenty degrees.

Methane is tetrahedral. Four bonding regions spread towards the corners of a tetrahedron. Its bond angle is one hundred and nine point five degrees. Remember, tetrahedral describes the three-dimensional arrangement, not a flat square or cross.

Now compare ammonia. Nitrogen has three bonding pairs and one lone pair. The electron-pair arrangement is tetrahedral, but the shape named from the atoms is trigonal pyramidal. The lone pair repels more strongly and compresses the bond angle to about one hundred and seven degrees.

Water has two bonding pairs and two lone pairs around oxygen. The molecular shape is bent, sometimes called V-shaped. The two lone pairs compress the H–O–H angle further, to about one hundred and four point five degrees.

For an OCR-style explanation, do not merely write that the angle decreases. Name the shape, give the angle, then explain that lone pairs repel more strongly than bonding pairs, so the bonding pairs are pushed closer together.

Pause now and answer aloud. What is the shape and angle of methane? Tetrahedral, one hundred and nine point five degrees. Why is ammonia about one hundred and seven degrees? One lone pair repels more strongly than bonding pairs. Why is water about one hundred and four point five degrees? Two lone pairs cause even greater compression.

Your method is simple: count regions around the central atom, identify the arrangement and molecular shape, recall the angle, and explain lone-pair repulsion when needed. That is the core of molecular shapes. Replay the lesson and try to say each answer before I do.
"""
async def main():
    communicate = edge_tts.Communicate(SCRIPT, voice="en-GB-RyanNeural", rate="-4%", pitch="-2Hz")
    await communicate.save("chemistry-tutor/narration.mp3")
if __name__ == "__main__":
    asyncio.run(main())
