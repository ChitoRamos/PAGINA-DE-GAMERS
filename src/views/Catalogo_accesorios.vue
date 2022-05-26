<template>
  <div id="inspire">
    <catalogo-accesorios />

    <div class="swiper" align="center">
      <v-img
        lazy-src="../assets/imagenes_de_fondo/pc.jpg"
        max-height="450"
        max-width="850"
        src="../assets/imagenes_de_fondo/pc.jpg"
      ></v-img>
    </div>
  </div>
</template>

<script>
import CatalogoAccesorios from "../components/CatalogoAccesorios";

export default {
  name: "Accesorios",

  components: {
    CatalogoAccesorios,
  },
};
</script>

<style>
/*Para posisionar la imagen en el centro*/
.swiper {
  position: center;
  transform: translateY(+20%);
}

#inspire {
}
</style>
