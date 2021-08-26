<template>

    <div class="contact">
      <div class="heading">
        <h1>Interested in working with us?</h1>
        <h2>Quality software guaranteed</h2>
      </div>

      <div class="buttons">
        <router-link to="/" class="button_link"
          ><button class="button request">Request Demo</button></router-link
        >
        <router-link to="/trial" class="button_link"
          ><button class="button trial">Free Trial</button></router-link
        >
      </div>
    </div>
</template>

<script>
export default {};
</script>

<style scoped>
.contact {
  text-align: center;
  background: white;
  font-style: italic;
  margin-bottom: var(--mb-4);
  line-height: 1.2;
}
.heading {
  margin-bottom: var(--mb-3);
  padding-top: 1rem;
}
.buttons {
  display: flex;
  justify-content: space-around;
  padding-bottom: var(--mb-4);
}

.button {
  font-style: italic;
  font-size: var(--h2-font-size);
  font-family: var(--body-font);
  font-weight: var(--font-semi-bold);
}
.button:hover {
  background: linear-gradient(to bottom right, var(--blue), var(--turquoise));
  color: var(--white);
  transition: 0.2s ease-in all;
}
.request {
  background-color: var(--white);
  color: var(--blue);
  border: 2px solid var(--blue);
  padding: 1rem 2rem;
}

.trial {
  background: var(--blue);
  color: var(--turquoise);
  border: 2px solid var(--turquoise);
  padding: 1rem 3rem;
}

/* ===== RESPONSIVE DESIGN ===== */

@media only screen and (max-width: 520px) {
  .heading {
    margin: 0;
  }
  .buttons {
    flex-direction: column;
  }

  .button {
    margin-top: 2rem;
  }

  .button:last-child {
    margin-bottom: 0;
  }
}
</style>