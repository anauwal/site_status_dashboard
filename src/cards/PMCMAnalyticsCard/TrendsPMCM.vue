<template>
  <div class="trends-pmcm-card">
    <div class="trends-pmcm-card-title">
      <span class="title-indicator"></span>
      PM & CM Ticketss 
    </div>
    <div class="trends-pmcm-chart-container">
      <v-chart class="chart" :option="chartOption" autoresize />
    </div>
  </div>
</template>

<script>
import { use } from 'echarts/core';
import { CanvasRenderer } from 'echarts/renderers';
import { LineChart, BarChart } from 'echarts/charts';
import {
  TitleComponent,
  TooltipComponent,
  LegendComponent,
  GridComponent,
} from 'echarts/components';
import VChart from 'vue-echarts';

use([
  CanvasRenderer,
  LineChart,
  BarChart,
  TitleComponent,
  TooltipComponent,
  LegendComponent,
  GridComponent,
]);

export default {
  name: 'TrendsPMCM',
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
  components: {
    VChart,
  },
  data() {
    return {
      chartOption: {},
    };
  },
  mounted() {
    this.processData();
  },
  methods: {
    processData() {
      const pmData = this.groupDataByDay(this.pm_json);
      const cmData = this.groupDataByDay(this.cm_json);
      this.updateChartOption(pmData, cmData);
    },
    groupDataByDay(data) {
      const groupedData = {};
      data.forEach(item => {
        const date = item.createtime.split(' ')[0];
        if (!groupedData[date]) {
          groupedData[date] = { total: 0, completed: 0, running: 0, cancel: 0 };
        }
        groupedData[date].total += 1;
        groupedData[date][item.ticketstatus] = (groupedData[date][item.ticketstatus] || 0) + 1;
      });
      return groupedData;
    },
    updateChartOption(pmData, cmData) {
      const dates = [...new Set([...Object.keys(pmData), ...Object.keys(cmData)])].sort();
      const pmTrend = dates.map(date => (pmData[date]?.total || 0));
      const cmTrend = dates.map(date => (cmData[date]?.total || 0));
      const completedTickets = dates.map(date => (
        (pmData[date]?.completed || 0) + (cmData[date]?.completed || 0)
      ));
      const runningTickets = dates.map(date => (
        (pmData[date]?.running || 0) + (cmData[date]?.running || 0)
      ));
      const canceledTickets = dates.map(date => (
        (pmData[date]?.cancel || 0) + (cmData[date]?.cancel || 0)
      ));

      this.chartOption = {
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'cross',
            crossStyle: {
              color: '#999'
            }
          }
        },
        legend: {
          data: ['PM Tickets', 'CM Tickets', 'Completed', 'Running', 'Canceled']
        },
        xAxis: [
          {
            type: 'category',
            data: dates,
            axisPointer: {
              type: 'shadow'
            }
          }
        ],
        yAxis: [
          {
            type: 'value',
            name: 'Number of Tickets',
            min: 0,
            interval: 1,
          }
        ],
        series: [
          {
            name: 'PM Tickets',
            type: 'line',
            data: pmTrend,
          },
          {
            name: 'CM Tickets',
            type: 'line',
            data: cmTrend,
          },
          {
            name: 'Completed',
            type: 'bar',
            stack: 'Ticket Status',
            data: completedTickets,
          },
          {
            name: 'Running',
            type: 'bar',
            stack: 'Ticket Status',
            data: runningTickets,
          },
          {
            name: 'Canceled',
            type: 'bar',
            stack: 'Ticket Status',
            data: canceledTickets,
          }
        ]
      };
    }
  }
};
</script>

<style scoped>
.trends-pmcm-card {
  z-index: 999;
  display: flex;
  border: 1px solid #007AC0;
  background-color: #007AC0;
  border-radius: 5px;
  overflow: hidden;
  flex-direction: column;
  width: 760px;
  height: 220px;
  max-width: 800px;
  padding: 10px;
}
.trends-pmcm-card-title{
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

.trends-pmcm-chart-container {
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
