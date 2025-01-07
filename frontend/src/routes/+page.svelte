<script>
    // Optional: Add interactivity or props
</script>

<!-- Hero Section -->
<section class="hero">
    <div class="hero-left">
        <h1 class="hero-title">THE HOME FOR <br /><span class="highlight">TOUGH TECH</span></h1>
    </div>
    <div class="hero-right">
        <p class="hero-text">
            Our residents are <span class="highlight">Tough Tech</span> companies building solutions for a healthier, more productive, and more sustainable world.
        </p>
    </div>
</section>

<!-- Publications Section -->
<section id="publications" class="scroll-section">
    <div class="content">
        <h2>Publications</h2>
        <p>Discover the latest research and innovations from our lab, pushing the boundaries of tough tech.</p>
        <ul>
            <li><a href="#">Publication 1: Breakthrough in Tough Tech</a></li>
            <li><a href="#">Publication 2: Sustainable Solutions for the Future</a></li>
            <li><a href="#">Publication 3: Productivity and Innovation</a></li>
        </ul>
    </div>
</section>

<!-- Team Section -->
<section id="team" class="scroll-section">
    <div class="content">
        <h2>Team</h2>
        <p>Meet the brilliant minds driving innovation in our lab.</p>
        <div class="team-grid">
            <div class="team-member">
                <img src="https://via.placeholder.com/150" alt="Team Member">
                <p><strong>Dr. Jane Doe</strong><br>Lead Scientist</p>
            </div>
            <div class="team-member">
                <img src="https://via.placeholder.com/150" alt="Team Member">
                <p><strong>Dr. John Smith</strong><br>Researcher</p>
            </div>
            <div class="team-member">
                <img src="https://via.placeholder.com/150" alt="Team Member">
                <p><strong>Ms. Alice Brown</strong><br>Engineer</p>
            </div>
        </div>
    </div>
</section>

<!-- Contact Section -->
<section id="contact" class="scroll-section">
    <div class="content">
        <h2>Contact</h2>
        <p>Have questions? Want to collaborate? Reach out to us today!</p>
        <form>
            <label for="name">Name</label>
            <input type="text" id="name" placeholder="Your Name" required>
            
            <label for="email">Email</label>
            <input type="email" id="email" placeholder="Your Email" required>
            
            <label for="message">Message</label>
            <textarea id="message" placeholder="Your Message" required></textarea>
            
            <button type="submit">Send Message</button>
        </form>
    </div>
</section>

<style>
    /* Reset default margins and paddings */
    html, body {
        margin: 0;
        padding: 0;
        background: #000; /* Black background */
        color: white;
        height: 100%;
        width: 100%;
    }

    /* Hero Section Styles */
    .hero {
        display: flex;
        justify-content: space-between;
        align-items: center;
        height: 100vh;
        padding: 2rem;
        background: #000; /* Black background */
        color: white;
    }

    .hero-left {
        flex: 1;
    }

    .hero-title {
        font-size: 4rem;
        font-weight: bold;
        line-height: 1.2;
    }

    .highlight {
        background: linear-gradient(90deg, #32cd32, #ff4500);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .hero-right {
        flex: 1;
        max-width: 500px;
    }

    .hero-text {
        font-size: 1.5rem;
        line-height: 1.6;
    }

    /* Scrolling Section Styles */
    .scroll-section {
        padding: 4rem 2rem;
        background: #000; /* Black background for all sections */
        color: white; /* White text to contrast */
        border-top: none; /* Remove any visible borders */
    }

    .content {
        max-width: 800px;
        margin: 0 auto;
        text-align: center;
    }

    h2 {
        font-size: 2.5rem;
        margin-bottom: 1.5rem;
        color: white; /* Ensure headings are visible */
    }

    p {
        font-size: 1.125rem;
        margin-bottom: 1.5rem;
        color: white; /* Ensure text is readable */
    }

    ul {
        list-style: none;
        padding: 0;
    }

    ul li {
        margin: 0.5rem 0;
    }

    ul li a {
        color: #32cd32; /* Green links for readability */
        text-decoration: none;
        font-weight: 600;
    }

    ul li a:hover {
        text-decoration: underline;
    }

    /* Team Grid Styles */
    .team-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 2rem;
    }

    .team-member {
        text-align: center;
    }

    .team-member img {
        border-radius: 50%;
        margin-bottom: 1rem;
    }

    .team-member p {
        font-size: 1rem;
        color: white;
    }

    /* Contact Form Styles */
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
        border: 1px solid #444; /* Darker border for consistency */
        background: #222; /* Slightly lighter black */
        color: white; /* White text */
        border-radius: 4px;
    }

    input:focus,
    textarea:focus {
        outline: none;
        border-color: #32cd32;
        box-shadow: 0 0 0 3px rgba(50, 205, 50, 0.3);
    }

    button {
        padding: 0.75rem 1.5rem;
        background-color: #32cd32; /* Green button */
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
