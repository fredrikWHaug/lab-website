import adapter from '@sveltejs/adapter-auto';
import { vitePreprocess } from '@sveltejs/vite-plugin-svelte';

/** @type {import('@sveltejs/kit').Config} */
const config = {
	// Consult https://svelte.dev/docs/kit/integrations for more information about preprocessors
	preprocess: vitePreprocess(),

	kit: {
		// Adapter for building the application
		adapter: adapter(),

		// Ensures app.css is globally applied
		files: {
			assets: 'src'
		}
	}
};

export default config;
