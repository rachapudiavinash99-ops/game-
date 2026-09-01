import axios from 'axios';

const host = typeof window !== 'undefined' ? window.location.hostname : '127.0.0.1';
export const API_BASE_URL = `http://${host}:8008/api/v1`;

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Request interceptor: Attach JWT token
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('gameverse_access_token');
  if (token && config.headers) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// Response interceptor: Handle 401 token refresh or logout
api.interceptors.response.use(
  (response) => response,
  async (error) => {
    const originalRequest = error.config;
    if (error.response?.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true;
      const refreshToken = localStorage.getItem('gameverse_refresh_token');
      if (refreshToken) {
        try {
          const res = await axios.post(`${API_BASE_URL}/auth/refresh`, {
            refresh_token: refreshToken,
          });
          const { access_token } = res.data;
          localStorage.setItem('gameverse_access_token', access_token);
          if (originalRequest.headers) {
            originalRequest.headers.Authorization = `Bearer ${access_token}`;
          }
          return api(originalRequest);
        } catch (refreshErr) {
          localStorage.removeItem('gameverse_access_token');
          localStorage.removeItem('gameverse_refresh_token');
          localStorage.removeItem('gameverse_user');
        }
      }
    }
    return Promise.reject(error);
  }
);

export default api;
