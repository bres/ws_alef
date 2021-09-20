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
          '88':  '22rem',
          '104': '26rem',
          '112': '28rem',
          '128': '32rem',
          '144': '36rem',
          '160': '40rem',
          '192': '48rem',
          '224': '56rem',
        }
      },
  },
  variants: {
    // The 'active' variant will be generated in addition to the defaults
    extend: {
      display: ['group-hover'],
      transitionDuration: ['group-hover'],
      transitionProperty: ['group-hover' ]

    }
  },
  plugins: [],
}
