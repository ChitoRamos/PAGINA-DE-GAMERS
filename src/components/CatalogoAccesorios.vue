


<template>


<body>
<div id="app" >
  <v-app id="inspire">


    <h2 align="center"> 
      CATALOGO DE ACCESORIOS GAMER
    </h2>


  <v-container
    class="fill-height"
    fluid
    style="min-height: 434px"
    
    
  >
    

  
    <v-fade-transition mode="out-in">
      <v-row>


              <v-col cols="6">
                <v-card
                
                color="#BBDEFB"
                >
                  

    <v-carousel cycle
      height="400"
      style=width:700px;
      hide-delimiter-background
      show-arrows-on-hover>

      <v-carousel-item
        v-for="(item, i) in items"
        :key="i"
        :src="item.src"

      >
        
          <v-row
            class="fill-height"
            align="center"
            justify="center"
          >
            
          </v-row>
      </v-carousel-item>
    </v-carousel>
                    
                  <v-card-title class="justify-center" >
                    Tira led 10 metros
                    
                    <v-banner
                      class="black--text"
                    >
                        Tiras Led 5050 Kit 10m Luz Musical Rab Controlada Por App



                    </v-banner>




<v-dialog
      v-model="dialog"
      width="500"
    >
      <template v-slot:activator="{ on, attrs }">
        <v-btn
          color="red lighten-2"
          dark
          v-bind="attrs"
          v-on="on"
        >
          ESPECIFICACIONES
        </v-btn>
      </template>

      <v-card>
        <v-card-title class="text-h5 grey lighten-2">
          TIRA LED
        </v-card-title>

        <v-card-text>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
        </v-card-text>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="primary"
            text
            @click="dialog = false"
          >
            OK
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>



                    
                  </v-card-title>
                
                </v-card>
              </v-col>

              







              <v-col cols="6">
                <v-card
                
                color="#BBDEFB"
                >
                  <v-img
                    src="../assets/juegos/fifa2022.jpeg"
                    class="grey darken-4"
                    contain
                    height="241"
                  ></v-img>
                  <v-card-title class="justify-center">
                    FIFA 22
                  </v-card-title>
                
                </v-card>
              </v-col>




              <v-col cols="6">
                <v-card
                color="#BBDEFB"
                >
                  <v-img
                    src="../assets/juegos/fortnite.jpeg"
                    class="grey darken-4"
                    contain
                    height="241"
                  ></v-img>
                  <v-card-title class="justify-center" >
                    FORTNITE
                  
                  </v-card-title>
                
                </v-card>
              </v-col>





              <v-col cols="6">
                <v-card
                
                color="#BBDEFB"
                >
                  <v-img
                    src="../assets/juegos/mortal.jpeg"
                    class="grey darken-4"
                    contain
                    height="241"
                  ></v-img>
                  <v-card-title class="justify-center">
                    MORTAL COMBAT
                  </v-card-title>
                
                </v-card>
              </v-col>


               <v-col cols="6">
                <v-card
                
                color="#BBDEFB"
                >
                  <v-img
                    src="../assets/juegos/Minecraft.jpeg"
                    class="grey darken-4"
                    contain
                    height="241"
                  ></v-img>
                  <v-card-title class="justify-center">
                    MINECRAFT
                  </v-card-title>
                
                </v-card>
              </v-col>


               <v-col cols="6">
                <v-card
                
                color="#BBDEFB"
                >
                  <v-img
                    src="../assets/juegos/Fora.jpeg"
                    class="grey darken-4"
                    contain
                    height="241"
                  ></v-img>
                  <v-card-title class="justify-center">
                    FORZA 5
                  </v-card-title>
                
                </v-card>
              </v-col>


               <v-col cols="6">
                <v-card
                
                color="#BBDEFB"
                >
                  <v-img
                    src="../assets/juegos/haloi.jpeg"
                    class="grey darken-4"
                    contain
                    height="241"
                  ></v-img>
                  <v-card-title class="justify-center">
                    HALO INFINITE
                  </v-card-title>
                
                </v-card>
              </v-col>


               <v-col cols="6">
                <v-card
                
                color="#0D47A1"
                >
                  <v-img
                    src="../assets/juegos/halos.jpeg"
                    class="grey darken-4"
                    contain
                    height="241"
                  ></v-img>
                  <v-card-title class="justify-center">
                    TODA LA SAGA DE HALO
                  </v-card-title>
                
                </v-card>
              </v-col>


               <v-col cols="6">
                <v-card
                
                color="#0D47A1"
                >
                  <v-img
                    src="../assets/juegos/black4.jpeg"
                    class="grey darken-4"
                    contain
                    height="241"
                  ></v-img>
                  <v-card-title class="justify-center">
                    BLACK 4 BLOOD
                  </v-card-title>
                
                </v-card>
              </v-col>


               <v-col cols="6">
                <v-card
                
                color="#0D47A1"
                >
                  <v-img
                    src="../assets/juegos/batlefieldv.jpeg"
                    class="grey darken-4"
                    contain
                    height="241"
                  ></v-img>
                  <v-card-title class="justify-center">
                    BATTLEFIELD V
                  </v-card-title>
                
                </v-card>
              </v-col>

               <v-col cols="6">
                <v-card
                
                color="#0D47A1"
                >
                  <v-img
                    src="../assets/juegos/gta.jpeg"
                    class="grey darken-4"
                    contain
                    height="241"
                  ></v-img>
                  <v-card-title class="justify-center">
                    GTA
                  </v-card-title>
                
                </v-card>
              </v-col>


               <v-col cols="6">
                <v-card
                
                color="#0D47A1"
                >
                  <v-img
                    src="../assets/juegos/gta_san_andreas.jpeg"
                    class="grey darken-4"
                    contain
                    height="241"
                  ></v-img>
                  <v-card-title class="justify-center">
                    GTA SAN ANDREAS
                  </v-card-title>
                
                </v-card>
                </v-col>


                <v-col cols="6">
                <v-card
                
                color="#0D47A1"
                >
                  <v-img
                    src="../assets/juegos/gears3.webp"
                    class="grey darken-4"
                    contain
                    height="241"
                  ></v-img>
                  <v-card-title class="justify-center">
                    GEARS 3
                  </v-card-title>
                
                </v-card>
                </v-col>


                <v-col cols="6">
                <v-card
                
                color="#0D47A1"
                >
                  <v-img
                    src="../assets/juegos/gears4.jpeg"
                    class="grey darken-4"
                    contain
                    height="241"
                  ></v-img>
                  <v-card-title class="justify-center">
                    GEARS OF WAR 4
                  </v-card-title>
                
                </v-card>
                </v-col>


                <v-col cols="6">
                <v-card
                
                color="#0D47A1"
                >
                  <v-img
                    src="../assets/juegos/gears5.jpeg"
                    class="grey darken-4"
                    contain
                    height="241"
                  ></v-img>
                  <v-card-title class="justify-center">
                    GEARS OF WAR 5
                  </v-card-title>
                
                </v-card>
                </v-col>


                <v-col cols="6">
                <v-card
                
                color="#0D47A1"
                >
                  <v-img
                    src="../assets/juegos/blackops3.jpeg"
                    class="grey darken-4"
                    contain
                    height="241"
                  ></v-img>
                  <v-card-title class="justify-center">
                    CALL OF DUTY BLACK OPS 3
                  </v-card-title>
                
                </v-card>
                </v-col>


                <v-col cols="6">
                <v-card
                
                color="#0D47A1"
                >
                  <v-img
                    src="../assets/juegos/f12021.jpeg"
                    class="grey darken-4"
                    contain
                    height="241"
                  ></v-img>
                  <v-card-title class="justify-center">
                    FORMULA 1 
                  </v-card-title>
                
                </v-card>
                </v-col>


                 <v-col cols="6">
                  <v-card
                
                  color="#0D47A1"
                  >
                  <v-img
                    src="../assets/juegos/halo5.webp"
                    class="grey darken-4"
                    contain
                    height="241"
                  ></v-img>
                  <v-card-title class="justify-center">
                    HALO 5 
                  </v-card-title>
                
                </v-card>
                </v-col>


                <v-col cols="6">
                  <v-card
                
                  color="#0D47A1"
                  >
                  <v-img
                    src="../assets/juegos/titanfall.webp"
                    class="grey darken-4"
                    contain
                    height="241"
                  ></v-img>
                  <v-card-title class="justify-center">
                    TITANFALL 2 
                  </v-card-title>
                
                </v-card>
                </v-col>
      </v-row>
    </v-fade-transition>
  </v-container>
    </v-app>

  </div>
  </body>

</template>

<script>
 export default {
    name: 'HelloWorld',

data () {
    return {
      items: [
        {
          src: require('../assets/Gamers11.jpg'),
        },
        {
          src: require('../assets/control4.jpeg'),
        },
        {
          src: require('../assets/control3.jpeg'),
        },
       
      ],
    }
  },

  data () {
    return {
      dialog: false,
    }
  },
 }
 

</script>


<style>
ul {
  list-style-type: square;
}
.v-card__title {
  font-family: Monaco;
  font-size: 40px;
  
  color: black;
}
.v-card__text {
  color: white!important;
}

.v-card {
  
}

.v-banner {
  color: "red";
  font-family: Monaco;
  font-size: 15px;
  background-color: "black";
}


#app {

  /*
  border-radius: 4px;
  padding: 20px;
  transition: all 0.2s;*/
  background-color: #616161;
}

#inspire{
    background-color: #616161;
}

h2{
  color: white;
  font-size: 30px;

}


</style>