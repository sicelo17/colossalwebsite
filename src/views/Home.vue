<template>
  <div>
    <Hero />
    <Services />
    <News />
  </div>
</template>

<script>
import Hero from "../components/Hero.vue"
import Services from "../components/Services.vue"
import News from "../components/News.vue"

export default {
  name: 'Home',
  components: {
  Hero,
  Services,
  News,
  }
}
</script>
