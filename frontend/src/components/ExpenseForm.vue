<template>
  <div class="modal-overlay" @click.self="$emit('close')">
    <div class="modal">
      <h3>{{ expense ? '수정' : '등록' }}</h3>
      <form @submit.prevent="submit">
        <label>날짜 *<input type="date" v-model="form.date" required data-testid="expense-form-date" /></label>
        <label>금액 *<input type="number" v-model.number="form.amount" min="1" required data-testid="expense-form-amount" /></label>
        <label>카테고리
          <select v-model="form.category_id" data-testid="expense-form-category">
            <option :value="null">선택 안함</option>
            <option v-for="c in store.categories" :key="c.id" :value="c.id">{{ c.name }}</option>
          </select>
        </label>
        <label>카드
          <select v-model="form.card_id" data-testid="expense-form-card">
            <option :value="null">선택 안함</option>
            <option v-for="c in store.cards" :key="c.id" :value="c.id">{{ c.name }}</option>
          </select>
        </label>
        <label>사용자
          <select v-model="form.user_id" data-testid="expense-form-user">
            <option :value="null">선택 안함</option>
            <option v-for="u in store.users" :key="u.id" :value="u.id">{{ u.name }}</option>
          </select>
        </label>
        <label>메모<input type="text" v-model="form.memo" data-testid="expense-form-memo" /></label>
        <div class="actions">
          <button type="submit" data-testid="expense-form-submit">저장</button>
          <button type="button" @click="$emit('close')">취소</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { reactive } from 'vue'
import { useAppStore } from '../stores/app'

const props = defineProps({ expense: Object })
const emit = defineEmits(['save', 'close'])
const store = useAppStore()

const form = reactive({
  date: props.expense?.date || new Date().toISOString().slice(0, 10),
  amount: props.expense?.amount || null,
  category_id: props.expense?.category_id || null,
  card_id: props.expense?.card_id || null,
  user_id: props.expense?.user_id || null,
  memo: props.expense?.memo || '',
})

function submit() {
  if (!form.date || !form.amount || form.amount <= 0) return
  emit('save', { ...form })
}
</script>

<style scoped>
.modal-overlay { position: fixed; inset: 0; background: rgba(0,0,0,0.4); display: flex; align-items: center; justify-content: center; }
.modal { background: #fff; padding: 24px; border-radius: 12px; min-width: 320px; }
form { display: flex; flex-direction: column; gap: 12px; margin-top: 12px; }
label { display: flex; flex-direction: column; gap: 4px; font-size: 14px; }
input, select { padding: 8px; border: 1px solid #ccc; border-radius: 6px; }
.actions { display: flex; gap: 8px; justify-content: flex-end; margin-top: 8px; }
.actions button { padding: 8px 16px; border-radius: 6px; border: none; cursor: pointer; }
.actions button[type="submit"] { background: #1976d2; color: #fff; }
</style>
