<template>
  <div class="home">
    <h1>欢迎来到工作协同系统</h1>
    <p>这里是首页，你可以查看公司的最新动态和公告。</p>
    <div class="sections">
      <div class="section">
        <h2>最新动态</h2>
        <p>了解公司的最新活动、项目进展和团队成就。</p>
      </div>
      <div class="section">
        <h2>任务看板</h2>
        <p>快速访问你的待办事项，查看任务进度和协作情况。</p>
      </div>
      <div class="section">
        <h2>报告分析</h2>
        <p>查看各部门和项目的统计报告，更好地了解工作状况。</p>
      </div>
      <div class="section">
        <h2>信息订阅</h2>
        <p>订阅感兴趣的部门和项目，不错过任何重要更新。</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HomePage',
};
</script>

<style>
.home {
  padding: 20px;
}

.sections {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
}

.section {
  flex: 1;
  min-width: 200px;
  padding: 15px;
  box-shadow: 0px 0px 5px rgba(0, 0, 0, 0.1);
  margin: 10px;
  border-radius: 8px;
}

h2 {
  color: #333;
  font-weight: 600;
}
</style>

