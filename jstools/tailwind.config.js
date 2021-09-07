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
