<template>
  <section class="section">
    <div class="bd-container">
      <div class="product-heading">
        <h1>Some of our products</h1>
      </div>
      <div class="products-page bd-grid">
         <div class="product" v-for="product in products"
        :key="product.id"
        :product="product">
            <router-link :to="product.get_absolute_url">
              <span class="app2"><i :class=product.icon></i></span>
              <p>{{product.name}}</p>
            </router-link>
          </div>
      </div>
    </div>
  </section>
</template>

<script>
import axios from 'axios'
export default {
  data(){
    return {
      products: []
    }
  },
  mounted() {
    this.getProducts()
    document.title = "Products | ColossalHub";
  },
  methods: {
    async getProducts() {
      await axios
        .get('/api/v1/products/')
        .then(response => {
          this.products = response.data
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
  background: rgba(185, 207, 236, 0.897);
}
.app2 {
  font-size: 4rem;
  padding: .5rem;
  border-radius: 1rem;
  background: var(--white);
}
.product {
  align-items: center;
  text-align: center;
  padding: 1.5rem;
}
.product:hover {
  transform: scale(1.1);
}
.product-heading {
  font-size: var(--h1-font-size);
  text-align: center;
  font-style: italic;
}

.products-page {
  grid-template-columns: repeat(3, 1fr);
}

/*==== RESPONSIVE DESIGN ==== */

@media only screen and (max-width: 450px) {
  .products-page {
    grid-template-columns: repeat(2, 1fr);
  }
}
</style>