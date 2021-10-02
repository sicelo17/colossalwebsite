<template>
  <div class="partners bd-container">
    <carousel :items-to-show="3" :wrapAround="true">
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

.carousel__next,
.carousel__prev {
  background-color: var(--blue);
}

</style>