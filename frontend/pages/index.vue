<template>
  <div>
    <v-container>
      <v-row justify="center">
        <v-col cols="12" sm="5">
          <v-tabs
            fixed-tabs
            v-model="tab"
          >
              <v-tab href="#summary-tab">Summary</v-tab>
              <v-tab href="#history-tab">Trade History</v-tab>
          </v-tabs>
        </v-col>
      </v-row>
    </v-container>

    <v-tabs-items
      class="background"
      v-model="tab"
    >
      <v-tab-item value="summary-tab">
        <v-container>
          <v-row justify="center">
            <v-col cols="12" sm="5">
              <NetWorth />
            </v-col>
          </v-row>
          <v-row justify="center">
            <v-col cols="12" sm="5">
              <BotInfo />
            </v-col>
          </v-row>
        </v-container>
      </v-tab-item>
      <v-tab-item value="history-tab">
        <v-container>
          <TradeHistory />
        </v-container>
      </v-tab-item>
    </v-tabs-items>
  </div>
</template>

<script>
export default {
  head() {
    return {
      title: "Home"
    }
  },
  data() {
    return {
      tab: 'summary-tab'
    }
  }
}
</script>