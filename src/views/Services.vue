<template>
  <section class="section">
    <div class="service-page">
      <div class="bd-container">
        <div class="service-title">
          <h1>Our Services</h1>
        </div>
        <div class="services">
          <div class="service_info">
            <div class="heading">
              <h2>Sales</h2>
            </div>
            <div
              v-for="service in service_1"
              :key="service"
              class="service_link"
            >
              <router-link :to="service.route">
                {{ service.name }}
              </router-link>
            </div>
          </div>

          <div class="service_info">
            <div class="heading">
              <h2>Finance</h2>
            </div>

            <div
              v-for="service in service_2"
              :key="service"
              class="service_link"
            >
              <router-link :to="service.route">
                {{ service.name }}
              </router-link>
            </div>
          </div>

          <div class="service_info">
            <div class="heading">
              <h2>Operations</h2>
            </div>

            <div
              v-for="service in service_3"
              :key="service"
              class="service_link"
            >
              <router-link :to="service.route">
                {{ service.name }}
              </router-link>
            </div>
          </div>

          <div class="service_info">
            <div class="heading">
              <h2>Manufacturing</h2>
            </div>

            <div
              v-for="service in service_4"
              :key="service"
              class="service_link"
            >
              <router-link :to="service.route">
                {{ service.name }}
              </router-link>
            </div>
          </div>

          <div class="service_info">
            <div class="heading">
              <h2>Human Resources</h2>
            </div>

            <div
              v-for="service in service_5"
              :key="service"
              class="service_link"
            >
              <router-link :to="service.route">
                {{ service.name }}
              </router-link>
            </div>
          </div>

          <div class="service_info">
            <div class="heading">
              <h2>Communication</h2>
            </div>

            <div
              v-for="service in service_6"
              :key="service"
              class="service_link"
            >
              <router-link :to="service.route">
                {{ service.name }}
              </router-link>
            </div>
          </div>

          <div class="service_info">
            <div class="heading">
              <h2>Marketing</h2>
            </div>
            <div
              v-for="service in service_7"
              :key="service"
              class="service_link"
            >
              <router-link :to="service.route">
                {{ service.name }}
              </router-link>
            </div>
          </div>

          <div class="service_info">
            <div class="heading">
              <h2>Website</h2>
            </div>

            <div
              v-for="service in service_8"
              :key="service"
              class="service_link"
            >
              <router-link :to="service.route">
                {{ service.name }}
              </router-link>
            </div>
          </div>

          <div class="service_info">
            <div class="heading">
              <h2>Analytics</h2>
            </div>

            <div
              v-for="service in service_9"
              :key="service"
              class="service_link"
            >
              <router-link :to="service.route">
                {{ service.name }}
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
  data() {
    return {
      service_1: [
        { name: "CRM", route: "/" },
        { name: "Sales", route: "/" },
        { name: "Point of Sale", route: "/" },
        { name: "Subscriptions", route: "/" },
        { name: "Rental", route: "/" },
      ],
      service_2: [
        { name: "Accounting", route: "/" },
        { name: "Invoicing", route: "/" },
        { name: "Expenses", route: "/" },
        { name: "Spreadsheet", route: "/" },
        { name: "Documents", route: "/" },
      ],
      service_3: [
        { name: "Inventory", route: "/" },
        { name: "Project", route: "/" },
        { name: "Purchase", route: "/" },
        { name: "Timesheets", route: "/" },
        { name: "Helpdesk", route: "/" },
        { name: "Field Service", route: "/" },
      ],
      service_4: [
        { name: "MRP", route: "/" },
        { name: "PLM", route: "/" },
        { name: "MRP Maintenance", route: "/" },
        { name: "Quality", route: "/" },
      ],
      service_5: [
        { name: "Recruitment", route: "/" },
        { name: "Employees", route: "/" },
        { name: "Fleet", route: "/" },
        { name: "Time-Off", route: "/" },
        { name: "Appraisals", route: "/" },
        { name: "Referral", route: "/" },
        { name: "Approvals", route: "/" },
      ],
      service_6: [
        { name: "Discuss", route: "/" },
        { name: "eSignature", route: "/" },
        { name: "Survey", route: "/" },
      ],
      service_7: [
        { name: "Automation", route: "/" },
        { name: "Email", route: "/" },
        { name: "SMS", route: "/" },
        { name: "Social", route: "/" },
      ],
      service_8: [
        { name: "Website Builder", route: "/" },
        { name: "eCommerce", route: "/" },
        { name: "Blogs", route: "/" },
        { name: "Forum", route: "/" },
        { name: "eLearning", route: "/" },
        { name: "Events", route: "/" },
        { name: "Live Chat", route: "/" },
        { name: "Appointments", route: "/" },
      ],
      service_9: [
        { name: "People Analytics", route: "/" },
        { name: "Customer Experience Analytics", route: "/" },
        { name: "Customer Segmentation", route: "/" },
        { name: "Customer Churn Prediction", route: "/" },
        { name: "Machine Failure Analytics", route: "/" },
        { name: "Marketing Analytics", route: "/" },
        { name: "Inventory Analytics", route: "/" },
        { name: "Sales Analytics", route: "/" },
      ],
    };
  },
  mounted() {
    document.title = "Services | ColossalHub";
  },
};
</script>

<style scoped>
.section {
  background: linear-gradient(
    to top left,
    rgba(161, 191, 231, 0.897),
    var(--turquoise)
  );
}
.services {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
}

.service_info {
  margin: 2rem 4rem;
}

.heading {
  font-size: var(--h3-font-size);
}

.service_link {
  font-size: var(--normal-font-size);
  margin-bottom: 0.5rem;
}

.service_link:hover {
  transform: scale(1.1);
  font-weight: var(--font-bold);
}

.service-title {
  text-align: center;
  font-size: var(--h1-font-size);
  font-style: italic;
}

/* ==== RESPONSIVE DESIGN ==== */

@media only screen and (max-width: 840px) {
  .services {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media only screen and (max-width: 510px) {
  .services {
    grid-template-columns: 1fr;
    place-items: center;
  }
}
</style>