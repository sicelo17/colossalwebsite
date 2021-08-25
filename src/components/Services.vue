<template>
  <section class="services">
    <h1 class="section-title service_title">
      Software suitable for every business
    </h1>

    <div class="bd-container categories">
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
          ><input type="radio" v-model="selectedCategory" value="Finance" />
          <span>Finance</span></label
        >
        <label
          ><input type="radio" v-model="selectedCategory" value="eLearning" />
          <span>E-learning</span></label
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
              <h2>{{ category.description }}</h2>
            </div>
          </div>
        </li>
      </ul>
    </div>

   <div class="bd-container categories-mobile bd-grid">
       <div class="cate">shjvbsjbv</div>
       <div class="cate">shjvbsjbv</div>
       <div class="cate">shjvbsjbv</div>
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
            "Our software will boost sales by making your work easier and increase in employee efficiency ",
        },
        {
          category: "Manufacturing",
          src: require("../assets/manufacturing.jpg"),
          description:
            "Software that helps to generate quotations and invoices at a faster rate and easier",
        },
        {
          category: "Finance",
          src: require("../assets/manufacturing.jpg"),
          description:
            "Software that makes handling all your acoounting needs a lot less stressful making you look forward to the end of the month",
        },
      ],
      selectedCategory: "Sales",
      mobile: null,
    };
  },
  created () {
      this.checkScreen();
      window.addEventListener("resize", this.checkScreen);
  },
  methods : {
      checkScreen () {
          const windowWidth = window.innerWidth;
          if (windowWidth <= 750) {
              this.mobile = true;
              return
          }
          this.mobile = false;
      }
  },
  computed: {
    filteredCategories: function () {
      var category = this.selectedCategory;

      return this.categories.filter(function (person) {
        return person.category === category;
      });
    },
  },
};
</script>

<style scoped>
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
}

.categories-mobile {
    grid-template-columns: repeat(3, 1fr);
}

/* ===== RESPONSIVE DESIGN ===== */


</style>