<template>
    <div class="hello">
      <h1>{{ message }}</h1>
      <button @click="changeMessage">Click me</button>
    </div>
  </template>
  
  <script>
  export default {
    name: 'HelloWorld',
    data() {
      return {
        message: 'Hello, World!'
      };
    },
    methods: {
      changeMessage() {
        this.message = 'You clicked the button!';
      }
    }
  };
  </script>
  
  <style scoped>
  .hello {
    text-align: center;
  }
  
  h1 {
    color: #42b983;
  }
  
  button {
    background-color: #42b983;
    color: white;
    border: none;
    padding: 10px 20px;
    cursor: pointer;
  }
  
  button:hover {
    background-color: #349a79;
  }
  </style>
  