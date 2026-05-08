<template>
  <div>
    <div class="month-selector">
      <button @click="changeMonth(-1)">◀</button>
      <span>{{ year }}년 {{ month }}월</span>
      <button @click="changeMonth(1)">▶</button>
    </div>

    <div v-if="stats" class="stats-content">
      <div class="summary">
        <h3>총 {{ stats.total.toLocaleString() }}원</h3>
        <p v-if="stats.diff_total != null" :class="stats.diff_total > 0 ? 'up' : 'down'">
          전월 대비 {{ stats.diff_total > 0 ? '+' : '' }}{{ stats.diff_total.toLocaleString() }}원
          ({{ stats.diff_rate > 0 ? '+' : '' }}{{ stats.diff_rate }}%)
        </p>
      </div>

      <div class="charts">
        <div class="chart-box">
          <h4>카테고리별</h4>
          <Pie v-if="categoryChartData" :data="categoryChartData" />
          <div class="category-diff" v-if="stats.by_category.length">
            <div v-for="c in stats.by_category" :key="c.category_id" class="diff-item">
              <span>{{ c.category_name }}</span>
              <span>{{ c.amount.toLocaleString() }}원 ({{ c.rate }}%)</span>
              <span v-if="c.diff != null" :class="c.diff > 0 ? 'up' : 'down'">
                {{ c.diff > 0 ? '+' : '' }}{{ c.diff.toLocaleString() }}원
              </span>
            </div>
          </div>
        </div>
        <div class="chart-box">
          <h4>카드별</h4>
          <div v-for="c in stats.by_card" :key="c.card_id" class="stat-row">
            <span>{{ c.card_name }}</span>
            <span>{{ c.amount.toLocaleString() }}원 ({{ c.rate }}%)</span>
          </div>
        </div>
        <div class="chart-box">
          <h4>사용자별</h4>
          <div v-for="u in stats.by_user" :key="u.user_id" class="stat-row">
            <span>{{ u.user_name }}</span>
            <span>{{ u.amount.toLocaleString() }}원 ({{ u.rate }}%)</span>
          </div>
        </div>
      </div>
    </div>
    <div v-else class="empty">데이터 없음</div>
  </div>
</template>

<script setup>
import { ref, computed, watch, onMounted } from 'vue'
import { Pie } from 'vue-chartjs'
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from 'chart.js'
import api from '../api'

ChartJS.register(ArcElement, Tooltip, Legend)

const now = new Date()
const year = ref(now.getFullYear())
const month = ref(now.getMonth() + 1)
const stats = ref(null)

const colors = ['#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF', '#FF9F40', '#C9CBCF', '#7BC8A4']

const categoryChartData = computed(() => {
  if (!stats.value || !stats.value.by_category.length) return null
  return {
    labels: stats.value.by_category.map(c => c.category_name),
    datasets: [{
      data: stats.value.by_category.map(c => c.amount),
      backgroundColor: colors.slice(0, stats.value.by_category.length),
    }],
  }
})

function changeMonth(delta) {
  month.value += delta
  if (month.value > 12) { month.value = 1; year.value++ }
  if (month.value < 1) { month.value = 12; year.value-- }
}

async function fetchStats() {
  const { data } = await api.statistics.monthly(year.value, month.value)
  stats.value = data
}

watch([year, month], fetchStats)
onMounted(fetchStats)
</script>

<style scoped>
.month-selector { display: flex; align-items: center; gap: 12px; margin-bottom: 16px; }
.month-selector button { background: none; border: 1px solid #ccc; border-radius: 4px; padding: 4px 8px; cursor: pointer; }
.summary h3 { margin-bottom: 4px; }
.up { color: #e53935; }
.down { color: #1976d2; }
.charts { display: flex; flex-direction: column; gap: 16px; margin-top: 16px; }
.chart-box { background: #fff; padding: 16px; border-radius: 8px; }
.chart-box h4 { margin-bottom: 8px; }
.stat-row, .diff-item { display: flex; justify-content: space-between; padding: 4px 0; font-size: 14px; }
.category-diff { margin-top: 12px; border-top: 1px solid #eee; padding-top: 8px; }
.empty { text-align: center; color: #999; padding: 32px; }
</style>
