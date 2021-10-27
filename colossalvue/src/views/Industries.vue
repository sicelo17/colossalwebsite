<template>
  <section class="section">
    <div class="industries-page">
      <div class="bd-container">
        <div class="industry-title">
          <h1>We serve the following industries</h1>
        </div>
        <div class="industry-items bd-grid">
          <div class="ind" v-for="industry in industries"
        :key="industry.id"
        :industry="industry">
            <router-link :to="industry.get_absolute_url">
              <span><i :class=industry.icon></i></span>
              <p>{{industry.name}}</p>
            </router-link>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import axios from 'axios'
export default {
  data(){
    return{
      industries: []
    }
  },
  mounted() {
    this.getIndustries()
    document.title = "Industries | ColossalHub";
  },
  methods: {
    async getIndustries() {
      await axios
        .get('/api/v1/industries/')
        .then(response => {
          this.industries = response.data
        })
        .catch(error => {
          console.log(error)
        })
    }
  }

};
</script>

<style scoped>
.section {
  background: linear-gradient(
    to top left,
    rgba(72, 140, 228, 0.897),
    var(--turquoise)
  );
}

span {
  font-size: 4rem;
  padding: 0.5rem;
  border-radius: 1rem;
  background: var(--white);
}

.industry-items {
  grid-template-columns: repeat(3, 1fr);
  text-align: center;
  margin: 2rem 0;
}

.ind:hover {
  transform: scale(1.1);
}

.industry-title {
  font-size: var(--h1-font-size);
  text-align: center;
  font-style: italic;
}

/* ==== RESPONSIVE DESIGN ==== */

@media only screen and (max-width: 500px) {
  .industry-items {
    grid-template-columns: repeat(2, 1fr);
  }
}
</style>