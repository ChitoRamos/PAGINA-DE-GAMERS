

<head>

  
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }} - GAMERS</title>
    <!-- Latest compiled and minified CSS -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/css/bootstrap.min.css">

    <!-- jQuery library -->
    <script src="https://cdn.jsdelivr.net/npm/jquery@3.6.0/dist/jquery.slim.min.js"></script>

    <!-- Popper JS -->
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js"></script>

    <!-- Latest compiled JavaScript -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/js/bootstrap.bundle.min.js"></script>

    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="icon" type="image/png" href="/static/img/Control2.jpeg"/>

    <!-- Librerias de Vue-->
    <link href="https://fonts.googleapis.com/css?family=Roboto:100,300,400,500,700,900" rel="stylesheet">
    <link href="https://cdn.jsdelivr.net/npm/@mdi/font@6.x/css/materialdesignicons.min.css" rel="stylesheet">
    <link href="https://cdn.jsdelivr.net/npm/vuetify@2.x/dist/vuetify.min.css" rel="stylesheet">
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no, minimal-ui">
    
</head>
<template
>

  <div class="text-center">
    <h1
    style=color:green;
    > GAMERS </h1>

    <v-btn
      class="ma-2"
      :loading="loading"
      :disabled="loading"
      color="black"
      @click="loader = 'loading'"
    >
    <h3>
      Catalogo de accesorios
    </h3>
    </v-btn>

    <v-btn
      class="ma-2"
      :loading="loading"
      :disabled="loading"
      color="black"
      @click="loader = 'loading'"
    >
    <h3>
      Catalogo de juegos
    </h3>
    </v-btn>

    <v-btn
      class="ma-2"
      :loading="loading"
      :disabled="loading"
      color="black"
      @click="loader = 'loading'"
    >
    <h3>
      Novedades
    </h3>
    </v-btn>


<div id="carrousel" align="center">
<v-carousel 
      cycle
      height="400"
      style=width:600px;
      hide-delimiter-background
      show-arrows-on-hover
>


      <v-carousel-item
        v-for="(item,i) in items"
        :key="i"
        :src="item.src"
      ></v-carousel-item>
    </v-carousel>
    </div>


    <v-icon
      
      size="70"
      color="blue"
    >
      mdi-facebook
    </v-icon>

    <v-icon
      
      size="70"
      color="green"
    >
      mdi-email
    </v-icon>


    <v-icon
      
    size="70"
    color="white"
  >
    mdi-twitter
  </v-icon>

    <h1>Numero: 9231043457</h1>


  </div>


    

  
</template>





<script>



  export default {
    name: 'HelloWorld',

    data: () => ({


      
      ecosystem: [
        {
          text: 'vuetify-loader',
          href: 'https://github.com/vuetifyjs/vuetify-loader',
        },
        {
          text: 'github',
          href: 'https://github.com/vuetifyjs/vuetify',
        },
        {
          text: 'awesome-vuetify',
          href: 'https://github.com/vuetifyjs/awesome-vuetify',
        },
      ],
      importantLinks: [
        {
          text: 'Documentation',
          href: 'https://vuetifyjs.com',
        },
        {
          text: 'Chat',
          href: 'https://community.vuetifyjs.com',
        },
        {
          text: 'Made with Vuetify',
          href: 'https://madewithvuejs.com/vuetify',
        },
        {
          text: 'Twitter',
          href: 'https://twitter.com/vuetifyjs',
        },
        {
          text: 'Articles',
          href: 'https://medium.com/vuetify',
        },
      ],
      whatsNext: [
        {
          text: 'Explore components',
          href: 'https://vuetifyjs.com/components/api-explorer',
        },
        {
          text: 'Select a layout',
          href: 'https://vuetifyjs.com/getting-started/pre-made-layouts',
        },
        {
          text: 'Frequently Asked Questions',
          href: 'https://vuetifyjs.com/getting-started/frequently-asked-questions',
        },
      ],

      
    }),


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
  

  }
  
  

</script>

<style>


h3
  {
    font-family: ginebra;
    color: #C8E6C9;
    font-size:20px;
  }

</style>