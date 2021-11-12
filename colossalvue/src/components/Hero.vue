<template>
  <section>

      <div class="hero-section">
      <agile
        :dots="false"
        :autoplay="true"
        :infinite="true"
        :autoplay-speed="8000"
        :speed="2500"
        :navButtons="false"
        fade
        :pauseOnHover="false"
      >
        <div class="slide">
          <div class="hero">
            <div class="hero__left">
            <div class="hero__text bd-container">
              <h2>Boost your sales</h2>
              <p>Struggling to boost your sales because you have to spend a lot of time and money doing repetitive tasks that can be easily automated? Try one of our systems and notice the difference in both time and your wallet.</p>
            </div>
            <router-link to="/trial">
              <button class="button">Try for free</button>
            </router-link>
          </div>

          <div class="hero__right">
            <img class="hero__img" src="../assets/img/home4.svg" alt="">
          </div>
          </div>
        </div>

        <div class="slide">
          <div class="hero">
            <div class="hero__left">
            <div class="hero__text bd-container">
              <h2>Move with the times</h2>
              <p>Have you been looking for a way to modernise your business to remain competitive? Let technology handle the stressful things while you relax and focus on being more productive.</p>
            </div>
            <router-link to="/trial">
              <button class="button">Request Demo</button>
            </router-link>
          </div>
          <div class="hero__right">
            <img class="hero__img" src="../assets/img/home1.svg" alt="">
          </div>
          </div>
        </div>
      </agile>
    </div>
  </section>
</template>

<script>
import { VueAgile } from "vue-agile";
export default {
  components: {
    agile: VueAgile,
  },
};
</script>

<style scoped>
.hero-section {
  height: 85vh;
}
.button {
  background-color: var(--blue);
  color: var(--white);
  padding: 1.2rem 2.5rem;
  font-size: var(--h3-font-size);
  font-family: var(--body-font);
  font-style: italic;
  font-weight: var(--font-bold);
  border: none;
  margin-top: 2rem;
}

.button:hover {
  background: linear-gradient(to bottom right, var(--blue), var(--turquoise));
  color: var(--white);
  transition: 0.2s ease-in all;
}

.hero {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 80vh;
  width: 100vw;
}
 .hero__left {
   flex: .5;
   text-align: center;
 }

 .hero__right {
   flex: .5;
   display: flex;
   align-items: center;
   justify-content: center;
 }

 .hero__text {
   line-height: 1.6rem;
 }

 .hero__text > h2 {
   font-size: 2.5rem;
   margin-bottom: 1rem;
 }

.hero__text > p {
  font-size: 1.3rem;
}

/* ===== RESPONSIVE DESIGN ===== */



@media only screen and (max-width: 600px) {

.hero-section {
    background: var(--blue);
    height: 90vh;
  }
  .hero__right {
    display: none;
  }
  .hero__left {
    flex: 1;
    background: var(--blue);
    color: var(--white);
  }

  .button {
    border: var(--white) 2px solid;
  }
}
</style>