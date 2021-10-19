<template>
  <div class="bd-container">
    <div class="news">
      <h1>Latest News</h1>

      <div class="cards">
        <div class="card" v-for="blog in blogs" :key="blog">
          <img :src="blog.image" />

          <div class="card-data">
            <h3>{{ blog.title }}</h3>
            <h5>{{ blog.subtitle }}</h5>
            <p>{{ blog.summary }}</p>
          </div>

          <a href="#">Read More</a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      blogs: [
        {
          image: require("../assets/logo.png"),
          title: "ERPs in business",
          subtitle: "Impact of ERPs in Zim business",
          summary:
            "ERPs are fast becoming a fan-favorite in Zimbabwe as people are realising how they increase efficiency in the workplace",
        },
        {
          image: require("../assets/logo.png"),
          title: "ERPs in business",
          subtitle: "Impact of ERPs in Zim business",
          summary:
            "ERPs are fast becoming a fan-favorite in Zimbabwe as people are realising how they increase efficiency in the workplace",
        },
        {
          image: require("../assets/logo.png"),
          title: "ERPs in business",
          subtitle: "Impact of ERPs in Zim business",
          summary:
            "ERPs are fast becoming a fan-favorite in Zimbabwe as people are realising how they increase efficiency in the workplace",
        },
      ],
    };
  },
};
</script>

<style scoped>
h1 {
  text-align: center;
  font-size: 3rem;
  font-style: italic;
  padding: 2rem;
}

a {
  float: right;
  font-weight: var(--font-bold);
}
.cards {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-gap: 2rem;
  margin-bottom: 2rem;
  font-family: var(--font-2);
}

.card {
  background-color: var(--white);
  border-radius: 0.5rem;
  overflow: hidden;
  box-shadow: 0 4px 6px rgba(174, 190, 205, 0.3);
  padding: 2rem;
}

.card:hover {
  transform: scale(1.04);
}

/* ===== RESPONSIVE DESIGN ===== */

@media only screen and (max-width: 800px) {
  .cards {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media only screen and (max-width: 500px) {
  .cards {
    grid-template-columns: 1fr;
  }
}
</style>