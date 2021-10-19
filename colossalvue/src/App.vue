<template>
  <Header />
  <router-view />
  <Footer />
</template>

<script>
import Header from "./components/Header.vue";
import Footer from "./components/Footer.vue";
import axios from 'axios';

export default {
  components: {
    Header,
    Footer,
  },
  beforeCreate(){
    this.$store.commit("initializeStore");
    const token = this.$store.state.token;
    if (token) {
      axios.defaults.headers.common["Authorization"] = "Token " + token;
    } else {
      axios.defaults.headers.common["Authorization"] = "";
    }
  }
};
</script>
<style>
/* ==== GOOGLE FONTS ==== */
@import url("https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,500;0,700;1,400;1,500;1,600;1,700&family=Poppins:wght@400;500;600&display=swap");

/* ==== VARIABLES CSS ==== */

:root {
  --header-height: 3rem;

  /* ==== COLORS ==== */
  --off-white: #e0e0e0;
  --white: #fff;
  --blue: #243665;
  --turquoise: #8bd8bd;

  /* ==== FONTS AND TYPOGRAPHY ==== */
  --body-font: "EB Garamond", serif;
  --font-2: "Poppins", sans-serif;
  --biggest-font-size: 2.5rem;
  --h1-font-size: 1.5rem;
  --h2-font-size: 1.25rem;
  --h3-font-size: 1.125rem;
  --normal-font-size: 0.938rem;
  --small-font-size: 0.813rem;
  --smaller-font-size: 0.75rem;

  /* ==== FONT WEIGHT ==== */
  --font-medium: 400;
  --font-semi-bold: 500;
  --font-bold: 700;

  /* ==== MARGINS ==== */
  --mb-1: 0.5rem;
  --mb-2: 1rem;
  --mb-3: 1.5rem;
  --mb-4: 2rem;
  --mb-5: 2.5rem;
  --mb-6: 3rem;

  /* ==== z-index ==== */
  --z-normal: 1;
  --z-top: 99;
}

@media screen and (min-width: 768px) {
  :root {
    --biggest-font-size: 4.5rem;
    --h1-font-size: 2.25rem;
    --h2-font-size: 1.5rem;
    --h3-font-size: 1.25rem;
    --normal-font-size: 1rem;
    --small-font-size: 0.875rem;
    --smaller-font-size: 0.813rem;
  }
}

/* ==== GLOBAL CSS ==== */

body {
  background-color: var(--off-white);
  margin: var(--header-height) 0 0 0;
  font-family: var(--body-font);
  font-size: var(--normal-font-size);
  font-weight: var(--font-medium);
  color: var(--blue);
  line-height: 1.6;
}

h1,
h2,
h3,
ul,
p {
  margin: 0;
}

h2,
h3 {
  font-weight: var(--font-semi-bold);
}

ul {
  padding: 0;
  list-style: none;
}

a {
  text-decoration: none;
  color: var(--blue);
}

img {
  max-width: 100%;
  height: auto;
  display: block;
}
/* ==== CLASS CSS ==== */

.section {
  padding: 4rem 0 2rem;
}

.section-title,
.section-subtitle {
  text-align: center;
}

.section-title {
  font-size: var(--h1-font-size);
  color: var(--first-color);
  margin-bottom: var(--mb-3);
}

.section-subtitle {
  display: block;
  font-size: var(--smaller-font-size);
  font-weight: var(--font-semi-bold);
}

.button {
  border-radius: 3rem;
  padding: 1rem 2rem;
  cursor: pointer;
}

/* ==== LAYOUT ==== */

.bd-container {
  max-width: auto;
  width: calc(100% - 2rem);
  margin-left: var(--mb-2);
  margin-right: var(--mb-2);
}

.bd-grid {
  display: grid;
  gap: 1.5rem;
}

.l-header {
  width: 100%;
  position: fixed;
  top: 0;
  left: 0;
  z-index: var(--z-top);
  background-color: var(--white);
  box-shadow: 0 0.3rem 0.3rem 0 rgba(0, 0, 0, 0.1);
}
</style>
