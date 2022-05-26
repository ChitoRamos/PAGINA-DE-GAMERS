<template>
  <div id="app">
    <catalogo-accesorios> </catalogo-accesorios>

    <imagenes-mouse> </imagenes-mouse>
  </div>
</template>

<script>
import CatalogoAccesorios from "../components/CatalogoAccesorios.vue";
import ImagenesMouse from "../components/ImagenesMouse.vue";

export default {
  name: "Accesorios",
  name: "Imagenes",

  components: {
    CatalogoAccesorios,
    ImagenesMouse,
  },
};
</script>
