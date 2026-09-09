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

**Week 2: Django Models, Views, and Templates (MVT)**
- [x] Built a custom `Project` model in `models.py` (and ran the migrations to back it up).
- [x] Wired up the views and URL routing so the new `/projects/` page actually loads.
- [x] Swapped out hardcoded HTML for Django Template tags to render database records dynamically.
- [x] Wrote unit tests in `tests.py` (and figured out how to use `django.utils.html.escape` so an apostrophe wouldn't break my assertions).


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


### Assignment 2
**1. Explain what happens when a user opens the new portfolio page, starting from the request received by the project until the data appears in the browser:**
When a user hits the `/projects/` URL, the request goes straight to the project's main `urls.py`. That file passes the baton to the main app's `urls.py`, which triggers the `show_projects` function inside `views.py`. The view basically taps the `Project` model on the shoulder and asks the database for all the project records using P`roject.objects.all()`. It bundles all that data into a dictionary (the context) and throws it over to `projects.html`. Finally, Django's template engine runs a `{% for %}` loop, injecting my actual project details into the HTML skeleton before shipping the final page back to the user's browser.

**2. Why should the data for the new portfolio section be stored in a model instead of being written directly in the template:**
It is all about separating the content from the presentation layer. If I hardcode everything directly into the HTML, adding a new project means opening the editor, copying a block of markup, risking a missing closing tag, and pushing a whole new Git commit. By using a database model, the HTML acts as a dumb, reusable skeleton. It makes maintenance effortless. Down the line, I can just log into a Django admin panel, fill out a form to add a new project, and the site updates automatically without me ever touching the raw code.

**3. What is the difference between makemigrations and migrate in Django? Give an example:**
- `makemigrations` is the drafting phase. When I wrote the `Project` class, running this told Django to scan my code and spit out a blueprint file in the `migrations/` folder. It basically takes notes on what needs to change, but leaves the actual database alone.
- `migrate` is the builder. It reads those blueprints and executes the real SQL commands to update the database.
- Example: When I built the `Project` model, `makemigrations` just drafted the fields (name, tech stack, etc.). Running `migrate` is what actually built the physical `main_project` table in my SQLite database so I could start saving my projects to it.

**AI Usage Disclosure:**
I used Gemini as a thought partner to get comfortable with the Django MVT flow and testing.
- **Prompt Strategy:** I asked Gemini to help me set up the initial boilerplate for the `Project` model and view. I also ran into a weird bug where an apostrophe in my projects' title broke the automated tests, so I asked for the cleanest way to handle HTML escaping in Django.
- **Limitations & Manual Fixes:** The AI gave me the `escape()` function fix, but I manually wrote the test logic, injected the actual real-world data for my projects, and hooked up the HTML template to match my raw CSS design from last week.
- **AI Chat Log:** https://share.gemini.google/zxuAI6ST87Br 