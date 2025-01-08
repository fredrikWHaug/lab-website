<script>
    // Static text variables for the hero section.
    let heading = "Welcome to My Website";
    let subheading = "Building a future for brain-computer interfaces.";
</script>

<section class="hero">
    <div class="hero-content">
        <!-- Main heading and subheading for the hero section. -->
        <h1>{heading}</h1>
        <p>{subheading}</p>
        <!-- Call-to-action button for initiating user interaction. -->
        <button class="cta">Get Started</button>
    </div>
</section>

<style>
    /* Base styling for the page, setting a full black background and white text. */
    html, body {
        margin: 0;
        padding: 0;
        background: #000;
        color: white;
        height: 100%;
        width: 100%;
    }

    /* Styles for the hero section, ensuring it spans the full viewport height. */
    .hero {
        display: flex;
        justify-content: space-between;
        align-items: center;
        height: 100vh;
        padding: 2rem;
        background: #000; /* Consistent black background for branding. */
        color: white;
    }

    /* Optional flex containers for structuring hero section content. */
    .hero-left {
        flex: 1;
    }

    .hero-right {
        flex: 1;
        max-width: 500px;
    }

    /* Main title styling for the hero section. */
    .hero-title {
        font-size: 4rem;
        font-weight: bold;
        line-height: 1.2;
    }

    /* Highlighted text styling using a gradient fill. */
    .highlight {
        background: linear-gradient(90deg, #32cd32, #ff4500);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    /* General text styling for readability and consistency. */
    .hero-text {
        font-size: 1.5rem;
        line-height: 1.6;
    }

    /* Styles for additional scrollable sections. */
    .scroll-section {
        padding: 4rem 2rem;
        background: #000; /* Black background for continuity. */
        color: white; /* High contrast text for readability. */
        border-top: none; /* Clean transitions between sections. */
    }

    .content {
        max-width: 800px;
        margin: 0 auto;
        text-align: center;
    }

    /* Headings and paragraph styles for section content. */
    h2 {
        font-size: 2.5rem;
        margin-bottom: 1.5rem;
        color: white;
    }

    p {
        font-size: 1.125rem;
        margin-bottom: 1.5rem;
        color: white;
    }

    /* Styled list with green links for emphasis. */
    ul {
        list-style: none;
        padding: 0;
    }

    ul li {
        margin: 0.5rem 0;
    }

    ul li a {
        color: #32cd32;
        text-decoration: none;
        font-weight: 600;
    }

    ul li a:hover {
        text-decoration: underline;
    }

    /* Grid-based team member layout with responsive support. */
    .team-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 2rem;
    }

    .team-member {
        text-align: center;
    }

    .team-member img {
        border-radius: 50%; /* Circular images for team members. */
        margin-bottom: 1rem;
    }

    .team-member p {
        font-size: 1rem;
        color: white;
    }

    /* Styling for a simple contact form with interactive focus states. */
    form {
        display: flex;
        flex-direction: column;
        gap: 1rem;
    }

    label {
        font-weight: 600;
        color: white;
    }

    input,
    textarea {
        width: 100%;
        padding: 0.75rem;
        font-size: 1rem;
        border: 1px solid #444;
        background: #222;
        color: white;
        border-radius: 4px;
    }

    /* Highlight inputs on focus for accessibility and interaction feedback. */
    input:focus,
    textarea:focus {
        outline: none;
        border-color: #32cd32;
        box-shadow: 0 0 0 3px rgba(50, 205, 50, 0.3);
    }

    /* Call-to-action button styles with hover effects for engagement. */
    button {
        padding: 0.75rem 1.5rem;
        background-color: #32cd32;
        color: black;
        border: none;
        border-radius: 4px;
        font-size: 1rem;
        cursor: pointer;
        transition: background-color 0.3s;
    }

    button:hover {
        background-color: #28a428;
    }
</style>
