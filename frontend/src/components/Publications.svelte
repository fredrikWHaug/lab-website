<script>
  let publications = [
    { id: 1, title: "Brain-Computer Interfaces 101", year: 2023, category: "Review" },
    { id: 2, title: "Advances in Neural Imaging", year: 2022, category: "Research" },
    { id: 3, title: "Decoding Brain Signals", year: 2023, category: "Research" },
    { id: 4, title: "Artificial Intelligence in Neuroscience", year: 2021, category: "Review" }
  ];

  let filterYear = "All";
  let filteredPublications = publications;

  // Filter publications dynamically
  function filterByYear() {
    if (filterYear === "All") {
      filteredPublications = publications;
    } else {
      filteredPublications = publications.filter(pub => pub.year.toString() === filterYear);
    }
  }
</script>

<section id="publications" class="section">
  <h2>Publications</h2>

  <!-- Filter Dropdown -->
  <div class="filter">
    <label for="year-filter">Filter by Year:</label>
    <select id="year-filter" bind:value={filterYear} on:change={filterByYear}>
      <option>All</option>
      <option>2023</option>
      <option>2022</option>
      <option>2021</option>
    </select>
  </div>

  <!-- Publications List -->
  <ul class="publication-list">
    {#each filteredPublications as pub}
      <li class="publication-card">
        <h3>{pub.title}</h3>
        <p>Year: {pub.year} | Category: {pub.category}</p>
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

  .filter {
    margin-bottom: 2rem;
  }

  select {
    padding: 0.5rem;
    border-radius: 4px;
    border: 1px solid #555;
    background: #1E1E1E;
    color: #EAEAEA;
  }

  .publication-list {
    list-style: none;
    padding: 0;
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1.5rem;
  }

  .publication-card {
    background: #2E2E2E;
    color: #EAEAEA;
    padding: 1.5rem;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
  }

  .publication-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
  }

  h3 {
    margin: 0 0 0.5rem;
  }

  p {
    margin: 0;
    font-size: 0.9rem;
    color: #FFD700;
  }

  @media (max-width: 768px) {
    .publication-card {
      padding: 1rem;
    }

    h3 {
      font-size: 1rem;
    }

    p {
      font-size: 0.8rem;
    }
  }
</style>
