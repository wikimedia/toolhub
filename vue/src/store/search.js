import Vue from 'vue';
import Vuex from 'vuex';

import i18n from '@/plugins/i18n';
import { makeApiCall, getFailurePayload } from '@/plugins/swagger';

Vue.use( Vuex );

/**
 * Generate facet data suitable for use by @/components/search/Filters from
 * a backend API search response.
 *
 * @param {Object} results - backend API response body
 * @param {string[][]} filters - filters added to query
 * @return {Object[]} facet descriptions
 */
export function extractFacets( results, filters ) {
	const facets = [];
	for ( const rawName in results.facets ) {
		if ( !rawName.startsWith( '_filter_' ) ) {
			continue;
		}
		const data = results.facets[ rawName ];
		const name = rawName.substring( 8 );
		const facet = data[ name ];
		facets.push( {
			name: name,
			type: facet.meta.type,
			multi: facet.meta.multi,
			param: facet.meta.param,
			missingValue: facet.meta.missing_value,
			missingParam: facet.meta.missing_param,
			docCount: data.doc_count,
			otherCount: facet.sum_other_doc_count,
			buckets: facet.buckets.sort( ( a ) =>
				// Push missing value buckets to the end of the list
				a.key === facet.meta.missing_value ? 1 : 0
			),
			selected: filters.reduce( ( acc, val ) => {
				if ( val[ 0 ] === facet.meta.param ) {
					acc.push( val[ 1 ] );
				}
				if ( val[ 0 ] === facet.meta.missing_param ) {
					acc.push( facet.meta.missing_value );
				}
				return acc;
			}, [] )
		} );
	}
	return facets;
}

export const getters = { };

export const actions = {
	/**
	 * Search for tools.
	 *
	 * @param {Object} context - Vuex context
	 * @param {Object} payload
	 * @param {string} payload.query - user provided query
	 * @param {number} payload.page - page number within results
	 * @param {number} payload.pageSize - number of tools per page
	 * @param {string} payload.ordering - Sort order
	 * @param {string[][]} payload.filters - filters to add to query
	 * @return {Promise}
	 */
	findTools( context, payload ) {
		const filters = payload.filters || [];
		const params = [
			[ 'q', payload.query || null ],
			...filters,
			[ 'ordering', payload.ordering || null ],
			[ 'page', payload.page || null ],
			[ 'page_size', payload.pageSize || null ]
		];
		const cleanParams = new URLSearchParams(
			params.filter( ( value ) => {
				const val = value[ 1 ];
				return val !== null && val !== undefined;
			} )
		);
		const request = {
			url: '/api/search/tools/?' + cleanParams.toString()
		};
		return makeApiCall( context, request ).then(
			( response ) => {
				const results = response.body;
				results.facets = extractFacets( results, filters );
				context.commit( 'onToolsResults', {
					results,
					qs: cleanParams
				} );
			},
			( failure ) => {
				const data = getFailurePayload( failure );
				this._vm.$notify.error(
					i18n.t( 'apierror', [ data ] )
				);
			}
		);
	}
};

export const mutations = {
	/**
	 * Store /api/search/tools/ results.
	 *
	 * @param {Object} state - Vuex state tree.
	 * @param {Object} payload - mutation payload.
	 * @param {Object} payload.results - API response
	 * @param {Object} payload.qs - Query string params
	 */
	onToolsResults( state, { results, qs } ) {
		state.toolsResponse = results;
		state.toolsQueryParams = qs;
	}
};

export default {
	namespaced: true,
	state: {
		toolsQueryParams: null,
		toolsResponse: {}
	},
	getters: getters,
	actions: actions,
	mutations: mutations,
	strict: process.env.NODE_ENV !== 'production'
};
