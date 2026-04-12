import axios from 'axios';
import { authState } from '../store/auth';

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL || 'http://127.0.0.1:5000',
});

// Otomatis menempelkan Token JWT di setiap request
api.interceptors.request.use((config) => {
  if (authState.token) {
    config.headers.Authorization = `Bearer ${authState.token}`;
  }
  return config;
});

export default api;