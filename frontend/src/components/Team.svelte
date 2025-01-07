<script>
  let team = [
    {
      id: 1,
      name: "Dr. Liu",
      role: "Principal Investigator",
      photo: "https://via.placeholder.com/150",
      linkedin: "#",
      github: "#"
    },
    {
      id: 2,
      name: "Alice Smith",
      role: "Postdoctoral Researcher",
      photo: "https://via.placeholder.com/150",
      linkedin: "#",
      github: "#"
    },
    {
      id: 3,
      name: "John Doe",
      role: "Graduate Student",
      photo: "https://via.placeholder.com/150",
      linkedin: "#",
      github: "#"
    },
    {
      id: 4,
      name: "Jane Roe",
      role: "Undergraduate Student",
      photo: "https://via.placeholder.com/150",
      linkedin: "#",
      github: "#"
    }
  ];
</script>

<section id="team" class="section">
  <h2>Our Team</h2>

  <!-- Team Grid -->
  <div class="team-grid">
    {#each team as member}
      <div class="team-card">
        <img src={member.photo} alt="Photo of {member.name}" />
        <h3>{member.name}</h3>
        <p>{member.role}</p>
        <div class="links">
          <a href={member.linkedin} target="_blank">LinkedIn</a>
          <a href={member.github} target="_blank">GitHub</a>
        </div>
      </div>
    {/each}
  </div>
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

  .team-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
    gap: 1.5rem;
    justify-items: center;
  }

  .team-card {
    background: #2E2E2E;
    color: #EAEAEA;
    padding: 1rem;
    border-radius: 8px;
    text-align: center;
    width: 100%;
    max-width: 250px;
  }

  .team-card img {
    width: 100px;
    height: 100px;
    border-radius: 50%;
    margin-bottom: 1rem;
  }

  .team-card h3 {
    margin: 0.5rem 0;
    font-size: 1.2rem;
  }

  .team-card p {
    margin: 0.5rem 0 1rem 0;
    font-size: 0.9rem;
    color: #FFD700;
  }

  .links a {
    margin: 0 0.25rem;
    color: #FFD700;
    text-decoration: none;
    font-size: 0.8rem;
  }

  .links a:hover {
    text-decoration: underline;
  }

  @media (max-width: 768px) {
    .team-card img {
      width: 80px;
      height: 80px;
    }

    .team-card h3 {
      font-size: 1rem;
    }

    .team-card p {
      font-size: 0.8rem;
    }
  }
</style>
