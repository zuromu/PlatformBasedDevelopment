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

**Week 3: Forms & Data Delivery**
- [x] Refactored all my HTML files so they extend a main `base.html` skeleton template instead of repeating the navbar and footer everywhere.
- [x] Set up a `ModelForm` so I can actually add and edit projects dynamically.
- [x] Added a delete button with a pop-up confirmation modal so I don't accidentally delete stuff.
- [x] Built a JSON API endpoint (`/api/projects/`) using Django serializers to serve my data.

**Week 4: Authentication, Sessions, and Authorization**
- [x] Implemented a `UserCreationForm` and `AuthenticationForm` for user registration and login.
- [x] Configured session cookies (`last_login`) to track when users log in and out.
- [x] Secured state-changing forms with `{% csrf_token %}` to prevent unauthorized request forgery.
- [x] Created an `Editor` group in Django Admin and applied role-based access control (Superuser, Editor, Regular, Anonymous) to my `views.py`.
- [x] Used `{% if %}` template tags to conditionally hide Add, Edit, and Delete buttons based on user permissions.
- [x] Implemented a ManyToMany `starred_by` field so authenticated users can star their favorite experiences and projects.

**Week 5: Web Interactivity with JavaScript**
- [x] Converted the Experience and Project page to use AJAX, so it loads data without reloading the whole page.
- [x] Built a custom JSON endpoint with `JsonResponse` to feed data to the frontend.
- [x] Added search debouncing so the API doesn't get spammed with requests while typing.
- [x] Put the Add Experience/Project form inside a popover modal and wired it up to submit using the Fetch API.
- [x] Added custom toast notifications to show success and error messages cleanly.
- [x] Protected the site against XSS attacks using `strip_tags` in the backend and a custom `escapeHtml` function in JavaScript.

**Week 6: Django REST Framework**
- [x] Installed DRF and built a Projects API (`/api/v1/projects/`) with `ProjectSerializer`, `IsPortfolioOwnerOrReadOnly`, and function-based `@api_view` views.
- [x] Applied the same pattern to Experience: `ExperienceSerializer`, `IsPortfolioOwnerOrEditorOrReadOnly`, and list/detail/star endpoints under `/api/v1/experience/`.
- [x] Rebuilt the Experience page to display, search, add, edit (PATCH), star, and delete through the API, with API errors shown in toasts.
- [x] Wrote `APITestCase` tests covering all four roles, validation, stars, and CSRF enforcement with `APIClient(enforce_csrf_checks=True)`.



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
When a user hits the `/projects/` URL, the request goes straight to the project's main `urls.py`. That file passes the baton to the main app's `urls.py`, which triggers the `show_projects` function inside `views.py`. The view basically taps the `Project` model on the shoulder and asks the database for all the project records using `Project.objects.all()`. It bundles all that data into a dictionary (the context) and throws it over to `projects.html`. Finally, Django's template engine runs a `{% for %}` loop, injecting my actual project details into the HTML skeleton before shipping the final page back to the user's browser.

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


### Assignment 3
**1. Explain why we use Django’s `ModelForm` instead of creating HTML forms manually. Additionally, explain why we are required to add `{% csrf_token %}` to these forms:**
Writing HTML forms manually takes forever because you have to write out every single `<input>` tag and then manually catch all the `request.POST` data in your view to save it. `ModelForm` basically just looks at my database model and builds the whole form for me, plus it handles data validation automatically. As for the `{% csrf_token %}`, it is a strict security requirement. It stops Cross-Site Request Forgery, which is when a malicious site tries to trick your browser into submitting a form to my site without me knowing. If that token isn't there, Django just blocks the submission completely.


**2. In Tutorial 03, we discussed JSON and XML data formats. Why is JSON preferred in modern web application development compared to XML:**
XML is just way too bulky. It relies on opening and closing tags for literally everything (like `<name>Ahmad</name>`), which makes the file size huge. JSON is much cleaner because it just uses simple key-value pairs (like `"name": "Ahmad"`), making it a lot lighter and faster to send over the internet. Plus, JSON literally stands for JavaScript Object Notation, so modern frontend frameworks can read and manipulate it natively without needing extra parsers.


