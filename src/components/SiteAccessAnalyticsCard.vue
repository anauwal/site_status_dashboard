<template>
  <div class="siteaccess-analytics-card">
    <div class="siteaccess-analytics-header">
      <h2 class="siteaccess-analytics-card-title">
        <span class="title-indicator"></span>
        Site Access Analytics
      </h2>
    </div>
    <div class="latest-activity"> 
      <LatestActivityCard :latest_sacc_json="latest_sacc_json" />
      <!-- <LatestActivityCard :latest_sacc_json="latest_sacc_json" /> -->
    </div>
    <div class="analytics-cards">
      <TrendsSiteAccess :sacc_json="sacc_json"/>
    </div>
  </div>
</template>

<script>
import TrendsSiteAccess from '../cards/SiteAccessAnalyticsCard/TrendsSiteAccess.vue';
import LatestActivityCard from '../cards/SiteAccessAnalyticsCard/LatestActivitySiteAccess.vue';

export default {
  name: 'SiteAccess',
  props: {
    sacc_json: {
      type: Array,
      default: () => []
    }
  },
  components: {
    TrendsSiteAccess,
    LatestActivityCard
  },
  computed: {
    latest_sacc_json() {
      if (this.sacc_json.length === 0) return null;
      
      return this.sacc_json.slice().sort((a, b) => {
        return new Date(b.create_time) - new Date(a.create_time);
      })[0];
    }
  }
};
</script>
  
  <style scoped>
  .siteaccess-analytics-card {
  border: 1px solid #0297EF;
  border-radius: 5px;
  overflow: hidden;
  width: 100%;
  width: 800px;
  height: 600.33px;
  margin: 0;
  align-items: left;
  margin-top: 10px;
}

.siteaccess-analytics-header {
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
  margin-top: 10px;
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

.latest-activity {
  display: flex;
  padding-left: 10px;
  padding-right: 10px;
  gap: 10px;
  justify-content: flex-start;
}
  </style>
  