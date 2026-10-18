# OCR A-level Chemistry: Molecular Shapes Tutor

A visual, spoken personal-tutor lesson on molecular shapes, electron-pair repulsion and bond angles.

## Built from an existing open-source project

This uses the existing [Manim Community animation engine](https://github.com/ManimCommunity/manim). GitHub Actions renders the animation and generates a UK-English tutor voice track using Edge TTS, then muxes narration into the MP4. No paid API key is required.

## Get the video

Open the repository's **Actions** tab, select **Render OCR Chemistry Tutor Video**, then open the latest successful run and download the `ocr-molecular-shapes-tutor` artifact. The artifact contains the narrated MP4. Runs are also triggered when the lesson source changes.

## Lesson contents

- Electron-pair repulsion and the relative strength of lone-pair repulsion.
- Linear CO₂ — 180°.
- Trigonal planar BF₃ — 120°.
- Tetrahedral CH₄ — 109.5°.
- Trigonal pyramidal NH₃ — approximately 107°.
- Bent H₂O — approximately 104.5°.
- An OCR-style answer structure and retrieval questions with pauses before the answer reveal.

The molecule diagrams are schematic projections for teaching; they are not intended as precise 3D molecular models. This is an independent study aid, not an official OCR resource. Check your current OCR specification and teacher's guidance for the exact assessed scope.

## Render locally

Install Manim and its system dependencies using the official guide: https://docs.manim.community/en/stable/installation.html

```bash
python -m pip install "manim>=0.18,<0.20" edge-tts
manim -qh tutor.py MolecularShapesTutor
python narration.py
```

The rendered MP4 is written under `media/videos/tutor/1080p60/`.
