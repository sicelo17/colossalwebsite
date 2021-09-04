<template>
  <section class="section">
      <div class="bd-container">
        <div class="product-heading">
          <h2>Some of our products</h2>
        </div>
        <div class="products-page bd-grid">
        <div class="products">
          <div class="product">
            <router-link to="/crm">
              <span class="app2"><i class="bx bx-support"></i></span>
              <p>CRM</p>
            </router-link>
          </div>

          <div class="product">
            <router-link to="/erp">
              <span class="app2"><i class='bx bx-cog'></i></span>
              <p>ERP</p>
            </router-link>
          </div>

          <div class="product">
            <router-link to="/human-management">
              <span class="app2"><i class='bx bxs-user-circle'></i></span>
              <p>Human Resources</p>
            </router-link>
          </div>
        </div>

        <div class="products">
          <div class="product">
            <router-link to="/sales">
              <span class="app2"><i class="bx bx-trending-up"></i></span>
              <p>Sales</p>
            </router-link>
          </div>

          <div class="product">
            <router-link to="/accounting">
              <span class="app2"><i class="bx bxs-coin-stack"></i></span>
              <p>Accounting</p>
            </router-link>
          </div>

          <div class="product">
            <router-link to="/ecommerce">
              <span class="app2"><i class='bx bxs-shopping-bags'></i></span>
              <p>E-commerce</p>
            </router-link>
          </div>
        </div>

         <div class="products">
          <div class="product">
            <router-link to="/websites">
              <span class="app2"><i class='bx bxl-html5'></i></span>
              <p>Websites</p>
            </router-link>
          </div>

          <div class="product">
            <router-link to="/analytics">
              <span class="app2"><i class='bx bx-line-chart-down'></i></span>
              <p>Analytics</p>
            </router-link>
          </div>

          <div class="product">
            <router-link to="/business-intelligence">
              <span class="app2"><i class='bx bxs-briefcase-alt-2'></i></span>
              <p>Business Intelligence</p>
            </router-link>
          </div>
        </div>
      </div>
      </div>
  </section>
</template>

<script>
export default {
mounted() {
    document.title = "Products | ColossalHub";
  },
}
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

.product-heading {
  font-size: var(--h2-font-size);
  text-align: center;
}
.products {
  display: flex;
  align-items: center;
  justify-content: space-around;
}
</style>