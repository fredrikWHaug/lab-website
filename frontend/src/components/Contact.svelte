<script>
  let name = "";
  let email = "";
  let message = "";

  function handleSubmit(event) {
    event.preventDefault();
    alert(`Thank you, ${name}! Your message has been sent.`);
    name = "";
    email = "";
    message = "";
  }
</script>

<section id="contact" class="contact-section">
  <h2 class="title">Get in Touch</h2>

  <div class="content">
    <!-- Contact Form -->
    <form on:submit={handleSubmit} class="contact-form">
      <div class="form-group">
        <label for="name">Name</label>
        <input
          type="text"
          id="name"
          bind:value={name}
          placeholder="Enter your name"
          required
        />
      </div>

      <div class="form-group">
        <label for="email">Email</label>
        <input
          type="email"
          id="email"
          bind:value={email}
          placeholder="Enter your email"
          required
        />
      </div>

      <div class="form-group">
        <label for="message">Message</label>
        <textarea
          id="message"
          bind:value={message}
          placeholder="Enter your message"
          rows="5"
          required
        ></textarea>
      </div>

      <button type="submit">Send</button>
    </form>

    <!-- Map Placeholder -->
    <div class="map-container">
      <iframe
        src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3151.8354345093743!2d-122.42067998468192!3d37.77492977975908!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x80858064a40b2fd1%3A0x94f7dcb2cf660f65!2sSan%20Francisco!5e0!3m2!1sen!2sus!4v1614756494385!5m2!1sen!2sus"
        width="100%"
        height="300"
        style="border:0;"
        allowfullscreen=""
        loading="lazy"
        title="Map of San Francisco"
      ></iframe>
    </div>
  </div>
</section>

<style>
  .contact-section {
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

  .content {
    display: flex;
    flex-wrap: wrap;
    gap: 2rem;
    max-width: 1200px;
    margin: 0 auto;
  }

  .contact-form {
    flex: 1;
    min-width: 300px;
    background: #1e1e1e;
    padding: 2rem;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  }

  .form-group {
    margin-bottom: 1.5rem;
    text-align: left;
  }

  label {
    display: block;
    margin-bottom: 0.5rem;
    color: var(--accent);
  }

  input,
  textarea {
    width: 100%;
    padding: 0.75rem;
    border: 1px solid #333;
    border-radius: 4px;
    background: #1e1e1e;
    color: #ffffff;
    font-size: 1rem;
  }

  input:focus,
  textarea:focus {
    outline: none;
    border-color: var(--accent);
    box-shadow: 0 0 5px var(--accent);
  }

  button {
    padding: 0.75rem 1.5rem;
    font-size: 1rem;
    background: var(--accent);
    color: #121212;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s, transform 0.3s;
  }

  button:hover {
    background-color: #ffffff;
    color: #121212;
    transform: translateY(-2px);
  }

  .map-container {
    flex: 1;
    min-width: 300px;
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  }

  iframe {
    width: 100%;
    height: 100%;
    border: 0;
  }

  @media (max-width: 768px) {
    .content {
      flex-direction: column;
    }

    .title {
      font-size: 2rem;
    }
  }
</style>
