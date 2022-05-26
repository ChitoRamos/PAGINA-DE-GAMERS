<template>
  <div class="text-center" id="inspire">
    <h1 style="color: #00e676">GAMERS</h1>

    <v-btn
      class="ma-2"
      :loading="loading"
      :disabled="loading"
      color="black"
      @click="loader = 'loading'"
      to="/Catalogo_accesorios"
    >
      <h3>Catalogo de accesorios</h3>
    </v-btn>

    <v-btn
      class="ma-2"
      :loading="loading"
      :disabled="loading"
      color="black"
      @click="loader = 'loading'"
      to="Catalogo_juegos"
    >
      <h3>Catalogo de juegos</h3>
    </v-btn>

    <v-btn
      class="ma-2"
      :loading="loading"
      :disabled="loading"
      color="black"
      @click="loader = 'loading'"
    >
      <h3>Entretenimiento</h3>
    </v-btn>

    <div id="carrousel" align="center">
      <v-carousel
        cycle
        height="400"
        style="width: 600px"
        hide-delimiter-background
        show-arrows-on-hover
      >
        <v-carousel-item
          v-for="(item, i) in items"
          :key="i"
          :src="item.src"
        ></v-carousel-item>
      </v-carousel>
    </div>

    <v-btn
      class="pa-7 rounded-circle"
      width="9"
      href="https://www.facebook.com/Gamers-483396008806272/"
    >
      <v-icon size="70" color="blue"> mdi-facebook </v-icon>
    </v-btn>

    <v-btn class="pa-7 rounded-circle" width="9" href="https://fb.watch/dbEih7yFxv/">
      <v-icon size="70" color="deep-orange darken-1"> mdi-instagram </v-icon>
    </v-btn>

    <v-btn
      class="pa-7 rounded-circle"
      width="9"
      href="https://wa.me/message/A6WH4LK32PP3L1"
    >
      <v-icon size="70" color="green"> mdi-whatsapp </v-icon>
    </v-btn>

    <h1>Numero: 9231043457</h1>
  </div>
</template>

<script>
export default {
  name: "HelloWorld",

  data: () => ({
    ecosystem: [
      {
        text: "vuetify-loader",
        href: "https://github.com/vuetifyjs/vuetify-loader",
      },
      {
        text: "github",
        href: "https://github.com/vuetifyjs/vuetify",
      },
      {
        text: "awesome-vuetify",
        href: "https://github.com/vuetifyjs/awesome-vuetify",
      },
    ],
    importantLinks: [
      {
        text: "Documentation",
        href: "https://vuetifyjs.com",
      },
      {
        text: "Chat",
        href: "https://community.vuetifyjs.com",
      },
      {
        text: "Made with Vuetify",
        href: "https://madewithvuejs.com/vuetify",
      },
      {
        text: "Twitter",
        href: "https://twitter.com/vuetifyjs",
      },
      {
        text: "Articles",
        href: "https://medium.com/vuetify",
      },
    ],
    whatsNext: [
      {
        text: "Explore components",
        href: "https://vuetifyjs.com/components/api-explorer",
      },
      {
        text: "Select a layout",
        href: "https://vuetifyjs.com/getting-started/pre-made-layouts",
      },
      {
        text: "Frequently Asked Questions",
        href: "https://vuetifyjs.com/getting-started/frequently-asked-questions",
      },
    ],
  }),

  data() {
    return {
      items: [
        {
          src: require("../assets/imagenes_de_fondo/Gamers11.jpg"),
        },
        {
          src: require("../assets/imagenes_de_fondo/control4.jpeg"),
        },
        {
          src: require("../assets/imagenes_de_fondo/control3.jpeg"),
        },
      ],
    };
  },
};
</script>

<style scoped>
h3 {
  font-family: ginebra;
  color: #ffffff;
  font-size: 20px;
}

#inspire {
  background-color: #616161;
  height: 900px;
  background: url("../assets/imagenes_de_fondo/fondo2.jpg");
  width: 100%;
  height: 100%;
  position: fixed;
  background-size: 100% 100%;
}

body {
  background-color: #fff;
}
</style>
