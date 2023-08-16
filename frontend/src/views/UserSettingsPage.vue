<script setup>

</script>

<template>
  <div>
    <h1>用户设置</h1>
    <AppUserSettings></AppUserSettings>
  </div>
</template>

<script>
import AppUserSettings from '@/components/pages/AppUserSettings.vue';

export default {
  name: 'UserSettingsPage',
  components: {
    AppUserSettings
  },
  // 其他代码
};
</script>
