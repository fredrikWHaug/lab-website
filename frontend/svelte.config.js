import adapter from '@sveltejs/adapter-auto';
import { vitePreprocess } from '@sveltejs/vite-plugin-svelte';

/** @type {import('@sveltejs/kit').Config} */
const config = {
	// Use Vite preprocess for handling Svelte files
	preprocess: vitePreprocess(),

	kit: {
		// Adapter for building the application
		adapter: adapter(),

		// Default static directory for assets
		files: {
			assets: 'static', // Ensure static files are served from the static folder
		}
	}
};

export default config;
