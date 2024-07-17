<template>
  <div class="trends-siteaccess-card">
    <div class="trends-siteaccess-card-title">
      <span class="title-indicator"></span>
      Site Access Tickets
    </div>
    <div class="trends-siteaccess-chart-container">
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
  name: 'TrendsSiteAccess',
  props: {
    sacc_json: {
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
      const groupedData = this.groupDataByDay(this.sacc_json);
      this.updateChartOption(groupedData);
    },
    groupDataByDay(data) {
      const groupedData = {};
      data.forEach(item => {
        const date = item.create_time.split(' ')[0];
        if (!groupedData[date]) {
          groupedData[date] = { total: 0, completed: 0, running: 0, cancel: 0, tickets: [] };
        }
        groupedData[date].total += 1;
        groupedData[date][item.order_status] += 1;
        groupedData[date].tickets.push(item);
      });
      return groupedData;
    },
    updateChartOption(groupedData) {
      const dates = Object.keys(groupedData).sort();
      const totalTrend = dates.map(date => groupedData[date].total);
      const completedTrend = dates.map(date => groupedData[date].completed);
      const runningTrend = dates.map(date => groupedData[date].running);
      const canceledTrend = dates.map(date => groupedData[date].cancel);

      this.chartOption = {
        tooltip: {
          trigger: 'axis',
          appendToBody: true,
          enterable: true,
          axisPointer: {
            type: 'cross',
            crossStyle: {
              color: '#999'
            }
          },
          formatter: (params) => {
            const date = params[0].axisValue;
            const dayData = groupedData[date];
            
            let tooltipContent = `
              <div style="width: 500px; max-height: 400px; overflow-y: auto; padding: 15px; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.15); background-color: #ffffff; font-family: Arial, sans-serif;">
                <div style="background-color: #007AC0; color: white; padding: 15px; margin: -15px -15px 15px -15px; border-top-left-radius: 8px; border-top-right-radius: 8px;">
                  <h3 style="margin: 0; font-size: 18px;">Site Access Summary for ${date}</h3>
                </div>
                <p style="font-size: 16px; margin: 0 0 10px 0;"><strong>Total Tickets:</strong> ${dayData.total}</p>
                <div style="margin-bottom: 15px;">
                  <p style="font-size: 14px; margin: 0 0 5px 0;"><strong>Status Summary:</strong></p>
                  <p style="font-size: 14px; margin: 0 0 3px 0;">Completed: ${dayData.completed}</p>
                  <p style="font-size: 14px; margin: 0 0 3px 0;">Running: ${dayData.running}</p>
                  <p style="font-size: 14px; margin: 0;">Canceled: ${dayData.cancel}</p>
                </div>
            `;

            dayData.tickets.forEach((ticket) => {
              tooltipContent += `
                <div style="border: 1px solid #e0e0e0; border-radius: 4px; padding: 10px; margin-bottom: 10px;">
                    <p style="font-size: 14px; margin: 0 0 5px 0;"><strong>Ticket ID:</strong> ${ticket.id}</p>
                    <p style="font-size: 14px; margin: 0 0 5px 0;"><strong>Status:</strong> ${ticket.order_status}</p>
                    <p style="font-size: 14px; margin: 0 0 5px 0; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;"><strong>Title:</strong> ${ticket.title}</p>
                    <p style="font-size: 14px; margin: 0 0 5px 0;"><strong>FME Name:</strong> ${ticket.fme_assigned}</p>
                    <p style="font-size: 14px; margin: 0 0 5px 0;"><strong>FME Mobile:</strong> ${ticket.fme_mobile}</p>
                    <p style="font-size: 14px; margin: 0;"><strong>Create Time:</strong> ${ticket.create_time}</p>
                    <p style="font-size: 14px; margin: 0;"><strong>End Time:</strong> ${ticket.end_time}</p>
                </div>
              `;
            });

            tooltipContent += '</div>';
            return tooltipContent;
          }
        },
        legend: {
          data: ['Total Tickets', 'Completed', 'Running', 'Canceled']
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
            name: 'Total Tickets',
            type: 'line',
            data: totalTrend,
          },
          {
            name: 'Completed',
            type: 'bar',
            stack: 'Ticket Status',
            data: completedTrend,
          },
          {
            name: 'Running',
            type: 'bar',
            stack: 'Ticket Status',
            data: runningTrend,
          },
          {
            name: 'Canceled',
            type: 'bar',
            stack: 'Ticket Status',
            data: canceledTrend,
          }
        ]
      };
    }
  }
};
</script>

<style scoped>
.trends-siteaccess-card {
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
.trends-siteaccess-card-title{
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

.trends-siteaccess-chart-container {
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