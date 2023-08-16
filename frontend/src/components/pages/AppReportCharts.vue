<template>
  <div class="report-charts">
    <line-chart :chart-data="dataCollection"></line-chart>
  </div>
</template>

<script>
import LineChart from '@/components/LineChart.vue';

export default {
  name: 'AppReportCharts',
  components: {
    LineChart,
  },
  data() {
    return {
      dataCollection: {
        labels: ['一月', '二月', '三月', '四月'],
        datasets: [
          {
            label: '任务完成',
            backgroundColor: '#f87979',
            data: [40, 20, 85, 60],
          },
        ],
      },
    };
  },
};
</script>

<style>
.report-charts {
  width: 100%;
  height: 400px;
}
</style>
