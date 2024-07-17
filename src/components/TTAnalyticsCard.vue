<template>
  <div class="tt-analytics-card">
    <div class="tt-analytics-header">
      <h2 class="tt-analytics-card-title">
        <span class="title-indicator"></span>
        Trouble Ticket Analytics
      </h2>
    </div>
    <div class="hud-stats"> 
      <HudNumber title="RUNNING" :value="runningCount" />
      <HudNumber title="CLOSED" :value="closedCount" />
      <HudNumber title="CANCEL" :value="cancelCount" />
      <HudNumber title="VIOLATION" :value="violationCount" />
      <HudNumber title="NORMAL" :value="normalCount" />
    </div>
    <div class="contributor-tt">
      <ContributorTT :trouble_ticket_json="trouble_ticket_json"/>
      <AgeingTT :trouble_ticket_json="trouble_ticket_json"/>
    </div>
    <div class="analytics-cards">
      <TrendsTT :trouble_ticket_json="trouble_ticket_json"/>
    </div>
  </div>
</template>
  
<script>
import TrendsTT from '../cards/TTAnalyticsCard/TrendsTT.vue';
import HudNumber from '../cards/TTAnalyticsCard/HudNumber.vue';
import ContributorTT from '../cards/TTAnalyticsCard/ContributorTT.vue';
import AgeingTT from '../cards/TTAnalyticsCard/AgeingTT.vue';

export default {
  name: 'TTAnalyticsCard',
  props: {
    trouble_ticket_json: {
      type: Array,
      default: () => []
    }
  },
  components: {
    HudNumber,
    TrendsTT,
    ContributorTT,
    AgeingTT,
  },
  computed: {
    runningCount() {
      return this.trouble_ticket_json.filter(ticket => ticket.ticketstatus === 'running').length;
    },
    closedCount() {
      return this.trouble_ticket_json.filter(ticket => ticket.ticketstatus === 'completed').length;
    },
    cancelCount() {
      return this.trouble_ticket_json.filter(ticket => ticket.ticketstatus === 'cancelled').length;
    },
    violationCount() {
      return this.trouble_ticket_json.filter(ticket => ticket.slastatus === 'sla_violation').length;
    },
    normalCount() {
      return this.trouble_ticket_json.filter(ticket => ticket.slastatus === 'normal').length;
    }
  }
};
</script>
  
  <style scoped>
  .tt-analytics-card {
  border: 1px solid #0297EF;
  border-radius: 5px;
  overflow: hidden;
  width: 100%;
  width: 800px;
  height: 695.33px;
  margin: 0;
  align-items: left;
  margin-left: 40px;
}

.tt-analytics-header {
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

.contributor-tt{
  display: flex;
  margin-top : -10px;
  padding-left: 10px;
  padding-right: 10px;
  padding-bottom: 10px;
  gap: 10px;
}

  </style>
  