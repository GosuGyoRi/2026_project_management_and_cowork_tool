import apiClient from './client'
import type { Task } from '@/types'

export const tasksApi = {
  list: async (projectId: string) => {
    const { data } = await apiClient.get<Task[]>(`/api/v1/projects/${projectId}/tasks`)
    return data
  },

  create: async (projectId: string, payload: { title: string; description?: string; priority?: string; due_date?: string }) => {
    const { data } = await apiClient.post<Task>(`/api/v1/projects/${projectId}/tasks`, payload)
    return data
  },

  update: async (projectId: string, taskId: string, payload: Partial<Task>) => {
    const { data } = await apiClient.patch<Task>(`/api/v1/projects/${projectId}/tasks/${taskId}`, payload)
    return data
  },

  delete: async (projectId: string, taskId: string) => {
    await apiClient.delete(`/api/v1/projects/${projectId}/tasks/${taskId}`)
  },
}
