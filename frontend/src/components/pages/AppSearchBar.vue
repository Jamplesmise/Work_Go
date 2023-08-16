<template>
  <div class="search-bar">
    <input v-model="searchQuery" @input="onSearch" placeholder="搜索..." />
    <button @click="onSearch" class="search-button">搜索</button> <!-- 添加搜索按钮 -->
  </div>
</template>

<script>
export default {
  name: 'AppSearchBar',
  data() {
    return {
      searchQuery: '',
    };
  },
  methods: {
    onSearch() {
      this.$emit('search', this.searchQuery);
    },
  },
};
</script>

<style>
.search-bar {
  display: flex;
  align-items: center;
  justify-content: right; /* 整体中间对齐 */
}

.search-bar input {
  width: 20%; /* 控制宽度 */
  padding: 10px;
  font-size: 16px;
  border-radius: 20px; /* 圆角效果 */
  border: 3px solid ; /* 边框样式 */
  margin-right: 20px; /* 与按钮的间距 */
}

.search-button { /* 搜索按钮样式 */
  padding: 10px 20px;
  font-size: 16px;
  border-radius: 20px; /* 圆角效果 */
  background-color: #008E9B; /* 背景颜色 */
  color: white; /* 文字颜色 */
  border: 10px;
  cursor: pointer; /* 鼠标样式 */
}

.search-button:hover { /* 悬停效果 */
  background-color: #205067;
}
</style>
