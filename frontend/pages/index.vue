<template>
  <div>
    <v-row justify="center">
      <v-col cols="12" sm="5">
        <v-tabs
          fixed-tabs
          v-model="tab"
        >
          <v-tab href="#summary-tab">Summary</v-tab>
          <v-tab href="#history-tab">Trade History</v-tab>
        </v-tabs>

        <v-tabs-items
          class="background"
          v-model="tab"
        >
          <v-tab-item value="summary-tab">
            <v-container class="mt-3">
              <v-row>
                <v-col cols="12">
                  <NetWorth />
                </v-col>
              </v-row>
              <v-row>
                <v-col cols="12">
                  <BotInfo />
                </v-col>
              </v-row>
            </v-container>
          </v-tab-item>
          <v-tab-item value="history-tab">
            <v-container class="mt-3">
              <TradeHistory />
            </v-container>
          </v-tab-item>
        </v-tabs-items>
      </v-col>
    </v-row>
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