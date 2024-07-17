<template>
  <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap" rel="stylesheet">

  <ParticlesBackground />
  <HeaderDash :dashboard_name="dashboardName"/>
  
  <div class="main-container">
    <div class="left-main-container">
      <SiteInfoCard :card_title="site_info_card_title"/>
      <AlarmAnalyticsCard :active_alarm_json="active_alarm_json"/>
      <SiteAccessAnalyticsCard :sacc_json="sacc_json"/>
    </div>
    <div class="right-main-container">
      <TTAnalyticsCard :trouble_ticket_json="trouble_ticket_json"/>
      <PMCMAnalyticsCard :pm_json="pm_json" :cm_json="cm_json"/>
    </div>
  </div>
</template>

<script>
import HeaderDash from './components/Header.vue'
import ParticlesBackground from './components/ParticlesBackground.vue'
// CARD
import SiteInfoCard from './components/SiteInfoCard.vue'
import TTAnalyticsCard from './components/TTAnalyticsCard.vue'
import AlarmAnalyticsCard from './components/AlarmAnalyticsCard.vue';
import PMCMAnalyticsCard from './components/PMCMAnalyticsCard.vue';
import SiteAccessAnalyticsCard from './components/SiteAccessAnalyticsCard.vue';

// DATA
import ttData from './data/tt_troubleticket.json';
import alarmactiveData from './data/alarm_active.json';
import pmData from './data/wfm_pm.json';
import cmData from './data/wfm_cm.json';
import siteaccessData from './data/site_access.json';
export default {
  name: 'App',
  pageTitle: 'Dashboard',
  components: {
    HeaderDash,
    SiteInfoCard,
    ParticlesBackground,
    TTAnalyticsCard,
    AlarmAnalyticsCard,
    PMCMAnalyticsCard,
    SiteAccessAnalyticsCard,
  },
  data() {
    return {
      dashboardName: "NO SITE ID",
      site_info_card_title : "NO SITE ID",
      trouble_ticket_json : ttData,
      active_alarm_json : alarmactiveData,
      cm_json : cmData,
      pm_json : pmData,
      sacc_json : siteaccessData,
    }
  },
  created() {
    this.getSiteIdFromUrl()
  },
  mounted() {
    // document.body.style.zoom = "75%";
  },
  methods: {
    getSiteIdFromUrl() {
      const urlParams = new URLSearchParams(window.location.search)
      const siteId = urlParams.get('site_id')
      if (siteId) {
        this.dashboardName = siteId + " Site Analytics Dashboard"
        this.site_info_card_title = siteId + " Site Informations"
      }
    }
  }
}
</script>

<style>
.main-container {
  padding-top : 30px; /* chnge to 20px LATER */
  padding-left: 20px;
  padding-right: 20px;
  padding-bottom: 10px;
  display: flex;
  justify-content: flex-start; 
}

.left-main-container {
  display: flex;
  flex-flow: column nowrap;
}
.right-main-container {
  display: flex;
  flex-flow: column nowrap;
}
* {
    font-family: 'Roboto', sans-serif;
  }
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif,Inter;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
body {
  margin: 0;
  padding: 0;
}
</style>
