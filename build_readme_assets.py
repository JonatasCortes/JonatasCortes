import svgblock as svg

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

logo_animation = svg.Sequence(
    svg.DropIn(easing=svg.Bounce(bounces=5, rebound=0.6)),
    svg.Sequence(svg.Jelly(), svg.Show(1), loop_limit=2),
    svg.SpinOut(),
    svg.Hide(0.7),
    loop_limit=None
)

for logo in ("python", "pytorch", "pandas", "numpy", "postgres", "docker"):
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

contact_animation = svg.Sequence(
    svg.PopIn(),
    svg.Sequence(
        svg.Pulse(duration=2, loop_limit=1),
        svg.Pulse(duration=0.2, loop_limit=1),
        loop_limit=2
    ),
    svg.Pulse(duration=2, loop_limit=1),
    svg.PopOut(),
    svg.Hide(1),
    loop_limit=None
)
(
    svg.Block(width=BLOCK_WIDTH, animation=contact_animation)
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
(
    svg.Block(width=BLOCK_WIDTH, animation=contact_animation)
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
