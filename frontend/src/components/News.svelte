<script>
  let news = [
    {
      id: 1,
      title: "Liu Lab Wins Prestigious Grant",
      date: "2025-01-05",
      preview: "We are thrilled to announce that Liu Lab has received a prestigious grant to advance research in brain-computer interfaces."
    },
    {
      id: 2,
      title: "New Publication in Nature Neuroscience",
      date: "2024-12-20",
      preview: "Our latest research on neural signal decoding has been published in Nature Neuroscience."
    },
    {
      id: 3,
      title: "Liu Lab Welcomes New Members",
      date: "2024-11-15",
      preview: "We are excited to welcome two new postdoctoral researchers to our team!"
    }
  ];
</script>

<section id="news" class="section fade-in">
  <h2>News & Updates</h2>

  <ul class="news-list">
    {#each news as item}
      <li class="card">
        <h3>{item.title}</h3>
        <p class="date">{item.date}</p>
        <p class="preview">{item.preview}</p>
        <!-- Example image placeholder -->
        <img src="https://via.placeholder.com/300x150" alt="News Thumbnail" loading="lazy" />
      </li>
    {/each}
  </ul>
</section>

<style>
  .section {
    padding: 3rem 1rem;
    border-top: 1px solid var(--border);
    text-align: center;
  }

  h2 {
    color: var(--accent);
    margin-bottom: 2rem;
  }

  .news-list {
    list-style: none;
    padding: 0;
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 1.5rem;
  }

  h3 {
    margin: 0 0 0.5rem;
    font-family: 'Merriweather', serif;
    color: var(--accent);
  }

  .date {
    margin: 0 0 1rem;
    font-size: 0.9rem;
    color: var(--text);
  }

  .preview {
    font-size: 0.95rem;
    color: var(--text);
  }

  img {
    width: 100%;
    border-radius: 8px;
    margin-top: 1rem;
  }
</style>
