<template>
  <header class="l-header" id="header">
    <nav class="nav bd-container" id="navbar">
      <a href="#" class="nav_logo">ColossalHub</a>

      <div class="nav_menu" id="nav-menu">
        <ul class="nav_list">
          <router-link class="nav_item" to="/">Home</router-link>
          <router-link class="nav_item" to="/">Services</router-link>
          <router-link class="nav_item" to="/">Industries</router-link>
          <router-link class="nav_item" to="/">Products</router-link>
        </ul>
      </div>

      <div class="nav_buttons" id="nav-buttons">
        <router-link to="/trial" class="button_link"
          ><button class="trial-button">Free Trial</button></router-link
        >
        <router-link to="/signIn" class="button_link"
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