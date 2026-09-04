/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        game: {
          bg: '#070913',
          surface: '#0f172a',
          card: '#131c31',
          border: '#1e293b',
          accent: '#8b5cf6',
          violet: '#7c3aed',
          cyan: '#06b6d4',
          emerald: '#10b981',
          gold: '#f59e0b',
          rose: '#f43f5e',
          fuchsia: '#d946ef',
          neonPink: '#ff007a',
          neonCyan: '#00f0ff',
          neonGreen: '#00ff88'
        }
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', 'sans-serif'],
        mono: ['JetBrains Mono', 'monospace']
      },
      boxShadow: {
        'neon-indigo': '0 0 25px -3px rgba(139, 92, 246, 0.5), 0 0 10px rgba(99, 102, 241, 0.3)',
        'neon-cyan': '0 0 25px -3px rgba(6, 182, 212, 0.5), 0 0 10px rgba(0, 240, 255, 0.3)',
        'neon-gold': '0 0 25px -3px rgba(245, 158, 11, 0.5), 0 0 10px rgba(251, 191, 36, 0.3)',
        'neon-emerald': '0 0 25px -3px rgba(16, 185, 129, 0.5), 0 0 10px rgba(0, 255, 136, 0.3)',
        'neon-rose': '0 0 25px -3px rgba(244, 63, 94, 0.5), 0 0 10px rgba(255, 0, 122, 0.3)',
        'neon-fuchsia': '0 0 25px -3px rgba(217, 70, 239, 0.5), 0 0 10px rgba(255, 0, 255, 0.3)',
        'cyber-border': 'inset 0 0 15px rgba(139, 92, 246, 0.2), 0 0 20px rgba(6, 182, 212, 0.15)'
      },
      animation: {
        'pulse-slow': 'pulse 3s cubic-bezier(0.4, 0, 0.6, 1) infinite',
        'glow': 'glow 2s ease-in-out infinite alternate',
        'float': 'float 3.5s ease-in-out infinite',
        'float-slow': 'float 6s ease-in-out infinite',
        'shimmer': 'shimmer 2.5s infinite linear',
        'spin-slow': 'spin 12s linear infinite',
        'bounce-soft': 'bounceSoft 2s ease-in-out infinite',
        'pulse-glow': 'pulseGlow 2s ease-in-out infinite',
        'shake': 'shake 0.4s ease-in-out',
        'fadeInUp': 'fadeInUp 0.5s ease-out forwards',
        'scaleIn': 'scaleIn 0.4s cubic-bezier(0.16, 1, 0.3, 1) forwards'
      },
      keyframes: {
        glow: {
          '0%': { filter: 'drop-shadow(0 0 3px rgba(139,92,246,0.6))' },
          '100%': { filter: 'drop-shadow(0 0 15px rgba(6,182,212,0.9))' }
        },
        float: {
          '0%, 100%': { transform: 'translateY(0px)' },
          '50%': { transform: 'translateY(-8px)' }
        },
        bounceSoft: {
          '0%, 100%': { transform: 'translateY(0) scale(1)' },
          '50%': { transform: 'translateY(-4px) scale(1.02)' }
        },
        pulseGlow: {
          '0%, 100%': { opacity: 0.6, transform: 'scale(1)' },
          '50%': { opacity: 1, transform: 'scale(1.05)' }
        },
        shimmer: {
          '0%': { backgroundPosition: '-200% 0' },
          '100%': { backgroundPosition: '200% 0' }
        },
        shake: {
          '0%, 100%': { transform: 'translateX(0)' },
          '20%, 60%': { transform: 'translateX(-6px)' },
          '40%, 80%': { transform: 'translateX(6px)' }
        },
        fadeInUp: {
          '0%': { opacity: 0, transform: 'translateY(16px)' },
          '100%': { opacity: 1, transform: 'translateY(0)' }
        },
        scaleIn: {
          '0%': { opacity: 0, transform: 'scale(0.92)' },
          '100%': { opacity: 1, transform: 'scale(1)' }
        }
      }
    },
  },
  plugins: [],
}
