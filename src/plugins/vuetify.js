import Vue from 'vue';
import Vuetify from 'vuetify';
import 'vuetify/dist/vuetify.min.css';
import colors from 'vuetify/lib/util/colors'



Vue.use(Vuetify);

/* 
ESTE ES EL ORIGINAL DE VUE
export default new Vuetify({
    theme: {
        options: {
            customProperties: true,
        },
        themes: {
            light: {
                primary: '#007BFF',
                secondary: '#424242',
                accent: '#82B1FF',
                error: '#FF5252',
                info: '#2196F3',
                success: '#4CAF50',
                warning: '#FFC107',

            },
        },
    },
});

*/

/* Este es el color para los fondos */
export default new Vuetify({
    theme: {
        options: {
            customProperties: true,
        },
        themes: {
            dark: {
                background: '#292930',
            },
        },
        dark: true,
    },
});