<template>
    <div>
      <button type="submit" class="btn btn-primary">{{ msg }}</button>
    </div>
  </template>

  <script>
  import axios from 'axios';

  export default {
    name: 'Shark',
    data() {
      return {
        msg: '',
      };
    },
    methods: {
      getResponse() {
        const path = 'http://localhost:5000/shark';
        axios.get(path)
          .then((res) => {
            console.log(res.data);
            this.msg = res.data;
          })
          .catch((err) => {
            console.error(err);
          });
      },
    },
    created() {
      this.getResponse();
    },
  };
  </script>

  <!-- Add "scoped" attribute to limit CSS to this component only -->
  <style scoped>
  h1 {
    margin: 40px 0 0;
  }
  </style>
