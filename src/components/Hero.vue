<template>
<section class="section">
      <div class="hero-section">
      <div class="bd-container">
      <agile :dots="false" :autoplay="true" :infinite="true" :autoplay-speed="8000" :speed="2500" :navButtons="false" fade :pauseOnHover="false" >
    <div class="slide">
     <div class="hero-1">
         <router-link to="/trial">
         <button class="button">
             Try for free
         </button>
         </router-link>
     </div>
    </div>

    <div class="slide">
      <div class="hero-2">
           <router-link to="/trial">
         <button class="button">
             Try for free
         </button>
         </router-link>
      </div>
    </div>
  </agile>
  </div>
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
	width: 100%;
}

.hero-section {
    height: 100vh;
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

.hero-1 {
    background-image: url("https://media.gettyimages.com/photos/mmmi-wonder-picture-id1047502598?k=6&m=1047502598&s=612x612&w=0&h=8JgvyNDhw7wD0E5FyI8rN2tYnWhvcKxE3v49jAYRbB8=");
    background-repeat: no-repeat;
    background-size: cover;
    width: 100%;
    height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}

.hero-2 {
    background-image: url("../assets/business-2.jpeg");
    background-repeat: no-repeat;
    background-size: cover;
    width: 100%;
    height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}

</style>