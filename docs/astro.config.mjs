// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

// https://astro.build/config
export default defineConfig({
	integrations: [
		starlight({
			title: 'A Shelves Voyage',
			logo: { src: './src/assets/oi_logo_white.png', alt:'Orpheus Instituut Logo'},
			social: [{ icon: 'github', label: 'GitHub', href: 'https://github.com/NicholasCorniaOrpheus/a_shelves_voyage' }],
			sidebar: [
				{
					label: 'Introduction',
					items: [
						// Each item here is one entry in the navigation menu.
						{ label: 'Example Guide', slug: 'guides/example' },
					],
				},
				{
					label: 'Reference',
					autogenerate: { directory: 'reference' },
				},
			],
			customCss : [
				'@fontsource/sofia-sans/400.css']
		}),
	],
});
