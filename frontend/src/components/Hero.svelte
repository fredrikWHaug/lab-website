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

<style>
  .hero {
    background: #1E1E1E;
    color: #EAEAEA;
    text-align: center;
    padding: 5rem 1rem;
  }
</style>
