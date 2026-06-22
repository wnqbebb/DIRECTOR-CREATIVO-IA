import { defineConfig } from 'vite'
import { resolve } from 'path'

export default defineConfig({
  build: {
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'index.html'),
        director: resolve(__dirname, 'director-creativo.html'),
        prendaCampana: resolve(__dirname, 'de-prenda-a-campana.html')
      }
    }
  }
})
