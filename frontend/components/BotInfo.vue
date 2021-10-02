<template>
  <v-card rounded="xl">
    <v-card-title>
      <div class="text-h6 text-sm-h5 font-weight-medium">
        Bot Info
      </div>
      <v-spacer></v-spacer>
      <v-switch
        class="mt-0 pt-0 align-self-center"
        color="primary"
        v-model="bot_status"
        inset
        hide-details
      ></v-switch>
    </v-card-title>
    <v-card-text>
      <v-row>
        <v-col col="12">
          <div class="text-subtitle-1 text-sm-h6 font-weight-medium">Current Coin</div>
          <div class="d-flex flex-wrap mt-2" style="gap: 10px">
            <v-chip
              v-for="coin in current_coin_list"
              :key="coin.name"
              label
              color="primary"
            >
              <v-avatar class="mr-2">
                <img
                  :src="coin.img"
                  :alt="coin.name"
                >
              </v-avatar>
              <div class="font-weight-medium">
                {{ coin.name }}<span class="ml-2" :style="{ 'color': coin.color }">{{ coin.profit }}</span>
              </div>
            </v-chip>
          </div>
        </v-col>
      </v-row>
      <v-row>
        <v-col col="12">
          <div class="text-subtitle-1 text-sm-h6 font-weight-medium">Available Coin</div>
          <div class="d-flex flex-wrap mt-2" style="gap: 10px">
            <v-chip
              v-for="coin in coin_list"
              :key="coin.name"
              label
              color="primary"
            >
              <v-avatar class="mr-2">
                <img
                  :src="coin.img"
                  :alt="coin.name"
                >
              </v-avatar>
              <div class="font-weight-medium">{{ coin.name }}</div>
            </v-chip>
          </div>
        </v-col>
      </v-row>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  data() {
    return {
      bot_status: true,
      current_coin_list: [
        {
          "name": "ETH",
          "img": "https://cryptoicon.s3.amazonaws.com/32/color/eth.png",
          "profit": "+15.23%",
          "color": "#43A047"
        },
        {
          "name": "AVAX",
          "img": "https://cryptoicon.s3.amazonaws.com/32/color/avax.png",
          "profit": "-5%",
          "color": "#E53935"
        },
      ],
      coin_list: [
        {
          "name": "SOL",
          "img": "https://cryptoicon.s3.amazonaws.com/32/color/sol.png",
        },
        {
          "name": "AVAX",
          "img": "https://cryptoicon.s3.amazonaws.com/32/color/avax.png",
        },
        {
          "name": "ETH",
          "img": "https://cryptoicon.s3.amazonaws.com/32/color/eth.png",
        },
        {
          "name": "LUNA",
          "img": "https://cryptoicon.s3.amazonaws.com/32/color/luna.png",
        },
        {
          "name": "AXS",
          "img": "https://cryptoicon.s3.amazonaws.com/32/color/axs.png",
        },
        {
          "name": "BTC",
          "img": "https://cryptoicon.s3.amazonaws.com/32/color/btc.png",
        },
      ]
    }
  },
}
</script>