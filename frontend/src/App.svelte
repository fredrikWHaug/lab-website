<script>
  let tagline = "Advancing Neuroscience Through Innovation";
</script>

<section class="hero">
  <h1 class="lab-name">Liu Lab</h1>
  <p class="tagline">{tagline}</p>
  <div class="cta-buttons">
    <button on:click={() => scrollTo('#about')}>About Us</button>
    <button on:click={() => scrollTo('#join')}>Join the Lab</button>
  </div>
</section>

<section id="about" class="section">
  <h2>About Us</h2>
  <p>Placeholder text for the lab's mission and research goals.</p>
</section>

<section id="publications" class="section">
  <h2>Publications</h2>
  <p>Placeholder for a dynamic list of publications with filters.</p>
</section>

<section id="team" class="section">
  <h2>Our Team</h2>
  <p>Grid layout for team profiles will go here.</p>
</section>

<section id="news" class="section">
  <h2>News & Updates</h2>
  <p>A feed of lab news and events will go here.</p>
</section>

<section id="contact" class="section">
  <h2>Contact Us</h2>
  <p>Interactive map and contact form placeholder.</p>
</section>

<style>
  .hero {
    background: #1E1E1E;
    color: #EAEAEA;
    text-align: center;
    padding: 5rem 1rem;
  }

  .section {
    padding: 3rem 1rem;
    border-top: 1px solid #333;
  }

  h2 {
    color: #FFD700;
    text-align: center;
    margin-bottom: 1rem;
  }

  p {
    text-align: center;
    max-width: 600px;
    margin: 0 auto;
  }
</style>
