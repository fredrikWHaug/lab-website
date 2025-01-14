<!-- Hero Section -->
<section class="hero">
  <div class="logo-container">
    <img
      src="https://www.ledr.com/colours/white.jpg"
      alt="Logo"
      class="logo"
      aria-label="Logo"
    />
  </div>
  <nav class="navbar">
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
        <li><a href="#people">People</a></li>
        <li><a href="#openings">Openings</a></li>
        <li><a href="#press">Press</a></li>
        <li><a href="#research">Research</a></li>
        <li><a href="#publications">Publications</a></li>
        <li><a href="#news">News</a></li>
        <li><a href="#pictures">Pictures</a></li>
        <li><a href="#contact">Contact</a></li>
      </ul>
    </div>
  </nav>
  <div class="hero-text">
    <p style="color: white;">
      Pictures
      Contact
      Using our specialized experimental and computational expertise, we aim to understand the relationship between the population dynamics of single-cell multimodal physiology and gene expression and the functions and dysfunctions of whole organs and organisms. Our research addresses questions in the field of brain-computer interfaces, neuroengineering, and stem cell engineering.
    </p>
  </div>
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

  .logo-container {
    position: absolute;
    margin-top: 1.5rem;
    margin-left: 2.8rem;
    display: flex;
    align-items: center;
  }

  .logo {
    width: 75px;
    height: 75px;
    border-radius: 50%;
    object-fit: cover;
    transition: transform 0.3s;
  }

  .logo:hover {
    transform: scale(1.1);
  }

  .navbar {
    display: flex;
    align-items: flex-end;
    justify-content: flex-end;
    width: 100%;
    padding: 1rem 2rem;
    font-family: "Inter", sans-serif;
    margin-top: 2rem;
  }

  .navbar-content {
    display: flex;
    align-items: center;
    justify-content: flex-end;
    width: auto;
    border-bottom: 1px solid rgba(255, 255, 255, 0.2);
    padding-bottom: 0.5rem;
  }

  .search {
    flex: 0 1 auto;
    display: flex;
    align-items: center;
    margin-right: 2rem;
    padding: 0.3rem 0.5rem;
    border: 1px solid rgba(255, 255, 255, 0.2);
    border-radius: 0;
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
    justify-content: flex-end;
    gap: 1.5rem;
    flex-wrap: wrap;
    padding-right: 1rem;
  }

  .nav-links li {
    list-style: none;
  }

  .nav-links a {
    text-decoration: none;
    color: white;
    font-size: 0.9rem;
    font-weight: 500;
    padding-bottom: 0.5rem;
    transition: color 0.3s, border-bottom 0.3s;
  }

  .nav-links a:hover {
    color: white;
    border-bottom: 2px solid white;
  }

  .hero-text {
    margin: auto 2rem;
    font-family: "Inter", sans-serif;
    font-size: 1.2rem;
    font-weight: 500;
    line-height: 1.8;
    color: rgba(255, 255, 255, 0.7);
    max-width: 45%;
    text-align: justify;
    position: absolute;
    right: 2rem;
    top: 15%;
  }

  .hero-text p {
    margin: 0;
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

    .hero-text {
      margin: 1rem;
      font-size: 1rem;
      max-width: 100%;
    }
  }
</style>
