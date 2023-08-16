<template>
  <div class="tasks">
    <h1>任务列表</h1>
    <div v-for="task in tasks" :key="task.id">
      <AppTaskCard :task="task"></AppTaskCard>
    </div>
  </div>
</template>

<script>
import AppTaskCard from '../components/pages/AppTaskCard.vue';

export default {
  name: 'TasksPage',
  components: {
    AppTaskCard,
  },
  data() {
    return {
      tasks: [
        // 示例任务，你可以从服务器动态获取
        { id: 1, title: '开发新功能', description: '...', status: '进行中', deadline: '2023-09-15' },
        // 更多任务...
      ],
    };
  },
};
</script>

<style>
.tasks {
  padding: 20px;
}
</style>
