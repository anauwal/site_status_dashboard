<template>
  <div class="pmcm-analytics-card">
    <div class="pmcm-analytics-header">
      <h2 class="pmcm-analytics-card-title">
        <span class="title-indicator"></span>
        WFM PM & CM Analytics
      </h2>
    </div>
    <div class="hud-stats"> 
      <HudNumberPMCM title="RUNNING PM" :value="runningPMCount" />
      <HudNumberPMCM title="SLA VIOLATION PM" :value="violationPMCount" />
      <HudNumberPMCM title="RUNNING CM" :value="runningCMCount" />
      <HudNumberPMCM title="SLA VIOLATION CM" :value="violationCMCount" />
      <HudNumberPMCM title="TOTAL PM CM" :value="totalRunningCount" />
    </div>
    <div class="contributor-pmcm">
      <ContributorPMCM :pm_json="pm_json" :cm_json="cm_json"/>
      <AgeingPMCM :pm_json="pm_json" :cm_json="cm_json"/>
    </div>
    <div class="analytics-cards">
      <TrendsPMCM :pm_json="pm_json" :cm_json="cm_json"/>
    </div>
  </div>
</template>
  
<script>
import TrendsPMCM from '../cards/PMCMAnalyticsCard/TrendsPMCM.vue';
import HudNumberPMCM from '../cards/PMCMAnalyticsCard/HudNumberPMCM.vue';
import ContributorPMCM from '../cards/PMCMAnalyticsCard/ContributorPMCM.vue';
import AgeingPMCM from '../cards/PMCMAnalyticsCard/AgeingPMCM.vue';

export default {
  name: 'PMCMAnalyticsCard',
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
    HudNumberPMCM,
    TrendsPMCM,
    ContributorPMCM,
    AgeingPMCM,
  },
  computed: {
    runningPMCount() {
      return this.pm_json.filter(ticket => ticket.ticketstatus === 'running').length;
    },
    violationPMCount() {
      return this.pm_json.filter(ticket => ticket.slastatus === 'sla_violation').length;
    },
    runningCMCount() {
      return this.cm_json.filter(ticket => ticket.ticketstatus === 'running').length;
    },
    violationCMCount() {
      return this.cm_json.filter(ticket => ticket.slastatus === 'sla_violation').length;
    },
    totalRunningCount() {
      return this.pm_json.filter(ticket => ticket.ticketstatus === 'completed').length + this.cm_json.filter(ticket => ticket.ticketstatus === 'completed').length;
    }
  }
};
</script>
  
  <style scoped>
  .pmcm-analytics-card {
  border: 1px solid #0297EF;
  border-radius: 5px;
  overflow: hidden;
  width: 100%;
  width: 800px;
  height: 695.33px;
  margin: 0;
  align-items: left;
  margin-top: 10px;
  margin-left: 40px;
}

.pmcm-analytics-header {
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
}

.contributor-pmcm{
  display: flex;
  margin-top : -10px;
  padding-left: 10px;
  padding-right: 10px;
  padding-bottom: 10px;
  gap: 10px;
}

  </style>
  