<script>
  import { onMount } from 'svelte';
  import Hero from '../components/Hero.svelte';
  import About from '../components/About.svelte';
  import Publications from '../components/Publications.svelte';
  import Team from '../components/Team.svelte';
  import News from '../components/News.svelte';
  import Contact from '../components/Contact.svelte';
  import Footer from '../components/Footer.svelte';

  // Add smooth scroll functionality
  onMount(() => {
    const smoothScroll = (event) => {
      if (event.target.tagName === 'A' && event.target.hash) {
        const target = document.querySelector(event.target.hash);
        if (target) {
          event.preventDefault();
          target.scrollIntoView({ behavior: 'smooth' });
        }
      }
    };

    document.addEventListener('click', smoothScroll);
    return () => document.removeEventListener('click', smoothScroll);
  });
</script>

<Hero />
<About />
<Publications />
<Team />
<News />
<Contact />
<Footer />
