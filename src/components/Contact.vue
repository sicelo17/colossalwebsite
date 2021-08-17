<template>
  <div class="bd-container">
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
  </div>
</template>

<script>
export default {

}
</script>

<style scoped>
.contact{
    text-align: center;
    background: white;
    font-style: italic;
    margin-bottom: 2rem;
}
.buttons {
    display: flex;
    justify-content: space-around;
    padding-bottom: 2rem;
}

.button {
    font-style: italic;
    font-size: 1.6rem;
    font-family: var(--body-font);
    font-weight: var(--font-semi-bold);
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
</style>