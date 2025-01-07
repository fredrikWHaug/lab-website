<script>
  let tagline = "Advancing Neuroscience Through Innovation";
</script>

<section class="hero">
  <h1 class="lab-name">Liu Lab</h1>
  <p class="tagline">{tagline}</p>
  <div class="cta-buttons">
    <button on:click={() => scrollTo('#research')}>Explore Research</button>
    <button on:click={() => scrollTo('#join')}>Join the Lab</button>
  </div>
</section>

<style>
  .hero {
    background: #1E1E1E;
    color: #EAEAEA;
    text-align: center;
    padding: 5rem 1rem;
  }

  .lab-name {
    font-size: 3rem;
    font-family: 'Merriweather', serif;
  }

  .tagline {
    font-size: 1.5rem;
    margin: 1rem 0;
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
