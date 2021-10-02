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
            <v-avatar class="mr-2" size="22">
              <img :src="item.img" :alt="item.pair">
            </v-avatar>
            <div class="text-subtitle-1 text-sm-h6 font-weight-medium">{{ item.pair }}</div>

            <v-spacer></v-spacer>

            <div
              v-if="item.side == 'Sell'"
              class="text-subtitle-1 text-sm-h6 font-weight-bold"
              :style="{ 'color': item.profit.color }"
            >
              {{ item.profit.percent }} %
            </div>
          </v-card-title>
          <v-card-text>
              <div class="d-flex">
                <div class="text-subtitle-2 text-sm-subtitle-1 font-weight-medium">Date</div>
                <v-spacer></v-spacer>
                <div class="text-subtitle-2 text-sm-subtitle-1 font-weight-medium">{{ item.date }}</div>
              </div>
              <div class="d-flex">
                <div class="text-subtitle-2 text-sm-subtitle-1 font-weight-medium">Price</div>
                <v-spacer></v-spacer>
                <div class="text-subtitle-2 text-sm-subtitle-1 font-weight-medium">{{ item.price }}</div>
              </div>
              <div class="d-flex">
                <div class="text-subtitle-2 text-sm-subtitle-1 font-weight-medium">Quantity</div>
                <v-spacer></v-spacer>
                <div class="text-subtitle-2 text-sm-subtitle-1 font-weight-medium">{{ item.quantity }}</div>
              </div>
              <div class="d-flex">
                <div class="text-subtitle-2 text-sm-subtitle-1 font-weight-medium">Amount</div>
                <v-spacer></v-spacer>
                <div class="text-subtitle-2 text-sm-subtitle-1 font-weight-medium">{{ item.amount }}</div>
              </div>
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
          "date": "2021-10-02 03:42",
          "pair": "AVAX/USDT",
          "img": "https://cryptoicon.s3.amazonaws.com/32/color/avax.png",
          "side": "Sell",
          "price": 60.03,
          "quantity": 16.258,
          "amount": 1463.987,
          "profit": {
            "color": "#E53935",
            "percent": "-12.39"
          }
        },
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
            "percent": "+11.402"
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