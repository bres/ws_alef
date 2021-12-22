module.exports = {
  future: {
      removeDeprecatedGapUtilities: true,
      purgeLayersByDefault: true,
  },
  purge: {
      enabled: false, //true for production build
      content: [
          '../**/templates/*.html',
          '../**/templates/**/*.html'
      ]
  },
  theme: {
      extend: {
        spacing: {
          '112': '28rem',
          '144': '36rem',
          '160': '40rem',
          '176': '44rem',
          '192': '48rem',
          '208': '52rem',
          '216': '54rem',
          '224': '56rem',
          '296': '74rem',
        },
        screens: {
          '3xl': '1925px',
        },
      },
  },
  variants: {
    // The 'active' variant will be generated in addition to the defaults
    extend: {
    }
  },
  plugins: [require('@tailwindcss/aspect-ratio'),],
}
