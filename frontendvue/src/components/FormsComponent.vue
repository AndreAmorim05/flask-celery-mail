<template>
  <div class="container">
    <form @submit.prevent="onSubmit">
      <div class="mb-3">
        <label for="exampleFormControlInput1" class="form-label"
          >Email address</label
        >
        <input
          type="email"
          class="form-control"
          id="exampleFormControlInput1"
          placeholder="name@example.com"
          v-model="email"
        />
      </div>
      <div class="mb-3">
        <label for="subject" class="form-label">Email subject</label>
        <input
          type="text"
          class="form-control"
          id="subject"
          placeholder="Title of the email"
          v-model="subject"
        />
      </div>

      <div class="mb-3">
        <label for="body" class="form-label">Email body</label>
        <textarea
          class="form-control"
          id="body"
          rows="3"
          v-model="body"
          placeholder="You can just use https://temp-mail.org to test your email delivery"
        >
        </textarea>
      </div>

      <div class="d-grid gap-1 col-6 mx-auto">
        <input class="btn btn-primary" type="submit" value="Send Email" />
      </div>
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "FormsComponent",
  data() {
    return {
      email: "",
      subject: "",
      body: "",
    };
  },
  methods: {
    onSubmit() {
      axios
        .post("http://localhost:5000/api/send-mail", {
          email: this.email,
          subject: this.subject,
          body: this.body,
        })
        .then(
          (response) => {
            console.log(response);
          },
          (error) => {
            console.log(error);
          }
        );

      this.email = "";
      this.subject = "";
      this.body = "";
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
