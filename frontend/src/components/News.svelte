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

<section id="news" class="section">
  <h2>News & Updates</h2>

  <!-- News Feed -->
  <ul class="news-list">
    {#each news as item}
      <li class="news-card">
        <h3>{item.title}</h3>
        <p class="date">{item.date}</p>
        <p class="preview">{item.preview}</p>
      </li>
    {/each}
  </ul>
</section>

<style>
  .section {
    padding: 3rem 1rem;
    border-top: 1px solid #333;
    text-align: center;
  }

  h2 {
    color: #FFD700;
    margin-bottom: 2rem;
  }

  .news-list {
    list-style: none;
    padding: 0;
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 1.5rem;
  }

  .news-card {
    background: #2E2E2E;
    color: #EAEAEA;
    padding: 1.5rem;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
  }

  .news-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
  }

  h3 {
    margin: 0 0 0.5rem;
  }

  .date {
    margin: 0 0 1rem;
    font-size: 0.9rem;
    color: #FFD700;
  }

  .preview {
    font-size: 0.95rem;
  }

  @media (max-width: 768px) {
    .news-card {
      padding: 1rem;
    }

    h3 {
      font-size: 1rem;
    }

    .date,
    .preview {
      font-size: 0.85rem;
    }
  }
</style>
