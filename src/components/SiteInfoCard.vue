<template>
  <div class="site-info-card">
    <div class="site-info-header">
      <h2 class="site-info-card-title">
        <span class="title-indicator"></span>
        {{ card_title }}
      </h2>
      <div class="battery-container">
        <div class="battery-icon">
          <img :src="batteryIcon" alt="Battery" />
        </div>
        <div class="battery-label">
          {{ batteryLabel }}
        </div>
      </div>
      <div class="battery-backup-container">
        <div class="battery-backup-icon">
          {{ batteryBackupDuration }}
        </div>
        <div class="battery-backup-label">
          🗲 Backup
        </div>
      </div>
      <div class="fm-office-container">
        <div class="fm-office-icon">
          <img src="../assets/fm-office.svg" alt="FM Office" />
        </div>
        <div class="fm-office-label">
          {{ fmOffice }}
        </div>
      </div>
      <div class="site-access-container">
        <div class="site-access-icon">
          <img src="../assets/site-access.svg" alt="Site Access" />
        </div>
        <div class="site-access-label">
          {{ siteAccess }}
        </div>
      </div>
      <div class="site-vendor-container">
        <div class="site-vendor-icon">
          <img :src="vendorIcon" alt="Site Access" />
        </div>
        <div class="site-vendor-label">
          Vendor
        </div>
      </div>
      
      <div class="priority">
        <span class="priority-text">{{ priority }}</span>
        <span class="priority-label">PRIORITY</span>
      </div>
    </div>
    <div class="running-text-container">
      <table class="running-text">
        <tr>
          <th>TYPE : GF</th>
          <th>VENDOR : HUAWEI</th>
          <th>HUB : -</th>
          <th>REGION : WR</th>
          <th>FM OFFICE : Sharorah.RAN</th>
          <th>CITY : MAYSAN</th>
          <th>ADDRESS : -</th>
          <th>ACTIVE ALARMS : 3</th>
          <th>ACTIVE TICKETS : 4</th>
        </tr>
      </table>
    </div>
    <div class="whole-site-cards">
      <WholeSiteCard
        tech="2G"
        state="Up"
        :uptime="1621234567"
        :downtime="0"
      />
      <WholeSiteCard
        tech="3G"
        state="Up"
        :uptime="1621234567"
        :downtime="0"
      />
      <WholeSiteCard
        tech="4G"
        state="Up"
        :uptime="1621234567"
        :downtime="0"
      />
      <WholeSiteCard
        tech="5G"
        state="Up"
        :uptime="1621234567"
        :downtime="0"
      />
    </div>
    <div class="status-cards">
      <StatusCard :tech="'2G'" :up="20" :down="0" :connected="22" />
      <StatusCard :tech="'3G'" :up="23" :down="0" :connected="23" />
      <StatusCard4G :tech="'4G'" :up="10" :down="1" :fdd="10" :tdd="10" />
      <StatusCard :tech="'5G'" :up="'-'" :down="'-'" :connected="'-'" />
    </div>
    <div class="analytics-cards">
      <div class="active-items-card-container">
        <ActiveItem/>
      </div>
      <div class="impacted-service-container">
        <ImpactedService/>
      </div>
    </div>
  </div>
</template>

<script>
import StatusCard from '../cards/SiteInfoCard/StatusCard.vue';
import StatusCard4G from '../cards/SiteInfoCard/StatusCard4G.vue';
import ActiveItem from '../cards/SiteInfoCard/ActiveItem.vue';
import ImpactedService from '../cards/SiteInfoCard/ImpactedService.vue';
import WholeSiteCard from '../cards/SiteInfoCard/WholeSiteCard.vue';
export default {
  name: 'SiteInfoCard',
  components: {
    StatusCard,
    StatusCard4G,
    ActiveItem,
    ImpactedService,
    WholeSiteCard,
  },
  props: {
    card_title: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      batteryIcon: require('../assets/battery-full.svg'),
      batteryLabel: 'Fully Charged',
      batteryBackupDuration: 4.08,
      siteAccess: 'Required',
      fmOffice: 'AL_SHARQ_CENTER',
      priority: 'P3',
      vendorIcon: require('../assets/vendor/huawei.png')
    };
  },
  methods: {
    updateVendorIcon(vendor){
      switch (vendor){
        case 'ericsson':
          this.vendorIcon=require('../assets/vendor/ericsson.png');
          break;
        case 'huawei':
          this.vendorIcon=require('../assets/vendor/huawei.png');
          break;
        case 'nokia':
          this.vendorIcon=require('../assets/vendor/nokia.png');
          break;
        default:
          this.vendorIcon=require('../assets/vendor/huawei.png');
          break;
      }
    },
    updateBatteryStatus(status) {
      switch (status) {
        case 'low':
          this.batteryIcon = require('../assets/battery-low.svg');
          this.batteryLabel = 'Low';
          break;
        case 'medium':
          this.batteryIcon = require('../assets/battery-medium.svg');
          this.batteryLabel = 'Medium';
          break;
        case 'full':
          this.batteryIcon = require('../assets/battery-full.svg');
          this.batteryLabel = 'Fully Charged';
          break;
        case 'charging':
          this.batteryIcon = require('../assets/battery-charging.svg');
          this.batteryLabel = 'Charging';
          break;
        case 'no':
          this.batteryIcon = require('../assets/no-battery.svg');
          this.batteryLabel = 'No Battery';
          break;
        default:
          this.batteryIcon = require('../assets/no-battery.svg');
          this.batteryLabel = 'No Battery';
          break;
      }
    },
    
  },
  mounted() {
    this.updateVendorIcon('huawei')
    this.updateBatteryStatus('full');
  },
};
</script>

