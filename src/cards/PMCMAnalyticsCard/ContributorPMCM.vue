<template>
  <div class="contributor-category-card">
    <div class="contributor-category-card-title">
      <span class="title-indicator"></span>
      WFM PM & CM Contributor Task Category
    </div>
    <div class="contributor-category-chart-container">
      <v-chart class="chart" :option="chartOption" autoresize />
    </div>
  </div>
</template>

<script>
import { use } from 'echarts/core';
import { CanvasRenderer } from 'echarts/renderers';
import { PieChart } from 'echarts/charts';
import { TitleComponent, TooltipComponent, LegendComponent } from 'echarts/components';
import VChart from 'vue-echarts';

use([CanvasRenderer, PieChart, TitleComponent, TooltipComponent, LegendComponent]);

export default {
  name: 'ContributorPMCM',
  components: {
    VChart,
  },
  props: {
    pm_json: {
      type: Array,
      default: () => []
    },
    cm_json: {
      type: Array,
      default: () => []
    }
  },
  data() {
    return {
      chartOption: {}
    };
  },
  mounted() {
    this.updateChart();
  },
  methods: {
    updateChart() {
      const pmData = this.calculateCategoryCounts(this.pm_json, 'PM');
      const cmData = this.calculateCategoryCounts(this.cm_json, 'CM');
      const combinedData = [...pmData, ...cmData];

      this.chartOption = {
        tooltip: {
          trigger: 'item',
          formatter: '{a} <br/>{b}: {c} ({d}%)'
        },
        legend: {
          orient: 'vertical',
          left: 10,
          data: combinedData.map(item => item.name)
        },
        series: [
          {
            name: 'Task Category',
            type: 'pie',
            radius: ['50%', '70%'],
            avoidLabelOverlap: false,
            label: {
              show: false,
              position: 'center'
            },
            emphasis: {
              label: {
                show: true,
                fontSize: '18',
                fontWeight: 'bold'
              }
            },
            labelLine: {
              show: false
            },
            data: combinedData
          }
        ]
      };
    },
    calculateCategoryCounts(data) {
      const categoryMap = new Map();
      
      data.forEach(item => {
        const category = `${item.task_category}`;
        categoryMap.set(category, (categoryMap.get(category) || 0) + 1);
      });

      return Array.from(categoryMap, ([name, value]) => ({ name, value }));
    }
  },
  watch: {
    pm_json: {
      handler() {
        this.updateChart();
      },
      deep: true
    },
    cm_json: {
      handler() {
        this.updateChart();
      },
      deep: true
    }
  }
};
</script>

<style scoped>
.contributor-category-card {
  z-index: 999;
  display: flex;
  border: 1px solid #007AC0;
  background-color: #007AC0;
  border-radius: 5px;
  overflow: hidden;
  flex-direction: column;
  width: 360px;
  height: 220px;
  max-width: 800px;
  padding: 10px;
}
.contributor-category-card-title {
  font-size: 15px;
  padding: 0;
  display: flex;
  margin-left: 5px;
  color: white;
}
.title-indicator {
  display: inline-block;
  width: 5px;
  height: 20px;
  background-color: white;
  margin-left: 5px;
  margin-right: 5px;
}
.contributor-category-chart-container {
  display: flex;
  background-color: white;
  border-radius: 5px;
  overflow: hidden;
  flex-direction: column;
  flex-grow: 1;
  margin-top: 10px;
}
.chart {
  height: 100%;
  width: 100%;
}
</style>