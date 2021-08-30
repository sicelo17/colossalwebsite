<template>
  <header class="l-header" id="header">
    <nav class="nav bd-container" id="navbar">
      <a href="#" class="nav_logo">ColossalHub</a>

      <div class="nav_menu" id="nav-menu">
        <ul class="nav_list">
          <router-link class="nav_item" to="/">Home</router-link>
          <router-link class="nav_item" to="/services">Services</router-link>
          <router-link class="nav_item" to="/industries">Industries</router-link>
          <router-link class="nav_item" to="/products">Products</router-link>
        </ul>
      </div>

      <div class="nav_buttons" id="nav-buttons">
        <router-link to="/trial" class="button_link"
          ><button class="trial-button">Free Trial</button></router-link
        >
        <router-link to="/login" class="button_link"
          ><button class="log-button">Sign In</button></router-link
        >
      </div>

      <div class="nav_toggle" id="nav-toggle">
        <button class="nav_button" id="nav-button" @click="toggleMenu">
          <i class="bx bx-menu-alt-right"></i>
        </button>
      </div>
    </nav>
  </header>
</template>

<script>
export default {
    name: "Header",
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
  },
};
</script>

<style scoped>
.router-link-active {
    background: var(--off-white);
    padding: .5rem;
    border-radius: .5rem;
    font-weight: var(--font-bold);
}
.nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 4rem;
  font-weight: var(--font-semi-bold);
  font-style: italic;
  font-size: var(--h2-font-size);
}

.nav_toggle {
  display: none;
}

.nav_item:hover {
  color: var(--turquoise);
  transition: 0.2s ease-in all;
}

.nav_item:not(:last-child) {
  margin-right: var(--mb-2);
}

.button_link:not(:last-child) {
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
  }

  .nav_item {
      padding: 2rem;
  }

  .nav_list {
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
