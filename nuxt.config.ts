import { defineNuxtConfig } from 'nuxt/config'

// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  css: ['vuetify/lib/styles/main.sass'], // 修正
  build: {
    transpile: ['vuetify', 'mdi/css/materialdesignicons.min.css', 'vuetify/lib/components/VCode/VCode.css'],
  },
  vite: {
    define: {
      'process.env.DEBUG': false,
    }
  },
})
