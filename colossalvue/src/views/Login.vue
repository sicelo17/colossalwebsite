<template>
  <div class="sign-in">
    <div class="bd-container">
      <div class="login-page">
        <div class="login__left">
          <img src="../assets/illustration-grow-together.svg" alt="" />
        </div>
        <div class="login__right">
          <div class="card">
          <div class="card-details">
            <img src="../assets/COLOSSAL-02.jpeg" alt="" />
            <h3>Sign In</h3>

            <form @submit.prevent="submitForm">
              <div class="field">
                <input
                  type="text"
                  class="input"
                  placeholder="Username"
                  v-model="username"
                />
              </div>

              <div class="field">
                <input
                  type="password"
                  class="input"
                  placeholder="Password"
                  v-model="password"
                />
              </div>

               <div class="notification is-danger" v-if="errors.length">
            <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
          </div>

              <div class="field">
                <button>Sign In</button>
              </div>

              <hr />

              Or
              <router-link to="/sign-up"
                ><span class="login">click here</span></router-link
              >
              to sign up!
            </form>
          </div>
        </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios  from 'axios';
export default {
  name: "Login",
  data() {
    return {
      username: "",
      password: "",
      errors: [],
    };
  },
  mounted() {
    document.title = "LogIn | ColossalHub";
  },
  methods: {
      async submitForm() {
      axios.defaults.headers.common["Authorization"] = "";
      localStorage.removeItem("token");
      const formData = {
        username: this.username,
        password: this.password,
      };
      await axios
        .post("/api/v1/token/login/", formData)
        .then((response) => {
          const token = response.data.auth_token;
          this.$store.commit("setToken", token);
          axios.defaults.headers.common["Authorization"] = "Token " + token;
          localStorage.setItem("token", token);
          const toPath = this.$route.query.to || "/";
          this.$router.push(toPath);
        })
        .catch((error) => {
          if (error.response) {
            for (const property in error.response.data) {
              this.errors.push(`${property}: ${error.response.data[property]}`);
            }
          } else {
            this.errors.push("Something went wrong. Please try again");
            console.log(JSON.stringify(error));
          }
        });
    },
  },
}
</script>

<style scoped>

.login-page {
  margin: 3rem 0 0 0;
  height: 95vh;
  display: flex;
}

.login__left {
  flex: .6;
}
.login__left > img {
  height: 100%;
}

.login__right {
  flex: .4;
}
.card {
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.card-details {
  background: var(--white);
  padding: 4rem;
  border-radius: 2rem;
  height: 50%;
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
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

span {
  font-style: italic;
  font-size: var(--h3-font-size);
}

h3 {
  font-size: var(--h2-font-size);
}

button {
  font-family: var(--body-font);
  font-style: italic;
  border-radius: 3rem;
  font-size: 1.3rem;
  padding: 0.6rem 2rem;
  cursor: pointer;
  background: var(--blue);
  color: var(--off-white);
  border: none;
}

button:hover {
  background: linear-gradient(to bottom right, var(--blue), var(--turquoise));
  color: var(--white);
  transition: 0.2s ease-in all;
}

.login {
  font-style: normal;
}

.login:hover {
  text-decoration: underline;
  font-style: normal;
}

img {
  height: 60px;
  object-fit: contain;
}

@media only screen and (max-width: 750px) {
  .sign-in {
  background: linear-gradient(to bottom right, var(--blue), var(--turquoise));
}

.login__left{
  display: none;
}

.login__right {
  flex: 1;
}
}
</style>