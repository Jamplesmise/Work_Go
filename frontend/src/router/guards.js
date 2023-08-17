import router from './index';

// 例如，一个全局的前置守卫
router.beforeEach((to, from, next) => {
  // 在这里添加导航逻辑
  next();
});

// 你也可以添加其他守卫，如路由解析守卫、全局后置守卫等
import store from '@/store';

export function requireAuth(to, from, next) {
  if (!store.getters.isLoggedIn) {
    next('/login'); // 未登录则重定向到登录页面
  } else {
    next(); // 已登录则继续
  }
}

// 在路由配置中使用此守卫
