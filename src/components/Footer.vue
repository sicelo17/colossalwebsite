<template>
  <footer>
    <div class="bd-container">
      <div class="footer_links">
        <div class="footer_column">
          <h1>About Us</h1>
          <div class="footer-links">
            <ul class="footer_routes">
              <router-link class="links" to="/">Our Company</router-link>
              <router-link class="links" to="/">Our team</router-link>
              <router-link class="links" to="/">Careers</router-link>
              <router-link class="links" to="/">Our Blogs</router-link>
            </ul>
          </div>
        </div>

        <div class="footer_column">
          <h1>Partnership</h1>
          <div class="footer-links">
            <ul class="footer_routes">
              <router-link class="links" to="/login">Sign In</router-link>
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
                <div class="links__div">
                  <span>
             <i class='bx bx-map' ></i>
            </span>
                Batanai Garderns, First Floor<br />
                Cnr First Street and Jason Moyo, Harare
              </div>
              <a href="mailto:info@colossalhub.com" class="footer__email"
                ><span>
                    <span>
              <i class='bx bxs-envelope-open' ></i>
            </span>
                    info@colossalhub.com</span></a
              > 
             <div class="social__icons">
                 <a href="#"><i class='bx bxl-facebook' ></i></a>
            <a href="#"><i class='bx bxl-twitter' ></i></a>
            <a href="#"><i class='bx bxl-instagram' ></i></a>
            <a href="#"><i class='bx bxl-linkedin'></i></a>
             </div>
              

             
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
export default {};
</script>

<style scoped>
footer {
  background: var(--blue);
  color: var(--turquoise);
  font-style: italic;
  z-index: var(--z-top);
}

h1 {
  font-size: 2.4rem;
  font-weight: var(--font-medium);
}
p {
  font-size: 1rem;
}

span {
    margin-right: .4rem;
}
.footer_links {
  display: flex;
  justify-content: space-between;
  padding: 2rem;
  flex-wrap: wrap;
}

.links{
  color: var(--turquoise);
  display: flex;
  font-size: 1rem;
  font-style: italic;
}

.links:hover {
  transform: scale(1.1);
}

.copyright {
  padding: 1rem;
}

.copyright,
.partnership {
  text-align: center;
}

.partnership {
  background: #172547;
  padding: 0.5rem;
}

.social__icons {
    display: flex;
    align-items: center;
    justify-content: space-between;
    color: var(--turquoise);
    font-size: 1rem;
}

.social__icons > a {
    color: var(--turquoise);
    font-size: 1rem;
}


.footer__email {
    color: var(--turquoise);
}

</style>