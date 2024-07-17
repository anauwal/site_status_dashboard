<template>
    <div class="header">
      <img src="../assets/huawei.png" alt="Left Logo" class="left-logo" />
      <div class="title-container">
        <h1 class="dashboard-name">{{ dashboard_name }}</h1>
        <div class="datetime-container">
          <p class="datetime">{{ currentDateTime }}</p>
          <p class="hijri-datetime">{{ currentHijriDate }}</p>
        </div>
      </div>
      <img src="../assets/mobily.svg" alt="Right Logo" class="right-logo" />
    </div>
  </template>
  
  <script>
  import moment from 'moment';
  import 'moment/locale/ar'; 
  import 'moment-hijri';
  
  export default {
    name: 'HeaderDash',
    
    props: {
      dashboard_name: {
        type: String,
        required: true
      }
    },
    data() {
      return {
        currentDateTime: this.getCurrentDateTime(),
        currentHijriDate: this.getCurrentHijriDate()
      };
    },
    created() {
      this.updateDateTime();
    },
    methods: {
      getCurrentDateTime() {
        return new Date().toLocaleString('en-US'); 
      },
      getCurrentHijriDate() {
        return moment().format('iYYYY/iM/iD');
      },
      updateDateTime() {
        setInterval(() => {
          this.currentDateTime = this.getCurrentDateTime();
          this.currentHijriDate = this.getCurrentHijriDate();
        }, 1000);
      }
    }
  }
  </script>
  
  <style scoped>
  .header {
    background-color: #F3FAFE;
    text-align: center;
    height: 60px;
    display: flex;
    align-items: center;
    justify-content: space-between;
  }
  
  .left-logo{
    padding-left: 10px;
    height: 50px;
    width: auto;
  }
  .right-logo {
    height: 100px;
    width: auto;
  }
  
  .title-container {
    flex-grow: 1;
    text-align: center;
  }
  
  .dashboard-name {
    margin: 0;
    color: #0297EF;
    font-family: 'Inter', sans-serif; /* Specify Inter font */
  }
  
  .datetime-container {
    display: flex;
    justify-content: center;
    align-items: center;
  }
  
  .datetime, .hijri-datetime {
    margin: 0;
    color: #0297EF;
    font-size: 0.8em;
    margin-left: 10px; 
    
  }
  </style>
  