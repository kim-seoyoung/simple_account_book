<template>
  <div>
    <div class="header">
      <div class="month-selector">
        <button data-testid="expense-prev-month" @click="changeMonth(-1)">◀</button>
        <span>{{ year }}년 {{ month }}월</span>
        <button data-testid="expense-next-month" @click="changeMonth(1)">▶</button>
      </div>
      <button class="btn-add" data-testid="expense-add-btn" @click="showForm = true">+ 등록</button>
    </div>

    <div class="filters">
      <select v-model="filterCategory" data-testid="expense-filter-category">
        <option :value="null">전체 카테고리</option>
        <option v-for="c in store.categories" :key="c.id" :value="c.id">{{ c.name }}</option>
      </select>
      <select v-model="filterCard" data-testid="expense-filter-card">
        <option :value="null">전체 카드</option>
        <option v-for="c in store.cards" :key="c.id" :value="c.id">{{ c.name }}</option>
      </select>
      <select v-model="filterUser" data-testid="expense-filter-user">
        <option :value="null">전체 사용자</option>
        <option v-for="u in store.users" :key="u.id" :value="u.id">{{ u.name }}</option>
      </select>
    </div>

    <ExpenseList :expenses="expenses" @edit="editExpense" @delete="confirmDelete" />

    <ExpenseForm
      v-if="showForm"
      :expense="editingExpense"
      @save="saveExpense"
      @close="closeForm"
    />

    <div v-if="deleteTarget" class="modal-overlay" @click.self="deleteTarget = null">
      <div class="modal">
        <p>이 내역을 삭제하시겠습니까?</p>
        <div class="modal-actions">
          <button data-testid="expense-delete-confirm" @click="doDelete">삭제</button>
          <button @click="deleteTarget = null">취소</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, watch, onMounted } from 'vue'
import api from '../api'
import { useAppStore } from '../stores/app'
import ExpenseList from '../components/ExpenseList.vue'
import ExpenseForm from '../components/ExpenseForm.vue'

const store = useAppStore()
const now = new Date()
const year = ref(now.getFullYear())
const month = ref(now.getMonth() + 1)
const expenses = ref([])
const showForm = ref(false)
const editingExpense = ref(null)
const deleteTarget = ref(null)
const filterCategory = ref(null)
const filterCard = ref(null)
const filterUser = ref(null)

async function fetchExpenses() {
  const params = { year: year.value, month: month.value }
  if (filterCategory.value) params.category_id = filterCategory.value
  if (filterCard.value) params.card_id = filterCard.value
  if (filterUser.value) params.user_id = filterUser.value
  const { data } = await api.expenses.list(params)
  expenses.value = data
}

function changeMonth(delta) {
  month.value += delta
  if (month.value > 12) { month.value = 1; year.value++ }
  if (month.value < 1) { month.value = 12; year.value-- }
}

function editExpense(e) { editingExpense.value = e; showForm.value = true }
function closeForm() { showForm.value = false; editingExpense.value = null }
function confirmDelete(e) { deleteTarget.value = e }

async function saveExpense(data) {
  if (editingExpense.value) {
    await api.expenses.update(editingExpense.value.id, data)
  } else {
    await api.expenses.create(data)
  }
  closeForm()
  fetchExpenses()
}

async function doDelete() {
  await api.expenses.delete(deleteTarget.value.id)
  deleteTarget.value = null
  fetchExpenses()
}

watch([year, month, filterCategory, filterCard, filterUser], fetchExpenses)
onMounted(() => { store.fetchAll(); fetchExpenses() })
</script>

<style scoped>
.header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; }
.month-selector { display: flex; align-items: center; gap: 12px; }
.month-selector button { background: none; border: 1px solid #ccc; border-radius: 4px; padding: 4px 8px; cursor: pointer; }
.btn-add { background: #1976d2; color: #fff; border: none; padding: 8px 16px; border-radius: 8px; cursor: pointer; }
.filters { display: flex; gap: 8px; margin-bottom: 12px; }
.filters select { padding: 6px; border-radius: 4px; border: 1px solid #ccc; }
.modal-overlay { position: fixed; inset: 0; background: rgba(0,0,0,0.4); display: flex; align-items: center; justify-content: center; }
.modal { background: #fff; padding: 24px; border-radius: 12px; min-width: 280px; }
.modal-actions { display: flex; gap: 8px; margin-top: 16px; justify-content: flex-end; }
.modal-actions button { padding: 8px 16px; border-radius: 6px; border: none; cursor: pointer; }
.modal-actions button:first-child { background: #e53935; color: #fff; }
</style>
