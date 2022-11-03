import {createApp } from "vue";


const app = createApp({});

app.component('main-matrix',require('./components/Main').default)

app.mount('#app');