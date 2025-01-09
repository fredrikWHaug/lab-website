<script>
  import Hero from '../components/Hero.svelte';

  // Static text variables for the hero section
  let heading = "Welcome to My Website";
  let subheading = "Building a future for brain-computer interfaces.";
</script>

<Hero {heading} {subheading} />
