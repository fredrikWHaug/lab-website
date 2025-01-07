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

<section id="contact" class="section">
  <h2>Contact Us</h2>

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

  <!-- Google Map Embed -->
  <div class="map-container">
    <iframe
      src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3151.8354345093743!2d-122.42067998468192!3d37.77492977975908!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x80858064a40b2fd1%3A0x94f7dcb2cf660f65!2sSan%20Francisco!5e0!3m2!1sen!2sus!4v1614756494385!5m2!1sen!2sus"
      width="100%"
      height="300"
      style="border:0;"
      allowfullscreen=""
      loading="lazy"
    ></iframe>
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

  .contact-form {
    max-width: 600px;
    margin: 0 auto;
    background: #2E2E2E;
    padding: 1.5rem;
    border-radius: 8px;
    color: #EAEAEA;
  }

  .form-group {
    margin-bottom: 1rem;
    text-align: left;
  }

  label {
    display: block;
    margin-bottom: 0.5rem;
    color: #FFD700;
  }

  input,
  textarea {
    width: 100%;
    padding: 0.75rem;
    border: 1px solid #555;
    border-radius: 4px;
    background: #1E1E1E;
    color: #EAEAEA;
  }

  button {
    padding: 0.75rem 1.5rem;
    border: none;
    background: #FFD700;
    color: #1E1E1E;
    font-weight: bold;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s;
  }

  button:hover {
    background-color: #FFC300;
  }

  .map-container {
    margin-top: 2rem;
    border-radius: 8px;
    overflow: hidden;
  }
</style>
