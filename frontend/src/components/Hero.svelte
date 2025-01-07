<script>
  function scrollToSection(id) {
    const section = document.querySelector(id);
    if (section) {
      section.scrollIntoView({ behavior: 'smooth' });
    }
  }
</script>

<section class="hero">
  <h1 class="lab-name">Liu Lab</h1>
  <p class="tagline">Advancing Neuroscience Through Innovation</p>
  <div class="cta-buttons">
    <button on:click={() => scrollToSection('#about')}>About Us</button>
    <button on:click={() => scrollToSection('#contact')}>Contact</button>
  </div>
</section>

<style>
  .hero {
    background: #1E1E1E;
    color: #EAEAEA;
    text-align: center;
    padding: 5rem 1rem;
  }

  .cta-buttons button {
    margin: 0.5rem;
    padding: 0.75rem 1.5rem;
    border: none;
    color: #1E1E1E;
    background-color: #EAEAEA;
    cursor: pointer;
    font-weight: bold;
    transition: background-color 0.3s;
  }

  .cta-buttons button:hover {
    background-color: #FFD700;
  }
</style>
