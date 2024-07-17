<template>
  <div class="alarm-analytics-card">
    <div class="alarm-analytics-header">
      <h2 class="alarm-analytics-card-title">
        <span class="title-indicator"></span>
        Active Alarm Analytics
      </h2>
    </div>
    <div class="hud-stats"> 
      <HudNumberAlarm title="TOTAL ACTIVE" :value="runningCount" />
      <HudNumberAlarm title="2G" :value="twoCount" />
      <HudNumberAlarm title="3G" :value="threeCount" />
      <HudNumberAlarm title="4G" :value="fourCount" />
      <HudNumberAlarm title="5G" :value="fiveCount" />
      <HudNumberAlarm title="OTHERS" :value="othersCount" />
    </div>
    <div class="contributor-alarm">
      <ContributorAlarm :active_alarm_json="active_alarm_json"/>
      <AgeingAlarm :active_alarm_json="active_alarm_json"/>
    </div>
    <div class="analytics-cards">
      <TrendsAlarm :active_alarm_json="active_alarm_json"/>
    </div>
  </div>
</template>
  
<script>
import TrendsAlarm from '../cards/AlarmAnalyticsCard/TrendsAlarm.vue';
import HudNumberAlarm from '../cards/AlarmAnalyticsCard/HudNumberAlarm.vue';

import ContributorAlarm from '../cards/AlarmAnalyticsCard/ContributorAlarm.vue';
import AgeingAlarm from '../cards/AlarmAnalyticsCard/AgeingAlarm.vue';


export default {
  name: 'AlarmAnalyticsCard',
  props: {
    active_alarm_json: {
      type: Array,
      default: () => []
    }
  },
  components: {
    HudNumberAlarm,
    TrendsAlarm,
    ContributorAlarm,
    AgeingAlarm,
  },
  computed: {
  runningCount() {
    return this.active_alarm_json.filter(alarm => alarm.cleartime === '0').length;
  },
  twoCount() {
    return this.active_alarm_json.filter(alarm => alarm.networktype === '2G').length;
  },
  threeCount() {
    return this.active_alarm_json.filter(alarm => alarm.networktype === '3G').length;
  },
  fourCount() {
    return this.active_alarm_json.filter(alarm => alarm.networktype === '4G').length;
  },
  fiveCount() {
    return this.active_alarm_json.filter(alarm => alarm.networktype === '5G').length;
  },
  othersCount() {
    return this.active_alarm_json.filter(alarm => alarm.cleartime === '0' && !['2G', '3G', '4G', '5G'].includes(alarm.networktype)).length;
  }
}

};
</script>
  
  <style scoped>
  .alarm-analytics-card {
  border: 1px solid #0297EF;
  border-radius: 5px;
  overflow: hidden;
  width: 100%;
  width: 800px;
  height: 695.33px;
  margin: 0;
  align-items: left;
  margin-top: 10px;
}

.alarm-analytics-header {
  color: #0297EF;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 50px;
}
.title-indicator {
  display: inline-block;
  width: 10px;
  height: 20px;
  background-color: #0297EF;
  margin-left: 5px;
  margin-right: 5px;
}

.analytics-cards{
  display: flex;
  padding-left: 10px;
  padding-right: 10px;
  padding-bottom: 10px;
}
.hud-stats{
  display: flex;
  padding-left: 10px;
  padding-right: 10px;
  gap: 10px;
  padding-top: 20px;
  padding-bottom: 10px;
}

.contributor-alarm{
  display: flex;
  margin-top : -10px;
  padding-left: 10px;
  padding-right: 10px;
  padding-bottom: 10px;
  gap: 10px;
}

  </style>
  