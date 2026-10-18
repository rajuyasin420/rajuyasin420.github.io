# OCR A-level Chemistry: Molecular Shapes Tutor

A short, visual personal-tutor lesson on molecular shapes, electron-pair repulsion and bond angles.

## Built with an existing open-source animation engine

This project uses [Manim Community](https://github.com/ManimCommunity/manim), with molecular diagrams drawn directly in Manim so the build does not depend on a fragile chemistry-plugin API. The lesson is written for OCR A-level Chemistry and covers electron domains, lone-pair repulsion, shapes and angles, followed by retrieval questions.

## Render locally

Install Manim and its system dependencies using the official guide: https://docs.manim.community/en/stable/installation.html

```bash
python -m pip install manim
manim -p -qh tutor.py MolecularShapesTutor
```

The MP4 is written under `media/videos/tutor/1080p60/`.

## Render on GitHub

Open **Actions → Render OCR Chemistry Tutor Video → Run workflow**. When the workflow completes, download the `ocr-molecular-shapes-tutor` artifact. GitHub Actions is used to render the video; no API key is required.

## Lesson scope

- Electron pairs repel and arrange themselves as far apart as possible.
- Bonding pairs and lone pairs; lone pairs repel more strongly.
- Linear (180°), trigonal planar (120°), tetrahedral (109.5°), trigonal pyramidal (about 107°), and bent water (about 104.5°).
- Exam answer structure: state shape, state angle, explain repulsion and lone-pair distortion.
- Quick recall questions with answers revealed after thinking time.

The video uses on-screen tutor narration/captions. It does not claim to be an official OCR resource; check your current OCR specification and teacher's guidance for the exact assessed scope.
