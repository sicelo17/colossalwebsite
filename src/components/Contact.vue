<template>

   <div class="contact">
        <div class="bd-container">
        <div class="contact__content">
          <div class="contact__data">
            <h3>Interested in working with us</h3>
            <p>Quality software guaranteed</p>
          </div>
          <form >
            <input type="email" placeholder="Enter your email address" class="contact__email">
            <a class="contact__link" href="#">Request Demo</a>
          </form>
        </div>
      </div>
   </div>
</template>

<script>
export default {};
</script>

<style scoped>
.contact {
  padding: var(--biggest-font-size) 0;
  background-color: var(--white);
}

.contact__content {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.contact__data h3 {
  font-size: var(--h1-font-size);
  font-weight: inherit;
}

.contact__data p {
  font-size: var(--normal-font-size);
  color: var(--blue);
}

.contact__email {
  font-size: 1rem;
  display: inline-block;
  width: 30vw;
  padding: 1rem;
  background-color: var(--off-white);
  border: none;
  text-indent: 1rem;
}

.contact__email:focus {
  outline: none;
}

.contact__link:link,
.contact__link:visited {
  display: inline-block;
  padding: 0.8rem 3rem;
  margin-left: -0.5rem;
  background-color: var(--blue);
  color: var(--white);
  transition: 0.3s;
}

.contact__link:hover {
  background-color: var(--turquoise);
  color: var(--blue);
}

/*
======================
contact Media Query
======================
*/
@media only screen and (max-width: 998px) {
  .contact {
    padding: 3rem 2rem;
  }

  .contact__content {
    flex-direction: column;
  }

  .contact__email {
    width: 40rem;
  }

  .contact__data {
    margin-bottom: 2rem;
  }

  .contact__link:link,
  .contact__link:visited {
    margin-left: 40%;
    margin-top: var(--h2-font-size);
  }
}

@media only screen and (max-width: 768px) {
  .contact__content {
    align-items: center;
    justify-content: center;
    text-align: center;
  }

  .contact__email {
    width: 30rem;
    display: block;
    margin-bottom: 1.6rem;
  }

  .contact__link:link,
  .contact__link:visited {
    margin-left: 0;
    margin-top: var(--h2-font-size);
  }
}

@media only screen and (max-width: 568px) {
  .contact__email {
    width: 30rem;
    font-size: 1rem;
  }

  .contact__data h3 {
    font-size: 1.6rem;
  }

  .contact__data p {
    font-size: 1rem;
  }

  .contact__link:link,
  .contact__link:visited {
    padding: 1.2rem 2rem;
    margin-left: 0;
  }
}

@media only screen and (max-width: 480px) {
  .contact__email {
    width: 20rem;
  }
}

</style>