<template>
  <div class="partners bd-container">
    <div class="partners__title">
      <h2>Our trusted Partners</h2>
    </div>
    <carousel :items-to-show="2" :wrapAround="true">
      <slide v-for="slide in slides" :key="slide">
        <img :src="slide.src" />
      </slide>

      <template #addons>
        <navigation />
      </template>
    </carousel>
  </div>
</template>

<script>
import "vue3-carousel/dist/carousel.css";
import { Carousel, Slide, Navigation } from "vue3-carousel";

export default {
  name: "App",
  data() {
    return {
      slides: [
        {
          src: require("../assets/financial-paradise.jpeg"),
        },
        {
          src: require("../assets/website.jpeg"),
        },
        {
          src: require("../assets/sales.jpg"),
        },
      ],
    };
  },
  components: {
    Carousel,
    Slide,
    Navigation,
  },
};
</script>

<style scoped>
.partners {
  width: 95vw;
  margin: 2rem 1rem;
}

img {
  height: 100px;
  width: 200px;
  object-fit: contain;
}

.partners__title {
  text-align: center;
  padding:0 1.2rem 1.2rem 1.2rem;
}

.partners__title h2 {
   font-weight: var(--font-semi-bold);
   font-size: var(--h2-font-size);
}

@media only screen and (max-width: 400px) {
  img {
    width: 150px;
  }
}
</style>