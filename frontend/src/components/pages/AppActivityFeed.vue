<template>
  <div class="activity-feed">
    <div v-for="activity in activities" :key="activity.id" class="activity">
      <h4>{{ activity.title }}</h4>
      <p>{{ activity.content }}</p>
      <small>{{ activity.date }}</small>
    </div>
  </div>
</template>

<script>
export default {
  name: 'AppActivityFeed',
  props: {
    activities: {
      type: Array,
      default: () => [],
    },
  },
};
</script>

<style>
.activity-feed {
  padding: 15px;
}

.activity {
  border-bottom: 1px solid #ccc;
  padding: 10px;
}
</style>
