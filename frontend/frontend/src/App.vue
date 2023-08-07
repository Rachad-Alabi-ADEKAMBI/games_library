<template>
  <nav class="mt-3">
    <router-link to="/">Home</router-link> |
    <router-link to="/shark">Shark</router-link>
    <router-link to="/games">Games</router-link>
  </nav>
  <router-view/>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

</style>
