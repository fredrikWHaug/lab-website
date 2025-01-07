<script>
  import { onMount } from 'svelte';
  let fadeIn = false;

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
    }
  ];

  onMount(() => {
    fadeIn = true;
  });
</script>

<section
  id="team"
  class="team-section fade-in"
  class:fade-in={fadeIn}
>
  <h2 class="title">Our Team</h2>

  <div class="grid">
    {#each team as member}
      <div class="card">
        <img src={member.photo} alt="{member.name}" loading="lazy" />
        <h3 class="name">{member.name}</h3>
        <p class="role">{member.role}</p>
        <div class="links">
          {#if member.linkedin}
            <a href={member.linkedin} target="_blank" class="link">LinkedIn</a>
          {/if}
          {#if member.github}
            <a href={member.github} target="_blank" class="link">GitHub</a>
          {/if}
        </div>
      </div>
    {/each}
  </div>
</section>

<style>
  .team-section {
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
    padding: 2rem;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    text-align: center;
    transition: transform 0.3s, box-shadow 0.3s;
  }

  .card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
  }

  img {
    width: 100px;
    height: 100px;
    border-radius: 50%;
    margin-bottom: 1rem;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  }

  .name {
    font-size: 1.25rem;
    margin: 0.5rem 0;
  }

  .role {
    font-size: 1rem;
    color: #d1d1d1;
    margin-bottom: 1rem;
  }

  .links {
    display: flex;
    justify-content: center;
    gap: 1rem;
  }

  .link {
    color: var(--accent);
    text-decoration: none;
    font-size: 0.9rem;
    transition: color 0.3s;
  }

  .link:hover {
    color: #ffffff;
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

    .name {
      font-size: 1rem;
    }

    .role {
      font-size: 0.85rem;
    }

    .link {
      font-size: 0.8rem;
    }
  }
</style>
