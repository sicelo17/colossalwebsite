<template>
  <header class="l-header" id="header">
    <nav class="nav bd-container" id="navbar">
      <nav class="nav bd-container" id="navbar">
        <router-link to="/" class="nav_logo">
          <img class="nav__img" src="../assets/COLOSSAL-02.jpeg" alt="" />
        </router-link>

        <div class="nav_menu" id="nav-menu">
          <div class="navLinks" v-for="link in links" :key="link">
            <router-link :to="link.route" class="nav__item">{{
              link.name
            }}</router-link>
          </div>
        </div>

        <div class="nav_menu">
          <div v-if="$store.state.isAuthenticated" class="nav_buttons">
            <button @click="logout()" class="trial-button">LogOut</button>
          </div>
          <div
            v-else
            class="nav_buttons"
            v-for="button in buttons"
            :key="button"
          >
            <router-link :to="button.route" class="button">
              <button :class="button.class">
                {{ button.name }}
              </button>
            </router-link>
          </div>
        </div>
      </nav>

      <div class="nav_toggle" id="nav-toggle">
        <button class="nav_button" id="nav-button" @click="toggleMenu">
          <i class="bx bx-menu-alt-right"></i>
        </button>
      </div>
    </nav>
  </header>
</template>

<script>
import axios from "axios";
export default {
  name: "Header",
  data() {
    return {
      links: [
        { name: "Home", route: "/" },
        { name: "Services", route: "/services" },
        { name: "Industries", route: "/industries" },
        { name: "Products", route: "/products" },
      ],
      buttons: [
        { name: "Free Trial", route: "/trial", class: "trial-button" },
        { name: "Sign In", route: "/login", class: "log-button" },
      ],
    };
  },
  methods: {
    toggleMenu() {
      const menuBox = document.getElementById("nav-menu");
      // if is menuBox displayed, hide it
      if (menuBox.style.right === "0.5rem") {
        menuBox.style.right = "-100%";
      }
      // if is menuBox hidden, display it
      else {
        menuBox.style.right = "0.5rem";
      }
    },
    logout() {
            axios.defaults.headers.common["Authorization"] = ""
            localStorage.removeItem("token")
            localStorage.removeItem("username")
            localStorage.removeItem("userid")
            this.$store.commit('removeToken')
            this.$router.push('/')
        },
  },
};
</script>

<style scoped>
.router-link-active {
  background: var(--off-white);
  padding: 0.5rem;
  border-radius: 0.5rem;
  font-weight: var(--font-bold);
}

.bx {
  font-size: 2rem;
}

.nav_logo {
  background: inherit;
}
.nav__img {
  height: 4rem;
  object-fit: contain;
}
.nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 4.1rem;
  font-weight: var(--font-semi-bold);
  font-style: italic;
  font-size: var(--h2-font-size);
}

.nav_toggle {
  display: none;
}

.nav_menu {
  display: flex;
}

.nav__item:hover {
  color: var(--turquoise);
  transition: 0.2s ease-in all;
}

.nav__item {
  margin-right: var(--mb-2);
}

.nav_buttons:not(:last-child) {
  margin-right: 1.5rem;
}

button {
  padding: 0.5rem 2rem;
  font-family: var(--body-font);
  font-style: italic;
  color: var(--blue);
  border: 1.5px solid var(--blue);
  border-radius: 0.3rem;
  font-size: var(--normal-font-size);
  font-weight: var(--font-semi-bold);
  cursor: pointer;
}

.button {
  padding: 0;
  background: inherit;
}

.trial-button {
  background-color: var(--turquoise);
}

.log-button {
  background-color: var(--white);
}

.trial-button:hover {
  background: linear-gradient(to bottom right, var(--blue), var(--turquoise));
  color: var(--white);
  transition: 0.2s ease-in all;
}

.log-button:hover {
  background: linear-gradient(to bottom left, var(--off-white), var(--blue));
  color: var(--white);
  transition: 0.2s ease-in all;
}

@media screen and (max-width: 768px) {
  .nav_menu {
    position: fixed;
    top: 8%;
    right: -100%;
    width: 95%;
    padding-top: 1rem;
    text-align: center;
    background-color: var(--off-white);
    transition: 0.4s;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    border-radius: 0 0 1rem 1rem;
    display: flex;
    flex-direction: column;
  }

  .nav__item {
    padding: 2rem;
  }

  .navLinks {
    display: flex;
    flex-direction: column;
  }

  .nav_toggle {
    display: block;
    border: none;
  }

  .nav_buttons {
    display: none;
  }

  .nav_button {
    border: none;
    background: inherit;
    font-size: 2rem;
    padding: 0;
  }
}
</style>>
