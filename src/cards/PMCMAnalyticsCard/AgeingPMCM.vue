<template>
  <div class="ageing-pmcm-card">
    <div class="ageing-pmcm-card-title">
      <span class="title-indicator"></span>
      Running Ageing PM&CM (UTC+3)
    </div>
    <div class="ageing-pmcm-chart-container">
      <v-chart class="chart" :option="chartOption" autoresize />
    </div>
  </div>
</template>

<script>
import { use } from 'echarts/core';
import { CanvasRenderer } from 'echarts/renderers';
import { BarChart } from 'echarts/charts';
import { GridComponent, TooltipComponent, LegendComponent } from 'echarts/components';
import VChart from 'vue-echarts';

use([CanvasRenderer, BarChart, GridComponent, TooltipComponent, LegendComponent]);

export default {
  name: 'AgeingPMCM',
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
      const ageingCategories = [
        '15 Minutes', '1 Hour', '4 Hours', '6 Hours',
        '12 Hours', '18 Hours', '>24 Hours'
      ];
      
      const runningTickets = [...this.pm_json, ...this.cm_json].filter(ticket => ticket.ticketstatus === 'running');
      const ageingCounts = this.calculateAgeingCounts(runningTickets);

      this.chartOption = {
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'shadow'
          },
          appendToBody: true,
          enterable: true,
          formatter: this.formatTooltip
        },
        grid: {
          left: '3%',
          right: '4%',
          bottom: '3%',
          containLabel: true
        },
        xAxis: {
          type: 'category',
          data: ageingCategories,
          axisLabel: {
            interval: 0,
            rotate: 45
          }
        },
        yAxis: {
          show: false,
          type: 'value'
        },
        series: [{
          data: ageingCounts,
          type: 'bar',
          itemStyle: {
            color: '#007AC0'
          },
          label: {
            show: true,
            position: 'top',
            color: 'black',
            formatter: (params) => {
              return params.value === 0 ? '' : params.value;
            }
          }
        }]
      };
    },
    calculateAgeingCounts(tickets) {
      const now = this.getUTC3Time(new Date());
      const ageingCounts = [0, 0, 0, 0, 0, 0, 0];

      tickets.forEach(ticket => {
        const createTime = this.getUTC3Time(new Date(ticket.createtime));
        const ageInHours = (now - createTime) / (1000 * 60 * 60);

        if (ageInHours <= 0.25) ageingCounts[0]++;
        else if (ageInHours <= 1) ageingCounts[1]++;
        else if (ageInHours <= 4) ageingCounts[2]++;
        else if (ageInHours <= 6) ageingCounts[3]++;
        else if (ageInHours <= 12) ageingCounts[4]++;
        else if (ageInHours <= 18) ageingCounts[5]++;
        else ageingCounts[6]++;
      });

      return ageingCounts;
    },
    getUTC3Time(date) {
      return new Date(date.getTime() + (3 * 60 * 60 * 1000));
    },
    formatTooltip(params) {
      const ageingCategory = params[0].axisValue;
      const allTickets = [...this.pm_json, ...this.cm_json];
      const ttForCategory = allTickets.filter(tt => {
        const createTime = new Date(tt.createtime);
        const now = new Date();
        const ageInHours = (now - createTime) / (1000 * 60 * 60);
        
        if (tt.ticketstatus !== 'running') return false;
        
        switch(ageingCategory) {
          case '15 Minutes': return ageInHours <= 0.25;
          case '1 Hour': return ageInHours > 0.25 && ageInHours <= 1;
          case '4 Hours': return ageInHours > 1 && ageInHours <= 4;
          case '6 Hours': return ageInHours > 4 && ageInHours <= 6;
          case '12 Hours': return ageInHours > 6 && ageInHours <= 12;
          case '18 Hours': return ageInHours > 12 && ageInHours <= 18;
          case '>24 Hours': return ageInHours > 24;
          default: return false;
        }
      });

      let tooltipContent = `
        <div style="width: 300px; max-height: 400px; overflow-y: auto; padding: 15px; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.15); background-color: #ffffff; font-family: Arial, sans-serif;">
          <div style="background-color: #007AC0; color: white; padding: 15px; margin: -15px -15px 15px -15px; border-top-left-radius: 8px; border-top-right-radius: 8px;">
            <h3 style="margin: 0; font-size: 18px;">Running Tasks - ${ageingCategory}</h3>
          </div>
          <p style="font-size: 16px; margin: 0 0 10px 0;"><strong>Total Running Tasks:</strong> ${ttForCategory.length}</p>
      `;

      ttForCategory.forEach((tt) => {
        tooltipContent += `
          <div style="border: 1px solid #e0e0e0; border-radius: 4px; padding: 10px; margin-bottom: 10px;">
            <p style="font-size: 14px; margin: 0 0 5px 0;"><strong>Task ID:</strong> ${tt.ticketid}</p>
            <p style="font-size: 14px; margin: 0 0 5px 0;"><strong>Category:</strong> ${tt.task_category}</p>
            <p style="font-size: 14px; margin: 0;"><strong>Create Time:</strong> ${tt.createtime}</p>
            <p style="font-size: 14px; margin: 0;"><strong>SLA Status:</strong> ${tt.slastatus}</p>
          </div>
        `;
      });

      tooltipContent += '</div>';
      return tooltipContent;
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
.ageing-pmcm-card {
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
.ageing-pmcm-card-title {
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
.ageing-pmcm-chart-container {
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