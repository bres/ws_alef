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
          '120': '30rem',
          '128': '32rem',
          '136': '34rem',
          '144': '36rem',
          '152': '38rem',
          '160': '40rem',
          '172': '42rem',
          '176': '44rem',
          '192': '48rem',
          '200': '50rem',
          '208': '52rem',
          '216': '54rem',
          '224': '56rem',
          '288': '72rem',
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
      display: ['group-hover'],
      transitionDuration: ['group-hover'],
      transitionProperty: ['group-hover' ]

    }
  },
  plugins: [require('@tailwindcss/aspect-ratio')],
}
