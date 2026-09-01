import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { 
  Gamepad2, 
  Trophy, 
  Award, 
  Flame, 
  Users, 
  User as UserIcon, 
  LogOut, 
  LogIn, 
  Shield, 
  Volume2, 
  VolumeX, 
  Sparkles,
  Calendar
} from 'lucide-react';
import { useAuth } from '../../store/useAuthStore';
import { sound } from '../../services/sound';

export const Navbar: React.FC = () => {
  const { user, isAuthenticated, isAdmin, logout } = useAuth();
  const navigate = useNavigate();
  const [soundEnabled, setSoundEnabled] = useState(sound.enabled);

  const toggleSound = () => {
    sound.enabled = !sound.enabled;
    setSoundEnabled(sound.enabled);
    if (sound.enabled) sound.playClick();
  };

  return (
    <nav className="sticky top-0 z-50 glass-panel border-b border-game-border/60 backdrop-blur-xl">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-16">
          {/* Brand Logo */}
          <Link to="/" className="flex items-center gap-3 group">
            <div className="w-10 h-10 rounded-xl bg-gradient-to-tr from-indigo-600 via-indigo-500 to-cyan-400 p-[2px] shadow-neon-indigo group-hover:scale-105 transition-transform">
              <div className="w-full h-full bg-[#090d16] rounded-[10px] flex items-center justify-center">
                <Gamepad2 className="w-6 h-6 text-cyan-400 group-hover:text-indigo-400 transition-colors" />
              </div>
            </div>
            <div className="flex flex-col">
              <span className="font-black text-xl tracking-wider text-transparent bg-clip-text bg-gradient-to-r from-indigo-400 via-cyan-300 to-emerald-400 font-mono">
                GAMEVERSE
              </span>
              <span className="text-[10px] text-slate-400 tracking-widest uppercase font-semibold -mt-1">
                Battle & Challenges
              </span>
            </div>
          </Link>

          {/* Navigation Links */}
          <div className="hidden md:flex items-center gap-1">
            <Link 
              to="/dashboard" 
              className="px-3 py-2 rounded-lg text-sm font-medium text-slate-300 hover:text-white hover:bg-slate-800/60 transition-colors"
            >
              Dashboard
            </Link>
            <Link 
              to="/topics" 
              className="px-3 py-2 rounded-lg text-sm font-medium text-slate-300 hover:text-white hover:bg-slate-800/60 transition-colors"
            >
              Topics
            </Link>
            <Link 
              to="/challenges/daily" 
              className="flex items-center gap-1.5 px-3 py-2 rounded-lg text-sm font-medium text-slate-300 hover:text-white hover:bg-slate-800/60 transition-colors"
            >
              <Calendar className="w-4 h-4 text-emerald-400" />
              Daily Quest
            </Link>
            <Link 
              to="/multiplayer" 
              className="flex items-center gap-1.5 px-3 py-2 rounded-lg text-sm font-medium text-indigo-400 hover:text-indigo-300 hover:bg-indigo-950/40 border border-indigo-500/20 transition-colors"
            >
              <Users className="w-4 h-4 text-indigo-400" />
              Multiplayer Arena
            </Link>
            <Link 
              to="/leaderboard" 
              className="flex items-center gap-1.5 px-3 py-2 rounded-lg text-sm font-medium text-slate-300 hover:text-white hover:bg-slate-800/60 transition-colors"
            >
              <Trophy className="w-4 h-4 text-amber-400" />
              Leaderboard
            </Link>
            <Link 
              to="/achievements" 
              className="flex items-center gap-1.5 px-3 py-2 rounded-lg text-sm font-medium text-slate-300 hover:text-white hover:bg-slate-800/60 transition-colors"
            >
              <Award className="w-4 h-4 text-rose-400" />
              Badges
            </Link>
            {isAdmin && (
              <Link 
                to="/admin" 
                className="flex items-center gap-1.5 px-3 py-2 rounded-lg text-sm font-bold text-amber-400 hover:bg-amber-950/40 border border-amber-500/30 transition-colors"
              >
                <Shield className="w-4 h-4 text-amber-400" />
                Admin Panel
              </Link>
            )}
          </div>

          {/* User Controls & Profile */}
          <div className="flex items-center gap-3">
            {/* Audio Toggle */}
            <button 
              onClick={toggleSound}
              className="p-2 rounded-lg bg-slate-800/60 hover:bg-slate-700/60 text-slate-300 transition-colors"
              title={soundEnabled ? "Mute Sound Effects" : "Enable Sound Effects"}
            >
              {soundEnabled ? <Volume2 className="w-4 h-4 text-cyan-400" /> : <VolumeX className="w-4 h-4 text-slate-500" />}
            </button>

            {isAuthenticated && user ? (
              <div className="flex items-center gap-3">
                {/* Level & XP Pill */}
                <div className="hidden sm:flex items-center gap-2 bg-slate-900/80 border border-indigo-500/30 px-3 py-1.5 rounded-full">
                  <div className="flex items-center gap-1">
                    <Sparkles className="w-3.5 h-3.5 text-amber-400" />
                    <span className="text-xs font-bold text-amber-400">LVL {user.profile?.level || 1}</span>
                  </div>
                  <div className="w-px h-3 bg-slate-700"></div>
                  <span className="text-xs font-semibold text-slate-300 font-mono">
                    {user.profile?.total_score || 0} pts
                  </span>
                </div>

                {/* Profile Link */}
                <Link to="/profile" className="flex items-center gap-2 group">
                  <img 
                    src={user.profile?.avatar_url || `https://api.dicebear.com/7.x/bottts/svg?seed=${user.username}`} 
                    alt={user.username} 
                    className="w-8 h-8 rounded-lg border border-indigo-500/40 group-hover:border-indigo-400 transition-colors"
                  />
                  <span className="hidden lg:inline text-sm font-semibold text-slate-200 group-hover:text-white">
                    {user.username}
                  </span>
                </Link>

                <button 
                  onClick={() => { logout(); navigate('/'); }}
                  className="p-2 rounded-lg bg-rose-950/30 hover:bg-rose-900/40 text-rose-400 border border-rose-800/40 transition-colors"
                  title="Logout"
                >
                  <LogOut className="w-4 h-4" />
                </button>
              </div>
            ) : (
              <div className="flex items-center gap-2">
                <Link 
                  to="/login"
                  className="px-3.5 py-1.5 rounded-lg text-sm font-semibold text-slate-200 hover:text-white hover:bg-slate-800/60 transition-colors"
                >
                  Sign In
                </Link>
                <Link 
                  to="/register"
                  className="px-4 py-1.5 rounded-lg text-sm font-bold text-white bg-gradient-to-r from-indigo-600 to-cyan-600 hover:from-indigo-500 hover:to-cyan-500 shadow-neon-indigo transition-all"
                >
                  Join Game
                </Link>
              </div>
            )}
          </div>
        </div>
      </div>
    </nav>
  );
};