**3. Explain the flow that occurs when you use a view function to return your portfolio data in JSON format. Why do we need to perform the serialization process on Django models before returning the data:**
When someone hits my JSON endpoint, the `urls.py` routes it to my view function. The view asks the database for all the projects using `Project.objects.all()`. But here is the catch: the database gives back complex Django Model objects, which web browsers and external APIs cannot understand. That is why we have to run `serializers.serialize("json", projects)`. Serialization translates those Python objects into a simple, standardized text string formatted as JSON. Finally, we wrap that string in an `HttpResponse` and ship it back to the client.




**AI Usage Disclosure:**
I barely used AI for this assignment since the Django MVT flow is starting to make sense.
- **Prompt Strategy:** I only used it to help me figure out the HTML/CSS structure for the popup delete confirmation modal and the notification popups.
- **Limitations & Manual Fixes:** I didn't use AI for any of the Python backend logic this time. I manually handled writing the `ModelForm`, creating the CRUD views, writing the JSON serializer endpoint, and refactoring all my HTML files to extend the `base.html` skeleton template.
- **AI Chat Log:** https://share.gemini.google/tlReTHDvUMlX 


### Assignment 4
(Note: Reflective questions were removed for this week's assignment).

**AI Usage Disclosure:**
I used Gemini to act as a pair programmer while implementing my role-based access control.
- **Prompt Strategy:** I provided my existing MVT codebase and asked for the cleanest way to enforce permission checks across four different roles (Superuser, Editor, Regular User, Anonymous).
- **Limitations & Manual Fixes:** The AI provided the backend logic and the `is_editor` helper function, but I had to manually integrate the logic into my custom views and apply the conditional `{% if %}` checks within my custom neo-brutalist HTML design system, as well as debugging case-sensitivity with `name__iexact`.
- **AI Chat Log:** https://share.gemini.google/4HlIQO7ZEdpj



### Assignment 5
**1. Explain what debouncing is and why this technique is important to implement in a search feature that uses AJAX.**
Debouncing is basically adding a slight delay so a function doesn't trigger a million times in a row. Without it, my AJAX search would spam the server with a new HTTP request for every single letter I type. By adding a 300ms delay, the code waits until I actually pause typing before sending the request. It saves server load and stops the results from glitching out if a slower, older request finishes after a newer one.


**2. Explain the purpose of using `await` when we use `fetch()`. What would happen if we did not use `await?`**
The `fetch()` function is asynchronous, meaning it runs in the background and immediately returns a "Promise" instead of the actual data. Putting `await` in front of it tells JavaScript to literally pause and wait for the server to reply before moving to the next line. If I didn't use `await`, the code would just keep executing, try to render the page before the data even arrived, and crash because my variable would hold an empty Promise object instead of the real JSON data.

**3. Explain what a Cross-Site Scripting (XSS) attack is and why data displayed through AJAX/JavaScript is more vulnerable to this attack than data displayed directly through a Django template.**
XSS happens when someone sneaks malicious JavaScript into your site's data (like submitting `<script>alert('hacked')</script>` as a project title) so it runs on other users' screens. With standard Django templates, Django automatically escapes HTML for us, rendering it safe. But with AJAX, we grab raw JSON and manually shove it into the DOM using JavaScript. The browser just blindly trusts and executes any scripts it finds in that raw data. That's why I had to write a custom `escapeHtml` function to sanitize the data before putting it on the screen.

**AI Usage Disclosure:**
I didn't use AI for this assignment.
- **Prompt Strategy:** None
- **Limitations & Manual Fixes:** I just followed the Tutorial 5 steps and manually adapted the AJAX, debouncing, modal, and XSS protection logic for my custom `Experience` page. I also had to manually clean up my old URLs and views to make sure my Editor role access checks from last week still worked flawlessly with the new JSON endpoints. No chat log needed this week.


### Assignment 6

**1. Explain what REST means and why returning JSON alone isn't enough to call an API RESTful. Also explain the difference between `PUT` and `PATCH`, with an example of when each should be used.**
REST is basically an architectural style for designing web APIs, not a library or a data format. The idea is that data is treated as resources with their own URLs (like `/api/v1/experience/<uuid>/`), the HTTP method says what you want to do (GET reads, POST creates, PUT/PATCH updates, DELETE removes), and the client and server just swap representations of that data. Returning JSON alone doesn't make it RESTful because the format is only one small piece. My Tutorial 05 endpoints returned JSON too, but they had the action baked into the URL (`/projects/add-ajax/`, `/projects/<id>/delete/`) and everything was a POST. The new API does `POST /api/v1/experience/` to create and `DELETE /api/v1/experience/<uuid>/` to delete, so the URL is the thing and the method is the action.
For `PUT` vs `PATCH`: `PUT` sends a full replacement of the object, so every required field has to be there. `PATCH` only sends the fields that need to change and leaves the rest alone. In my tests, a `PUT` with only a title got a 400 because the description was missing, while a `PATCH` with only a title worked and kept the old description. So I'd use `PUT` when replacing a whole record (like submitting the full edit form), and `PATCH` for a small fix like correcting a typo in the title.

**2. Explain the role of a serializer in Django REST Framework. What are its advantages over manually assembling a dictionary with `JsonResponse` as in Tutorial 05?**
A serializer is the translator between my Django model objects and plain data. Going out, it turns an `Experience` object into data that DRF's renderer can turn into JSON. Coming in, it checks the data the client sent and turns it into something ready to save. In Tutorial 05, `get_experience_json` looped through every object and built a dictionary by hand, field by field, with the star logic mixed in. And the validation lived in a totally separate place (`ExperienceForm`), so I had to remember to keep both in sync. With `ExperienceSerializer`, one class handles reading, creating, and updating. The `fields` list decides exactly what gets exposed (so no emails or password hashes), `read_only_fields` stops a client from forging `star_count`, and `validate_title` does the `strip_tags` cleaning in the same spot. If I add a new model field later, it's one line instead of hunting through a loop.

**3. Explain the difference between authentication and authorization in Django REST Framework. Why must access rights be checked with a permission class on the server, rather than only by hiding a button in the template?**
Authentication answers "who are you?" and authorization answers "what are you allowed to do?". In my API, `SessionAuthentication` reads the session cookie from my existing login and sets `request.user`. Then the permission class, `IsPortfolioOwnerOrEditorOrReadOnly`, looks at that user and decides if the request can keep going. Hiding a button in the template is just a UI courtesy, not security. Anyone can open DevTools, or use `fetch` or curl, and send a `DELETE` straight to `/api/v1/experience/<uuid>/` without ever seeing my button. Only the server can actually refuse that. My tests prove it: a regular user trying to `DELETE` gets a 403 and the database still has the record.

**4. Explain why requests that change data still need a CSRF token when an API uses `SessionAuthentication`. Why isn't a test using `force_authenticate` enough to prove that CSRF protection works?**
With `SessionAuthentication`, the login lives in a cookie, and the browser attaches that cookie automatically to every request to my site, even ones triggered by a different malicious website. So without a CSRF token, an evil page could make a logged-in owner's browser fire a `DELETE` without them knowing. The `X-CSRFToken` header fixes that, because the token has to match what Django expects and another site can't read it. That's why my `fetch()` calls for POST, PATCH, and DELETE all send it. `force_authenticate` isn't enough because it sets `request.user` directly and skips the real authentication step, so CSRF never even gets checked and the test would pass either way. To actually prove it, I used `APIClient(enforce_csrf_checks=True)` with a real `.login()`, and confirmed a write without the token gets a 403 and changes nothing.

**AI Usage Disclosure:**
I used Claude for this assignment, and I used it more than I did for Assignment 5.
- **Prompt Strategy:** I gave it the Tutorial 07 and Assignment 6 pages and my repo, and asked it to adapt the DRF pattern to my own models (`Project` for the tutorial, `Experience` for the assignment). I also asked it conceptual questions about things I didn't get, like how permission classes run and why `force_authenticate` skips CSRF, and got it to explain debugging errors. It drafted the serializer, permission, API view, test, and JavaScript code, and it drafted the wording of these reflective answers to match my earlier README style.
- **Limitations & Manual Fixes:** The AI's first version put the Editor permission on the tutorial's Projects API, but Tutorial 07 says Projects are owner-only and the Editor rules belong to my own section, so I changed that. Its code also assumed the tutorial's field names (`title`, `project_url`), but my `Project` model uses `name` and `github_url`, so everything had to be matched to my models. I also had to fix my old tests, because they expected data in the HTML even though the pages have been rendered by JavaScript since Assignment 5. I ran everything myself and tested each role (owner, Editor, regular user, visitor) in the browser.
- **AI Chat Log:** https://claude.ai/share/43c96126-b34d-46fb-ab83-5276bfb17129
