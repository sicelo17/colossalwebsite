<template>
  <div class="partners bd-container">
      <carousel :items-to-show="0.5" :wrapAround= "true">
    <slide v-for="slide in slides" :key="slide">
      <img :src="slide.src">
    </slide>

    <template #addons>
      <navigation />
      <pagination />
    </template>
  </carousel>
  </div>
</template>

<script>
import 'vue3-carousel/dist/carousel.css';
import { Carousel, Slide, Pagination, Navigation } from 'vue3-carousel';

export default {
  name: 'App',
  data(){
    return{
      slides: [
        {
          src: require("../assets/financial-paradise.jpeg"),
        }
      ],
    }
  },
  components: {
    Carousel,
    Slide,
    Pagination,
    Navigation,
  },
};
</script>

<style scoped>
.partners {
  margin: 2rem 4rem;
}

</style>