import inspect
from datetime import datetime
from pathlib import Path

import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image, ImageDraw, ImageFont

PROFILE = {
    "name": "Michael Lois Z. Gaviola",                   
    "section": "F2",          
    "program": "BS Computer Science",         
    "year_level": "3rd Year",            
    "school": "Cebu Institute of Technology - University",         
    "tagline": "Learn from your mistake.", 
    "location": "Talisay City, Cebu, Philippines",        
    "photo": "assets/profile.png",            
    "short_bio": (
        "I am a third-year Bachelor of Science in Computer Science student at "
        "Cebu Institute of Technology - University, aspiring to become a software "
        "engineer who solves problems and develops innovative solutions."
    ),
}

STATS = {
    "Years coding": 3,
    "Projects built": 3,
    "Hackathons": 1,
    "Cups of coffee / day": 2,
}

FACTS = {
    "What got you into tech?": "When I was in high school, I developed a calculator that sparked my interest in technology.",
    "What's your dream job?": "I aspire to become a software engineer.",
    "Describe yourself in 3 words": "Curious, Observative, Friendly.",
    "What are you learning right now?": "I am still learning Python, and I am continuing to improve my programming skills by practicing regularly and exploring different concepts.",
}

INTERESTS = {
    "Gaming": "I like playing Roblox for fun, Valorant and ML for competitive, and Open-world games for exploration.",
    "Music": "I like listening to both OPM and International Musics.",
    "Reading": "I like reading manga, manhwa and any books that got me interested.",
    "Sports": "I am interested in playing badminton and pickleball.",
    "Food": "My favorite foods are fries and other potato-based dishes.",
}

STORY = {
    "Where I come from": {
        "short": "I come from Talisay City, Cebu.",
        "full": (
            "I come from Talisay City, Cebu, a vibrant and developing city known "
            "for its rich culture, welcoming community, and beautiful surroundings. "
            "Growing up there has shaped my experiences, values, and perspective, "
            "helping me appreciate the importance of hard work, resilience, and community."
        ),
    },
    "School years": {
        "short": "My school life before college was relatively worry-free, allowing me "
        "to enjoy my time, explore my interests, and do the things I wanted without facing too many responsibilities or pressures.",
        "full": (
            "My school life before college was relatively worry-free. During that time, "
            "I could enjoy learning, spend time with my friends, participate in activities, "
            "and pursue the things that interested me without having to deal with too many "
            "serious responsibilities or pressures. It was a memorable period of my life "
            "because I had the freedom to explore my interests, have fun, and enjoy each day "
            "while gradually preparing myself for the challenges of college."
        ),
    },
    "College years": {
        "short": "These were the years when I became more focused on my academic performance "
        "and worked hard to achieve meaningful results.",
        "full": (
            "These were the years when I became more focused and determined to improve my "
            "academic performance. I dedicated more time and effort to my studies, strengthened "
            "my understanding of different subjects, and worked consistently to achieve better "
            "results. Through discipline, perseverance, and commitment, I was able to grow as a "
            "student and become more confident in my abilities."
        ),
    },
    "Where I'm headed": {
        "short": "I set a clear goal for myself to graduate with a degree in Computer Science and "
        "eventually secure a good job in the technology industry.",
        "full": (
            "I set clear and meaningful goals for myself: to successfully graduate with a degree "
            "in Computer Science and build a rewarding career in the technology industry. I am "
            "committed to working hard, continuously improving my technical skills, and gaining "
            "valuable experience so that I can secure a good job and become a capable software "
            "professional in the future."
        ),
    },
}

MILESTONES = [
    {"year": 2024, "title": "Started college as Computer Science student",
     "detail": "I got interested in tech industry."},
    {"year": 2024, "title": "Improved my programming skills",
     "detail": "Consistently practicing improved my skills."},
    {"year": 2025, "title": "Created our first Capstone Project",
     "detail": "We developed our very first large programming as a group."},
    {"year": 2025, "title": "Developed my first mobile app",
     "detail": "We have a project where we have to develop a mobile app alone."},
    {"year": 2026, "title": "Joined my first hackathon",
     "detail": "The hackathon is still ongoing."},
]

EDUCATION = pd.DataFrame(
    [
        {"Level": "Senior High School", "School": "St. Scholastica's Academy - Tabunok", "Years": "2018 - 2024", "Notes": "STEM"},
        {"Level": "College", "School": PROFILE["school"], "Years": "2024 - present", "Notes": PROFILE["program"]},
    ]
)

