import { defineStore } from 'pinia'
import api from '../api'

export const useAppStore = defineStore('app', {
  state: () => ({
    cards: [],
    categories: [],
    users: [],
  }),
  actions: {
    async fetchCards() {
      const { data } = await api.cards.list()
      this.cards = data
    },
    async fetchCategories() {
      const { data } = await api.categories.list()
      this.categories = data
    },
    async fetchUsers() {
      const { data } = await api.users.list()
      this.users = data
    },
    async fetchAll() {
      await Promise.all([this.fetchCards(), this.fetchCategories(), this.fetchUsers()])
    },
  },
})
