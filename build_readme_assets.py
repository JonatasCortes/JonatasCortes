import svgblock as svg
import random

BLOCK_WIDTH = 900
TITLE_SIZE = 30
SUBSECTION_SIZE = 20
TEXT_SIZE = 18

# ABOUT ME

light_sign = svg.Sequence(svg.FlickerIn(flickers=2),
                          svg.Show(6), loop_limit=None)
(
    svg.Block(width=BLOCK_WIDTH, animation=light_sign)
    .title("JÔNATAS CÔRTES", 30)
    .divider()
    .text("Passionate about experimenting new things and contributing to the **__python open source community__**.", TEXT_SIZE)
    .text("Mostly interested in **Machine Learning**, **LLMs**, **Automations** and **Data Engineering**.", TEXT_SIZE)
    .save("assets/title.svg")
)

# LOGOS

random.seed(0)
for logo in ("python", "pytorch", "pandas", "numpy", "postgres", "docker"):

    t_drop = random.uniform(0.7, 0.95)
    t_jelly = random.uniform(0.8, 1.1)
    t_spin = random.uniform(0.7, 0.9)
    t_hide = random.uniform(0.6, 0.85)

    jelly_wobbles = random.choice([3, 4, 5])

    logo_animation = svg.Sequence(
        svg.DropIn(
            duration=t_drop, distance=40,
            easing=svg.Bounce(bounces=5, rebound=0.6)
        ),
        svg.Sequence(
            svg.Jelly(duration=t_jelly, amount=0.15, wobbles=jelly_wobbles),
            svg.Show(1),
            loop_limit=2
        ),
        svg.SpinOut(duration=t_spin, angle=45),
        svg.Hide(t_hide),
        loop_limit=None
    )

    (
        svg.Block(animation=logo_animation, width=100, hide_frame=True)
        .image(f"logos/{logo}_logo.png")
        .save(f"assets/{logo}_logo.svg")
    )

# PROJECTS AND CONTRIBUTIONS

(
    svg.Block(width=BLOCK_WIDTH)
    .title("PROJECTS AND CONTRIBUTIONS", TITLE_SIZE)
    .divider()
    .divider(0)
    .columns(
        svg.Column()
        .divider(0)
        .divider(0)
        .divider(0)
        .divider(0)
        .image("logos/svgblock_logo.png"),
        svg.Column()
        .text("Want to make your GitHub profile **__stand out__**?", TEXT_SIZE)
        .text(" Meet __**SVGblock**__!", TEXT_SIZE)
        .text("Create beautiful, themed and animated SVG blocks with just a few lines of ##Python##.", TEXT_SIZE)
        .text(" Bring your ideas to life and use them anywhere an image fits!", TEXT_SIZE)
    )
    .divider(0)
    .divider()
    .divider(0)
    .columns(
        svg.Column()
        .divider(0)
        .image("logos/desklab_logo.png"),
        svg.Column()
        .text("Looking for an open-source ##Python GUI## library that puts you in direct control of the event loop?", TEXT_SIZE)
        .text("Meet __**DeskLab**__!", TEXT_SIZE)
        .text("DeskLab gives you greater control over:", TEXT_SIZE)
        .text("⠀⠀⠀##•## __User input__.", TEXT_SIZE)
        .text("⠀⠀⠀##•## __Event Handling__.", TEXT_SIZE)
        .text("⠀⠀⠀##•## __Concurrent Processing__.", TEXT_SIZE)
    )
    .save("assets/projects_and_contributions.svg")
)

# RESEARCH

(
    svg.Block(width=BLOCK_WIDTH)
    .title("ACADEMIC RESEARCH", TITLE_SIZE)
    .divider()
    .divider(0)
    .columns(
        svg.Column()
        .subsection("HNSW CHARACTER RECOGNITION", SUBSECTION_SIZE)
        .text("Build, train and test your own **HNSW** (Hierarchical Navigable Small World) \
              in pure ##Python## (no ML libraries involved), on the __Balanced EMNIST__ dataset \
              of handwritten characters.", TEXT_SIZE)
        .text("Explore detailed performance metrics, such as __accuracy__, total __test time__ and a \
              complete __47-class confusion matrix__.", TEXT_SIZE),
        svg.Column()
        .image("logos/hnsw_logo.png")
    )
    .save("assets/academic_research.svg")
)

# CONTACT

linkedin_animation = svg.Sequence(
    svg.PopIn(),
    svg.Drift(loop_limit=None),
)
(
    svg.Block(width=BLOCK_WIDTH, animation=linkedin_animation)
    .columns(
        svg.Column(10)
        .image(f"logos/linkedin_logo.png", width=300),
        svg.Column(1),
        svg.Column(20)
        .divider(0)
        .divider(0)
        .divider(0)
        .divider(0)
        .divider(0)
        .divider(0)
        .text("**CONTACT ⬆**", 70)
    )
    .save(f"assets/linkedin.svg")
)

gmail_animation = svg.Sequence(
    svg.PopIn(),
    svg.Show(3),
    svg.Drift(loop_limit=None)
)
(
    svg.Block(width=BLOCK_WIDTH, animation=gmail_animation)
    .columns(
        svg.Column(10)
        .image(f"logos/gmail_logo.png", width=300),
        svg.Column(1),
        svg.Column(20)
        .divider(0)
        .divider(0)
        .divider(0)
        .divider(0)
        .text("**CONTACT ⬆**", 70)
    )
    .save(f"assets/gmail.svg")
)
