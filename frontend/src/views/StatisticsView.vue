<template>
  <div>
    <div class="tabs">
      <button :class="{ active: tab === 'monthly' }" data-testid="stats-tab-monthly" @click="tab = 'monthly'">월별</button>
      <button :class="{ active: tab === 'yearly' }" data-testid="stats-tab-yearly" @click="tab = 'yearly'">연간</button>
    </div>

    <MonthlyChart v-if="tab === 'monthly'" />
    <YearlyChart v-if="tab === 'yearly'" />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import MonthlyChart from '../components/MonthlyChart.vue'
import YearlyChart from '../components/YearlyChart.vue'

const tab = ref('monthly')
</script>

<style scoped>
.tabs { display: flex; gap: 8px; margin-bottom: 16px; }
.tabs button { padding: 8px 20px; border: 1px solid #ccc; border-radius: 8px; background: #fff; cursor: pointer; }
.tabs button.active { background: #1976d2; color: #fff; border-color: #1976d2; }
</style>
