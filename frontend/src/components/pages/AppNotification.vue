<template>
  <div v-if="notifications.length" class="notification">
    <ul>
      <li v-for="note in notifications" :key="note.id">{{ note.message }}</li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'AppNotification',
  props: {
    notifications: {
      type: Array,
      default: () => [],
    },
  },
};
</script>

<style>
.notification {
  position: fixed;
  top: 0;
  right: 0;
  background-color: #f5f5f5;
  padding: 15px;
}
</style>
