<template>
  <div>
    <div class="year-selector">
      <button @click="year--">◀</button>
      <span>{{ year }}년</span>
      <button @click="year++">▶</button>
    </div>

    <div v-if="stats" class="stats-content">
      <div class="summary">
        <h3>연간 총 {{ stats.total.toLocaleString() }}원</h3>
        <p v-if="stats.diff_total != null" :class="stats.diff_total > 0 ? 'up' : 'down'">
          전년 대비 {{ stats.diff_total > 0 ? '+' : '' }}{{ stats.diff_total.toLocaleString() }}원
          ({{ stats.diff_rate > 0 ? '+' : '' }}{{ stats.diff_rate }}%)
        </p>
      </div>

      <div class="chart-box">
        <h4>월별 추이</h4>
        <Bar :data="monthlyChartData" :options="chartOptions" />
      </div>

      <div class="chart-box">
        <h4>카테고리별 전년 대비</h4>
        <div v-for="c in stats.by_category" :key="c.category_id" class="diff-item">
          <span>{{ c.category_name }}</span>
          <span>{{ c.total.toLocaleString() }}원</span>
          <span v-if="c.diff != null" :class="c.diff > 0 ? 'up' : 'down'">
            {{ c.diff > 0 ? '+' : '' }}{{ c.diff.toLocaleString() }}원
            ({{ c.diff_rate != null ? (c.diff_rate > 0 ? '+' : '') + c.diff_rate + '%' : '-' }})
          </span>
        </div>
      </div>
    </div>
    <div v-else class="empty">데이터 없음</div>
  </div>
</template>

<script setup>
import { ref, computed, watch, onMounted } from 'vue'
import { Bar } from 'vue-chartjs'
import { Chart as ChartJS, CategoryScale, LinearScale, BarElement, Tooltip, Legend } from 'chart.js'
import api from '../api'

ChartJS.register(CategoryScale, LinearScale, BarElement, Tooltip, Legend)

const year = ref(new Date().getFullYear())
const stats = ref(null)

const monthlyChartData = computed(() => {
  if (!stats.value) return { labels: [], datasets: [] }
  return {
    labels: stats.value.monthly.map(m => `${m.month}월`),
    datasets: [{
      label: '월별 소비',
      data: stats.value.monthly.map(m => m.amount),
      backgroundColor: '#36A2EB',
    }],
  }
})

const chartOptions = { responsive: true, plugins: { legend: { display: false } } }

async function fetchStats() {
  const { data } = await api.statistics.yearly(year.value)
  stats.value = data
}

watch(year, fetchStats)
onMounted(fetchStats)
</script>

<style scoped>
.year-selector { display: flex; align-items: center; gap: 12px; margin-bottom: 16px; }
.year-selector button { background: none; border: 1px solid #ccc; border-radius: 4px; padding: 4px 8px; cursor: pointer; }
.summary h3 { margin-bottom: 4px; }
.up { color: #e53935; }
.down { color: #1976d2; }
.chart-box { background: #fff; padding: 16px; border-radius: 8px; margin-top: 16px; }
.chart-box h4 { margin-bottom: 8px; }
.diff-item { display: flex; justify-content: space-between; padding: 4px 0; font-size: 14px; }
.empty { text-align: center; color: #999; padding: 32px; }
</style>
