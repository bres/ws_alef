module.exports = {
  future: {
      removeDeprecatedGapUtilities: true,
      purgeLayersByDefault: true,
  },
  purge: {
      enabled: true, //true for production build
      content: [
        '../**/templates/*.html',
        '../**/templates/**/*.html',
        '../**/templates/**/**/*.html'
      ],
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
       fontSize: {
        'xs': '.75rem',
        'sm': '.875rem',
        'tiny': '.875rem',
        'base': '1rem',
        'lg': '1.125rem',
        'xl': '1.25rem',
        '2xl': '1.5rem',
        '3xl': '1.875rem',
        '4xl': '2.25rem',
        '5xl': '3rem',
        '6xl': '4rem',
        '7xl': '5rem',
        '8xl': '7rem',
      }
      },
  },
  variants: {
    // The 'active' variant will be generated in addition to the defaults
    extend: {
    }
  },
  plugins: [
    require('@tailwindcss/aspect-ratio'),
  ],
}
