import Vue from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import axios from "axios"; // 引入 Element UI 样式

Vue.config.productionTip = false;

// 使用 Element UI
Vue.use(ElementUI);

// 将 Axios 实例添加到 Vue 原型中
Vue.prototype.$http = axios;

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app');
