<template>
  <v-app>
    <v-app-bar
      app
      flat
    >
      <div v-if="isMobile">
        <Logo />
      </div>
      <v-container v-else>
        <Logo />
      </v-container>
    </v-app-bar>

    <v-main class="background">
      <Nuxt />
    </v-main>
  </v-app>
</template>

<script>
export default {
  computed: {
    isMobile() {
      return this.$vuetify.breakpoint.xs
    }
  }
}
</script>