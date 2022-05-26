<template>
  <div id="app">
    
    

    <v-app id="inspire">
      <!--<h2 align="center">CATALOGO DE ACCESORIOS GAMER</h2>-->
      <v-container class="fill-height" fluid style="min-height: 434px">
        <v-fade-transition mode="out-in">
          <v-row justify="space-around">
            <v-col cols="6" align="center">
              <v-card color="#00ACC1" width="500" align="center">
                <v-carousel
                  cycle
                  height="400"
                  style="width: 800px"
                  hide-delimiter-background
                  show-arrows-on-hover
                >
                  <v-carousel-item
                    v-for="(item, i) in items"
                    :key="i"
                    :src="item.src"
                    contain
                  >
                    <v-row class="fill-height" align="center" justify="center"> </v-row>
                  </v-carousel-item>
                </v-carousel>

                <v-card-title class="justify-center">
                  Tira led 5 metros
                  <br />

                  <div class="text-center">
                    <v-banner class="black--text">
                      Tira Luces Led Bluetooth 5m Control App Usb Impermeable Rgb
                      <br />
                    </v-banner>
                  </div>
                </v-card-title>
                <v-row justify="space-around">
                  <v-col cols="auto">
                    <v-dialog transition="dialog-bottom-transition" max-width="600">
                      <template v-slot:activator="{ on, attrs }">
                        <v-btn color="teal" v-bind="attrs" v-on="on"
                          >ESPECIFICACIONES</v-btn
                        >
                      </template>
                      <template v-slot:default="dialog">
                        <v-card>
                          <v-toolbar color="primary" dark>Especificaciones</v-toolbar>
                          <v-card-text>
                            <div class="text-h6 pa-12">
                              Tira LED Bluetooth 5M, Tira Música RGB 5050 150 LEDs/Música
                              Activada ,Control Musical Inteligente RGB/Tira de Luz para
                              la Decoración del Hogar. <br />
                              NOTA: 1. Este producto solo puede acceder a la fuente de
                              alimentación DC5V. 2.Conecte y use el producto de acuerdo
                              con las instrucciones. La conexión debe conectarse mediante
                              una flecha. 3.Los niños menores de 16 años deben usar el
                              producto bajo la supervisión de un adulto.
                              <br />
                              El paquete incluye: <br />
                              1 X tira de luz <br />
                              1 X controlador bluetooth inteligente <br />
                              1 X instrucción
                            </div>
                          </v-card-text>
                          <v-card-actions class="justify-end">
                            <v-btn text @click="dialog.value = false">Cerrar</v-btn>
                          </v-card-actions>
                        </v-card>
                      </template>
                    </v-dialog>
                  </v-col>

                  <v-col cols="auto">
                    <v-dialog transition="dialog-top-transition" max-width="600">
                      <template v-slot:activator="{ on, attrs }">
                        <v-btn color="teal" v-bind="attrs" v-on="on"> $ PRECIO</v-btn>
                      </template>
                      <template v-slot:default="dialog">
                        <v-card>
                          <v-toolbar color="primary" dark>Precio del articulo</v-toolbar>
                          <v-card-text>
                            <div class="text-h6 pa-12">
                              $ 300 MX. <br />

                              Para mas informacion llamar al numero 923-104-34-57
                              <br />
                              Whatsapp: 923-104-34-57 <br />

                              !Comenta que viste el articulo en la pagina web y ganas 10 %
                              de descuento en tu primer compra¡.
                            </div>
                          </v-card-text>
                          <v-card-actions class="justify-end">
                            <v-btn text @click="dialog.value = false">Cerrar</v-btn>
                          </v-card-actions>
                        </v-card>
                      </template>
                    </v-dialog>
                  </v-col>
                </v-row>
              </v-card>
            </v-col>

            <v-col cols="6" align="center">
              <v-card color="#00ACC1" width="500" align="center">
                <v-carousel
                  cycle
                  height="400"
                  style="width: 800px"
                  hide-delimiter-background
                  show-arrows-on-hover
                >
                  <v-carousel-item
                    v-for="(item, i) in items2"
                    :key="i"
                    :src="item.src"
                    contain
                  >
                    <v-row class="fill-height" align="center" justify="center"> </v-row>
                  </v-carousel-item>
                </v-carousel>

                <v-card-title class="justify-center">
                  Tira led 20 metros
                  <br />

                  <div class="text-center">
                    <v-banner class="black--text">
                      Tira De Luces Led App Bluetooth Control 5050 Rgb 20m (2x10m)
                      <br />
                    </v-banner>
                  </div>
                </v-card-title>
                <v-row justify="space-around">
                  <v-col cols="auto">
                    <v-dialog transition="dialog-bottom-transition" max-width="600">
                      <template v-slot:activator="{ on, attrs }">
                        <v-btn color="teal" v-bind="attrs" v-on="on"
                          >ESPECIFICACIONES</v-btn
                        >
                      </template>
                      <template v-slot:default="dialog">
                        <v-card>
                          <v-toolbar color="primary" dark>Especificaciones</v-toolbar>
                          <v-card-text>
                            <div class="text-h6 pa-12">
                              20 m (2x10 m) led 5050 rgb tira de luces Bluetooth que
                              cambia de color el control de la aplicación viene con
                              control remoto por infrarrojos para la decoración del hogar
                              <br />
                              - Caracteristicas: <br />
                              Tira de luz led de 20m (2x10m) tipo de led: smd5050 (tiene
                              luz blanca) cantidad: 18leds/metro (360led) voltaje de
                              entrada de trabajo: dc12v temperatura de trabajo : -20 60
                              modo de color: rojo, verde, azul, blanco, morado, amarillo,
                              etc.
                              <br />
                              <br />
                              - Lista de empaque: <br />
                              2 x 10 metros de luces de tira led <br />
                              1 x receptor bluetooth <br />
                              1 x 24 teclas de control remoto <br />
                              1 x adaptador de corriente de 12v 20 x hebilla 1 x manual de
                              usuario
                            </div>
                          </v-card-text>
                          <v-card-actions class="justify-end">
                            <v-btn text @click="dialog.value = false">Cerrar</v-btn>
                          </v-card-actions>
                        </v-card>
                      </template>
                    </v-dialog>
                  </v-col>

                  <v-col cols="auto">
                    <v-dialog transition="dialog-top-transition" max-width="600">
                      <template v-slot:activator="{ on, attrs }">
                        <v-btn color="teal" v-bind="attrs" v-on="on"> $ PRECIO</v-btn>
                      </template>
                      <template v-slot:default="dialog">
                        <v-card>
                          <v-toolbar color="primary" dark>Precio del articulo</v-toolbar>
                          <v-card-text>
                            <div class="text-h6 pa-12">
                              $ 650 MX. <br />

                              Para mas informacion llamar al numero 923-104-34-57
                              <br />
                              Whatsapp: 923-104-34-57 <br />

                              !Comenta que viste el articulo en la pagina web y ganas 10 %
                              de descuento en tu primer compra¡.
                            </div>
                          </v-card-text>
                          <v-card-actions class="justify-end">
                            <v-btn text @click="dialog.value = false">Cerrar</v-btn>
                          </v-card-actions>
                        </v-card>
                      </template>
                    </v-dialog>
                  </v-col>
                </v-row>
              </v-card>
            </v-col>

            <v-col cols="6" align="center">
              <v-card color="#00ACC1" width="500" align="center">
                <v-carousel
                  cycle
                  height="400"
                  style="width: 800px"
                  hide-delimiter-background
                  show-arrows-on-hover
                >
                  <v-carousel-item
                    v-for="(item, i) in items3"
                    :key="i"
                    :src="item.src"
                    contain
                  >
                    <v-row class="fill-height" align="center" justify="center"> </v-row>
                  </v-carousel-item>
                </v-carousel>

                <v-card-title class="justify-center">
                  Tira led 10 metros
                  <br />

                  <div class="text-center">
                    <v-banner class="black--text">
                      Tira de luces led wifi trabajo con alexa app control 10m (1x10m)
                      <br />
                    </v-banner>
                  </div>
                </v-card-title>
                <v-row justify="space-around">
                  <v-col cols="auto">
                    <v-dialog transition="dialog-bottom-transition" max-width="600">
                      <template v-slot:activator="{ on, attrs }">
                        <v-btn color="teal" v-bind="attrs" v-on="on"
                          >ESPECIFICACIONES</v-btn
                        >
                      </template>
                      <template v-slot:default="dialog">
                        <v-card>
                          <v-toolbar color="primary" dark>Especificaciones</v-toolbar>
                          <v-card-text>
                            <div class="text-h6 pa-12">
                              Tira de luces led wifi trabajo con alexa app control 10m
                              (1x10m) descripción tira de luces led, wifi inalámbrico
                              controlado por smartphone no impermeable rgb cuerda de luces
                              flexibles 5050smd 24 teclas controlador remoto ir dc12v
                              adaptador de corriente funciona con android ios alexa.
                              <br />

                              Voltaje: 110v/220v <br />
                              Voltaje de funcionamiento: 12V <br />
                              Grado de proteccion: IP20 <br />

                              <br />
                              incluye: <br />
                              1 x 10 metros tira de luz 1 x 24 teclas de control remoto
                              <br />
                              1 x controlador wifi 1 x adaptador de corriente aprobado.
                              <br />
                              conectores de 1 x 1 pines 1 x manual de usuario El paquete
                              <br />
                            </div>
                          </v-card-text>
                          <v-card-actions class="justify-end">
                            <v-btn text @click="dialog.value = false">Cerrar</v-btn>
                          </v-card-actions>
                        </v-card>
                      </template>
                    </v-dialog>
                  </v-col>

                  <v-col cols="auto">
                    <v-dialog transition="dialog-top-transition" max-width="600">
                      <template v-slot:activator="{ on, attrs }">
                        <v-btn color="teal" v-bind="attrs" v-on="on"> $ PRECIO</v-btn>
                      </template>
                      <template v-slot:default="dialog">
                        <v-card>
                          <v-toolbar color="primary" dark>Precio del articulo</v-toolbar>
                          <v-card-text>
                            <div class="text-h6 pa-12">
                              $ 350 MX. <br />

                              Para mas informacion llamar al numero 923-104-34-57
                              <br />
                              Whatsapp: 923-104-34-57 <br />

                              !Comenta que viste el articulo en la pagina web y ganas 10 %
                              de descuento en tu primer compra¡.
                            </div>
                          </v-card-text>
                          <v-card-actions class="justify-end">
                            <v-btn text @click="dialog.value = false">Cerrar</v-btn>
                          </v-card-actions>
                        </v-card>
                      </template>
                    </v-dialog>
                  </v-col>
                </v-row>
              </v-card>
            </v-col>

            <v-col cols="6" align="center">
              <v-card color="#00ACC1" width="500" align="center">
                <v-carousel
                  cycle
                  height="400"
                  style="width: 800px"
                  hide-delimiter-background
                  show-arrows-on-hover
                >
                  <v-carousel-item
                    v-for="(item, i) in items4"
                    :key="i"
                    :src="item.src"
                    contain
                  >
                    <v-row class="fill-height" align="center" justify="center"> </v-row>
                  </v-carousel-item>
                </v-carousel>

                <v-card-title class="justify-center">
                  Audifonos Gamer
                  <br />

                  <div class="text-center">
                    <v-banner class="black--text">
                      Audífonos gamer Kotion Each G9000 black y blue <br />
                    </v-banner>
                  </div>
                </v-card-title>
                <v-row justify="space-around">
                  <v-col cols="auto">
                    <v-dialog transition="dialog-bottom-transition" max-width="600">
                      <template v-slot:activator="{ on, attrs }">
                        <v-btn color="teal" v-bind="attrs" v-on="on"
                          >ESPECIFICACIONES</v-btn
                        >
                      </template>
                      <template v-slot:default="dialog">
                        <v-card>
                          <v-toolbar color="primary" dark>Especificaciones</v-toolbar>
                          <v-card-text>
                            <div class="text-h6 pa-12">
                              ¡Experimenta la adrenalina de sumergirte en la escena de
                              otra manera! Tener auriculares específicos para jugar cambia
                              completamente tu experiencia en cada partida. Con los Kotion
                              G9000 no te pierdes ningún detalle y escuchas el audio tal y
                              como fue diseñado por los creadores. El formato perfecto
                              para ti El diseño over-ear genera una comodidad insuperable
                              gracias a sus suaves almohadillas. Al mismo tiempo, su
                              sonido envolvente del más alto nivel se convierte en el
                              protagonista de la escena.. <br />

                              - Caracteristicas--------------------- <br />
                              -Largo del cable: 2.2 m <br />
                              -Con cable desmontable: No <br />
                              -Consolas de videojuegos compatibles: PS4<br />
                              -Es inalámbrico: No <br />
                              -Con Bluetooth: No <br />
                              -Con tecnología TWS: No<br />
                              -Tipo de conector: Jack 3.5 mm<br />
                            </div>
                          </v-card-text>
                          <v-card-actions class="justify-end">
                            <v-btn text @click="dialog.value = false">Cerrar</v-btn>
                          </v-card-actions>
                        </v-card>
                      </template>
                    </v-dialog>
                  </v-col>

                  <v-col cols="auto">
                    <v-dialog transition="dialog-top-transition" max-width="600">
                      <template v-slot:activator="{ on, attrs }">
                        <v-btn color="teal" v-bind="attrs" v-on="on"> $ PRECIO</v-btn>
                      </template>
                      <template v-slot:default="dialog">
                        <v-card>
                          <v-toolbar color="primary" dark>Precio del articulo</v-toolbar>
                          <v-card-text>
                            <div class="text-h6 pa-12">
                              $ 380 MX. <br />

                              Para mas informacion llamar al numero 923-104-34-57
                              <br />
                              Whatsapp: 923-104-34-57 <br />

                              !Comenta que viste el articulo en la pagina web y ganas 10 %
                              de descuento en tu primer compra¡.
                            </div>
                          </v-card-text>
                          <v-card-actions class="justify-end">
                            <v-btn text @click="dialog.value = false">Cerrar</v-btn>
                          </v-card-actions>
                        </v-card>
                      </template>
                    </v-dialog>
                  </v-col>
                </v-row>
              </v-card>
            </v-col>

            <v-col cols="6" align="center">
              <v-card color="#00ACC1" width="500" align="center">
                <v-carousel
                  cycle
                  height="400"
                  style="width: 800px"
                  hide-delimiter-background
                  show-arrows-on-hover
                >
                  <v-carousel-item
                    v-for="(item, i) in items5"
                    :key="i"
                    :src="item.src"
                    contain
                  >
                    <v-row class="fill-height" align="center" justify="center"> </v-row>
                  </v-carousel-item>
                </v-carousel>

                <v-card-title class="justify-center">
                  Audífonos Onikuma
                  <br />

                  <div class="text-center">
                    <v-banner class="black--text">
                      Audífonos Gamer Onikuma K19 con luz rgb LED <br />
                    </v-banner>
                  </div>
                </v-card-title>
                <v-row justify="space-around">
                  <v-col cols="auto">
                    <v-dialog transition="dialog-bottom-transition" max-width="600">
                      <template v-slot:activator="{ on, attrs }">
                        <v-btn color="teal" v-bind="attrs" v-on="on"
                          >ESPECIFICACIONES</v-btn
                        >
                      </template>
                      <template v-slot:default="dialog">
                        <v-card>
                          <v-toolbar color="primary" dark>Especificaciones</v-toolbar>
                          <v-card-text>
                            <div class="text-h6 pa-12">
                              ¡Experimenta la adrenalina de sumergirte en la escena de
                              otra manera! Tener auriculares específicos para jugar cambia
                              completamente tu experiencia en cada partida. Con los
                              Onikuma K19 no te pierdes ningún detalle y escuchas el audio
                              tal y como fue diseñado por los creadores. El formato
                              perfecto para ti El diseño over-ear genera una comodidad
                              insuperable gracias a sus suaves almohadillas. Al mismo
                              tiempo, su sonido envolvente del más alto nivel se convierte
                              en el protagonista de la escena. <br />
                              <br />
                              -Caracteristicas--------------------- <br />
                              -Es inalambrico: No <br />
                              -Con microfono: Si <br />
                              -Con iluminaciòn led: Si <br />
                              -Cancelaciòn de ruido: Si <br />
                            </div>
                          </v-card-text>
                          <v-card-actions class="justify-end">
                            <v-btn text @click="dialog.value = false">Cerrar</v-btn>
                          </v-card-actions>
                        </v-card>
                      </template>
                    </v-dialog>
                  </v-col>

                  <v-col cols="auto">
                    <v-dialog transition="dialog-top-transition" max-width="600">
                      <template v-slot:activator="{ on, attrs }">
                        <v-btn color="teal" v-bind="attrs" v-on="on"> $ PRECIO</v-btn>
                      </template>
                      <template v-slot:default="dialog">
                        <v-card>
                          <v-toolbar color="primary" dark>Precio del articulo</v-toolbar>
                          <v-card-text>
                            <div class="text-h6 pa-12">
                              $ 480 MX. <br />

                              Para mas informacion llamar al numero 923-104-34-57
                              <br />
                              Whatsapp: 923-104-34-57 <br />

                              !Comenta que viste el articulo en la pagina web y ganas 10 %
                              de descuento en tu primer compra¡.
                            </div>
                          </v-card-text>
                          <v-card-actions class="justify-end">
                            <v-btn text @click="dialog.value = false">Cerrar</v-btn>
                          </v-card-actions>
                        </v-card>
                      </template>
                    </v-dialog>
                  </v-col>
                </v-row>
              </v-card>
            </v-col>

            <v-col cols="6" align="center">
              <v-card color="#00ACC1" width="500" align="center">
                <v-carousel
                  cycle
                  height="400"
                  style="width: 800px"
                  hide-delimiter-background
                  show-arrows-on-hover
                >
                  <v-carousel-item
                    v-for="(item, i) in items6"
                    :key="i"
                    :src="item.src"
                    contain
                  >
                    <v-row class="fill-height" align="center" justify="center"> </v-row>
                  </v-carousel-item>
                </v-carousel>

                <v-card-title class="justify-center">
                  Audifonos Gamer
                  <br />

                  <div class="text-center">
                    <v-banner class="black--text">
                      Onikuma K19 camuflaje gris con luz rgb LED <br />
                    </v-banner>
                  </div>
                </v-card-title>
                <v-row justify="space-around">
                  <v-col cols="auto">
                    <v-dialog transition="dialog-bottom-transition" max-width="600">
                      <template v-slot:activator="{ on, attrs }">
                        <v-btn color="teal" v-bind="attrs" v-on="on"
                          >ESPECIFICACIONES</v-btn
                        >
                      </template>
                      <template v-slot:default="dialog">
                        <v-card>
                          <v-toolbar color="primary" dark>Especificaciones</v-toolbar>
                          <v-card-text>
                            <div class="text-h6 pa-12">
                              ¡Experimenta la adrenalina de sumergirte en la escena de
                              otra manera! Tener auriculares específicos para jugar cambia
                              completamente tu experiencia en cada partida. Con los
                              Onikuma K19 no te pierdes ningún detalle y escuchas el audio
                              tal y como fue diseñado por los creadores. El formato
                              perfecto para ti El diseño over-ear genera una comodidad
                              insuperable gracias a sus suaves almohadillas. Al mismo
                              tiempo, su sonido envolvente del más alto nivel se convierte
                              en el protagonista de la escena.. <br />
                              <br />
                              -Caracteristicas--------------------- <br />
                              -Es inalambrico: No <br />
                              -Con microfono: Si <br />
                              -Con iluminaciòn led: Si <br />
                              -Cancelaciòn de ruido: Si <br />
                              -Consolas de videojuegos compatibles: Xbox One y PS4
                              <br />
                            </div>
                          </v-card-text>
                          <v-card-actions class="justify-end">
                            <v-btn text @click="dialog.value = false">Cerrar</v-btn>
                          </v-card-actions>
                        </v-card>
                      </template>
                    </v-dialog>
                  </v-col>

                  <v-col cols="auto">
                    <v-dialog transition="dialog-top-transition" max-width="600">
                      <template v-slot:activator="{ on, attrs }">
                        <v-btn color="teal" v-bind="attrs" v-on="on"> $ PRECIO</v-btn>
                      </template>
                      <template v-slot:default="dialog">
                        <v-card>
                          <v-toolbar color="primary" dark>Precio del articulo</v-toolbar>
                          <v-card-text>
                            <div class="text-h6 pa-12">
                              $ 760 MX. <br />

                              Para mas informacion llamar al numero 923-104-34-57
                              <br />
                              Whatsapp: 923-104-34-57 <br />

                              !Comenta que viste el articulo en la pagina web y ganas 10 %
                              de descuento en tu primer compra¡.
                            </div>
                          </v-card-text>
                          <v-card-actions class="justify-end">
                            <v-btn text @click="dialog.value = false">Cerrar</v-btn>
                          </v-card-actions>
                        </v-card>
                      </template>
                    </v-dialog>
                  </v-col>
                </v-row>
              </v-card>
            </v-col>

            <v-col cols="6" align="center">
              <v-card color="#00ACC1" width="500" align="center">
                <v-carousel
                  cycle
                  height="400"
                  style="width: 800px"
                  hide-delimiter-background
                  show-arrows-on-hover
                >
                  <v-carousel-item
                    v-for="(item, i) in items"
                    :key="i"
                    :src="item.src"
                    contain
                  >
                    <v-row class="fill-height" align="center" justify="center"> </v-row>
                  </v-carousel-item>
                </v-carousel>

                <v-card-title class="justify-center">
                  Tira led 5 metros
                  <br />

                  <div class="text-center">
                    <v-banner class="black--text">
                      Tira Luces Led Bluetooth 5m Control App Usb Impermeable Rgb
                      <br />
                    </v-banner>
                  </div>
                </v-card-title>
                <v-row justify="space-around">
                  <v-col cols="auto">
                    <v-dialog transition="dialog-bottom-transition" max-width="600">
                      <template v-slot:activator="{ on, attrs }">
                        <v-btn color="teal" v-bind="attrs" v-on="on"
                          >ESPECIFICACIONES</v-btn
                        >
                      </template>
                      <template v-slot:default="dialog">
                        <v-card>
                          <v-toolbar color="primary" dark>Especificaciones</v-toolbar>
                          <v-card-text>
                            <div class="text-h6 pa-12">
                              Tira LED Bluetooth 5M, Tira Música RGB 5050 150 LEDs/Música
                              Activada ,Control Musical Inteligente RGB/Tira de Luz para
                              la Decoración del Hogar. <br />
                              NOTA: 1. Este producto solo puede acceder a la fuente de
                              alimentación DC5V. 2.Conecte y use el producto de acuerdo
                              con las instrucciones. La conexión debe conectarse mediante
                              una flecha. 3.Los niños menores de 16 años deben usar el
                              producto bajo la supervisión de un adulto.
                              <br />
                              El paquete incluye: <br />
                              1 X tira de luz <br />
                              1 X controlador bluetooth inteligente <br />
                              1 X instrucción
                            </div>
                          </v-card-text>
                          <v-card-actions class="justify-end">
                            <v-btn text @click="dialog.value = false">Cerrar</v-btn>
                          </v-card-actions>
                        </v-card>
                      </template>
                    </v-dialog>
                  </v-col>

                  <v-col cols="auto">
                    <v-dialog transition="dialog-top-transition" max-width="600">
                      <template v-slot:activator="{ on, attrs }">
                        <v-btn color="teal" v-bind="attrs" v-on="on"> $ PRECIO</v-btn>
                      </template>
                      <template v-slot:default="dialog">
                        <v-card>
                          <v-toolbar color="primary" dark>Precio del articulo</v-toolbar>
                          <v-card-text>
                            <div class="text-h6 pa-12">
                              $ 300 Mx. <br />

                              Para mas informacion llamar al numero 923-104-34-57
                              <br />
                              Whatsapp: 923-104-34-57 <br />

                              !Comenta que viste el articulo en la pagina web y ganas 10 %
                              de descuento en tu primer compra¡.
                            </div>
                          </v-card-text>
                          <v-card-actions class="justify-end">
                            <v-btn text @click="dialog.value = false">Cerrar</v-btn>
                          </v-card-actions>
                        </v-card>
                      </template>
                    </v-dialog>
                  </v-col>
                </v-row>
              </v-card>
            </v-col>

            <v-col cols="6" align="center">
              <v-card color="#00ACC1" width="500" align="center">
                <v-carousel
                  cycle
                  height="400"
                  style="width: 800px"
                  hide-delimiter-background
                  show-arrows-on-hover
                >
                  <v-carousel-item
                    v-for="(item, i) in items"
                    :key="i"
                    :src="item.src"
                    contain
                  >
                    <v-row class="fill-height" align="center" justify="center"> </v-row>
                  </v-carousel-item>
                </v-carousel>

                <v-card-title class="justify-center">
                  Tira led 5 metros
                  <br />

                  <div class="text-center">
                    <v-banner class="black--text">
                      Tira Luces Led Bluetooth 5m Control App Usb Impermeable Rgb
                      <br />
                    </v-banner>
                  </div>
                </v-card-title>
                <v-row justify="space-around">
                  <v-col cols="auto">
                    <v-dialog transition="dialog-bottom-transition" max-width="600">
                      <template v-slot:activator="{ on, attrs }">
                        <v-btn color="teal" v-bind="attrs" v-on="on"
                          >ESPECIFICACIONES</v-btn
                        >
                      </template>
                      <template v-slot:default="dialog">
                        <v-card>
                          <v-toolbar color="primary" dark>Especificaciones</v-toolbar>
                          <v-card-text>
                            <div class="text-h6 pa-12">
                              Tira LED Bluetooth 5M, Tira Música RGB 5050 150 LEDs/Música
                              Activada ,Control Musical Inteligente RGB/Tira de Luz para
                              la Decoración del Hogar. <br />
                              NOTA: 1. Este producto solo puede acceder a la fuente de
                              alimentación DC5V. 2.Conecte y use el producto de acuerdo
                              con las instrucciones. La conexión debe conectarse mediante
                              una flecha. 3.Los niños menores de 16 años deben usar el
                              producto bajo la supervisión de un adulto.
                              <br />
                              El paquete incluye: <br />
                              1 X tira de luz <br />
                              1 X controlador bluetooth inteligente <br />
                              1 X instrucción
                            </div>
                          </v-card-text>
                          <v-card-actions class="justify-end">
                            <v-btn text @click="dialog.value = false">Cerrar</v-btn>
                          </v-card-actions>
                        </v-card>
                      </template>
                    </v-dialog>
                  </v-col>

                  <v-col cols="auto">
                    <v-dialog transition="dialog-top-transition" max-width="600">
                      <template v-slot:activator="{ on, attrs }">
                        <v-btn color="teal" v-bind="attrs" v-on="on"> $ PRECIO</v-btn>
                      </template>
                      <template v-slot:default="dialog">
                        <v-card>
                          <v-toolbar color="primary" dark>Precio del articulo</v-toolbar>
                          <v-card-text>
                            <div class="text-h6 pa-12">
                              $ 300 Mx. <br />

                              Para mas informacion llamar al numero 923-104-34-57
                              <br />
                              Whatsapp: 923-104-34-57 <br />

                              !Comenta que viste el articulo en la pagina web y ganas 10 %
                              de descuento en tu primer compra¡.
                            </div>
                          </v-card-text>
                          <v-card-actions class="justify-end">
                            <v-btn text @click="dialog.value = false">Cerrar</v-btn>
                          </v-card-actions>
                        </v-card>
                      </template>
                    </v-dialog>
                  </v-col>
                </v-row>
              </v-card>
            </v-col>

            <v-col cols="6" align="center">
              <v-card color="#00ACC1" width="500" align="center">
                <v-carousel
                  cycle
                  height="400"
                  style="width: 800px"
                  hide-delimiter-background
                  show-arrows-on-hover
                >
                  <v-carousel-item
                    v-for="(item, i) in items"
                    :key="i"
                    :src="item.src"
                    contain
                  >
                    <v-row class="fill-height" align="center" justify="center"> </v-row>
                  </v-carousel-item>
                </v-carousel>

                <v-card-title class="justify-center">
                  Tira led 5 metros
                  <br />

                  <div class="text-center">
                    <v-banner class="black--text">
                      Tira Luces Led Bluetooth 5m Control App Usb Impermeable Rgb
                      <br />
                    </v-banner>
                  </div>
                </v-card-title>
                <v-row justify="space-around">
                  <v-col cols="auto">
                    <v-dialog transition="dialog-bottom-transition" max-width="600">
                      <template v-slot:activator="{ on, attrs }">
                        <v-btn color="teal" v-bind="attrs" v-on="on"
                          >ESPECIFICACIONES</v-btn
                        >
                      </template>
                      <template v-slot:default="dialog">
                        <v-card>
                          <v-toolbar color="primary" dark>Especificaciones</v-toolbar>
                          <v-card-text>
                            <div class="text-h6 pa-12">
                              Tira LED Bluetooth 5M, Tira Música RGB 5050 150 LEDs/Música
                              Activada ,Control Musical Inteligente RGB/Tira de Luz para
                              la Decoración del Hogar. <br />
                              NOTA: 1. Este producto solo puede acceder a la fuente de
                              alimentación DC5V. 2.Conecte y use el producto de acuerdo
                              con las instrucciones. La conexión debe conectarse mediante
                              una flecha. 3.Los niños menores de 16 años deben usar el
                              producto bajo la supervisión de un adulto.
                              <br />
                              El paquete incluye: <br />
                              1 X tira de luz <br />
                              1 X controlador bluetooth inteligente <br />
                              1 X instrucción
                            </div>
                          </v-card-text>
                          <v-card-actions class="justify-end">
                            <v-btn text @click="dialog.value = false">Cerrar</v-btn>
                          </v-card-actions>
                        </v-card>
                      </template>
                    </v-dialog>
                  </v-col>

                  <v-col cols="auto">
                    <v-dialog transition="dialog-top-transition" max-width="600">
                      <template v-slot:activator="{ on, attrs }">
                        <v-btn color="teal" v-bind="attrs" v-on="on"> $ PRECIO</v-btn>
                      </template>
                      <template v-slot:default="dialog">
                        <v-card>
                          <v-toolbar color="primary" dark>Precio del articulo</v-toolbar>
                          <v-card-text>
                            <div class="text-h6 pa-12">
                              $ 300 Mx. <br />

                              Para mas informacion llamar al numero 923-104-34-57
                              <br />
                              Whatsapp: 923-104-34-57 <br />

                              !Comenta que viste el articulo en la pagina web y ganas 10 %
                              de descuento en tu primer compra¡.
                            </div>
                          </v-card-text>
                          <v-card-actions class="justify-end">
                            <v-btn text @click="dialog.value = false">Cerrar</v-btn>
                          </v-card-actions>
                        </v-card>
                      </template>
                    </v-dialog>
                  </v-col>
                </v-row>
              </v-card>
            </v-col>

            <v-col cols="6" align="center">
              <v-card color="#00ACC1" width="500" align="center">
                <v-carousel
                  cycle
                  height="400"
                  style="width: 800px"
                  hide-delimiter-background
                  show-arrows-on-hover
                >
                  <v-carousel-item
                    v-for="(item, i) in items"
                    :key="i"
                    :src="item.src"
                    contain
                  >
                    <v-row class="fill-height" align="center" justify="center"> </v-row>
                  </v-carousel-item>
                </v-carousel>

                <v-card-title class="justify-center">
                  Tira led 5 metros
                  <br />

                  <div class="text-center">
                    <v-banner class="black--text">
                      Tira Luces Led Bluetooth 5m Control App Usb Impermeable Rgb
                      <br />
                    </v-banner>
                  </div>
                </v-card-title>
                <v-row justify="space-around">
                  <v-col cols="auto">
                    <v-dialog transition="dialog-bottom-transition" max-width="600">
                      <template v-slot:activator="{ on, attrs }">
                        <v-btn color="teal" v-bind="attrs" v-on="on"
                          >ESPECIFICACIONES</v-btn
                        >
                      </template>
                      <template v-slot:default="dialog">
                        <v-card>
                          <v-toolbar color="primary" dark>Especificaciones</v-toolbar>
                          <v-card-text>
                            <div class="text-h6 pa-12">
                              Tira LED Bluetooth 5M, Tira Música RGB 5050 150 LEDs/Música
                              Activada ,Control Musical Inteligente RGB/Tira de Luz para
                              la Decoración del Hogar. <br />
                              NOTA: 1. Este producto solo puede acceder a la fuente de
                              alimentación DC5V. 2.Conecte y use el producto de acuerdo
                              con las instrucciones. La conexión debe conectarse mediante
                              una flecha. 3.Los niños menores de 16 años deben usar el
                              producto bajo la supervisión de un adulto.
                              <br />
                              El paquete incluye: <br />
                              1 X tira de luz <br />
                              1 X controlador bluetooth inteligente <br />
                              1 X instrucción
                            </div>
                          </v-card-text>
                          <v-card-actions class="justify-end">
                            <v-btn text @click="dialog.value = false">Cerrar</v-btn>
                          </v-card-actions>
                        </v-card>
                      </template>
                    </v-dialog>
                  </v-col>

                  <v-col cols="auto">
                    <v-dialog transition="dialog-top-transition" max-width="600">
                      <template v-slot:activator="{ on, attrs }">
                        <v-btn color="teal" v-bind="attrs" v-on="on"> $ PRECIO</v-btn>
                      </template>
                      <template v-slot:default="dialog">
                        <v-card>
                          <v-toolbar color="primary" dark>Precio del articulo</v-toolbar>
                          <v-card-text>
                            <div class="text-h6 pa-12">
                              $ 300 Mx. <br />

                              Para mas informacion llamar al numero 923-104-34-57
                              <br />
                              Whatsapp: 923-104-34-57 <br />

                              !Comenta que viste el articulo en la pagina web y ganas 10 %
                              de descuento en tu primer compra¡.
                            </div>
                          </v-card-text>
                          <v-card-actions class="justify-end">
                            <v-btn text @click="dialog.value = false">Cerrar</v-btn>
                          </v-card-actions>
                        </v-card>
                      </template>
                    </v-dialog>
                  </v-col>
                </v-row>
              </v-card>
            </v-col>

            <v-col cols="6" align="center">
              <v-card color="#00ACC1" width="500" align="center">
                <v-carousel
                  cycle
                  height="400"
                  style="width: 800px"
                  hide-delimiter-background
                  show-arrows-on-hover
                >
                  <v-carousel-item
                    v-for="(item, i) in items"
                    :key="i"
                    :src="item.src"
                    contain
                  >
                    <v-row class="fill-height" align="center" justify="center"> </v-row>
                  </v-carousel-item>
                </v-carousel>

                <v-card-title class="justify-center">
                  Tira led 5 metros
                  <br />

                  <div class="text-center">
                    <v-banner class="black--text">
                      Tira Luces Led Bluetooth 5m Control App Usb Impermeable Rgb
                      <br />
                    </v-banner>
                  </div>
                </v-card-title>
                <v-row justify="space-around">
                  <v-col cols="auto">
                    <v-dialog transition="dialog-bottom-transition" max-width="600">
                      <template v-slot:activator="{ on, attrs }">
                        <v-btn color="teal" v-bind="attrs" v-on="on"
                          >ESPECIFICACIONES</v-btn
                        >
                      </template>
                      <template v-slot:default="dialog">
                        <v-card>
                          <v-toolbar color="primary" dark>Especificaciones</v-toolbar>
                          <v-card-text>
                            <div class="text-h6 pa-12">
                              Tira LED Bluetooth 5M, Tira Música RGB 5050 150 LEDs/Música
                              Activada ,Control Musical Inteligente RGB/Tira de Luz para
                              la Decoración del Hogar. <br />
                              NOTA: 1. Este producto solo puede acceder a la fuente de
                              alimentación DC5V. 2.Conecte y use el producto de acuerdo
                              con las instrucciones. La conexión debe conectarse mediante
                              una flecha. 3.Los niños menores de 16 años deben usar el
                              producto bajo la supervisión de un adulto.
                              <br />
                              El paquete incluye: <br />
                              1 X tira de luz <br />
                              1 X controlador bluetooth inteligente <br />
                              1 X instrucción
                            </div>
                          </v-card-text>
                          <v-card-actions class="justify-end">
                            <v-btn text @click="dialog.value = false">Cerrar</v-btn>
                          </v-card-actions>
                        </v-card>
                      </template>
                    </v-dialog>
                  </v-col>

                  <v-col cols="auto">
                    <v-dialog transition="dialog-top-transition" max-width="600">
                      <template v-slot:activator="{ on, attrs }">
                        <v-btn color="teal" v-bind="attrs" v-on="on"> $ PRECIO</v-btn>
                      </template>
                      <template v-slot:default="dialog">
                        <v-card>
                          <v-toolbar color="primary" dark>Precio del articulo</v-toolbar>
                          <v-card-text>
                            <div class="text-h6 pa-12">
                              $ 300 Mx. <br />

                              Para mas informacion llamar al numero 923-104-34-57
                              <br />
                              Whatsapp: 923-104-34-57 <br />

                              !Comenta que viste el articulo en la pagina web y ganas 10 %
                              de descuento en tu primer compra¡.
                            </div>
                          </v-card-text>
                          <v-card-actions class="justify-end">
                            <v-btn text @click="dialog.value = false">Cerrar</v-btn>
                          </v-card-actions>
                        </v-card>
                      </template>
                    </v-dialog>
                  </v-col>
                </v-row>
              </v-card>
            </v-col>

            <v-col cols="6" align="center">
              <v-card color="#00ACC1" width="500" align="center">
                <v-carousel
                  cycle
                  height="400"
                  style="width: 800px"
                  hide-delimiter-background
                  show-arrows-on-hover
                >
                  <v-carousel-item
                    v-for="(item, i) in items"
                    :key="i"
                    :src="item.src"
                    contain
                  >
                    <v-row class="fill-height" align="center" justify="center"> </v-row>
                  </v-carousel-item>
                </v-carousel>

                <v-card-title class="justify-center">
                  Tira led 5 metros
                  <br />

                  <div class="text-center">
                    <v-banner class="black--text">
                      Tira Luces Led Bluetooth 5m Control App Usb Impermeable Rgb
                      <br />
                    </v-banner>
                  </div>
                </v-card-title>
                <v-row justify="space-around">
                  <v-col cols="auto">
                    <v-dialog transition="dialog-bottom-transition" max-width="600">
                      <template v-slot:activator="{ on, attrs }">
                        <v-btn color="teal" v-bind="attrs" v-on="on"
                          >ESPECIFICACIONES</v-btn
                        >
                      </template>
                      <template v-slot:default="dialog">
                        <v-card>
                          <v-toolbar color="primary" dark>Especificaciones</v-toolbar>
                          <v-card-text>
                            <div class="text-h6 pa-12">
                              Tira LED Bluetooth 5M, Tira Música RGB 5050 150 LEDs/Música
                              Activada ,Control Musical Inteligente RGB/Tira de Luz para
                              la Decoración del Hogar. <br />
                              NOTA: 1. Este producto solo puede acceder a la fuente de
                              alimentación DC5V. 2.Conecte y use el producto de acuerdo
                              con las instrucciones. La conexión debe conectarse mediante
                              una flecha. 3.Los niños menores de 16 años deben usar el
                              producto bajo la supervisión de un adulto.
                              <br />
                              El paquete incluye: <br />
                              1 X tira de luz <br />
                              1 X controlador bluetooth inteligente <br />
                              1 X instrucción
                            </div>
                          </v-card-text>
                          <v-card-actions class="justify-end">
                            <v-btn text @click="dialog.value = false">Cerrar</v-btn>
                          </v-card-actions>
                        </v-card>
                      </template>
                    </v-dialog>
                  </v-col>

                  <v-col cols="auto">
                    <v-dialog transition="dialog-top-transition" max-width="600">
                      <template v-slot:activator="{ on, attrs }">
                        <v-btn color="teal" v-bind="attrs" v-on="on"> $ PRECIO</v-btn>
                      </template>
                      <template v-slot:default="dialog">
                        <v-card>
                          <v-toolbar color="primary" dark>Precio del articulo</v-toolbar>
                          <v-card-text>
                            <div class="text-h6 pa-12">
                              $ 300 Mx. <br />

                              Para mas informacion llamar al numero 923-104-34-57
                              <br />
                              Whatsapp: 923-104-34-57 <br />

                              !Comenta que viste el articulo en la pagina web y ganas 10 %
                              de descuento en tu primer compra¡.
                            </div>
                          </v-card-text>
                          <v-card-actions class="justify-end">
                            <v-btn text @click="dialog.value = false">Cerrar</v-btn>
                          </v-card-actions>
                        </v-card>
                      </template>
                    </v-dialog>
                  </v-col>
                </v-row>
              </v-card>
            </v-col>
          </v-row>
        </v-fade-transition>
      </v-container>
    </v-app>
  </div>
