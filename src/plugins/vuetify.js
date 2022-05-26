import Vue from 'vue';
import Vuetify from 'vuetify';
import 'vuetify/dist/vuetify.min.css';
import colors from 'vuetify/lib/util/colors'




Vue.use(Vuetify);





/* Este es el color para los fondos */


export default new Vuetify({
    theme: {
        options: {
            customProperties: true,
        },
        themes: {
            light: {
                background: '#FF5252',
            },
        },
        dark: true,
    },
});