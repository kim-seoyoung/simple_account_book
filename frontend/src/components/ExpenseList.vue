<template>
  <div class="expense-list">
    <div v-if="expenses.length === 0" class="empty">이 달의 소비 내역이 없습니다.</div>
    <div v-for="e in expenses" :key="e.id" class="expense-item" data-testid="expense-item">
      <div class="item-info">
        <span class="date">{{ e.date }}</span>
        <span class="category">{{ e.category_name || '-' }}</span>
        <span class="memo">{{ e.memo || '' }}</span>
      </div>
      <div class="item-right">
        <span class="amount">{{ e.amount.toLocaleString() }}원</span>
        <span class="meta">{{ e.card_name || '' }} {{ e.user_name ? `(${e.user_name})` : '' }}</span>
        <div class="item-actions">
          <button data-testid="expense-edit-btn" @click="$emit('edit', e)">✏️</button>
          <button data-testid="expense-delete-btn" @click="$emit('delete', e)">🗑️</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({ expenses: Array })
defineEmits(['edit', 'delete'])
</script>

<style scoped>
.expense-list { display: flex; flex-direction: column; gap: 8px; }
.empty { text-align: center; color: #999; padding: 32px; }
.expense-item { display: flex; justify-content: space-between; align-items: center; background: #fff; padding: 12px 16px; border-radius: 8px; }
.item-info { display: flex; gap: 12px; align-items: center; }
.date { color: #666; font-size: 13px; }
.category { background: #e3f2fd; padding: 2px 8px; border-radius: 4px; font-size: 12px; }
.item-right { display: flex; align-items: center; gap: 12px; }
.amount { font-weight: 600; }
.meta { font-size: 12px; color: #999; }
.item-actions button { background: none; border: none; cursor: pointer; font-size: 14px; }
</style>
