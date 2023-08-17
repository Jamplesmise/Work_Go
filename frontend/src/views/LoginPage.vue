<script setup>

</script>

<template>
  <div>
    <h1>登录</h1>
    <form @submit.prevent="login">
      <input type="text" v-model="username" placeholder="用户名" required />
      <input type="password" v-model="password" placeholder="密码" required />
      <button type="submit">登录</button>
    </form>
  </div>
  <div v-if="loginError" class="error">{{ loginError }}</div>
</template>

<script>
// ...

export default {
  data() {
    return {
      username: '',
      password: '',
      loginError: '',
    };
  },
  // ...
  async login() {
    this.loginError = '';

    try {
      await this.login({ username: this.username, password: this.password });
      this.$router.push('/'); // 跳转到主页或其他页面
    } catch (error) {
      this.loginError = '登录失败: ' + error.message;
    }
  },
};

</script>

<!-- 同样的样式 -->
