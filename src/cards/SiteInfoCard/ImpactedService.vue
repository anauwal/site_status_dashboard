<template>
  <div class="impacted-service-card">
    <div class="impacted-service-card-title">
      <span class="title-indicator"></span>
      Impacted Service 
    </div>
    <div class="impacted-service-chart-container">
      <v-chart class="chart" :option="chartOption" autoresize />
    </div>
  </div>
</template>

<script>
import { use } from "echarts/core";
import { CanvasRenderer } from "echarts/renderers";
import { PieChart } from "echarts/charts";
import {
  TitleComponent,
  TooltipComponent,
  LegendComponent,
} from "echarts/components";
import VChart from "vue-echarts";

use([
  CanvasRenderer,
  PieChart,
  TitleComponent,
  TooltipComponent,
  LegendComponent,
]);

export default {
  name: 'ImpactedService',
  components: {
    VChart,
  },
  data() {
    return {
      service2G: [
        'N3876', 'N4229', 'N4231', 'N4232', 'N4233', 'N4234', 'N4235', 'N4236', 
        'N4237', 'N4238', 'N4239', 'N4241', 'N4243', 'N4247', 'N4250', 'N4326', 
        'N4327', 'N4328', 'N4490', 'N4496', 'N6630'
      ],
      service3G: [
        'N3876', 'N4231', 'N4233', 'N4234', 'N4237', 'N4238', 'N4250', 'N4326', 
        'N4327', 'N4490', 'N4496', 'N4857', 'N4235', 'N4229', 'N4328', 'N4236', 
        'N4616', 'N4241', 'N4247', 'N4239', 'N4232', 'N4243'
      ],
      serviceFDD: [
        'N4237', 'N4616', 'N4490', 'N4250', 'N4238', 'N4231', 'N4241', 'N4328', 
        'N4233', 'N4235', 'N4232', 'N4234', 'N4327', 'N4239', 'N4236', 'N4229', 
        'N4243', 'N3876', 'N4496', 'N4247', 'N4326', 'N4857', 'N6630'
      ],
      serviceTDD: [
        'N4237', 'N4490', 'N4496'
      ],
      serviceBC: 15,
    };
  },
  computed: {
    chartOption() {
      return {
        grid: {
          top: '0%',
          bottom: '0%',
          left: '0%',
          right: '0%'
        },
        tooltip: {
      trigger: 'item',
      appendToBody: true,
      position: [300, 0],
      enterable: true,
      formatter: (params) => {
        const serviceName = params.name;
        if (serviceName === 'BC') {
          return `<div style="width: 300px; padding: 15px; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.15); background-color: #ffffff; font-family: Arial, sans-serif;">
            <div style="background-color: #007AC0; color: white; padding: 15px; border-top-left-radius: 8px; border-top-right-radius: 8px;">
              <h3 style="margin: 0; font-size: 18px;">BC Service</h3>
            </div>
            <div style="padding: 15px;">
              <p style="font-size: 16px; margin: 0;"><strong>Count:</strong> ${params.value}</p>
            </div>
          </div>`;
        } else {
          const sites = this[`service${serviceName}`];
          const sitesList = sites.map(site => `<li>${site}</li>`).join('');
          return `<div style="width: 300px; height: 330px; overflow-y: auto; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.15); background-color: #ffffff; font-family: Arial, sans-serif;">
            <div style="background-color: #007AC0; color: white; padding: 15px; border-top-left-radius: 8px; border-top-right-radius: 8px;">
              <h3 style="margin: 0; font-size: 18px;">${serviceName} Service</h3>
            </div>
            <div style="padding: 15px;">
              <p style="font-size: 16px; margin: 0 0 10px 0;"><strong>Count:</strong> ${params.value}</p>
              <p style="font-size: 16px; margin: 0 0 5px 0;"><strong>Sites:</strong></p>
              <ul style="list-style-type: none; padding: 0; margin: 0; max-height: 180px; overflow-y: auto; border: 1px solid #e0e0e0; border-radius: 4px;">
                ${sitesList}
              </ul>
            </div>
          </div>`;
        }
      }
    },
        legend: {
          orient: 'horizontal',
          top: 0,
        },
        series: [
          {
            name: 'Impacted Service',
            type: 'pie',
            
            radius: ['40%', '70%'],
            
            data: [
              { value: this.service2G.length, name: '2G' },
              { value: this.service3G.length, name: '3G' },
              { value: this.serviceFDD.length, name: 'FDD' },
              { value: this.serviceTDD.length, name: 'TDD' },
              { value: this.serviceBC, name: 'BC' },
            ],
            itemStyle: {
              borderRadius: 10,
              borderColor: '#fff',
              borderWidth: 2
            },
            emphasis: {
              
              itemStyle: {
                shadowBlur: 10,
                shadowOffsetX: 0,
                shadowColor: 'rgba(0, 0, 0, 0.5)'
              }
            }
          }
        ]
      };
    }
  },
};
</script>

<style scoped>
.impacted-service-card {
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
.impacted-service-card-title{
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

.impacted-service-chart-container {
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