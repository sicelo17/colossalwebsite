<template>
  <div>
    <Hero />
    <Services />
    <News />
    <Contact />
  </div>
</template>

<script>
import Hero from "../components/Hero.vue"
import Services from "../components/Services.vue"
import News from "../components/News.vue"
import Contact from "../components/Contact.vue"

export default {
  name: 'Home',
  components: {
  Hero,
  Services,
  News,
  Contact,
  }
}
</script>
