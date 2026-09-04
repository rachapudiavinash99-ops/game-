import { useState, useEffect } from 'react';

export type ThemeMode = 'emerald' | 'cyber-purple' | 'crimson-inferno' | 'ocean-azure' | 'solar-gold';

export function applyTheme(theme: ThemeMode) {
  if (typeof document !== 'undefined') {
    if (theme === 'emerald') {
      document.documentElement.removeAttribute('data-theme');
    } else {
      document.documentElement.setAttribute('data-theme', theme);
    }
  }
  if (typeof localStorage !== 'undefined') {
    localStorage.setItem('gameverse_theme', theme);
  }
  window.dispatchEvent(new Event('themechange'));
}

export function useThemeStore() {
  const [currentTheme, setCurrentTheme] = useState<ThemeMode>(() => {
    if (typeof localStorage !== 'undefined') {
      return (localStorage.getItem('gameverse_theme') as ThemeMode) || 'emerald';
    }
    return 'emerald';
  });

  useEffect(() => {
    applyTheme(currentTheme);

    const handleThemeChange = () => {
      const saved = (localStorage.getItem('gameverse_theme') as ThemeMode) || 'emerald';
      setCurrentTheme(saved);
    };

    window.addEventListener('themechange', handleThemeChange);
    return () => window.removeEventListener('themechange', handleThemeChange);
  }, [currentTheme]);

  return {
    currentTheme,
    setTheme: (theme: ThemeMode) => {
      setCurrentTheme(theme);
      applyTheme(theme);
    }
  };
}
