<script setup>
import { ref } from 'vue';

// 示例任务数据，你可以从服务器或其他来源获取
const tasks = ref([
  { id: 1, title: '完成开发任务A', status: '进行中', deadline: '2023-08-20' },
  { id: 2, title: '准备项目B的设计文档', status: '待办', deadline: '2023-08-15' },
  // 更多任务...
]);
</script>

<template>
  <div>
    <h1>任务仪表盘</h1>
    <div class="task-board">
      <div v-for="status in ['待办', '进行中', '已完成']" :key="status" class="task-column">
        <h2>{{ status }}</h2>
        <AppTaskCard v-for="task in tasks.filter(task => task.status === status)" :key="task.id" :task="task"></AppTaskCard>
      </div>
    </div>
  </div>
</template>

<script>
import AppTaskCard from '@/components/pages/AppTaskCard.vue';

export default {
  name: 'DashboardPage',
  components: {
    AppTaskCard
  },
};
</script>

<style>
.task-board {
  display: flex;
  justify-content: space-between;
}

.task-column {
  width: 30%;
  padding: 20px;
  border: 1px solid #e0e0e0;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.task-column h2 {
  margin: 0 0 10px;
  color: #333;
  font-weight: 600;
}
</style>
