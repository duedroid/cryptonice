<template>
  <v-row class="mt-2" justify="center">
    <v-col cols="12" sm="5">
      <v-card class="pa-2" rounded="xl">
        <v-card-title>
          <div class="text-h6 text-sm-h5 font-weight-medium">Bot Info</div>
        </v-card-title>
        <v-card-text>
          <v-row>
            <v-col cols="12">
              <div class="d-flex">
                <v-switch
                  class="mt-0 pt-0 align-self-center"
                  color="primary"
                  v-model="bot_status"
                  inset
                  hide-details
                ></v-switch>
                <div class="text-subtitle-1 text-sm-h6 font-weight-medium mr-4 align-self-center">
                  Status : <span :class="bot_status_data.class">{{ this.bot_status_data.text }}</span>
                </div>
              </div>
            </v-col>
          </v-row>
          <v-row>
            <v-col col="12">
              <div class="text-subtitle-1 text-sm-h6 font-weight-medium">Current Coin</div>
              <v-chip
                label
                color="primary"
              >
                <v-avatar class="mr-2">
                  <img
                    :src="curren_coin.img"
                    :alt="curren_coin.name"
                  >
                </v-avatar>
                <div class="font-weight-medium">{{ curren_coin.name }}</div>
              </v-chip>
            </v-col>
          </v-row>
          <v-row>
            <v-col col="12">
              <div class="text-subtitle-1 text-sm-h6 font-weight-medium">Coin List</div>
              <div class="d-flex flex-wrap" style="gap: 10px">
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
    </v-col>
  </v-row>
</template>

<script>
export default {
  data() {
    return {
      bot_status: true,
      curren_coin: {
        "name": "AVAX",
        "img": "https://cryptoicon.s3.amazonaws.com/32/color/avax.png"
      },
      coin_list: [
        {
          "name": "SOL",
          "img": "https://cryptoicon.s3.amazonaws.com/32/color/sol.png"
        },
        {
          "name": "AVAX",
          "img": "https://cryptoicon.s3.amazonaws.com/32/color/avax.png"
        },
        {
          "name": "ADA",
          "img": "https://cryptoicon.s3.amazonaws.com/32/color/ada.png"
        },
        {
          "name": "DOT",
          "img": "https://cryptoicon.s3.amazonaws.com/32/color/dot.png"
        },
        {
          "name": "AXS",
          "img": "https://cryptoicon.s3.amazonaws.com/32/color/axs.png"
        },
      ]
    }
  },

  computed: {
    bot_status_data() {
      if (this.bot_status) {
        return {
          text: "Running",
          class: "primary--text"
        }
      } else {
        return {
          text: "Stop",
          class: "black--text"
        }
      }
    }
  }
}
</script>