<script>
  import { onMount } from 'svelte';
  let fadeIn = false;

  onMount(() => {
    fadeIn = true;
  });
</script>

<section
  id="about"
  class="about-section fade-in"
  class:fade-in={fadeIn}
>
  <div class="content">
    <div class="text">
      <h2 class="title">About Us</h2>
      <p class="description">
        At Liu Lab, we are dedicated to advancing the frontiers of neuroscience through cutting-edge research and transformative technology. Our mission is to bridge the gap between scientific discovery and real-world applications.
      </p>
    </div>
    <div class="image">
      <img src="https://via.placeholder.com/600x400" alt="Liu Lab Research" loading="lazy" />
    </div>
  </div>
</section>

<style>
  .about-section {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    padding: 3rem 1rem;
    background-color: #121212;
    color: #ffffff;
  }

  .content {
    display: flex;
    flex-wrap: wrap;
    max-width: 1200px;
    gap: 2rem;
    align-items: center;
  }

  .text {
    flex: 1;
    min-width: 300px;
  }

  .image {
    flex: 1;
    min-width: 300px;
    display: flex;
    justify-content: center;
  }

  img {
    max-width: 100%;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
  }

  .title {
    font-size: 2.5rem;
    margin-bottom: 1rem;
  }

  .description {
    font-size: 1.25rem;
    line-height: 1.8;
    color: #d1d1d1;
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
    .content {
      flex-direction: column;
    }

    .title {
      font-size: 2rem;
    }

    .description {
      font-size: 1rem;
    }
  }
</style>
