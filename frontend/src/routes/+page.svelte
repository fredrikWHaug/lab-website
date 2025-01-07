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
        background: #f9fafb; /* Light grey background */
        color: #111827; /* Dark text */
        border-top: 1px solid #e5e7eb;
    }

    .scroll-section:nth-child(even) {
        background: #ffffff; /* Alternate section background */
    }

    .content {
        max-width: 800px;
        margin: 0 auto;
        text-align: center;
    }

    h2 {
        font-size: 2.5rem;
        margin-bottom: 1.5rem;
        color: #1f2937; /* Darker heading color */
    }

    p {
        font-size: 1.125rem;
        margin-bottom: 1.5rem;
        color: #374151; /* Subtle text color */
    }

    ul {
        list-style: none;
        padding: 0;
    }

    ul li {
        margin: 0.5rem 0;
    }

    ul li a {
        color: #2563eb; /* Blue links */
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
        color: #374151;
    }

    /* Contact Form Styles */
    form {
        display: flex;
        flex-direction: column;
        gap: 1rem;
    }

    label {
        font-weight: 600;
        color: #1f2937;
    }

    input,
    textarea {
        width: 100%;
        padding: 0.75rem;
        font-size: 1rem;
        border: 1px solid #d1d5db;
        border-radius: 4px;
    }

    input:focus,
    textarea:focus {
        outline: none;
        border-color: #2563eb;
        box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.3);
    }

    button {
        padding: 0.75rem 1.5rem;
        background-color: #2563eb;
        color: white;
        border: none;
        border-radius: 4px;
        font-size: 1rem;
        cursor: pointer;
        transition: background-color 0.3s;
    }

    button:hover {
        background-color: #1d4ed8;
    }
</style>
