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
          '120': '30rem',
          '128': '32rem',
          '136': '34rem',
          '144': '36rem',
          '152': '38rem',
          '168': '42rem',
          '176': '44rem',
          '184': '46rem',
          '200': '50rem',
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
          '108': '27rem',
          '112': '28rem',
          '116': '29rem',
          '120': '30rem',
          '128': '32rem',
          '136': '34rem',
          '144': '36rem',
          '152': '38rem',
          '192': '48rem',
          '200': '50rem',
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
