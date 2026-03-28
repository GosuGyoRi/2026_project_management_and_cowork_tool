// ─── 공통 타입 정의 ───────────────────────────────────────────

export interface User {
  id: string
  email: string
  username: string
  full_name: string
  avatar_url: string | null
  is_active: boolean
  created_at: string
}

export interface Workspace {
  id: string
  name: string
  slug: string
  description: string | null
  logo_url: string | null
  owner_id: string
  created_at: string
}

export interface Project {
  id: string
  workspace_id: string
  name: string
  description: string | null
  status: 'active' | 'archived' | 'completed'
  color: string | null
  start_date: string | null
  end_date: string | null
  created_by: string
  created_at: string
}

export interface Task {
  id: string
  project_id: string
  parent_task_id: string | null
  title: string
  description: string | null
  status: 'todo' | 'in_progress' | 'in_review' | 'done'
  priority: 'low' | 'medium' | 'high' | 'urgent'
  due_date: string | null
  created_by: string
  created_at: string
  updated_at: string
}

export interface Message {
  id: string
  channel_id: string
  sender_id: string
  content: string
  is_edited: boolean
  created_at: string
}

export interface Notification {
  id: string
  type: string
  title: string
  body: string | null
  is_read: boolean
  resource_id: string | null
  created_at: string
}

// API 응답 래퍼
export interface ApiResponse<T> {
  data: T
  message?: string
}

export interface PaginatedResponse<T> {
  items: T[]
  total: number
  page: number
  size: number
}
