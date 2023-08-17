import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios'; // 如果你使用axios进行HTTP请求

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    user: null,
    // 其他状态
  },
  mutations: {
    setUser(state, user) {
      state.user = user;
    },
    // 其他 mutations
  },
  actions: {
  async login({ commit }, credentials) {
    try {
      const response = await axios.post('/api/login', credentials);
      commit('setUser', response.data.user);
    } catch (error) {
      console.error('An error occurred while logging in:', error);
      throw error;
    }
  },
  logout({ commit }) {
    // 可以添加与服务器通信的代码来执行服务器端的登出操作
    commit('setUser', null);
  },
  // 其他 actions
  },
  getters: {
  isLoggedIn(state) {
    return state.user !== null;
  },
  // 其他 getters
  },


});

