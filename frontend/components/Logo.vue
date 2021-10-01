<template>
  <v-btn
    class="no-background-hover pl-0"
    href="/"
    text
    :ripple="false"
  >
    <v-img src="/logo.png" :width="size"></v-img>
    <div class="text-subtitle-1 text-sm-h6 font-weight-medium ml-4">CRYPTONICE</div>
  </v-btn>
</template>

<script>
export default {
  computed: {
    size() {
      return this.$vuetify.breakpoint.xs ? 35 : 45
    }
  }
}
</script>

<style lang="scss">
.no-background-hover::before {
  background-color: transparent !important;
}
</style>