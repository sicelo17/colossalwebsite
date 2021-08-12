<template>
  <div id="nav">
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link>
  </div>
  <router-view/>
</template>

<style>
/* ==== GOOGLE FONTS ==== */
@import url("https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,500;0,700;1,400;1,500;1,600;1,700&family=Poppins:wght@400;500;600&display=swap");

/* ==== VARIABLES CSS ==== */

:root {
  --header-height: 3rem;

  /* ==== COLORS ==== */
  --off-white: #efefef;
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
</style>
