<template>
  <section class="services">
    <h1 class="bd-container section-title service_title">
      Software suitable for every business
    </h1>

    <div v-if="!mobile" class="categories">
      <div class="filter">
        <label
          ><input type="radio" v-model="selectedCategory" value="Sales" /><span
            >Sales</span
          ></label
        >
        <label
          ><input
            type="radio"
            v-model="selectedCategory"
            value="Manufacturing"
          />
          <span>Manufacturing</span></label
        >
        <label
          ><input type="radio" v-model="selectedCategory" value="Accounting" />
          <span>Accounting</span></label
        >
        <label
          ><input type="radio" v-model="selectedCategory" value="eLearning" />
          <span>e-Learning</span></label
        >
        <label
          ><input type="radio" v-model="selectedCategory" value="Websites" />
          <span>Websites</span></label
        >
        <label
          ><input type="radio" v-model="selectedCategory" value="Marketing" />
          <span>Marketing</span></label
        >
      </div>

      <ul class="categories-list">
        <li v-for="category in filteredCategories" :key="category">
          <div class="category_list">
            <div class="category-left">
              <img :src="category.src" />
            </div>
            <div class="category-right">
              <h3>{{ category.description }}</h3>
            </div>
          </div>
        </li>
      </ul>
    </div>

    <div v-else class="categories-mobile bd-grid">
      <div class="categories_mobile">
        <div class="category-heading">
          <h3>Boost your sales</h3>
        </div>
        <div class="apps">
          <div class="app">
            <router-link to="/sales">
              <span class="app1"><i class="bx bx-trending-up"></i></span>
              <p>Sales</p>
            </router-link>
          </div>
          <div class="app">
            <router-link to="/crm">
              <span class="app2"><i class="bx bx-support"></i></span>
              <p>CRM</p>
            </router-link>
          </div>
          <div class="app">
            <router-link to="/point-of-sale">
              <span class="app3"><i class="bx bxs-bank"></i></span>
              <p>POS</p>
            </router-link>
          </div>
        </div>
      </div>
      <div class="categories_mobile">
        <div class="category-heading">
          <h3>Have Your Services Integrated</h3>
        </div>
        <div class="apps">
          <div class="app">
            <router-link to="/timesheet">
              <span class="app1"><i class="bx bxs-time-five"></i></span>
              <p>Timesheet</p>
            </router-link>
          </div>
          <div class="app">
            <router-link to="/project">
              <span class="app2"><i class="bx bx-clipboard"></i></span>
              <p>Project</p>
            </router-link>
          </div>
          <div class="app">
            <router-link to="/helpdesk">
              <span class="app3"><i class="bx bx-desktop"></i></span>
              <p>Helpdesk</p>
            </router-link>
          </div>
        </div>
      </div>
      <div class="categories_mobile">
        <div class="category-heading">
          <h3>Manage Your Finances</h3>
        </div>
        <div class="apps">
          <div class="app">
            <router-link to="/timesheet">
              <span class="app1"><i class="bx bx-money"></i></span>
              <p>Invoicing</p>
            </router-link>
          </div>
          <div class="app">
            <router-link to="/accounting">
              <span class="app2"><i class="bx bxs-coin-stack"></i></span>
              <p>Accounting</p>
            </router-link>
          </div>
        </div>
      </div>

      <div class="categories_mobile">
        <router-link to="/services">
          <button class="button">More Apps</button>
        </router-link>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: "Services",
  data() {
    return {
      categories: [
        {
          category: "Sales",
          src: require("../assets/sales.jpg"),
          description:
            "Send clear and complete quotations to your prospects. Add product descriptions, beautiful images, and additional information simply by dragging and dropping building blocks.",
        },
        {
          category: "Manufacturing",
          src: require("../assets/manufacturing.jpg"),
          description:
            "Use make-to-order rules, minimum stock rules or the master production schedule to automate procurements. ",
        },
        {
          category: "Accounting",
          src: require("../assets/accounting.jpeg"),
          description:
            "Send reminders to your debtors in just a few clicks. Automatically create invoices from sales orders, delivery orders or base them on time and material.",
        },
        {
          category: "eLearning",
          src: require("../assets/eLearning.jpeg"),
          description:
            "Meaningful learning experiences lead to increased attention and focus, higher levels of critical thinking and more productivity!",
        },
        {
          category: "Websites",
          src: require("../assets/website.jpeg"),
          description:
            "Having your business online is one of the requirements of the fourth industrial revolution as this will broaden your target market.",
        },
        {
          category: "Marketing",
          src: require("../assets/marketing2.jpeg"),
          description:
            "Being present on Social Media increases awareness, connects you with your customers, boosts leads, and income. ",
        },
      ],
      selectedCategory: "Sales",
      mobile: null,
    };
  },
  created() {
    this.checkScreen();
    window.addEventListener("resize", this.checkScreen);
  },
  methods: {
    checkScreen() {
      const windowWidth = window.innerWidth;
      if (windowWidth <= 800) {
        this.mobile = true;
        return;
      }
      this.mobile = false;
    },
  },
  computed: {
    filteredCategories: function () {
      var category = this.selectedCategory;

      return this.categories.filter(function (cate) {
        return cate.category === category;
      });
    },
  },
};
</script>

<style scoped>
.services {
  line-height: 1.2;
}

.service_title {
  font-size: 3rem;
}

label {
  display: inline-block;
  line-height: 1.5em;
  font-size: 2rem;
  cursor: pointer;
}
label:not(:last-child) {
  margin-right: 4rem;
}

ul {
  margin-left: 0;
  padding-left: 0;
  list-style: none;
}

li {
  padding: 8px 16px;
  border-bottom: 1px solid #eee;
}

input[type="radio"] {
  -webkit-appearance: none;
  -moz-appearance: none;
  -ms-appearance: none;
  -o-appearance: none;
  appearance: none;
}
img {
  border-radius: 3rem;
}

h2 {
  font-size: var(--h1-font-size);
}

.filter input[type="radio"]:checked ~ * {
  border-bottom: solid 4px var(--turquoise);
  transition: 0.3s ease all;
}

.filter {
  background: white;
  padding: 0.875rem;
}

.category_list {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  grid-gap: 3rem;
  padding: 3rem;
}

.category-right {
  padding: 2rem;
  font-size: var(--h3-font-size);
}

.categories-mobile {
  grid-template-columns: 1fr;
  text-align: center;
  margin: 2rem 0;
}

.category-heading {
  font-size: var(--h2-font-size);
  margin: 0 0 1.5rem 0;
}

.apps {
  display: flex;
  align-items: center;
  justify-content: center;
}

.app:not(:last-child) {
  margin-right: var(--h3-font-size);
}

.app {
  background: var(--white);
}
.app p {
  font-size: var(--h3-font-size);
  font-weight: var(--font-bold);
  padding-bottom: 1.4rem;
}
.bx {
  font-size: var(--biggest-font-size);
  padding: 2rem;
}

.button {
  border: 2px solid var(--blue);
  color: var(--blue);
  font-family: var(--body-font);
  font-size: var(--h1-font-size);
  font-style: italic;
}
</style>