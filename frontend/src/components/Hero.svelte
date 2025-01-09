
<section class="hero">
  <!-- Navigation Bar -->
  <nav class="navbar">
    <!-- Left: Search Section -->
    <div class="search">
      <span class="search-text">Search</span>
    </div>

    <!-- Center: Navigation Links -->
    <ul class="nav-links">
      <li><a href="#companies">Companies</a></li>
      <li><a href="#residency">Residency</a></li>
      <li><a href="#programs">Programs</a></li>
      <li><a href="#ecosystem">Ecosystem</a></li>
      <li><a href="#about">About</a></li>
    </ul>
  </nav>
</section>

<style>
  /* Hero Section */
  .hero {
    background-color: #000;
    color: white;
    height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    padding: 0;
  }

  /* Navbar */
  .navbar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    width: 100%;
    padding: 1rem 2rem;
    border-bottom: 1px solid rgba(255, 255, 255, 0.2); /* Single underline for entire navbar */
    font-family: "Inter", sans-serif;
  }

  /* Search Section */
  .search {
    flex: 0 1 auto;
    display: flex;
    align-items: center;
  }

  .search-text {
    font-size: 1rem;
    color: rgba(255, 255, 255, 0.7);
    cursor: pointer;
    border-bottom: 1px solid rgba(255, 255, 255, 0.2); /* Underline for search */
  }

  .search-text:hover {
    color: white;
  }

  /* Navigation Links */
  .nav-links {
    flex: 1;
    display: flex;
    justify-content: center; /* Center the links */
    gap: 2rem; /* Spacing between links */
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
    transition: color 0.3s;
  }

  .nav-links a:hover {
    color: #fbbd08;
  }
</style>