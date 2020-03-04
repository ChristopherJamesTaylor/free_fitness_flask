import Vue from 'vue'
import './plugins/axios'
import App from './App.vue'
import vuetify from './plugins/vuetify';
import './registerServiceWorker'
import router from './router'
import store from './state/store'
import * as Vue2Leaflet from 'vue2-leaflet';


Vue.config.productionTip = false
Vue.use(Vue2Leaflet);


new Vue({
  vuetify,
  router,
  store,
  render: h => h(App)
}).$mount('#app')
