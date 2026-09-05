# Platform-Based Development Portfolio

**Author**: Ahmad Hoesin  
**NPM**: 2506555400  
**Class**: KKI  
**Deployment URL**: [ahmad-hoesin-myportofolio.pws.cs.ui.ac.id](https://ahmad-hoesin-myportofolio.pws.cs.ui.ac.id)

---

## Local Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/zuromu/PlatformBasedDevelopment.git
   cd PlatformBasedDevelopment 
   ```

2. **Create and activate virtual environment:**
    ```bash
    python3 -m venv env
    source env/bin/activate 
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt 
    ```

4. **Run development server:**
    ```bash
    python manage.py runserver 
    ```

5. **Access the application at http://127.0.0.1:8000/.**


## Weekly Progress

**Week 1: Static Web Basics**
- [x] Set up the base Django project and got it running on PWS.
- [x] Structured the page using proper semantic HTML (`<header>`, `<main>`, `<section>`, `<article>`) instead of just spamming `<div>` tags.
- [x] Wrote custom CSS using CSS variables for a raw, high-contrast look.
- [x] Fixed mobile responsiveness using basic CSS Grid and Flexbox.
- [x] Added smooth scrolling and hover animations.
- [x] Replaced the tutorial sample data with my actual info (Skills, Experiences, Info).


### Assignment 1

**1. Usage of Semantic HTML5 Elements:**
I used semantic tags like `<section>` and `<article>` to organize the page structure. `<section>` separates the main areas (Profile, Tech Arsenal, Experience), and `<article>` wraps the individual items, like my UI/UX role at BEM Fasilkom. It keeps the code much cleaner than using generic `<div>` tags for everything, makes debugging easier, and is better for screen reader accessibility.

**2. CSS Responsive Layout Challenges:**
The main challenge was the grid layout breaking on mobile screens. The side-by-side cards in the Tech Arsenal and Experience sections got too narrow to read. I solved this by adding a `@media (max-width: 600px)` query. It changes the `grid-template-columns` to `1fr` so the content stacks vertically instead of trying to squeeze horizontally.

**3. Limitations of Static Web & Future Enhancements:**
Static websites are difficult to maintain. Every time I want to add a new skill or update my experience, I have to edit the hardcoded HTML and push a new commit. For future iterations, I plan to use Django models and a database so I can add or edit portfolio items dynamically through an admin panel without touching the raw code.

**AI Usage Disclosure:**
I used Gemini to help write the initial CSS boilerplate for this assignment. 
- **Prompt Strategy:** I asked the AI to generate CSS Grid and Flexbox layouts. I specifically told it to avoid modern "vibe" trends (like gradients, soft shadows, and rounded buttons) and instead use a sharp, high-contrast minimalist style.
- **Limitations & Manual Fixes:** The AI output was a starting point, but I had to manually adjust the grid spacing, fix CSS syntax errors (like putting styles inside the wrong media query), and handle the actual responsive breakpoint logic. I also managed the Git branching and PWS deployment entirely manually, and wrote the HTML content to include my actual data.
- **AI Chat Log:** https://share.gemini.google/mh22PtnrSk50
