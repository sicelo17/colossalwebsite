<template>
  <div class="sign-up">
    <div class="bd-container">
      <div class="register-page">
        <div class="register__left">
          <img src="../assets/illustration-flowing-conversation.svg" alt="" />
        </div>
        <div class="register__right">
          <div class="card">
            <div class="card-details">
              <img src="../assets/COLOSSAL-02.jpeg" alt="" />
              <h3>Sign Up</h3>

              <form @submit.prevent="submitForm">
                <div class="field">
                  <input
                    type="name"
                    class="input"
                    placeholder="Username"
                    v-model="username"
                  />
                </div>

                <div class="field">
                  <input
                    type="email"
                    class="input"
                    placeholder="Email Address"
                    v-model="email"
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

                <div class="field">
                  <input
                    type="password"
                    class="input"
                    placeholder="Confirm Password"
                    v-model="password2"
                  />
                </div>

                <div class="notification is-danger" v-if="errors.length">
                  <p v-for="error in errors" :key="error">
                    {{ error }}
                  </p>
                </div>

                <div class="field">
                  <button class="button">Sign Up</button>
                </div>

                <hr />
                <router-link to="/login"
                  ><span class="login-link"
                    >I already have an account</span
                  ></router-link
                >
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "SignUp",
  data() {
    return {
      email: "",
      username: "",
      password: "",
      password2: "",
      errors: [],
    };
  },
  mounted() {
    document.title = "Sign Up | ColossalHub";
  },
  methods: {
    async submitForm() {
      this.errors = [];
      if (this.email === "") {
        this.error.push("The email is missing");
      }
      if (this.username === "") {
        this.errors.push("The username is missing");
      }
      if (this.password === "") {
        this.errors.push("The password is too short");
      }
      if (this.password !== this.password2) {
        this.errors.push("The passwords doesn't match");
      }
      if (!this.errors.length) {
        const formData = {
          username: this.username,
          email: this.email,
          password: this.password,
        }
        await axios
          .post("/api/v1/users/", formData)
          .then((response) => {
            this.$router.push("/login");
          })
          .catch((error) => {
            if (error.response) {
              for (const property in error.response.data) {
                this.errors.push(
                  `${property}: ${error.response.data[property]}`
                );
              }
              console.log(JSON.stringify(error.response.data));
            } else if (error.message) {
              this.errors.push("Something went wrong. Please try again");

              console.log(JSON.stringify(error));
            }
          });
      }
    },
  },
};
</script>

<style scoped>
.register-page {
  height: 95%;
  padding: 2rem 0;
  display: flex;
}

.register__left {
  flex: 0.6;
}

.register__right {
  flex: 0.4;
}

.register__left > img {
  height: 100%;
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

.button {
  font-family: var(--body-font);
  font-style: italic;
  border-radius: 3rem;
  font-size: var(--h3-font-size);
  padding: 0.6rem 2rem;
  cursor: pointer;
  background: var(--blue);
  color: var(--off-white);
  border: none;
}

.button:hover {
  background: linear-gradient(to bottom right, var(--blue), var(--turquoise));
  color: var(--white);
  transition: 0.2s ease-in all;
}

.register {
  font-style: normal;
}

.register:hover {
  text-decoration: underline;
  font-style: normal;
}

.login-link:hover {
  text-decoration: underline;
}

img {
  height: 60px;
  object-fit: contain;
}
.notification {
  width: 200px;
}
.notification p {
  background: rgb(226, 81, 81);
  color: aliceblue;
  display: flex;
  flex-direction: column;
  border-radius: 0.5rem;
  margin-top: 0.5rem;
}

@media only screen and (max-width: 770px) {
  .sign-up {
    background: linear-gradient(to bottom right, var(--blue), var(--turquoise));
  }

  .register__left {
    display: none;
  }

  .register__right {
    flex: 1;
  }
}
</style>