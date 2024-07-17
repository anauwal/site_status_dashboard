<template>
  <div class="active-alarm-card">
    <div class="active-alarm-card-title">
      <span class="title-indicator"></span>
      Active Alarm Trends
    </div>
    <div class="active-alarm-chart-container">
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
  name: 'TrendsAlarm',
  props: {
    active_alarm_json: {
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
      networkTypes: [
        'IP', 'Fixed Access Network', '2G', '3G', 'EnM', '5G', 'CS', 'SNFN DWDM', 
        '4G', 'PS', 'Fixed Core Network', 'Microwave', 'Transmission Network', 
        'NFV', 'DPI', 'SDN', 'Seamless', 'Radio Access Network', 'Unknown', 'Blank'
      ]
    };
  },
  mounted() {
    this.processData();
  },
  methods: {
    processData() {
      const dailyData = this.groupDataByDay(this.active_alarm_json);
      this.updateChartOption(dailyData);
    },
    groupDataByDay(data) {
      const groupedData = {};
      
      data.forEach(item => {
        if (item.cleartime === "0") {
          const date = item.firstoccurrence.split(' ')[0];
          if (!groupedData[date]) {
            groupedData[date] = { total: 0 };
            this.networkTypes.forEach(type => {
              groupedData[date][type] = 0;
            });
          }
          groupedData[date].total += 1;
          
          let networkType = item.networktype ? item.networktype.trim() : 'Blank';
          if (!this.networkTypes.includes(networkType)) {
            networkType = 'Unknown';
          }
          groupedData[date][networkType] += 1;
        }
      });
      return groupedData;
    },
    updateChartOption(dailyData) {
      const dates = Object.keys(dailyData).sort();
      const totalAlarms = dates.map(date => dailyData[date].total);
      const alarmsByType = {};
      this.networkTypes.forEach(type => {
        alarmsByType[type] = dates.map(date => dailyData[date][type]);
      });

      // Filter out network types with all zero values
      const activeNetworkTypes = this.networkTypes.filter(type => 
        alarmsByType[type].some(value => value > 0)
      );

      this.chartOption = {
        grid: {
          top: '15%',
          bottom: '0%',
          left: '6%',
          right: '3%',
          containLabel: true
        },
        tooltip: {
          trigger: 'axis',
          appendToBody: true,
          enterable: true,
          axisPointer: {
            type: 'cross',
            crossStyle: {
              color: '#999'
            }
          }
        },
        legend: {
          data: ['Total Active Alarms', ...activeNetworkTypes]
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
            name: 'Active Alarms',
            min: 0,
            interval: 10,
            axisLabel: {
              show: false
            }
          }
        ],
        series: [
          {
            name: 'Total Active Alarms',
            type: 'line',
            data: totalAlarms,
          },
          ...activeNetworkTypes.map(type => ({
            name: type,
            type: 'bar',
            stack: 'NetworkType',
            data: alarmsByType[type],
          }))
        ]
      };
    }
  }
};
</script>

<style scoped>
.active-alarm-card {
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
.active-alarm-card-title{
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

.active-alarm-chart-container {
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