<template>
  <div class="site-card">
    <div class="card-header">
      <h3 class="tech">{{ tech }}</h3>
      <span :class="['status', stateClass]">{{ state }}</span>
    </div>
    <div class="card-body">
      <div class="duration-item">
        <span class="label">Uptime:</span>
        <span class="value">{{ formattedUptimeDuration }}</span>
      </div>
      <div class="duration-item">
        <span class="label">Downtime:</span>
        <span class="value">{{ formattedDowntimeDuration }}</span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'WholeSiteCard',
  props: {
    tech: {
      type: String,
      default: '-'
    },
    state: {
      type: String,
      default: '-'
    },
    uptime: {
      type: Number,
      default: null
    },
    downtime: {
      type: Number,
      default: null
    }
  },
  computed: {
    stateClass() {
      return this.state.toLowerCase() === 'up' ? 'up' : 'down';
    },
    uptimeDuration() {
      if (this.uptime) {
        const duration = Date.now() - this.uptime * 1000;
        return duration;
      }
      return null;
    },
    downtimeDuration() {
      if (this.downtime) {
        const duration = Date.now() - this.downtime * 1000;
        return duration;
      }
      return null;
    },
    formattedUptimeDuration() {
      if (this.uptimeDuration !== null) {
        return this.formatDuration(this.uptimeDuration);
      }
      return '-';
    },
    formattedDowntimeDuration() {
      if (this.downtimeDuration !== null) {
        return this.formatDuration(this.downtimeDuration);
      }
      return '-';
    }
  },
  methods: {
    formatDuration(duration) {
      const seconds = Math.floor((duration / 1000) % 60);
      const minutes = Math.floor((duration / (1000 * 60)) % 60);
      const hours = Math.floor((duration / (1000 * 60 * 60)) % 24);
      const days = Math.floor(duration / (1000 * 60 * 60 * 24));

      let formattedDuration = '';
      if (days > 0) formattedDuration += `${days}d `;
      if (hours > 0) formattedDuration += `${hours}h `;
      if (minutes > 0) formattedDuration += `${minutes}m `;
      if (seconds > 0) formattedDuration += `${seconds}s `;

      return formattedDuration.trim();
    }
  }
};
</script>

<style scoped>
.site-card {
  background-color: #ffffff;
  border-radius: 4px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  padding: 8px;
  width: 150.5px;
  height: 60px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 4px;
}

.tech {
  font-size: 14px;
  font-weight: 600;
  margin: 0;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  max-width: 70%;
}

.status {
  padding: 2px 6px;
  border-radius: 10px;
  font-size: 12px;
  font-weight: 500;
}

.status.up {
  background-color: #e6f4ea;
  color: #1e7e34;
}

.status.down {
  background-color: #fce8e6;
  color: #d50000;
}

.card-body {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.duration-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 12px;
}

.label {
  color: #5f6368;
}

.value {
  font-weight: 500;
}
</style>