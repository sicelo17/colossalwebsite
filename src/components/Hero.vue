<template>
<section class="section">
      <div class="hero-section">
      <div class="bd-container">
      <agile :dots="true" :autoplay="true" :infinite="true" :autoplay-speed="8000" :speed="2500" :navButtons="false" fade :pauseOnHover="false" >
    <div class="slide">
     <div class="hero-1">
         evsdfcevf
     </div>
    </div>

    <div class="slide">
      <div class="hero-2">
gfdsvf
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

<style>
.agile__dots {
  bottom: 10px;
  flex-direction: column;
  right: 30px;
  position: absolute;
}

.agile__dot {
  margin: 5px 0;
}

.agile button {
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

img {
    object-fit: cover;
}

.slide {
    display: block;
	height: 500px;
	object-fit: cover;
	width: 100%;
}

.hero-1 {
    background-image: url("../assets/business.jpeg");
    background-repeat: no-repeat;
    background-size: cover;
    width: 100%;
    height: 100vh;
}

.hero-2 {
    background-image: url("../assets/logo.png");
    width: 100%;
    height: 100vh;
}

</style>