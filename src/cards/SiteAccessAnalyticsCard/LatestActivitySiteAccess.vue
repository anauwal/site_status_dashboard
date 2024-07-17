<template>
    <div v-if="latest_sacc_json" class="latest-activity-card">
      <div class="header-activity">
        Latest Activity {{ latest_sacc_json.create_time }}
      </div>
      <div class="info-grid">
        <div class="info-item">
          <strong>Title:</strong> <span>{{ latest_sacc_json.title }}</span>
        </div>
        <div class="info-item">
          <strong>Current Phase:</strong> <span>{{ latest_sacc_json.current_phase_name }}</span>
        </div>
        <div class="info-item">
          <strong>Site:</strong> <span>{{ latest_sacc_json.site }}</span>
        </div>
        <div class="info-item">
          <strong>Status:</strong> <span>{{ latest_sacc_json.order_status }}</span>
        </div>
        <div class="info-item">
          <strong>Start Time:</strong> <span>{{ latest_sacc_json.create_time }}</span>
        </div>
        <div class="info-item">
          <strong>End Time:</strong> <span>{{ latest_sacc_json.end_time }}</span>
        </div>
        <div class="info-item">
          <strong>SLA Status:</strong> <span>{{ latest_sacc_json.sla_status }}</span>
        </div>
        <div class="info-item">
          <strong>FME Assigned:</strong> <span>{{ latest_sacc_json.fme_assigned }}</span>
        </div>
        <div class="info-item">
          <strong>FME Mobile:</strong> <span>{{ latest_sacc_json.fme_mobile }}</span>
        </div>
        <div class="info-item">
          <strong>Associated Ticket:</strong> <span>{{ latest_sacc_json.associated_ticket_required }}</span>
        </div>
        <div class="info-item alarm-container">
          <strong>Old Alarms Before Access:</strong>
          <span @mouseenter="showAlarms = true" class="alarm-hover">
            {{ alarmCount }} (hover to view)
          </span>
          <div v-if="showAlarms" class="alarm-list" @mouseleave="showAlarms = false">
            <div v-for="(alarm, index) in alarms" :key="index">
              {{ alarm.alarm_name }} ({{ alarm.alarm_id }})
            </div>
          </div>
        </div>
        <div class="info-item alarm-container">
          <strong>Current Live Alarms:</strong>
          <span @mouseenter="showAlarms = true" class="alarm-hover">
            {{ alarmCount }} (hover to view)
          </span>
          <div v-if="showAlarms" class="alarm-list" @mouseleave="showAlarms = false">
            <div v-for="(alarm, index) in alarms" :key="index">
              {{ alarm.alarm_name }} ({{ alarm.alarm_id }})
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'LatestActivityCard',
    props: {
      latest_sacc_json: {
        type: Object,
        required: true
      }
    },
    data() {
      return {
        showAlarms: false
      }
    },
    computed: {
      alarms() {
        return JSON.parse(this.latest_sacc_json.alarm_list || '[]')
      },
      alarmCount() {
        return this.alarms.length
      }
    }
  }
  </script>
  
  <style scoped>
.latest-activity-card {
  border: 1px solid #ddd;
  border-radius: 8px;
  padding-bottom: 10px;
  
  max-width: 700px;
  margin: 0 auto;
  font-size: 12px;
  border: 1px solid #007AC0;
}

.header-activity{
  height: 20px;
  font-size: 16px; 
  margin-bottom: 12px;
  font-weight: bold;
  color: white;
  background-color: #007AC0;
}


.info-grid {
  padding-left: 10px;
  padding-bottom: 10px;
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 10px;
}

.info-item {
  display: flex;
  flex-direction: column;
}

.info-item strong {
  margin-bottom: 2px;
  font-size: 11px; /* Slightly smaller for labels */
}

.alarm-container {
  position: relative;
}

.alarm-hover {
  cursor: pointer;
  color: blue;
  text-decoration: underline;
  font-size: 11px; /* Consistent with other text */
}

.alarm-list {
  position: absolute;
  background-color: white;
  border: 1px solid #ddd;
  padding: 6px;
  max-height: 150px;
  overflow-y: auto;
  z-index: 1000;
  left: 0;
  top: 100%;
  min-width: 180px;
  font-size: 11px; /* Consistent small font for alarm list */
}

.alarm-list div {
  margin-bottom: 4px;
}
</style>