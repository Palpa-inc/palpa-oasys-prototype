import { defineNuxtConfig } from 'nuxt/config'

// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  css: ['vuetify/lib/styles/main.sass', 'mdi/css/materialdesignicons.min.css'], // 修正
  build: {
    transpile: ['vuetify', /vue3-library-reproduction/],
  },
  vite: {
    define: {
      'process.env.DEBUG': false,
    }
  },
})
