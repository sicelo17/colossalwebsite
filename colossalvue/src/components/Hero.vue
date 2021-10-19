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
          <div class="hero-1">
            <div class="hero-text bd-grid bd-container">
              <h2>Struggling to boost your sales because you have to spend a lot of time and money doing repetitive tasks that can be easily automated? Try one of our systems and notice the difference in both time and your wallet.</h2>
            </div>
            <router-link to="/trial">
              <button class="button">Try for free</button>
            </router-link>
          </div>
        </div>

        <div class="slide">
          <div class="hero-2">
            <div class="hero-text bd-grid bd-container">
              <h2>Have you been looking for a way to modernise your business to remain competitive? Let technology handle the stressful things while you relax and focus on being more productive.</h2>
            </div>
            <router-link to="/trial">
              <button class="button">Request Demo</button>
            </router-link>
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
.agile__dots {
  bottom: 10px;
  flex-direction: column;
  right: 30px;
  position: absolute;
}

.agile__dot {
  margin: 5px 0;
}

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

img {
  object-fit: cover;
}

.slide {
  display: block;
  height: 80vh;
  object-fit: cover;
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
}

.button:hover {
  background: linear-gradient(to bottom right, var(--blue), var(--turquoise));
  color: var(--white);
  transition: 0.2s ease-in all;
}

.hero-1,
.hero-2 {
  background-image: url("https://media.gettyimages.com/photos/mmmi-wonder-picture-id1047502598?k=6&m=1047502598&s=612x612&w=0&h=8JgvyNDhw7wD0E5FyI8rN2tYnWhvcKxE3v49jAYRbB8=");
  background-repeat: no-repeat;
  background-size: cover;
  object-fit: contain;
  width: 100%;
  height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.hero-2 {
  background-image: url("https://images.pexels.com/photos/3184465/pexels-photo-3184465.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940");
}

.hero-text {
  grid-template-columns: repeat(2, 1fr);
  line-height: 1.3;
}

/* ===== RESPONSIVE DESIGN ===== */

@media only screen and (max-width:900px){
  .hero-text {
    grid-template-columns: 1fr;
    padding-bottom: 2rem;
    text-align: center;
  }
}

@media only screen and (max-width: 400px) {
  .hero-1,
  .hero-2 {
    background: var(--blue);
    color: var(--white);
  }

  .button {
    border: var(--white) 2px solid;
  }
}
</style>