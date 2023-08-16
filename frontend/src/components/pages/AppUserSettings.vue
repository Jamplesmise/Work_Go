<template>
  <div class="user-settings">
    <label>
      接收通知:
      <input type="checkbox" v-model="settings.notifications" />
    </label>
    <label>
      关注部门:
      <select v-model="settings.department">
        <!-- 可以根据实际需求添加部门选项 -->
        <option value="development">开发</option>
        <option value="marketing">市场</option>
      </select>
    </label>
    <button @click="saveSettings">保存设置</button>
  </div>
</template>

<script>
export default {
  name: 'AppUserSettings',
  data() {
    return {
      settings: {
        notifications: true,
        department: 'development',
      },
    };
  },
  methods: {
    saveSettings() {
      // 保存设置的逻辑
      this.$emit('save', this.settings);
    },
  },
};
</script>

<style>
.user-settings label {
  display: block;
  margin-bottom: 10px;
}

.user-settings button {
  padding: 10px;
  cursor: pointer;
}
</style>
