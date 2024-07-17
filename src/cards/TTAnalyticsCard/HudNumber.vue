<template>
    <div class="hud-container">
      <div class="hud-layer title">
        {{ title }}
      </div>
      <div class="hud-layer values">
        {{ value }}
      </div>
      <img class="hud-layer inner" src="../../assets/hud/inner.png" alt="Inner HUD">
      <img class="hud-layer rim" src="../../assets/hud/rim.png" alt="Rim HUD">
      <img class="hud-layer outer" src="../../assets/hud/outer.png" alt="Outer HUD">
    </div>
  </template>
  
  <script>
  export default {
    name: 'HudNumber',
    props: {
      title: {
        type: String,
        default: 'OPEN'
      },
      value: {
        type: [Number, String],
        default: 0
      }
    },
    data() {
      return {
        innerRotation: 0,
        rimRotation: 0,
        outerRotation: 0,
      };
    },
    mounted() {
      this.startRotation();
    },
    methods: {
      startRotation() {
        setInterval(() => {
          this.innerRotation += 0.5;
          this.rimRotation -= 0.3;
          this.outerRotation += 0.1;
          
          this.updateRotation('.inner', this.innerRotation);
          this.updateRotation('.rim', this.rimRotation);
          this.updateRotation('.outer', this.outerRotation);
        }, 16); 
      },
      updateRotation(selector, angle) {
        const element = this.$el.querySelector(selector);
        element.style.transform = `rotate(${angle}deg)`;
      }
    }
  };
  </script>
  
  <style scoped>
  @font-face {
    font-family: 'Solaris';
    src: url('../../assets/hud/Solaris.ttf') format('truetype');
    font-weight: normal;
    font-style: normal;
  }
  
  .hud-container {
    position: relative;
    width: 150px;
    height: 150px;
  }
  
  .hud-layer {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
  }
  
  .inner {
    z-index: 3;
  }
  
  .rim {
    z-index: 2;
  }
  
  .outer {
    z-index: 1;
  }
  
  .title {
    font-family: 'Solaris', sans-serif;
    font-size: 17px;
    top: -0.3rem;
    color: #0297EF;
    
    z-index: 4;
    width: 100%;
    text-align: center;
    position: absolute;
  }

  .values {
    font-family: 'Solaris', sans-serif;
    font-size: 40px;
    top: 3.3rem;
    color: #0297EF;
    
    z-index: 4;
    width: 100%;
    text-align: center;
    position: absolute;
  }
  
  </style>