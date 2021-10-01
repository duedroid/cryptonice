<template>
  <div>
    <v-row v-for="(item, index) in trade_history_list" :key="index" justify="center">
      <v-col cols="12" sm="5">
        <v-card rounded="xl">
          <v-card-title>
            <v-chip
              class="mr-2"
              label
              :color="item.side == 'Buy' ? 'green darken-1' : 'red darken-1'"
              dark
            >{{ item.side }}</v-chip>
            <v-avatar class="mr-2" size="24">
              <img :src="item.img" :alt="item.pair">
            </v-avatar>
            <div class="text-subtitle-1 text-sm-h6 font-weight-medium">{{ item.pair }}</div>
          </v-card-title>
          <v-card-text>
            <v-row justify="space-between">
              <v-col>
                <div class="text-subtitle-2 text-sm-subtitle-1 font-weight-medium">Date</div>
              </v-col>
              <v-col class="text-right">
                <div class="text-subtitle-2 text-sm-subtitle-1 font-weight-medium">{{ item.date }}</div>
              </v-col>
            </v-row>
            <v-row justify="space-between">
              <v-col>
                <div class="text-subtitle-2 text-sm-subtitle-1 font-weight-medium">Price</div>
              </v-col>
              <v-col class="text-right">
                <div class="text-subtitle-2 text-sm-subtitle-1 font-weight-medium">{{ item.price }}</div>
              </v-col>
            </v-row>
            <v-row justify="space-between">
              <v-col>
                <div class="text-subtitle-2 text-sm-subtitle-1 font-weight-medium">Quantity</div>
              </v-col>
              <v-col class="text-right">
                <div class="text-subtitle-2 text-sm-subtitle-1 font-weight-medium">{{ item.quantity }}</div>
              </v-col>
            </v-row>
            <v-row justify="space-between">
              <v-col>
                <div class="text-subtitle-2 text-sm-subtitle-1 font-weight-medium">Amount</div>
              </v-col>
              <v-col class="text-right">
                <div class="text-subtitle-2 text-sm-subtitle-1 font-weight-medium">{{ item.amount }}</div>
              </v-col>
            </v-row>
            <v-row v-if="item.side == 'Sell'" justify="space-between">
              <v-col>
                <div class="text-subtitle-2 text-sm-subtitle-1 font-weight-medium">Profit</div>
              </v-col>
              <v-col class="text-right">
                <div
                  class="text-subtitle-2 text-sm-subtitle-1 font-weight-medium"
                  :style="{ 'color': item.profit.color }"
                >
                  {{ item.profit.amount }} ({{ item.profit.percent }}%)
                </div>
              </v-col>
            </v-row>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </div>
</template>

<script>
export default {
  data() {
    return {
      trade_history_list: [
        {
          "date": "2021-10-02 03:01",
          "pair": "AVAX/USDT",
          "img": "https://cryptoicon.s3.amazonaws.com/32/color/avax.png",
          "side": "Buy",
          "price": 68.52,
          "quantity": 16.258,
          "amount": 1671.038,
        },
        {
          "date": "2021-10-02 02:24",
          "pair": "SOL/USDT",
          "img": "https://cryptoicon.s3.amazonaws.com/32/color/sol.png",
          "side": "Sell",
          "price": 162.71,
          "quantity": 10.27,
          "amount": 1671.038,
          "profit": {
            "color": "#43A047",
            "amount": 171.038,
            "percent": 11.402
          }
        },
        {
          "date": "2021-10-01 18:05",
          "pair": "SOL/USDT",
          "img": "https://cryptoicon.s3.amazonaws.com/32/color/sol.png",
          "side": "Buy",
          "price": 146.0559,
          "quantity": 10.27,
          "amount": 1500
        },
      ]
    }
  }
}
</script>