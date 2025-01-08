<script>
    import Hero from '../components/Hero.svelte';
  
    // Static text variables for the hero section
    let heading = "Welcome to My Website";
    let subheading = "Building a future for brain-computer interfaces.";
  </script>
  
  <Hero {heading} {subheading} />
  
  <style>
    /* Base styling for the page, setting a full black background and white text */
    html, body {
      margin: 0;
      padding: 0;
      background: #000;
      color: white;
      height: 100%;
      width: 100%;
    }
  
    /* Styles for the hero section, ensuring it spans the full viewport height */
    .hero {
      display: flex;
      justify-content: space-between;
      align-items: center;
      height: 100vh;
      padding: 2rem;
      background: #000; /* Consistent black background for branding */
      color: white;
    }
  
    /* Optional flex containers for structuring hero section content */
    .hero-left {
      flex: 1;
    }
  
    .hero-right {
      flex: 1;
      max-width: 500px;
    }
  
    /* Main title styling for the hero section */
    .hero-title {
      font-size: 4rem;
      font-weight: bold;
      line-height: 1.2;
    }
  
    /* Highlighted text styling using a gradient fill */
    .highlight {
      background: linear-gradient(90deg, #32cd32, #ff4500);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }
  
    /* General text styling for readability and consistency */
    .hero-text {
      font-size: 1.5rem;
      line-height: 1.6;
    }
  </style>
  