SKILLS = pd.DataFrame(
    [
        {"Skill": "C",             "Category": "Programming", "Years": 1.0},
        {"Skill": "C++",           "Category": "Programming", "Years": 1.0},
        {"Skill": "Java",          "Category": "Programming", "Years": 1.5},
        {"Skill": "Assembly",      "Category": "Programming", "Years": 0.5},
        {"Skill": "Javascript",    "Category": "Programming", "Years": 1.5},
        {"Skill": "Kotlin",        "Category": "Programming", "Years": 0.5},
        {"Skill": "Python",        "Category": "Programming", "Years": 0.5},
        {"Skill": "SQL",           "Category": "Data",        "Years": 1.0},
        {"Skill": "Git & GitHub",  "Category": "Tools",       "Years": 2.0},
        {"Skill": "HTML / CSS",    "Category": "Programming", "Years": 2.0},
        {"Skill": "Machine Learning", "Category": "AI",       "Years": 0.5},
        {"Skill": "Communication", "Category": "Soft skills", "Years": 5.0},
        {"Skill": "Teamwork",      "Category": "Soft skills", "Years": 5.0},
    ]
)

PROJECTS = [
    {
        "title": "NeighborKnock",
        "role": "Sole Developer",
        "tools": ["Android", "Kotlin", "Git & GitHub"],
        "outcome": "A mobile app that lets neighbors borrow and lend an item in the neighborhood.",
        "link": "https://github.com/TocciFrame/NeighborKnock",
        "year": 2026, "status": "Not Completed",
        "description": (
            "NeighborKnock is an Android application that lets neighbors lend and borrow everyday items "
            "within their community. Users can register, log in, browse available items by category on the "
            "Dashboard, mark items as favorites, add new listings with a camera or gallery photo, and manage "
            "their own listed items through a Profile screen. Key features include category filtering, real-time "
            "search, a bottom sheet notification panel, lending rules per item, and item status badges (Available / Lent)."
        ),
        "image": "assets/project1.png",
    },
    {
        "title": "WildDocs",
        "role": "Full-Stack Developer",
        "tools": ["PHP", "PostgreSQL", "Supabase", "HTML", "CSS", "JavaScript", "Git & GitHub"],
        "outcome": "Developed a centralized document request system with request tracking, "
        "payment management, automated notifications, and administrative request processing, "
        "providing students and administrators with a unified workflow.",
        "link": "https://github.com/nathanaelandrew/WildDocs",
        "year": 2026, "status": "Completed",
        "description": "A web-based document request management system that enables students "
        "to request academic documents, monitor request statuses, manage payment records, "
        "and view notifications. Implemented an administrative dashboard for processing requests, "
        "managing payments, tracking request statuses, searching records, and archiving completed "
        "requests. Integrated a PostgreSQL database hosted on Supabase to manage application data "
        "and support student and administrator workflows.",
        "image": "assets/project2.png",
    },
    {
        "title": "LIGTAS-Brgy.",
        "role": "Full-Stack Developer",
        "tools": ["Java", "JavaFX", "FXML", "PostgreSQL", "Supabase", "JDBC", "Maven", "Git & Github"],
        "outcome": "Developed a centralized disaster management application integrating incident "
        "tracking, emergency responder dispatch, vulnerable resident monitoring, resource inventory, "
        "evacuation center management, broadcast alerts, and automated report generation in one system.",
        "link": "https://github.com/trealcoseba/CSIT228-Capstone",
        "year": 2026, "status": "Completed",
        "description": "Collaborated on LIGTAS-Brgy (Local Integrated Guard & Task-Alert System for Barangays), "
        "a Java desktop application designed to support barangay officials in disaster preparedness and emergency "
        "response. Implemented integrated workflows for incident management, emergency resource monitoring, "
        "responder dispatch, resident vulnerability tracking, evacuation center occupancy, and public alert "
        "broadcasting. Developed reporting capabilities with PDF and Word document exports, analytics dashboards. "
        "Used JavaFX for the desktop interface and Supabase-hosted PostgreSQL for centralized data management, "
        "applying MVC architecture and design patterns to maintain modularity and separation of concerns.",
        "image": "assets/project3.png",
    },
]

CONTACT = {
    "email": "michaelgaviola50@gmail.com",                     
    "github": "https://github.com/TocciFrame",    
    
}

STRETCH = (
    {"width": "stretch"}
    if "width" in inspect.signature(st.button).parameters
    else {"use_container_width": True}
)