</template>



<script>
export default {
  name: "CatalogoImagenes",


  data() {
    return {
      
      items: [
        {
          src: require("../assets/accesorios/tira/tira5.png"),
        },
        {
          src: require("../assets/accesorios/tira/tira5_1.png"),
        },
        {
          src: require("../assets/accesorios/tira/tira20_2.png"),
        },
      ],

      items2: [
        {
          src: require("../assets/accesorios/tira/tira20.png"),
        },
        {
          src: require("../assets/accesorios/tira/tira20_1.png"),
        },
        {
          src: require("../assets/accesorios/tira/tira20_2.png"),
        },
      ],

      items3: [
        {
          src: require("../assets/accesorios/tira/tira10.png"),
        },
        {
          src: require("../assets/accesorios/tira/tira10_1.png"),
        },
        {
          src: require("../assets/accesorios/tira/tira10_2.png"),
        },
      ],

      items4: [
        {
          src: require("../assets/accesorios/audifonos/audifonos_cotion.png"),
        },
        {
          src: require("../assets/accesorios/audifonos/audifonos_cotion_1.png"),
        },
        {
          src: require("../assets/accesorios/audifonos/audifonos.png"),
        },
      ],

      items5: [
        {
          src: require("../assets/accesorios/audifonos/audifonos_onikuma.png"),
        },
        {
          src: require("../assets/accesorios/audifonos/audifonos_onikuma_1.png"),
        },
        {
          src: require("../assets/accesorios/audifonos/audifonos2.png"),
        },
      ],

      items6: [
        {
          src: require("../assets/accesorios/audifonos/audifonos_onikumak19.png"),
        },
        {
          src: require("../assets/accesorios/audifonos/audifonos_onikumak19_1.png"),
        },
        {
          src: require("../assets/accesorios/audifonos/audifonos_onikumak19_2.png"),
        },
      ],

      items7: [
        {
          src: require("../assets/accesorios/tira/tira10.png"),
        },
        {
          src: require("../assets/accesorios/tira/tira10.png"),
        },
        {
          src: require("../assets/accesorios/tira/tira10.png"),
        },
      ],

      items8: [
        {
          src: require("../assets/accesorios/tira/tira10.png"),
        },
        {
          src: require("../assets/accesorios/tira/tira10.png"),
        },
        {
          src: require("../assets/accesorios/tira/tira10.png"),
        },
      ],

      items9: [
        {
          src: require("../assets/accesorios/tira/tira10.png"),
        },
        {
          src: require("../assets/accesorios/tira/tira10.png"),
        },
        {
          src: require("../assets/accesorios/tira/tira10.png"),
        },
      ],

      items10: [
        {
          src: require("../assets/accesorios/tira/tira10.png"),
        },
        {
          src: require("../assets/accesorios/tira/tira10.png"),
        },
        {
          src: require("../assets/accesorios/tira/tira10.png"),
        },
      ],

      drawer: false,
      group: null,

      watch: {
        group() {
          this.drawer = false;
        },
      },
    };
  },
  



};

</script>

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
  background-color: #d3914f;
}
/*
#inspire {
  background-color: #009688;
}*/

h2 {
  color: white;
  font-size: 30px;
}

pre {
  width: 100%;
  border: solid;
}
</style>
