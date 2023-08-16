<template>
  <div class="task-card">
    <h4>{{ task.title }}</h4>
    <p>{{ task.description }}</p>
    <span class="status">{{ task.status }}</span>
    <span class="deadline">截止日期: {{ task.deadline }}</span>
  </div>
</template>

<script>
export default {
  name: 'AppTaskCardPage',
  props: {
    task: {
      type: Object,
      required: true,
    },
  },
};
</script>

<style>
.task-card {
  border: 1px solid #ccc;
  padding: 15px;
  margin: 10px;
}

.status {
  color: #333;
}

.deadline {
  color: #888;
}
</style>
