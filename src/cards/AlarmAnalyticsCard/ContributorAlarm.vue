<template>
  <div class="contributor-network-card">
    <div class="contributor-network-card-title">
      <span class="title-indicator"></span>
      Active Alarms Network Type Contributor
    </div>
    <div class="contributor-network-chart-container">
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
  name: 'ContributorNetworkType',
  components: {
    VChart,
  },
  props: {
    active_alarm_json: {
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
      const activeAlarms = this.active_alarm_json.filter(alarm => alarm.cleartime === "0");
      const networkTypeCounts = this.calculateNetworkTypeCounts(activeAlarms);
      this.chartOption = {
        tooltip: {
          trigger: 'item',
          appendToBody: true,
          enterable: true,
          formatter: (params) => {
            const networkType = params.name;
            const count = params.value;
            const percentage = params.percent.toFixed(2);
            
            const alarmsForNetworkType = activeAlarms.filter(alarm => alarm.networktype === networkType);

            let tooltipContent = `
              <div style="width: 300px; max-height: 400px; overflow-y: auto; padding: 15px; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.15); background-color: #ffffff; font-family: Arial, sans-serif;">
                <div style="background-color: #007AC0; color: white; padding: 15px; margin: -15px -15px 15px -15px; border-top-left-radius: 8px; border-top-right-radius: 8px;">
                  <h3 style="margin: 0; font-size: 18px;">Network Type: ${networkType || 'Blank'}</h3>
                </div>
                <p style="font-size: 16px; margin: 0 0 10px 0;"><strong>Total Active Alarms:</strong> ${count} (${percentage}%)</p>
            `;

            alarmsForNetworkType.forEach((alarm) => {
              tooltipContent += `
                <div style="border: 1px solid #e0e0e0; border-radius: 4px; padding: 10px; margin-bottom: 10px;">
                  <p style="font-size: 14px; margin: 0 0 5px 0;"><strong>Alarm ID:</strong> ${alarm.id}</p>
                  <p style="font-size: 14px; margin: 0 0 5px 0; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;"><strong>Alarm Name:</strong> ${alarm.alarmname}</p>
                  <p style="font-size: 14px; margin: 0;"><strong>First Occurrence:</strong> ${alarm.firstoccurrence}</p>
                  <p style="font-size: 14px; margin: 0;"><strong>Site Code:</strong> ${alarm.sitecode}</p>
                </div>
              `;
            });

            tooltipContent += '</div>';
            return tooltipContent;
          }
        },
        legend: {
          top: '5%',
          left: 'center'
        },
        series: [
          {
            name: 'Network Type Contributor',
            type: 'pie',
            radius: ['70%', '140%'],
            center: ['50%', '90%'],
            startAngle: 180,
            endAngle: 360,
            avoidLabelOverlap: false,
            label: {
              show: false,
              position: 'center'
            },
            emphasis: {
              label: {
                show: true,
                fontSize: '35',
                fontWeight: 'bold',
                color: '#007AC0',
              }
            },
            labelLine: {
              show: true
            },
            data: networkTypeCounts
          }
        ]
      };
    },
    calculateNetworkTypeCounts(alarms) {
      const networkTypeMap = new Map();
      
      alarms.forEach(alarm => {
        const networkType = alarm.networktype || 'Blank';
        networkTypeMap.set(networkType, (networkTypeMap.get(networkType) || 0) + 1);
      });

      return Array.from(networkTypeMap, ([name, value]) => ({ name, value }));
    }
  },
  watch: {
    active_alarm_json: {
      handler() {
        this.updateChart();
      },
      deep: true
    }
  }
};
</script>

<style scoped>
.contributor-network-card {
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
.contributor-network-card-title {
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
.contributor-network-chart-container {
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