def make_page_icon(name: str, size: int = 256) -> Image.Image:
    """Unique browser-tab icon: gradient rounded tile with your initials (first + last name)."""
    scale = 4                                   # draw big, then shrink for smooth edges
    px = size * scale
    parts = [p for p in name.split() if p]
    text = (parts[0][0] + parts[-1][0]).upper() if len(parts) > 1 else (name[:2].upper() or "ME")

    c1, c2 = (108, 92, 231), (0, 184, 217)      # purple -> cyan (same as the banner)
    t = np.add.outer(np.arange(px), np.arange(px)) / (2 * (px - 1))
    arr = np.stack([c1[i] + (c2[i] - c1[i]) * t for i in range(3)], axis=-1).astype("uint8")
    img = Image.fromarray(arr, "RGB").convert("RGBA")

    mask = Image.new("L", (px, px), 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, px - 1, px - 1), radius=px // 4, fill=255)
    img.putalpha(mask)

    d = ImageDraw.Draw(img)
    try:
        font = ImageFont.load_default(size=int(px * 0.46))
    except TypeError:                           # very old Pillow
        font = ImageFont.load_default()
    d.text((px / 2, px / 2), text, fill="white", font=font, anchor="mm",
           stroke_width=px // 100, stroke_fill="white")
    r = px // 14                                # little "knock" dot, top-right
    d.ellipse((px * 0.80 - r, px * 0.20 - r, px * 0.80 + r, px * 0.20 + r), fill=(255, 255, 255, 235))
    return img.resize((size, size), Image.LANCZOS)

st.set_page_config(
    page_title=f"{PROFILE['name']} | Portfolio",
    page_icon=make_page_icon(PROFILE['name']),
    layout="wide",
    menu_items={
        "About": f"Autobiography & portfolio of {PROFILE['name']} – {PROFILE['section']}.",
    },
)

# session state
st.session_state.setdefault("waves", 0)
st.session_state.setdefault("likes", {p["title"]: 0 for p in PROJECTS})
st.session_state.setdefault("messages", [])

# helpers
def placeholder_image(label: str, size=(600, 600), color="#6C5CE7") -> Image.Image:
    """A labeled stand-in used when a real image file is missing."""
    img = Image.new("RGB", size, color)
    d = ImageDraw.Draw(img)
    try:
        font = ImageFont.load_default(size=max(18, size[0] // 14))
    except TypeError:  # very old Pillow
        font = ImageFont.load_default()
    small = "(placeholder – add your own image)"
    d.text((size[0] / 2, size[1] / 2 - 20), label, fill="white", font=font, anchor="mm")
    d.text((size[0] / 2, size[1] / 2 + 30), small, fill="#E0DCFF", font=ImageFont.load_default(), anchor="mm")
    return img


def load_image(path, label, size=(600, 600), color="#6C5CE7"):
    if path and Path(path).exists():
        return Image.open(path)
    return placeholder_image(label, size, color)


@st.cache_data
def skills_df() -> pd.DataFrame:
    return SKILLS.copy()


def initials(name: str) -> str:
    parts = [p for p in name.split() if p]
    return "".join(p[0] for p in parts[:2]).upper() or "ME"

# hero
st.markdown(
    f"""
    <div class="hero">
      <h1>{PROFILE['name']}</h1>
      <p>{PROFILE['tagline']}</p>
      <span class="badge">{PROFILE['program']}</span>
      <span class="badge">{PROFILE['year_level']}</span>
      <span class="badge">{PROFILE['school']}</span>
      <span class="badge">{PROFILE['section']}</span>
    </div>
    """,
    unsafe_allow_html=True,
)

# settings
_, settings_col = st.columns([13, 1])
with settings_col.popover("Settings"):
    accent = st.color_picker("Banner accent color", "#6C5CE7")
    show_details = st.checkbox("Show milestone details", value=True)
    compact = st.toggle("Compact project cards", value=False)

# global styling 
st.markdown(
    f"""
    <style>
      .hero {{
        background: linear-gradient(120deg, {accent} 0%, #00B8D9 100%);
        padding: 2.2rem 2.4rem; border-radius: 22px; color: white;
        box-shadow: 0 10px 30px rgba(0,0,0,.12); margin-bottom: 1rem;
      }}
      .hero h1 {{ color: white; margin: 0 0 .3rem 0; font-size: 2.6rem; }}
      .hero p  {{ color: rgba(255,255,255,.92); margin: .15rem 0; font-size: 1.1rem; }}
      .badge {{
        display:inline-block; padding:.25rem .7rem; margin:.4rem .35rem 0 0;
        background: rgba(255,255,255,.2); border-radius: 999px; font-size:.85rem;
      }}
      .tool {{
        display:inline-block; padding:.15rem .6rem; margin:.15rem .25rem .15rem 0;
        background:#EEEBFF; color:#4B3FCF; border-radius:999px; font-size:.8rem; font-weight:600;
      }}
      .tl-year {{ font-weight:800; color:{accent}; font-size:1.2rem; }}
    </style>
    """,
    unsafe_allow_html=True,
)

tab_about, tab_story, tab_skills, tab_projects, tab_contact = st.tabs(
    ["About me", "Autobiography", "Skills", "Projects", "Contact"]
)


# about page
with tab_about:
    left, right = st.columns([1, 2], gap="large")
    with left:
        st.image(
            load_image(PROFILE["photo"], initials(PROFILE["name"])),
            **STRETCH,
        )
    with right:
        st.header("Hello, I'm " + PROFILE["name"].split()[0])
        st.write(PROFILE["short_bio"])

        stats = dict(STATS)
        stats["Projects built"] = len(PROJECTS)
        cols = st.columns(len(stats))
        for col, (label, value) in zip(cols, stats.items()):
            col.metric(label, value)

        st.subheader("Ask me anything")
        question = st.selectbox("Pick a question", list(FACTS.keys()))
        st.info(FACTS[question])

    st.divider()
    st.subheader("Interests")
    picked = st.pills("Click an interest to learn more", list(INTERESTS.keys()), selection_mode="single")
    if picked:
        st.success(INTERESTS[picked])
    else:
        st.caption("Nothing selected yet. Tap a chip above.")


# autobiography

with tab_story:
    st.header("My Story")
    mode = st.radio("Reading mode", ["Short", "Full"], horizontal=True)
    key = mode.lower()

    c1, c2 = st.columns([3, 2], gap="large")
    with c1:
        for heading, versions in STORY.items():
            with st.container(border=True):
                st.subheader(heading)
                st.write(versions[key])

        st.subheader("Education")
        st.table(EDUCATION)

    with c2:
        st.subheader("Milestones")
        years = [m["year"] for m in MILESTONES]
        options = list(range(min(years), max(years) + 1))
        # One handle (not a range) so it can never get stuck on top of a second handle.
        if len(options) > 1:
            up_to = st.select_slider("Show my journey up to", options=options, value=max(options))
        else:
            up_to = options[0]
        shown = [m for m in MILESTONES if m["year"] <= up_to]
        if not shown:
            st.warning("No milestones in that range.")
        for m in shown:
            st.markdown(f"<span class='tl-year'>{m['year']}</span> &nbsp; **{m['title']}**",
                        unsafe_allow_html=True)
            if show_details:
                st.caption(m["detail"])

        st.write("")
        st.caption("Milestones per year")
        per_year = pd.Series([m["year"] for m in MILESTONES]).value_counts().sort_index()
        st.bar_chart(per_year)

# skills
with tab_skills:
    st.header("Skills")
    df = skills_df()
    longest = df.loc[df["Years"].idxmax()]
    st.write(
        f"I work with **{len(df)} skills** across **{df['Category'].nunique()} categories**. "
        f"My longest-running skill is **{longest['Skill']}** ({longest['Years']:.1f} years), "
        f"and on average I have **{np.mean(df['Years']):.1f} years** with each one."
    )

    f1, f2, f3 = st.columns([2, 1, 1])
    cats = f1.multiselect("Categories", sorted(df["Category"].unique()), placeholder="All categories")
    min_years = f2.slider("Minimum years", 0.0, float(df["Years"].max()), 0.0, step=0.5)
    chart_kind = f3.radio("Chart type", ["Bar", "Area"], horizontal=True)

    in_category = df["Category"].isin(cats) if cats else pd.Series(True, index=df.index)
    filtered = df[in_category & (df["Years"] >= min_years)].sort_values("Years", ascending=False)

    if filtered.empty:
        st.warning("No skills match those filters.")
    else:
        t1, t2 = st.columns(2, gap="large")
        with t1:
            st.subheader("Table")
            st.dataframe(
                filtered,
                hide_index=True,
                column_config={
                    "Years": st.column_config.ProgressColumn(
                        "Years of experience", min_value=0.0, max_value=float(df["Years"].max()), format="%.1f yrs"
                    ),
                },
                **STRETCH,
            )
            if st.checkbox("Show summary statistics"):
                st.write(filtered[["Years"]].describe())
        with t2:
            st.subheader("Chart")
            chart_data = filtered.set_index("Skill")["Years"]
            if chart_kind == "Bar":
                st.bar_chart(chart_data)
            else:
                st.area_chart(chart_data)

        st.subheader("Longest-running skills")
        top3 = filtered.head(3)
        for col, (_, row) in zip(st.columns(len(top3)), top3.iterrows()):
            col.metric(row["Skill"], f"{row['Years']:.1f} yrs", row["Category"], delta_color="off")

        st.download_button(
            "⬇️ Download skills (CSV)",
            filtered.to_csv(index=False).encode("utf-8"),
            file_name="my_skills.csv",
            mime="text/csv",
        )

# projects
with tab_projects:
    st.header("Projects")

    all_tools = sorted({t for p in PROJECTS for t in p["tools"]})
    p1, p2 = st.columns([3, 1])
    tool_filter = p1.multiselect("Filter by tool", all_tools, placeholder="All tools")
    sort_by = p2.selectbox("Sort by", ["Newest first", "Oldest first", "Most liked"])

    projects = [p for p in PROJECTS if not tool_filter or set(tool_filter) & set(p["tools"])]
    if sort_by == "Newest first":
        projects.sort(key=lambda p: p["year"], reverse=True)
    elif sort_by == "Oldest first":
        projects.sort(key=lambda p: p["year"])
    else:
        projects.sort(key=lambda p: st.session_state.likes.get(p["title"], 0), reverse=True)

    if not projects:
        st.warning("No projects use those tools.")

    for i, p in enumerate(projects):
        with st.container(border=True):
            if compact:
                img_col, body = None, st.container()
            else:
                img_col, body = st.columns([1, 2], gap="large")
                with img_col:
                    st.image(
                        load_image(p.get("image"), f"{p['title'].split(':')[0]}",
                                   size=(600, 360), color="#00A3BF"),
                        **STRETCH,
                    )
            with body:
                st.subheader(f"{p['title']}")
                st.caption(f"{p['year']}  ·  {p['status']}")
                st.markdown(f"**Role:** {p['role']}")
                st.markdown(
                    "**Tools:** " + "".join(f"<span class='tool'>{t}</span>" for t in p["tools"]),
                    unsafe_allow_html=True,
                )
                st.markdown(f"**Outcome:** {p['outcome']}")

                b1, b2, b3 = st.columns([1, 1, 2])
                b1.link_button("View project", p["link"], **STRETCH)
                if b2.button(f"Like ({st.session_state.likes.get(p['title'], 0)})", key=f"like_{i}", **STRETCH):
                    st.session_state.likes[p["title"]] = st.session_state.likes.get(p["title"], 0) + 1
                    st.toast("Thanks for the like!", icon="💜")
                    st.rerun()
                with b3.popover("More details"):
                    st.write(p["description"])
                    st.caption(f"Status: {p['status']}")

    st.divider()
    st.subheader("Tools across my projects")
    tool_counts = pd.Series([t for p in PROJECTS for t in p["tools"]]).value_counts()
    st.bar_chart(tool_counts)

# contacts
with tab_contact:
    st.header("Contact & Feedback")
    form_col, info_col = st.columns([3, 2], gap="large")

    with form_col:
        with st.form("contact_form"):
            n1, n2 = st.columns(2)
            visitor = n1.text_input("Your name", placeholder="Juan Dela Cruz")
            email = n2.text_input("Your email", placeholder="you@example.com")
            topic = st.selectbox("Topic", ["Say hello", "Project feedback", "Collaboration", "Other"])
            rating = st.slider("How would you rate this site?", 1, 5, 5)
            message = st.text_area("Message", placeholder="Write your message or feedback here…", height=140)
            agree = st.checkbox("It's okay to reply to this email address")
            submitted = st.form_submit_button("Send message", type="primary")

        if submitted:
            if not visitor.strip() or not message.strip():
                st.error("Please add your name and a message.")
            elif "@" not in email:
                st.error("Please enter a valid email address.")
            else:
                with st.spinner("Sending…"):
                    import time
                    time.sleep(0.8)
                st.session_state.messages.append(
                    {
                        "Time": datetime.now().strftime("%Y-%m-%d %H:%M"),
                        "Name": visitor, "Email": email, "Topic": topic,
                        "Rating": rating, "Reply OK": agree, "Message": message,
                    }
                )
                st.success(f"Thank you, {visitor}! Your message was received. ({'⭐' * rating})")
                st.balloons()

    with info_col:
        with st.container(border=True):
            st.subheader("📬 Reach me")
            st.write(f"**Email:** {CONTACT['email']}")
            st.write(f"**Location:** {PROFILE['location']}")
            st.link_button("GitHub profile", CONTACT["github"], **STRETCH)

        if st.session_state.messages:
            with st.expander(f"Messages sent this session ({len(st.session_state.messages)})"):
                st.dataframe(pd.DataFrame(st.session_state.messages), hide_index=True, **STRETCH)

# footer
st.divider()
st.caption(f"© {datetime.now().year} {PROFILE['name']} · {PROFILE['section']} · Built with Streamlit 🎈")
