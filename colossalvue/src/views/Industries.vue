<template>
  <section class="section">
    <div class="industries-page">
      <div class="bd-container">
        <div class="industry-title">
          <h1>We serve the following industries</h1>
        </div>
        <div class="industry-items bd-grid">
          <div class="ind" v-for="product in latestProducts"
        :key="product.id"
        :product="product">
            <router-link :to="product.get_absolute_url">
              <span><i :class=product.icon></i></span>
              <p>{{product.name}}</p>
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
      latestProducts: []
    }
  },
  mounted() {
    this.getLatestProducts()
    document.title = "Industries | ColossalHub";
  },
  methods: {
    async getLatestProducts() {
      await axios
        .get('/api/v1/latest-products/')
        .then(response => {
          this.latestProducts = response.data
          console.log(response.data)
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