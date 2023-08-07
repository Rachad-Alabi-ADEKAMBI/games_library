<template>
    <div class="home">
      <Shark />
    </div>
  </template>

  <script>
  // @ is an alias to /src
  import Shark from '@/components/Shark.vue'

  export default {
    name: 'SharkView',
    components: {
      Shark
    }
  }
  </script>
