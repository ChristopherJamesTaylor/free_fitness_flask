module.exports = {
  "transpileDependencies": [
    "vuetify"
  ],

  devServer: {
        port: 5000,
        proxy: "http://localhost/"
    },
  // publicPath: process.env.NODE_ENV === 'production'
  //   ? '/free_fitness_flask/'
  //   : '/'
  publicPath: '/'
};