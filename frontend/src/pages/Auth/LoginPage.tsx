import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { authApi } from '@/api/auth'
import { useAuthStore } from '@/store'

export default function LoginPage() {
  const navigate = useNavigate()
  const { setToken } = useAuthStore()
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    const { access_token } = await authApi.login(email, password)
    setToken(access_token)
    navigate('/dashboard')
  }

  return (
    <form onSubmit={handleSubmit}>
      <h1>로그인</h1>
      <input value={email} onChange={(e) => setEmail(e.target.value)} placeholder="이메일" type="email" required />
      <input value={password} onChange={(e) => setPassword(e.target.value)} placeholder="비밀번호" type="password" required />
      <button type="submit">로그인</button>
    </form>
  )
}
