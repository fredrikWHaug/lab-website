<script>
  import { onMount } from 'svelte';
  let fadeIn = false;

  onMount(() => {
    fadeIn = true;
  });

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

  .content {
    position: relative;
    z-index: 2;
  }

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

  .fade-in {
    opacity: 0;
    animation: fadeIn 1s forwards;
  }

  @keyframes fadeIn {
    to {
      opacity: 1;
    }
  }

  @media (max-width: 768px) {
    .title {
      font-size: 2rem;
    }

    .subtitle {
      font-size: 1rem;
    }
  }
</style>
