<template>
    <div class="trends-tt-card">
      <div class="trends-tt-card-title">
        <span class="title-indicator"></span>
        TT Trends History
      </div>
      <div class="trends-tt-chart-container">
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
    name: 'TrendsTTChart',
    props: {
      trouble_ticket_json: {
          type: Object,
          default: () => ({})
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
        const dailyData = this.groupDataByDay(this.trouble_ticket_json);
        this.updateChartOption(dailyData);
      },
      groupDataByDay(data) {
        const groupedData = {};
        data.forEach(item => {
          const date = item.createtime.split(' ')[0];
          if (!groupedData[date]) {
            groupedData[date] = { total: 0, Minor: 0, Major: 0, Critical: 0, 'No Severity': 0 };
          }
          groupedData[date].total += 1;
          
          const severity = item.enm_severity ? item.enm_severity.trim() : 'No Severity';
          if (severity === '') {
            groupedData[date]['No Severity'] += 1;
          } else {
            groupedData[date][severity] = (groupedData[date][severity] || 0) + 1;
          }
        });
        return groupedData;
      },
      updateChartOption(dailyData) {
        const dates = Object.keys(dailyData).sort();
        const totalTT = dates.map(date => dailyData[date].total);
        const minorTT = dates.map(date => dailyData[date].Minor);
        const majorTT = dates.map(date => dailyData[date].Major);
        const criticalTT = dates.map(date => dailyData[date].Critical);
        const noSeverityTT = dates.map(date => dailyData[date]['No Severity']);
  
        this.chartOption = {
            tooltip: {
               
                hideDelay: 500,
      trigger: 'axis',
      appendToBody: true,
      enterable: true,
      formatter: (params) => {
        const date = params[0].axisValue;
        const ttForDate = this.trouble_ticket_json.filter(tt => tt.createtime.startsWith(date));
        
        const severityCounts = ttForDate.reduce((acc, tt) => {
          const severity = tt.enm_severity ? tt.enm_severity.trim() : 'No Severity';
          acc[severity] = (acc[severity] || 0) + 1;
          return acc;
        }, {});

        let tooltipContent = `
          <div style="width: 300px; max-height: 400px; overflow-y: auto; padding: 15px; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.15); background-color: #ffffff; font-family: Arial, sans-serif;">
            <div style="background-color: #007AC0; color: white; padding: 15px; margin: -15px -15px 15px -15px; border-top-left-radius: 8px; border-top-right-radius: 8px;">
              <h3 style="margin: 0; font-size: 18px;">TT Summary for ${date}</h3>
            </div>
            <p style="font-size: 16px; margin: 0 0 10px 0;"><strong>Total TTs:</strong> ${ttForDate.length}</p>
            <div style="margin-bottom: 15px;">
              <p style="font-size: 14px; margin: 0 0 5px 0;"><strong>Severity Summary:</strong></p>
              <p style="font-size: 14px; margin: 0 0 3px 0;">Minor: ${severityCounts.Minor || 0}</p>
              <p style="font-size: 14px; margin: 0 0 3px 0;">Major: ${severityCounts.Major || 0}</p>
              <p style="font-size: 14px; margin: 0 0 3px 0;">Critical: ${severityCounts.Critical || 0}</p>
              <p style="font-size: 14px; margin: 0;">No Severity: ${severityCounts['No Severity'] || 0}</p>
            </div>
        `;

        ttForDate.forEach((tt) => {
          tooltipContent += `
            <div style="border: 1px solid #e0e0e0; border-radius: 4px; padding: 10px; margin-bottom: 10px;">
                <p style="font-size: 14px; margin: 0 0 5px 0;"><strong>TT ID:</strong> ${tt.ticketid}</p>
                <p style="font-size: 14px; margin: 0 0 5px 0;"><strong>Severity:</strong> ${tt.enm_severity || 'No Severity'}</p>
                <p style="font-size: 14px; margin: 0 0 5px 0; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;"><strong>Title:</strong> ${tt.title}</p>
                <p style="font-size: 14px; margin: 0 0 5px 0;"><strong>Status:</strong> ${tt.ticketstatus}</p>
                <p style="font-size: 14px; margin: 0;"><strong>Create Time:</strong> ${tt.createtime}</p>
                <p style="font-size: 14px; margin: 0;"><strong>Close Time:</strong> ${tt.closetime}</p>
                <p style="font-size: 14px; margin: 0;"><strong>SLA Status:</strong> ${tt.slastatus}</p>
            </div>

          `;
        });

        tooltipContent += '</div>';
        return tooltipContent;
      }
    },
        grid: {
          top: '15%',
          bottom: '0%',
          left: '3%',
          right: '6%',
          containLabel: true
        },
          legend: {
            data: ['Total TT', 'Minor', 'Major', 'Critical', 'No Severity']
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
              name: 'Number of TT',
              min: 0,
              interval: 1,
            },
            {
              type: 'value',
              name: 'ENM Severity',
              min: 0,
              interval: 1,
            }
          ],
          series: [
            {
              name: 'Total TT',
              type: 'line',
              data: totalTT,
            },
            {
              name: 'Minor',
              type: 'bar',
              stack: 'ENM Severity',
              data: minorTT,
            },
            {
              name: 'Major',
              type: 'bar',
              stack: 'ENM Severity',
              data: majorTT,
            },
            {
              name: 'Critical',
              type: 'bar',
              stack: 'ENM Severity',
              data: criticalTT,
            },
            {
              name: 'No Severity',
              type: 'bar',
              stack: 'ENM Severity',
              data: noSeverityTT,
            }
          ]
        };
      }
    }
  };
  </script>

<style scoped>
.trends-tt-card {
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
.trends-tt-card-title{
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

.trends-tt-chart-container {
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
