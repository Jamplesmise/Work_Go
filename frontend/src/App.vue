<template>
  <div id="app">
    <AppNavbar></AppNavbar> <!-- 导航栏组件 -->
    <AppSearchBar></AppSearchBar> <!-- 搜索组件 -->
    <router-view></router-view> <!-- 路由视图，用于显示页面级别的组件 -->
  </div>
</template>

<script>
// 导入组件
import AppNavbar from './components/pages/AppNavbar.vue';
import AppSearchBar from './components/pages/AppSearchBar.vue';

export default {
  name: 'App', // 修改组件名称
  components: {
    AppNavbar, // 注册导航栏组件
    AppSearchBar // 注册搜索组件
  },
  // 其他 Vue 选项
}
</script>

<style>
/* 你可以在这里添加全局样式，或者将它们移到单独的样式文件中并在main.js中导入 */
.navbar {
  list-style: none;
  padding: 0;
  display: flex;
  justify-content: space-around;
}
.navbar li {
  display: inline;
}
</style>
