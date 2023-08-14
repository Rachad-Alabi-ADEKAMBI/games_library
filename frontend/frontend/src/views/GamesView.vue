<template>
    <div>
      <Games />
    </div>
  </template>

  <script>
  // @ is an alias to /src
  import Games from '@/components/Games.vue'

  export default {
    name: 'GamesView',
    components: {
      Games
    }
  }
  </script>
