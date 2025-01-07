<script>
  import { onMount } from 'svelte';
  let fadeIn = false;

  let publications = [
    {
      id: 1,
      title: "Brain-Computer Interfaces: A Comprehensive Review",
      year: 2023,
      category: "Review",
      link: "https://example.com/publication1"
    },
    {
      id: 2,
      title: "Neural Decoding with AI: Advances in 2023",
      year: 2022,
      category: "Research",
      link: "https://example.com/publication2"
    },
    {
      id: 3,
      title: "Insights into Neural Signal Processing",
      year: 2023,
      category: "Research",
      link: "https://example.com/publication3"
    }
  ];

  onMount(() => {
    fadeIn = true;
  });
</script>

<section
  id="publications"
  class="publications-section fade-in"
  class:fade-in={fadeIn}
>
  <h2 class="title">Publications</h2>

  <div class="grid">
    {#each publications as pub}
      <a href={pub.link} target="_blank" class="card">
        <h3 class="card-title">{pub.title}</h3>
        <p class="card-meta">
          Year: {pub.year} | Category: {pub.category}
        </p>
      </a>
    {/each}
  </div>
</section>

<style>
  .publications-section {
    padding: 5rem 1rem;
    background-color: #121212;
    color: #ffffff;
    text-align: center;
  }

  .title {
    font-size: 2.5rem;
    margin-bottom: 3rem;
    color: var(--accent);
  }

  .grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 2rem;
    max-width: 1200px;
    margin: 0 auto;
  }

  .card {
    background: #1e1e1e;
    padding: 1.5rem;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    text-decoration: none;
    color: #ffffff;
    transition: transform 0.3s, box-shadow 0.3s;
  }

  .card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
  }

  .card-title {
    font-size: 1.25rem;
    margin-bottom: 0.5rem;
  }

  .card-meta {
    font-size: 0.95rem;
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
    .title {
      font-size: 2rem;
    }

    .card-title {
      font-size: 1rem;
    }

    .card-meta {
      font-size: 0.85rem;
    }
  }
</style>
