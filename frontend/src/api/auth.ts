import apiClient from './client'
import type { User } from '@/types'

export const authApi = {
  login: async (email: string, password: string) => {
    const { data } = await apiClient.post<{ access_token: string }>('/api/v1/auth/login', { email, password })
    return data
  },

  register: async (email: string, username: string, full_name: string, password: string) => {
    const { data } = await apiClient.post<User>('/api/v1/auth/register', { email, username, full_name, password })
    return data
  },

  getMe: async () => {
    const { data } = await apiClient.get<User>('/api/v1/users/me')
    return data
  },
}
