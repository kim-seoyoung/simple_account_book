import { createRouter, createWebHistory } from 'vue-router'
import ExpenseView from '../views/ExpenseView.vue'
import StatisticsView from '../views/StatisticsView.vue'
import SettingsView from '../views/SettingsView.vue'

const routes = [
  { path: '/', component: ExpenseView },
  { path: '/statistics', component: StatisticsView },
  { path: '/settings', component: SettingsView },
]

export default createRouter({ history: createWebHistory(), routes })
