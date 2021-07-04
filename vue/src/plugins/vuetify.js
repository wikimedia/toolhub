import '@mdi/font/css/materialdesignicons.css';
import Vue from 'vue';
import Vuetify from 'vuetify/lib';

Vue.use( Vuetify );

export default new Vuetify( {
	theme: {
		options: {
			customProperties: true
		},
		themes: {
			light: {
				primary: '#1976D2',
				secondary: '#424242',
				base90: '#f8f9fa',
				accent: '#F4F4F4',
				error: '#FF5252',
				info: '#2196F3',
				success: '#4CAF50',
				warning: '#FFC107',
				bgtext: '#FFFFFF'
			}
		}
	}
} );
