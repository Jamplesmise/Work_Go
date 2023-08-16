<template>
  <nav>
    <ul class="navbar">
      <li><router-link to="/">首页</router-link></li>
      <li><router-link to="/tasks">任务</router-link></li>
      <li><router-link to="/activity">动态墙</router-link></li>
      <li><router-link to="/settings">设置</router-link></li>
      <li><router-link to="/reports">报告</router-link></li>
    </ul>
  </nav>
</template>

<script>
export default {
  name: "AppNavbar",
};
</script>

<style>
.navbar {
  list-style: none;
  padding: 5px 0;
  margin: 0;
  display: flex;
  border-radius: 10px; /* 圆角效果 */
  justify-content: space-around;
  background-color: #008E9B; /* 改变背景颜色 */
  box-shadow: 0px 0px 5px rgba(0, 0, 0, 0.1); /* 添加阴影 */
}

.navbar li {
  padding: 15px;
}

.router-link-active { /* 当前激活的路由链接样式 */
  font-weight: bold;
  color: white;
}

.router-link-exact-active { /* 精确匹配的路由链接样式 */
  text-decoration: underline;
}

.navbar a { /* 链接样式 */
  color: white; /* 文字颜色 */
  text-decoration: none;
  padding: 10px 15px; /* 增加内边距 */
  transition: color 0.3s; /* 过渡效果 */
}

.navbar a:hover { /* 悬停效果 */
  color: #f1f1f1; /* 改变颜色 */
}
</style>
