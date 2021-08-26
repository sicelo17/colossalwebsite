<template>
  <footer>
     <div class="bd-container">
          <div class="footer_links">
         <div class="footer_column">
             <h1>About Us</h1>
             <div class="footer-links">
                <ul class="footer_routes">
                     <router-link class="links" to="/about-us">Our Company</router-link>
                     <router-link class="links" to="/team">Our team</router-link>
                     <router-link class="links" to="/careers">Careers</router-link>
                     <router-link class="links" to="/blogs">Our Blogs</router-link>
                </ul>
             </div>
         </div>

          <div class="footer_column">
             <h1>Partnership</h1>
             <div class="footer-links">
                <ul class="footer_routes">
                     <router-link class="links" to="/signIn">Sign In</router-link>
                     <router-link class="links" to="/">Become a Partner</router-link>
                     <router-link class="links" to="/">Newsletter</router-link>
                     <router-link class="links" to="/">Testimonies</router-link>
                </ul>
             </div>
         </div>

          <div class="footer_column">
             <h1>Contact Us</h1>
             <div class="footer-links">
                <ul class="footer_routes">
                     <router-link class="links" to="/about-us">Our Location</router-link>
                     <router-link class="links" to="/">Our email</router-link>
                     <router-link class="links" to="/map">Site Map</router-link>
                     <router-link class="links" to="/">Social Media</router-link>
                </ul>
             </div>
         </div>
      </div>

      <div class="copyright">
          <p>Copyright &copy; 2021 - ColossalHub</p>
      </div>
     </div>
     <div class="partnership">
          <p>In partnership with Odoo &reg;</p>
      </div>
  </footer>
</template>

<script>
export default {

}
</script>

<style scoped>
footer {
    background: var(--blue);
    color: var(--turquoise);
    font-style: italic;
}

h1 {
    font-size: 2.4rem;
}
p {
    font-size: 1rem;
}
.footer_links {
    display: flex;
    justify-content: space-between;
    padding: 2rem;
}

.links{
    color: var(--turquoise);
    display: flex;
    font-size: 1.4rem;
}

.links:hover {
    transform: scale(1.1);
}

.copyright {
    padding: 1rem;
}

.copyright, 
.partnership{
    text-align: center;
}

.partnership {
    background: #172547;
    padding: .5rem;
}

/* ===== RESPONSIVE DESIGN ===== */

@media only screen and (max-width: 672px) {
    .footer_links {
        display: grid;
        grid-template-columns: repeat(2 ,1fr);
    }
}

@media only screen and (max-width: 500px) {
    .footer_links {
        grid-template-columns: 1fr;
    }
}
</style>