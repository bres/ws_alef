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
          '120': '28rem',
          '144': '32rem',
          '168': '36rem',
          '192': '48rem',
        }
      },
  },
  variants: {},
  plugins: [],
}
