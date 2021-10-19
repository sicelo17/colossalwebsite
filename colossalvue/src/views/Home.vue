<template>
  <div>
    <Hero />
    <Services />
    <Contact />
    <Partners />
  </div>
</template>

<script>
import Hero from "../components/Hero.vue"
import Services from "../components/Services.vue"
import Partners from "../components/Partners.vue"
import Contact from "../components/Contact.vue"

export default {
  name: 'Home',
  components: {
  Hero,
  Services,
  Partners,
  Contact,
  },
  mounted() {
    document.title = "Home | ColossalHub";
  },
}
</script>
