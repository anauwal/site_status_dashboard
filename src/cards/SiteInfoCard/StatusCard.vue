<template>
   
    <div :class="statusCardClass">
      <div class="cascade-title">
        Cascade
      </div>
      <div :class="circleCardClass">
        {{ tech }}
      </div>
      <div class="status-container">
        Status
        <div class="status-values-container">
          <div class="up-container">
            <div class="up-label">
              UP
            </div>
            <div class="up-values">
              {{ up }}
            </div>
          </div>
          <div class="down-container">
            <div class="down-label">
              DOWN
            </div>
            <div class="down-values">
              {{ down }}
            </div>
          </div>
        </div>
      </div>  
      <div class="separator"></div>
      <div class="connected-container">
        <div class="connected-label">
          Nr. Tech
        </div>
        <div class="connected-values">
          {{ connected }}
        </div>
      </div>  
    </div>
  </template>
  
  <script>
  export default {
    name: 'StatusCard',
    props: {
      tech:{
        type: String,
        default: '-'
      },
      up: {
        type: Number,
        default: 0
      },
      down: {
        type: Number,
        default: 0
      },
      connected: {
        type: [Number, String],
        default: '-'
      }
    },
    computed: {
      statusCardClass() {
        if (this.connected === '-') {
          return 'status-card na';
        }else if (this.down > 0) {
          return 'status-card down-positive';
        } else if (this.down === 0) {
          return 'status-card down-zero';
        } 
        return 'status-card';
      },
      circleCardClass() {
        if (this.connected === '-') {
          return 'circle-card na';
        }else if (this.down > 0) {
          return 'circle-card down-positive';
        } else if (this.down === 0) {
          return 'circle-card down-zero';
        } 
        return 'circle-card';
      }
    }
  }
  </script>
  
  <style scoped>
  

  /* CIRCLE CARD */
  .cascade-title{
    position: absolute;
    font-size: 10px;
    left: 4.2rem;
    top: 0rem;
  }
  .circle-card {
    position: absolute;
    font-size: 15px;
    left: -0.9rem;
    top: -0.8rem;
    background-color: #EB1829;
    color: white;
    width: 30px;
    height: 30px;
    border-radius: 50%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    border: 2px solid white;
  }
  
  .circle-card.down-zero {
    background-color: #34A853;
  }
  .circle-card.down-positive {
    background-color: #EB1829;
  }
  .circle-card.na {
    background-color: #8C8A8F;
  }
  
  /* MAIN CARD */
  .status-card {
  position: relative;
  background-color: #ffebee;
  border-radius: 8px;
  padding: 10px;
  height: 60px;
  width: 170px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  font-family: Arial, sans-serif;
  display: flex;
  justify-content: space-between;
  transition: transform 0.3s ease, box-shadow 0.3s ease; /* Add transition for smooth effect */
}

.status-card::after {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-image: url('../../assets/tower.png');
  background-size: 23% auto;
  background-repeat: no-repeat;
  background-position: right bottom;
  opacity: 0.2;
  z-index: 1;
}

.status-card:hover {
  transform: scale(1.05); /* Zoom in effect */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3), 0 0 15px rgba(2, 151, 239, 0.5); /* Glow effect with new color */
}

  
  .status-card.down-positive {
    background-color: #ffebee;
  }
  
  .status-card.down-zero {
    background-color: #D1EED9;
  }
  
  .status-card.na {
    background-color: #E1DFE2;
  }
  
  .separator {
    width: 1px;
    border-right: 3px dotted #bbb;
  }
  
  .status-container {
    display: flex;
    flex-direction: column;
  }
  
  .status-values-container {
    margin-top: 5px;
    justify-content: space-between;
    display: flex;
    flex-wrap: wrap;
  }
  
  .status-values-container > * {
    margin: 2px;
  }
  
  .up-container {
    display: flex;
    flex-direction: column;
  }
  
  .up-label {
    font-size: 10px;
  }
  
  .down-container {
    display: flex;
    flex-direction: column;
  }
  
  .down-label {
    font-size: 10px;
  }
  
  .connected-container {
    display: flex;
    flex-direction: column;
  }
  
  .connected-label {
  }
  
  .connected-values {
    margin-top: 5px;
    font-size: 35px;
  }
  </style>
  