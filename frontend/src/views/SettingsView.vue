<template>
  <div>
    <div class="tabs">
      <button :class="{ active: tab === 'categories' }" @click="tab = 'categories'">카테고리</button>
      <button :class="{ active: tab === 'cards' }" @click="tab = 'cards'">카드</button>
      <button :class="{ active: tab === 'users' }" @click="tab = 'users'">사용자</button>
    </div>

    <!-- Categories -->
    <div v-if="tab === 'categories'" class="section">
      <div class="add-row">
        <input v-model="newName" placeholder="새 카테고리" data-testid="settings-category-input" @keyup.enter="addItem" />
        <button data-testid="settings-category-add" @click="addItem">추가</button>
      </div>
      <div v-for="item in store.categories" :key="item.id" class="list-item">
        <span>{{ item.name }}</span>
        <div>
          <button @click="startEdit(item)">✏️</button>
          <button @click="confirmDelete(item)" :disabled="item.is_default && item.name === '기타'">🗑️</button>
        </div>
      </div>
    </div>

    <!-- Cards -->
    <div v-if="tab === 'cards'" class="section">
      <div class="add-row">
        <input v-model="newName" placeholder="새 카드" data-testid="settings-card-input" @keyup.enter="addItem" />
        <button data-testid="settings-card-add" @click="addItem">추가</button>
      </div>
      <div v-for="item in store.cards" :key="item.id" class="list-item">
        <span>{{ item.name }}</span>
        <div>
          <button @click="startEdit(item)">✏️</button>
          <button @click="confirmDelete(item)">🗑️</button>
        </div>
      </div>
    </div>

    <!-- Users -->
    <div v-if="tab === 'users'" class="section">
      <div class="add-row">
        <input v-model="newName" placeholder="새 사용자" data-testid="settings-user-input" @keyup.enter="addItem" />
        <button data-testid="settings-user-add" @click="addItem">추가</button>
      </div>
      <div v-for="item in store.users" :key="item.id" class="list-item">
        <span>{{ item.name }}</span>
        <div>
          <button @click="startEdit(item)">✏️</button>
          <button @click="confirmDelete(item)">🗑️</button>
        </div>
      </div>
    </div>

    <!-- Edit Modal -->
    <div v-if="editing" class="modal-overlay" @click.self="editing = null">
      <div class="modal">
        <h4>이름 수정</h4>
        <input v-model="editName" @keyup.enter="saveEdit" />
        <div class="modal-actions">
          <button @click="saveEdit">저장</button>
          <button @click="editing = null">취소</button>
        </div>
      </div>
    </div>

    <!-- Delete Confirm -->
    <div v-if="deleting" class="modal-overlay" @click.self="deleting = null">
      <div class="modal">
        <p>"{{ deleting.name }}"을(를) 삭제하시겠습니까?</p>
        <div class="modal-actions">
          <button class="btn-danger" @click="doDelete">삭제</button>
          <button @click="deleting = null">취소</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import api from '../api'
import { useAppStore } from '../stores/app'

const store = useAppStore()
const tab = ref('categories')
const newName = ref('')
const editing = ref(null)
const editName = ref('')
const deleting = ref(null)

function getApi() {
  if (tab.value === 'categories') return api.categories
  if (tab.value === 'cards') return api.cards
  return api.users
}

function getFetch() {
  if (tab.value === 'categories') return store.fetchCategories
  if (tab.value === 'cards') return store.fetchCards
  return store.fetchUsers
}

async function addItem() {
  if (!newName.value.trim()) return
  await getApi().create({ name: newName.value.trim() })
  newName.value = ''
  getFetch()()
}

function startEdit(item) { editing.value = item; editName.value = item.name }

async function saveEdit() {
  if (!editName.value.trim()) return
  await getApi().update(editing.value.id, { name: editName.value.trim() })
  editing.value = null
  getFetch()()
}

function confirmDelete(item) { deleting.value = item }

async function doDelete() {
  await getApi().delete(deleting.value.id)
  deleting.value = null
  getFetch()()
}
</script>

<style scoped>
.tabs { display: flex; gap: 8px; margin-bottom: 16px; }
.tabs button { padding: 8px 20px; border: 1px solid #ccc; border-radius: 8px; background: #fff; cursor: pointer; }
.tabs button.active { background: #1976d2; color: #fff; border-color: #1976d2; }
.section { background: #fff; border-radius: 8px; padding: 16px; }
.add-row { display: flex; gap: 8px; margin-bottom: 12px; }
.add-row input { flex: 1; padding: 8px; border: 1px solid #ccc; border-radius: 6px; }
.add-row button { padding: 8px 16px; background: #1976d2; color: #fff; border: none; border-radius: 6px; cursor: pointer; }
.list-item { display: flex; justify-content: space-between; align-items: center; padding: 8px 0; border-bottom: 1px solid #f0f0f0; }
.list-item button { background: none; border: none; cursor: pointer; font-size: 14px; }
.modal-overlay { position: fixed; inset: 0; background: rgba(0,0,0,0.4); display: flex; align-items: center; justify-content: center; }
.modal { background: #fff; padding: 24px; border-radius: 12px; min-width: 280px; }
.modal input { width: 100%; padding: 8px; border: 1px solid #ccc; border-radius: 6px; margin-top: 8px; }
.modal-actions { display: flex; gap: 8px; margin-top: 16px; justify-content: flex-end; }
.modal-actions button { padding: 8px 16px; border-radius: 6px; border: none; cursor: pointer; }
.modal-actions button:first-child { background: #1976d2; color: #fff; }
.btn-danger { background: #e53935 !important; color: #fff; }
</style>
