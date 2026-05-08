import axios from 'axios'

const http = axios.create({
  baseURL: import.meta.env.VITE_API_URL || 'http://localhost:8000/api',
})

export default {
  expenses: {
    list: (params) => http.get('/expenses', { params }),
    create: (data) => http.post('/expenses', data),
    update: (id, data) => http.put(`/expenses/${id}`, data),
    delete: (id) => http.delete(`/expenses/${id}`),
  },
  cards: {
    list: () => http.get('/cards'),
    create: (data) => http.post('/cards', data),
    update: (id, data) => http.put(`/cards/${id}`, data),
    delete: (id) => http.delete(`/cards/${id}`),
  },
  categories: {
    list: () => http.get('/categories'),
    create: (data) => http.post('/categories', data),
    update: (id, data) => http.put(`/categories/${id}`, data),
    delete: (id) => http.delete(`/categories/${id}`),
  },
  users: {
    list: () => http.get('/users'),
    create: (data) => http.post('/users', data),
    update: (id, data) => http.put(`/users/${id}`, data),
    delete: (id) => http.delete(`/users/${id}`),
  },
  statistics: {
    monthly: (year, month) => http.get('/statistics/monthly', { params: { year, month } }),
    yearly: (year) => http.get('/statistics/yearly', { params: { year } }),
  },
}
