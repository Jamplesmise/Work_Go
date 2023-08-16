<template>
  <div class="activity">
    <h1>最新动态</h1>
    <p>这里是公司的最新动态和进展，包括项目更新、公告和团队活动等。</p>
    <div class="activities">
      <div class="activity-item" v-for="item in activityList" :key="item.id">
        <h3>{{ item.title }}</h3>
        <p>{{ item.content }}</p>
        <span>{{ item.date }}</span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ActivityPage',
  data() {
    return {
      activityList: [
        { id: 1, title: '项目A更新', content: '项目A已经完成第二阶段的开发，进入测试阶段。', date: '2023-08-10' },
        { id: 2, title: '新团队成员', content: '欢迎新团队成员张三加入我们的开发团队。', date: '2023-08-08' },
        // 更多动态...
      ],
    };
  },
};
</script>

<style>
.activity {
  padding: 20px;
}

.activities {
  margin: 20px 0;
}

.activity-item {
  padding: 10px;
  border-bottom: 1px solid #e0e0e0;
}

.activity-item:last-child {
  border-bottom: none;
}

h3 {
  margin: 0;
  color: #333;
  font-weight: 600;
}

span {
  font-size: 12px;
  color: #999;
}
</style>
