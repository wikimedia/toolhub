import Vue from 'vue';
import Vuex from 'vuex';
import UserModule from './user';
import ToolsModule from './tools';

Vue.use( Vuex );

export default new Vuex.Store( {
	modules: {
		user: UserModule,
		tools: ToolsModule
	},
	// Strict mode in development/testing, but disabled for performance in prod
	strict: process.env.NODE_ENV !== 'production'
} );
