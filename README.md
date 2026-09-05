# Platform-Based Development Portfolio

**Author**: Ahmad Hoesin  
**NPM**: 2506555400  
**Class**: KKI  
**Deployment URL**: [ahmad-hoesin-myportofolio.pws.cs.ui.ac.id](https://ahmad-hoesin-myportofolio.pws.cs.ui.ac.id)

---

## Local Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/zuromu/PlatformBasedDevelopment.git](https://github.com/zuromu/PlatformBasedDevelopment.git)
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


### Assignment 1

1. Usage of Semantic HTML5 Elements:
For the structure, I definitely leaned into semantic HTML5 tags like `<section>` and `<article>`. Instead of just nesting endless, meaningless `<div>` tags everywhere, I used `<section>` to create clear, logical boundaries between areas like my Tech Arsenal and my Experience (such as my UI/UX Intern stint at BEM Fasilkom). Inside those sections, I used `<article>` to wrap standalone content blocks. It honestly just makes the DOM so much easier to read when I'm debugging, and it’s way better for screen readers since the structure essentially documents itself.

2. CSS Responsive Layout Challenges:
The biggest headache was keeping my Hero section and Tech Arsenal from getting completely squished on mobile screens. I had a nice horizontal grid going for desktop, but on smaller screens, it just wasn't readable. I had to decide what to prioritize, and readability easily won out over keeping the horizontal layout. I fixed it by throwing in a @media (max-width: 600px) query to override my desktop grid-template-columns. This collapses the layout into a single 1fr vertical column, forcing everything to stack naturally and making it actually usable on a phone.

3. Limitations of Static Web & Future Enhancements:
Building a purely static site is fine for a one-off, but the limitations get annoying fast. If I want to add a new skill, update my experiences, or even just fix a typo, I have to manually dig into the HTML and push a whole new commit. It’s just not scalable for a growing portfolio. For the next iteration, I’m really looking forward to plugging in a dynamic Django backend. That way, I can manage, add, and delete portfolio entries through a secure admin database without ever having to touch the raw source code again.

AI Usage Disclosure:
I used AI as a collaborative coding partner for this assignment.
- Prompt Strategy: 
I specifically prompted the AI to avoid generic, "vibe-coded" modern web trends (like soft gradients or pill buttons) and asked for CSS Grid/Flexbox boilerplate to help me build a more raw, minimalist/brutalist aesthetic.

- Limitations & Manual Fixes: 
While the AI was great at generating the baseline CSS and the logic for the high-contrast hover inversions, it isn't perfect. I had to manually tweak the grid spacing and handle all the Git branching, troubleshooting, and responsive quirks that the AI missed. I also manually integrated all my personal data and finalized the styling.

- AI Chat Log:
https://share.gemini.google/mh22PtnrSk50   

