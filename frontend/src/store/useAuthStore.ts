import { useState, useEffect } from 'react';
import api from '../services/api';
import { User, AuthTokens } from '../types';

export function useAuth() {
  const [user, setUser] = useState<User | null>(() => {
    const saved = localStorage.getItem('gameverse_user');
    return saved ? JSON.parse(saved) : null;
  });
  const [loading, setLoading] = useState<boolean>(true);

  const fetchProfile = async () => {
    try {
      const res = await api.get('/auth/me');
      setUser(res.data);
      localStorage.setItem('gameverse_user', JSON.stringify(res.data));
    } catch (e) {
      setUser(null);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    const token = localStorage.getItem('gameverse_access_token');
    if (token) {
      fetchProfile();
    } else {
      setLoading(false);
    }
  }, []);

  const login = (tokens: AuthTokens) => {
    localStorage.setItem('gameverse_access_token', tokens.access_token);
    localStorage.setItem('gameverse_refresh_token', tokens.refresh_token);
    fetchProfile();
  };

  const logout = () => {
    localStorage.removeItem('gameverse_access_token');
    localStorage.removeItem('gameverse_refresh_token');
    localStorage.removeItem('gameverse_user');
    setUser(null);
  };

  return {
    user,
    loading,
    isAuthenticated: !!user,
    isAdmin: user?.role === 'ADMIN',
    login,
    logout,
    refreshUser: fetchProfile
  };
}
