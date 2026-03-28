import apiClient from './client'
import type { Project } from '@/types'

export const projectsApi = {
  list: async (workspaceId: string) => {
    const { data } = await apiClient.get<Project[]>(`/api/v1/workspaces/${workspaceId}/projects`)
    return data
  },

  create: async (workspaceId: string, payload: { name: string; description?: string; color?: string }) => {
    const { data } = await apiClient.post<Project>(`/api/v1/workspaces/${workspaceId}/projects`, payload)
    return data
  },

  update: async (workspaceId: string, projectId: string, payload: Partial<Project>) => {
    const { data } = await apiClient.patch<Project>(`/api/v1/workspaces/${workspaceId}/projects/${projectId}`, payload)
    return data
  },

  delete: async (workspaceId: string, projectId: string) => {
    await apiClient.delete(`/api/v1/workspaces/${workspaceId}/projects/${projectId}`)
  },
}
