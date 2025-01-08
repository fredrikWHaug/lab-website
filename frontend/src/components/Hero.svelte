<script>
  import { onMount } from 'svelte';

  // Controls whether the hero section should display the fade-in animation.
  let fadeIn = false;

  // Trigger the fade-in effect when the component is mounted.
  onMount(() => {
    fadeIn = true;
  });

  // Smoothly scrolls to a section of the page identified by its ID.
  function scrollToSection(id) {
    const section = document.querySelector(id);
    if (section) {
      section.scrollIntoView({ behavior: 'smooth' });
    }
  }
</script>

<section
  class="hero"
  class:fade-in={fadeIn}
>
  <div class="content">
    <h1 class="title">Innovating the Future of Neuroscience</h1>
    <p class="subtitle">Explore cutting-edge research and transformative technology.</p>
    <div class="cta-buttons">
      <button on:click={() => scrollToSection('#about')}>Learn More</button>
      <button on:click={() => scrollToSection('#contact')}>Get in Touch</button>
    </div>
  </div>
</section>

<style>
  /* Main hero section: occupies full viewport height with a gradient background and centered content. */
  .hero {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    background: linear-gradient(120deg, #0f2027, #203a43, #2c5364);
    color: #ffffff;
    text-align: center;
    padding: 0 1rem;
    overflow: hidden;
    position: relative;
  }

  /* Background image overlay with reduced opacity for a subtle effect. */
  .hero::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: url('https://via.placeholder.com/1920x1080') center/cover no-repeat;
    opacity: 0.3;
    z-index: 1;
  }

  /* Ensures content appears above the background overlay. */
  .content {
    position: relative;
    z-index: 2;
  }

  /* Styling for the headline and supporting text. */
  .title {
    font-size: 3rem;
    font-weight: 700;
    margin-bottom: 1rem;
  }

  .subtitle {
    font-size: 1.5rem;
    margin-bottom: 2rem;
    color: #d1d1d1;
  }

  /* Call-to-action buttons with hover effects. */
  .cta-buttons button {
    padding: 1rem 2rem;
    font-size: 1rem;
    margin: 0.5rem;
    border: none;
    border-radius: 4px;
    color: #ffffff;
    background: #ff7f50;
    cursor: pointer;
    transition: transform 0.3s, background-color 0.3s;
  }

  .cta-buttons button:hover {
    transform: translateY(-5px);
    background: #ff4500;
  }

  /* Fade-in animation for the hero section. */
  .fade-in {
    opacity: 0;
    animation: fadeIn 1s forwards;
  }

  @keyframes fadeIn {
    to {
      opacity: 1;
    }
  }

  /* Adjustments for smaller screens to maintain readability. */
  @media (max-width: 768px) {
    .title {
      font-size: 2rem;
    }

    .subtitle {
      font-size: 1rem;
    }
  }
</style>
