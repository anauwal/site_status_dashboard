<template>
  <div class="active-items-card">
    <div class="active-items-card-title">
      <span class="title-indicator"></span>
      Active Items
    </div>
    <div class="active-items-chart-container">
      <v-chart class="chart" :option="chartOption" autoresize />
    </div>
  </div>
</template>

<script>
import { use } from "echarts/core";
import { CanvasRenderer } from "echarts/renderers";
import { BarChart } from "echarts/charts";
import {
  TitleComponent,
  TooltipComponent,
  GridComponent,
  LegendComponent,
} from "echarts/components";
import VChart from "vue-echarts";

use([
  CanvasRenderer,
  BarChart,
  TitleComponent,
  TooltipComponent,
  GridComponent,
  LegendComponent,
]);

export default {
  name: 'ActiveItem',
  components: {
    VChart,
  },
  data() {
    return {
      activeAlarms: 10,
      activeTickets: 15,
      activePM: 10,
      activeCM: 11,
    };
  },
  computed: {
    chartOption() {
      return {  
        legend: {
          data: ['Alarms', 'Tickets', 'PM', 'CM']
        },
        grid: {
          top: '10%',
          bottom: '0%',
          left: '5%',
          right: '10%',
          containLabel: true
        },
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'shadow'
          }
        },
        xAxis: {
          type: 'category',
          data: ['Alarms', 'Tickets', 'PM', 'CM'],
          axisLabel: {
            interval: 0,
            rotate: 0
          }
        },
        yAxis: {
          max: 25,
          type: 'value'
        },
        series: [{
          data: [
            {
              value: this.activeAlarms,
              itemStyle: {
                color: {
                  type: 'linear',
                  x: 0,
                  y: 0,
                  x2: 0,
                  y2: 1,
                  colorStops: [{
                    offset: 0,
                    color: 'rgb(0, 122, 192)'
                  }, {
                    offset: 1,
                    color: 'rgb(2, 151, 239)'
                  }]
                }
              }
            },
            {
              value: this.activeTickets,
              itemStyle: {
                color: {
                  type: 'linear',
                  x: 0,
                  y: 0,
                  x2: 0,
                  y2: 1,
                  colorStops: [{
                    offset: 0,
                    color: 'rgb(0, 122, 192)'
                  }, {
                    offset: 1,
                    color: 'rgb(2, 151, 239)'
                  }]
                }
              }
            },
            {
              value: this.activePM,
              itemStyle: {
                color: {
                  type: 'linear',
                  x: 0,
                  y: 0,
                  x2: 0,
                  y2: 1,
                  colorStops: [{
                    offset: 0,
                    color: 'rgb(0, 122, 192)'
                  }, {
                    offset: 1,
                    color: 'rgb(2, 151, 239)'
                  }]
                }
              }
            },
            {
              value: this.activeCM,
              itemStyle: {
                color: {
                  type: 'linear',
                  x: 0,
                  y: 0,
                  x2: 0,
                  y2: 1,
                  colorStops: [{
                    offset: 0,
                    color: 'rgb(0, 122, 192)'
                  }, {
                    offset: 1,
                    color: 'rgb(2, 151, 239)'
                  }]
                }
              }
            }
          ],
          type: 'bar',
          itemStyle: {
            barBorderRadius: [0, 0, 0, 0]
          },
          label: {
            show: true,
            position: 'top',
            color: '#000',
            fontSize: 14
          }
        }],
      };
    }
  },
  methods: {
  }
};
</script>

<style scoped>
.active-items-card {
  display: flex;
  border: 1px solid #007AC0;
  background-color: #007AC0;
  border-radius: 5px;
  overflow: hidden;
  flex-direction: column;
  width: 360px;
  height: 360px;
  max-width: 800px;
  padding: 10px;
}
.active-items-card-title{
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

.active-items-chart-container {
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