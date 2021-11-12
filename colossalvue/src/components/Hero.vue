<template>
  <section class="section">

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
              <h2>Struggling to boost your sales because you have to spend a lot of time and money doing repetitive tasks that can be easily automated? Try one of our systems and notice the difference in both time and your wallet.</h2>
            </div>
            <router-link to="/trial">
              <button class="button">Try for free</button>
            </router-link>
          </div>

          <div class="hero__right">
            <img class="hero__img" src="../assets/img/home2.svg" alt="">
          </div>
          </div>
        </div>

        <div class="slide">
          <div class="hero">
            <div class="hero__left">
            <div class="hero__text bd-container">
              <h2>Have you been looking for a way to modernise your business to remain competitive? Let technology handle the stressful things while you relax and focus on being more productive.</h2>
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


/*.agile button {
  background: transparent;
  border: 1px solid #fff;
  cursor: pointer;
  display: block;
  height: 10px;
  font-size: 0;
  line-height: 0;
  margin: 0;
  padding: 0;
  transition-duration: 0.3s;
  width: 10px;
}

.agile button:hover {
    background-color: var(--white);
}
*/


.slide {
  height: 90vh;
  width: 100vw;
}

.hero-section {
  height: 90vh;
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
   flex: .6;
   text-align: center;
 }

 .hero__right {
   flex: .4;
 }

 .hero__text {
   line-height: 1.6rem;
 }


/* ===== RESPONSIVE DESIGN ===== */

@media only screen and (max-width:900px){
  .hero__text {
    grid-template-columns: 1fr;
    padding-bottom: 2rem;
    text-align: center;
  }
}

@media only screen and (max-width: 400px) {

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