<template>
  <section class="section">
    <div class="industries-page bd-grid">
      <div class="bd-container">
        <div class="industry-items">
          <div class="industry">
            <div class="ind">
              <router-link to="/fashion">
                <span><i class="bx bxs-t-shirt"></i></span>
                <p>Fashion</p>
              </router-link>
            </div>

            <div class="ind">
              <router-link to="/manufacturing">
                <span><i class="bx bxs-factory"></i></span>
                <p>Manufacturing</p>
              </router-link>
            </div>

            <div class="ind">
              <router-link to="/retail">
                <span><i class="bx bxl-shopify"></i></span>
                <p>Retail</p>
              </router-link>
            </div>
          </div>

          <div class="industry">
            <div class="ind">
              <router-link to="/consulting">
                <span><i class="bx bxs-group"></i></span>
                <p>Consulting</p>
              </router-link>
            </div>

            <div class="ind">
              <router-link to="/education">
                <span><i class="bx bxs-graduation"></i></span>
                <p>Education</p>
              </router-link>
            </div>

            <div class="ind">
              <router-link to="/foodbeverage">
                <span><i class="bx bxs-coffee-alt"></i></span>
                <p>Food & Beverage</p>
              </router-link>
            </div>
          </div>

          <div class="industry">
            <div class="ind">
              <router-link to="/restaurants">
                <span><i class="bx bx-restaurant"></i></span>
                <p>Restaurants</p>
              </router-link>
            </div>

            <div class="ind">
              <router-link to="/it-services">
                <span><i class="bx bxl-visual-studio"></i></span>
                <p>IT Services</p>
              </router-link>
            </div>

            <div class="ind">
              <router-link to="/realestate">
                <span><i class="bx bxs-home"></i></span>
                <p>Real Estate</p>
              </router-link>
            </div>
          </div>

          <div class="industry">
            <div class="ind">
              <router-link to="/professionalservices">
                <span><i class="bx bxs-user-check"></i></span>
                <p>Professional Services</p>
              </router-link>
            </div>

            <div class="ind">
              <router-link to="/transportation">
                <span><i class="bx bxs-truck"></i></span>
                <p>Transportation & Logistics</p>
              </router-link>
            </div>

            <div class="ind">
              <router-link to="/wholesale">
                <span><i class="bx bxs-building-house"></i></span>
                <p>Wholesale & Distribution</p>
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  mounted() {
    document.title = "Industries | ColossalHub";
  },
};
</script>

<style scoped>

span {
  font-size: 4rem;
}

.industry-items {
  grid-template-columns: 1fr;
  text-align: center;
  margin: 2rem 0;
}

.industry {
  display: flex;
  align-items: center;
  justify-content: center;
}

.ind:not(:last-child) {
  margin-right: 8rem;
}
</style>