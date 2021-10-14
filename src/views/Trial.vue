<template>
  <div class="page__trial">
    <div class="bd-container">
      <h2>Request a Demo</h2>

      <div class="trial__page">
        <div class="trial__left">
          <img src="../assets/illustration-your-users.svg" alt="" />
        </div>
        <div class="trial__right">
          <form @submit.prevent="submitForm">
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
            email:""
        }
    }
};
</script>

<style scoped>
.page__trial {
  margin: 5rem;
}
h2 {
  text-align: center;
}

.trial__page {
  display: flex;
}

.trial__left,
.trial__right {
  flex: 0.5;
}
</style>