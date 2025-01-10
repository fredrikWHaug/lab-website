<!-- Hero Section -->
<section class="hero">
  <nav class="navbar">
    <div class="logo-container">
      <img
        src="https://soldered.com/productdata/2023/03/schematic-bjt-npn.png"
        alt="Logo"
        class="logo"
        aria-label="Logo"
      />
    </div>
    <div class="navbar-content">
      <div class="search">
        <input
          type="text"
          placeholder="Search..."
          class="search-input"
          aria-label="Search input"
        />
      </div>

      <ul class="nav-links">
        <li><a href="#companies">Companies</a></li>
        <li><a href="#residency">Residency</a></li>
        <li><a href="#programs">Programs</a></li>
        <li><a href="#ecosystem">Ecosystem</a></li>
        <li><a href="#about">About</a></li>
      </ul>
    </div>
  </nav>
</section>

<!-- Style Section -->
<style>
  .hero {
    background-color: #000;
    color: white;
    height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    padding: 0;
  }

  .navbar {
    display: flex;
    align-items: flex-end; /* Keeps the alignment of the navbar as requested */
    justify-content: flex-end;
    width: 100%;
    padding: 1rem 2rem;
    font-family: "Inter", sans-serif;
  }

  .navbar-content {
    display: flex;
    align-items: center;
    justify-content: flex-end;
    width: auto;
    border-bottom: 1px solid rgba(255, 255, 255, 0.2);
    padding-bottom: 0.5rem;
  }

  .logo-container {
    margin-top: 0.5rem; /* Adjust this value to move the logo down */
    margin-right: auto; /* Keeps the logo aligned to the far left */
    display: flex;
    align-items: center; /* Ensures vertical centering within the container */
  }



  .logo {
    width: 75px; /* Maintains increased size */
    height: 75px; /* Maintains proportions */
    border-radius: 50%; /* Makes the logo circular */
    object-fit: cover;
    transition: transform 0.3s;
  }

  .logo:hover {
    transform: scale(1.1); /* Subtle increase in size on hover */
  }

  .search {
    flex: 0 1 auto;
    display: flex;
    align-items: center;
    margin-right: 2rem; /* Adjust spacing from the next word */
    padding: 0.3rem 0.5rem;
    border: 1px solid rgba(255, 255, 255, 0.2);
    border-radius: 0; /* Sharp edges */
    transition: border 0.3s, background-color 0.3s;
  }

  .search:hover {
    border: 1px solid white;
    background-color: rgba(255, 255, 255, 0.1);
  }

  .search-input {
    font-size: 1rem;
    color: rgba(255, 255, 255, 0.7);
    background: none;
    border: none;
    outline: none;
    width: 100%;
  }

  .nav-links {
    display: flex;
    justify-content: flex-end; /* Aligns links closer to the right */
    gap: 2rem;
    padding-right: 1rem; /* Adds natural spacing from the right edge */
  }

  .nav-links li {
    list-style: none;
  }

  .nav-links a {
    text-decoration: none;
    color: white;
    font-size: 1rem;
    font-weight: 500;
    padding-bottom: 0.5rem;
    transition: color 0.3s, border-bottom 0.3s;
  }

  .nav-links a:hover {
    color: white;
    border-bottom: 2px solid white;
  }

  @media (max-width: 768px) {
    .navbar-content {
      flex-direction: column;
      align-items: flex-start;
    }

    .nav-links {
      justify-content: flex-start;
      gap: 1rem;
      flex-wrap: wrap;
    }

    .search {
      margin-bottom: 1rem;
    }
  }
</style>
