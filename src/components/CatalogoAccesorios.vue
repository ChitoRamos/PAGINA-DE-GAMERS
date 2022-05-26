<template>
  <div id="app">
    <v-toolbar-title class="text-h4" align="center">ACCESORIOS</v-toolbar-title>
    <div class="text-center">
      <v-btn
        class="ma-2"
        :loading="loading"
        :disabled="loading"
        color="red"
        @click="loader = 'loading'"
        to="/Accesorio_mouse"
      >
        <h3>Mouse Gamer</h3>
      </v-btn>

      <v-btn
        class="ma-2"
        :loading="loading"
        :disabled="loading"
        color="yellow darken-3"
        @click="loader = 'loading'"
        to="Accesorio_teclado"
      >
        <h3>Teclados Gamer</h3>
      </v-btn>

      <v-btn
        class="ma-2"
        :loading="loading"
        :disabled="loading"
        color="green"
        @click="loader = 'loading'"
        to="Accesorio_tira"
      >
        <h3>Tira Led</h3>
      </v-btn>

      <v-btn
        class="ma-2"
        :loading="loading"
        :disabled="loading"
        color="light-blue darken-4"
        @click="loader = 'loading'"
        to="Accesorio_audifono"
      >
        <h3>Audifonos Gamer</h3>
      </v-btn>
      <v-btn
        class="ma-2"
        :loading="loading"
        :disabled="loading"
        color="deep-purple accent-2"
        @click="loader = 'loading'"
        to="Accesorio_cable"
      >
        <h3>Cables de internet</h3>
      </v-btn>
    </div>
  </div>
</template>

<style>
.v-app-bar {
  background-color: #616161;
}

.v-toolbar-title {
  font-size: 40px;
  color: white;
}

ul {
  list-style-type: square;
}
.v-card__title {
  font-family: Arial;
  font-size: 20px;

  color: black;
}
.v-card__text {
  color: white !important;
}

.v-card {
  width: 800px;
}

.v-banner {
  color: "black";
  font-family: Arial;
  font-size: 15px;
}

/*aqui modifico la barra de titulo de catalogo de accesorios*/
#app {
  /*
  border-radius: 4px;
  padding: 20px;
  transition: all 0.2s;*/
  background-color: #eb3d3d;
}

/*
#inspire {
  background-color: #000707;
}

*/

h2 {
  color: white;
  font-size: 30px;
}

pre {
  width: 100%;
  border: solid;
}
</style>
