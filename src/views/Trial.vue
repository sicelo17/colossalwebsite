<template>
  <div class="page__trial">
    <div class="bd-container">
      <h2>Request A Demo</h2>

      <div class="trial__page">
        <div class="trial__left">
          <img src="../assets/illustration-your-users.svg" alt="" />
        </div>
        <div class="trial__right">
          <form @submit.prevent="requestDemo">
            <div class="field">
              <input
                type="text"
                class="input"
                placeholder="Name"
                v-model="name"
                required
              />
            </div>

            <div class="field">
              <input
                type="email"
                class="input"
                placeholder="Enter Email Address"
                v-model="email"
                required
              />
            </div>

            <div class="field">
              <input
                type="tel"
                class="input"
                placeholder="Enter Phone Number"
                v-model="phone_no"
              />
            </div>

            <div class="field">
              <input
                type="text"
                class="input"
                placeholder="What's your app of choice"
                v-model="app"
              />
            </div>

            <div class="field">
              <button>Request Demo</button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      name: "",
      phone_no: "",
      email: "",
      app: "",
    };
  },
  methods: {
      requestDemo() {
          const formDetails = {
              name :this.name,
              phone_no : this.phone_no,
              email:  this.email,
              app : this.app,
          }

          console.log(formDetails)
      }
  },
  mounted() {
    document.title = "Trial | ColossalHub";
  },
};
</script>

<style scoped>
.page__trial {
    padding-bottom: 3rem;
}
h2 {
  text-align: center;
  font-style: italic;
  font-size: 2rem;
  margin-top: 5rem;
}

.trial__page {
  display: flex;
  flex-wrap: wrap;
}

.trial__left {
  flex: 0.6;
}

.trial__right {
  flex: 0.4;
  padding: 0 2rem;
}

input {
  border-radius: 2rem;
  border: 1px solid var(--blue);
  color: var(--blue);
  width: 100%;
  font-size: 1.2rem;
  padding: 0.5rem;
  font-family: var(--body-font);
  font-style: italic;
}

input:focus {
  outline: none;
  border: 3px solid var(--blue);
}

::placeholder {
  font-family: var(--body-font);
  font-style: italic;
}
.field {
  margin-top: 2rem;
}

button {
  padding: 1rem;
  font-family: var(--body-font);
  font-style: italic;
  font-size: 1.3rem;
  border: 1px solid var(--blue);
  cursor: pointer;
  color: var(--white);
  background-color: var(--blue);
}

button:hover {
  background: linear-gradient(to bottom right, var(--blue), var(--turquoise));
  color: var(--white);
  transition: 0.2s ease-in all;
}

@media only screen and (max-width: 800px){
    .trial__left{
        display: flex;
        flex: .5;
    }

    .trial__right{
        flex: .5;
    }
}
@media only screen and (max-width: 690px) {
    .page__trial {
        background: url("../assets/illustration-your-users.svg");
        object-fit: contain;
    }
    .trial__left{
        display: none;
    }

    .trial__right{
        flex: 1;
    }
}
</style>