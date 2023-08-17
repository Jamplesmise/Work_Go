<script setup>

</script>

<template>
  <div>
    <h1>注册</h1>
    <form @submit.prevent="register">
      <input type="text" v-model="username" placeholder="用户名" required pattern="\w{3,}" />
      <div v-if="usernameError" class="error">{{ usernameError }}</div>
      <input type="password" v-model="password" placeholder="密码" required pattern=".{6,}" />
      <div v-if="passwordError" class="error">{{ passwordError }}</div>
      <button type="submit">注册</button>
    </form>
    <div v-if="registerError" class="error">{{ registerError }}</div>
  </div>
</template>

<script>
import { mapActions } from 'vuex';

export default {
  data() {
    return {
      username: '',
      password: '',
      usernameError: '',
      passwordError: '',
      registerError: '',
    };
  },
  methods: {
    ...mapActions(['register']),
    async register() {
      this.usernameError = this.passwordError = this.registerError = '';

      if (this.username.length < 3) {
        this.usernameError = '用户名必须至少包含3个字符';
        return;
      }

      if (this.password.length < 6) {
        this.passwordError = '密码必须至少包含6个字符';
        return;
      }

      try {
        await this.register({ username: this.username, password: this.password });
        this.$router.push('/'); // 跳转到主页或其他页面
      } catch (error) {
        this.registerError = '注册失败: ' + error.message;
      }
    },
  },
};
</script>

<style>
.error {
  color: red;
}
</style>