<style scoped>
/* ALL HEADER AND RUNNING TEXT */
.site-info-card {
  border: 1px solid #0297EF;
  border-radius: 5px;
  overflow: hidden;
  height: 695.33px;
  width: 800px;
  margin: 0;
  align-items: left;
}

.site-info-header {
  color: #0297EF;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.site-info-card-title {
  font-size: 18px;
  font-weight: bold;
  padding: 0;
  display: flex;
  align-items: center;
  margin-left: 5px;
}

.title-indicator {
  display: inline-block;
  width: 10px;
  height: 20px;
  background-color: #0297EF;
  margin-left: 5px;
  margin-right: 5px;
}

/* BATTERY */
.battery-container {
  position: absolute;
  left: 45.5em;
  top: 6.55rem;
  width: 65px;
  height: 60px;
  display: flex;
  align-items: center;
  flex-direction: column;
}

.battery-icon {
    flex-shrink: 0;
    
}

.battery-icon img {
    width: 24px;
    height: auto;
    visibility: visible;
    display: block;
    opacity: 1;
}


.battery-label {
  max-width: 100px;
  font-size: 10px;
}

/* BATTERY BACKUP  */
.battery-backup-container {
  position: absolute;
  left: 41.5em;
  top: 6.3rem;
  width: 60px;
  height: 60px;
  display: flex;
  align-items: center;
  flex-direction: column;
}
.battery-backup-container > * {
  margin-bottom: -5px; 
}
.battery-backup-icon {    
    font-size: 18px;
    font-weight: bold;
    color: #007AC0;
}

.battery-backup-label {
  max-width: 60px;
  font-size: 10px;
}

/* FM OFFICE */
.fm-office-container {
  position: absolute;
  left: 37.5em;
  top: 6.05rem;
  width: 60px;
  height: 60px;
  display: flex;
  align-items: center;
  flex-direction: column;
  overflow: hidden;
}

.fm-office-icon {
    flex-shrink: 0;
    
}

.fm-office-icon img {
    width: 24px;
    visibility: visible;
    display: block;
    opacity: 1;
}


.fm-office-label {
  max-width: 60px;
  font-size: 10px;
}

/* SITE VENDOR */
.site-vendor-container {
  position: absolute;
  left: 28.5em; /*27.5*/
  top: 6.45rem;
  width: 120px;
  height: 120px;
  display: flex;
  align-items: center;
  flex-direction: column;
  overflow: hidden;
}
.site-vendor-container > * {
  margin-bottom: 0px; 
}
.site-vendor-icon {
    flex-shrink: 0;
    
}

.site-vendor-icon img {
    width: 50px;
    visibility: visible;
    display: block;
    opacity: 1;
}


.site-vendor-label {
  max-width: 60px;
  font-size: 10px;
}
/* SITE ACCESS */
.site-access-container {
  position: absolute;
  left: 33.6em;
  top: 6.45rem;
  width: 60px;
  height: 60px;
  display: flex;
  align-items: center;
  flex-direction: column;
  overflow: hidden;
}

.site-access-icon {
    flex-shrink: 0;
    
}

.site-access-icon img {
    width: 24px;
    visibility: visible;
    display: block;
    opacity: 1;
}


.site-access-label {
  max-width: 60px;
  font-size: 10px;
}
/* PRIORITY CIRCLE */
.priority {
  position: absolute;
  left: 49rem;
  top: 4rem;
  background-color: white;
  color: #007AC0;
  width: 60px;
  height: 60px;
  border-radius: 50%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  border: 2px solid #007AC0;
  box-shadow: 0 0 0 4px white;
  overflow: hidden;
}

.priority::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 40%;
  background-color: #007AC0;
  z-index: 1;
}

.priority-text {
  font-size: 24px;
  font-weight: bold;
  line-height: 1;
  z-index: 2;
}

.priority-label {
  font-size: 8px;
  text-transform: uppercase;
  color: white;
  z-index: 2;
  margin-top: -2px;
}

.running-text-container {
  width: 100%;
  overflow: hidden;
  position: relative;
  background-color: #007AC0;
  display: flex;
  align-items: center;
  color: white;
}

.running-text {
  display: inline-block;
  white-space: nowrap;
  padding: 0;
  animation: marquee 20s linear infinite;
}

.running-text-container:hover .running-text {
  animation-play-state: paused;
}

@keyframes marquee {
  0% {
    transform: translateX(100%);
  }
  100% {
    transform: translateX(-100%);
  }
}

table {
  width: 100%;
  border-collapse: collapse;
}

th {
  text-align: left;
  font-weight: normal;
  padding: 5px;
}

/* WHOLE SITE CARDS  */
.whole-site-cards {
  padding: 5px;
  display: flex;
  justify-content: space-between;
}
.whole-site-cards > * {
  margin: 10px;
}

/* STATUS CARDS */
.status-cards {
  padding: 5px;
  display: flex;
  justify-content: center;
}

.status-cards > * {
  margin: 10px;
}

/* ANALYTICS CARDS */
.analytics-cards{
  display: flex;
  padding-left: 10px;
  padding-right: 10px;
  padding-bottom: 10px;
  gap: 10px;
}
.active-items-card-container{
  display:flex;
}
.impacted-service-card-container{
  display:flex;
}
</style>
