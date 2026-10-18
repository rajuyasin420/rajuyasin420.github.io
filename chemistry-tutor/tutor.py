from manim import *
import numpy as np

# A self-contained teaching animation built on the existing Manim Community engine.
# Use schematic 2D projections for clarity; angles and shape labels are explicit.

BG = "#101522"
ACCENT = "#65D6CE"
ATOM = "#F3F5FA"
BOND = "#B7C3D7"
LONE = "#F6B84A"
TEXT = "#F3F5FA"
MUTED = "#B7C3D7"

class MolecularShapesTutor(Scene):
    def construct(self):
        self.camera.background_color = BG
        self.title_card()
        self.repulsion()
        self.shape("LINEAR", "CO₂", "2 bonding regions • 0 lone pairs", "180°", [180], "The two regions spread to opposite sides.")
        self.shape("TRIGONAL PLANAR", "BF₃", "3 bonding regions • 0 lone pairs", "120°", [120, 120, 120], "Three regions lie in one plane, 120° apart.")
        self.shape("TETRAHEDRAL", "CH₄", "4 bonding regions • 0 lone pairs", "109.5°", [109.5]*4, "Four bonding pairs point towards the corners of a tetrahedron.")
        self.shape("TRIGONAL PYRAMIDAL", "NH₃", "3 bonding regions • 1 lone pair", "≈107°", [107]*3, "One lone pair repels more strongly, squeezing the N–H bonds closer together.")
        self.shape("BENT", "H₂O", "2 bonding regions • 2 lone pairs", "≈104.5°", [104.5]*2, "Two lone pairs squeeze the O–H bonds even closer.")
        self.exam_method()
        self.quiz()

    def heading(self, eyebrow, title, subtitle=None):
        top = Text(eyebrow, font_size=22, color=ACCENT, weight=MEDIUM).to_edge(UP, buff=0.42)
        main = Text(title, font_size=38, color=TEXT, weight=BOLD).next_to(top, DOWN, buff=0.25)
        group = VGroup(top, main)
        if subtitle:
            sub = Text(subtitle, font_size=21, color=MUTED).next_to(main, DOWN, buff=0.18)
            group.add(sub)
        group.move_to([0, 2.55 if subtitle else 2.65, 0])
        self.play(FadeIn(group, shift=DOWN*0.15), run_time=0.7)
        return group

    def tutor_line(self, text, wait=2.4):
        line = Text(text, font_size=22, color=TEXT, line_width=12, should_center=True)
        line.to_edge(DOWN, buff=0.48)
        panel = SurroundingRectangle(line, color="#35445D", buff=0.18, corner_radius=0.12)
        panel.set_fill("#1B2538", opacity=1)
        self.play(FadeIn(panel), Write(line), run_time=0.55)
        self.wait(wait)
        self.play(FadeOut(VGroup(panel, line)), run_time=0.35)

    def title_card(self):
        kicker = Text("OCR A-LEVEL CHEMISTRY", font_size=24, color=ACCENT, weight=BOLD)
        title = Text("MOLECULAR SHAPES", font_size=46, color=TEXT, weight=BOLD)
        subtitle = Text("Your personal tutor • See the shape, explain the angle", font_size=22, color=MUTED)
        group = VGroup(kicker, title, subtitle).arrange(DOWN, buff=0.35)
        self.play(FadeIn(group, shift=UP*0.25), run_time=1)
        self.wait(1.8)
        self.play(FadeOut(group), run_time=0.5)
        self.tutor_line("By the end, you should predict shapes and justify bond angles.", 2.2)

    def repulsion(self):
        h = self.heading("THE CORE IDEA", "Electron-pair repulsion", "Electron density around the central atom")
        center = Dot(ORIGIN, radius=0.16, color=ACCENT)
        center_label = Text("central atom", font_size=18, color=MUTED).next_to(center, DOWN, buff=0.25)
        dirs = [UP, DOWN, LEFT, RIGHT]
        pairs = VGroup()
        for i, d in enumerate(dirs):
            pos = d * 1.05
            dot = Dot(pos, radius=0.13, color=LONE if i == 0 else ATOM)
            arrow = Arrow(center.get_center(), pos*0.72, buff=0.18, color=ACCENT, stroke_width=3, max_tip_length_to_length_ratio=0.16)
            pairs.add(VGroup(arrow, dot))
        self.play(FadeIn(center), FadeIn(center_label), LaggedStart(*[Create(x) for x in pairs], lag_ratio=0.2), run_time=1.4)
        self.tutor_line("Electron pairs repel, so they arrange as far apart as possible.", 2.6)
        self.tutor_line("Lone pair–lone pair repulsion > lone pair–bond pair > bond pair–bond pair.", 3)
        self.play(FadeOut(VGroup(h, center, center_label, pairs)), run_time=0.5)

    def shape(self, name, formula, regions, angle, angles, explanation):
        h = self.heading("MOLECULAR GEOMETRY", name, f"{formula}   |   {regions}")
        center = Dot([0, -0.1, 0], radius=0.16, color=ACCENT)
        center_text = Text(formula, font_size=25, color=ACCENT, weight=BOLD).next_to(center, DOWN, buff=0.25)
        if formula == "CO₂":
            dirs = [LEFT*2.4, RIGHT*2.4]
        elif formula == "BF₃":
            dirs = [UP*1.65, rotate_vector(DOWN, PI/6)*1.9, rotate_vector(DOWN, -PI/6)*1.9]
        elif formula == "CH₄":
            dirs = [UP*1.65, rotate_vector(DOWN, PI/5)*1.8, rotate_vector(DOWN, -PI/5)*1.8, DOWN*1.6]
        elif formula == "NH₃":
            dirs = [UP*1.6, rotate_vector(DOWN, PI/5)*1.8, rotate_vector(DOWN, -PI/5)*1.8]
        else:
            dirs = [rotate_vector(UP, PI/4)*1.8, rotate_vector(UP, -PI/4)*1.8]
        atoms = VGroup()
        bonds = VGroup()
        labels = VGroup()
        for i, d in enumerate(dirs):
            endpoint = center.get_center()+d
            bonds.add(Line(center.get_center(), endpoint, color=BOND, stroke_width=6))
            atom = Dot(endpoint, radius=0.17, color=ATOM)
            atoms.add(atom)
            labels.add(Text("X", font_size=18, color=BG, weight=BOLD).move_to(atom))
        self.play(Create(bonds), FadeIn(center), FadeIn(center_text), LaggedStart(*[FadeIn(a) for a in atoms], lag_ratio=0.12), run_time=1)
        self.play(LaggedStart(*[FadeIn(l) for l in labels], lag_ratio=0.08), run_time=0.35)
        angle_text = Text(f"Bond angle: {angle}", font_size=28, color=ACCENT, weight=BOLD).move_to([0, -1.65, 0])
        self.play(Write(angle_text), run_time=0.5)
        if formula in ("NH₃", "H₂O"):
            lp_positions = [np.array([0.0, 1.25, 0.0])] if formula == "NH₃" else [np.array([-0.55, 1.15, 0.0]), np.array([0.55, 1.15, 0.0])]
            lone_pairs = VGroup()
            for p in lp_positions:
                lone_pairs.add(Dot(p, radius=0.10, color=LONE), Dot(p+np.array([0.18,0.06,0]), radius=0.10, color=LONE))
            self.play(FadeIn(lone_pairs), run_time=0.4)
            lp_label = Text("lone pair(s)", font_size=17, color=LONE).next_to(lone_pairs, UP, buff=0.08)
            self.play(FadeIn(lp_label), run_time=0.3)
        else:
            lone_pairs = VGroup()
            lp_label = VGroup()
        self.tutor_line(explanation, 2.7)
        self.play(FadeOut(VGroup(h, center, center_text, atoms, bonds, labels, angle_text, lone_pairs, lp_label)), run_time=0.5)

    def exam_method(self):
        h = self.heading("OCR EXAM TECHNIQUE", "Build a full-mark explanation", "Don't stop at naming the shape")
        steps = [
            ("1", "Count regions of electron density around the central atom."),
            ("2", "Name the molecular shape from the atom positions."),
            ("3", "State the expected or observed bond angle."),
            ("4", "If lone pairs exist, explain the angle decrease using stronger repulsion."),
        ]
        rows = VGroup()
        for n, s in steps:
            num = Text(n, font_size=24, color=ACCENT, weight=BOLD)
            txt = Text(s, font_size=20, color=TEXT, line_width=10)
            rows.add(VGroup(num, txt).arrange(RIGHT, buff=0.3, aligned_edge=UP))
        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.32).move_to([0, 0.25, 0])
        self.play(LaggedStart(*[FadeIn(r, shift=RIGHT*0.12) for r in rows], lag_ratio=0.18), run_time=1.4)
        self.tutor_line("Model answer: NH₃ is trigonal pyramidal, about 107°. A lone pair repels more strongly than bonding pairs, reducing the H–N–H angle from 109.5°.", 3.8)
        self.play(FadeOut(VGroup(h, rows)), run_time=0.5)

    def quiz(self):
        h = self.heading("YOUR TURN", "Pause and predict", "Say your answer before the reveal")
        qs = [
            ("1. CH₄: shape and angle?", "Tetrahedral • 109.5°"),
            ("2. Why is NH₃ about 107°?", "One lone pair repels more strongly than bonding pairs."),
            ("3. Why is H₂O about 104.5°?", "Two lone pairs cause greater compression of the bond angle."),
        ]
        for q, a in qs:
            question = Text(q, font_size=30, color=TEXT, weight=BOLD, line_width=12)
            question.move_to([0, 0.5, 0])
            self.play(Write(question), run_time=0.65)
            self.wait(2.5)
            answer = Text(a, font_size=22, color=ACCENT, line_width=12)
            answer.next_to(question, DOWN, buff=0.5)
            self.play(FadeIn(answer, shift=UP*0.12), run_time=0.5)
            self.wait(2.4)
            self.play(FadeOut(VGroup(question, answer)), run_time=0.4)
        closing = VGroup(
            Text("Remember:", font_size=28, color=ACCENT, weight=BOLD),
            Text("count regions → predict arrangement → account for lone pairs", font_size=23, color=TEXT)
        ).arrange(DOWN, buff=0.3)
        self.play(FadeIn(closing), run_time=0.8)
        self.wait(2.5)
        self.play(FadeOut(VGroup(h, closing)), run_time=0.5)
