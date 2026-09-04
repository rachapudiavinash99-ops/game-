import React from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { 
  Gamepad2, 
  Trophy, 
  Award, 
  Calendar, 
  Users, 
  User as UserIcon, 
  LogOut, 
  Shield, 
  Volume2, 
  VolumeX,
  Sparkles
} from 'lucide-react';
import { useAuth } from '../../store/useAuthStore';
import { sound } from '../../services/sound';

export const Navbar: React.FC = () => {
  const { user, isAuthenticated, isAdmin, logout } = useAuth();
  const [muted, setMuted] = React.useState(sound.isMuted());
  const navigate = useNavigate();

  const toggleSound = () => {
    const isNowMuted = sound.toggleMute();
    setMuted(isNowMuted);
    if (!isNowMuted) sound.playClick();
  };

  const handleLogout = () => {
    sound.playClick();
    logout();
    navigate('/login');
  };

  return (
    <header className="sticky top-0 z-50 glass-panel border-b border-white/10 backdrop-blur-xl">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
        {/* Brand Logo */}
        <Link 
          to="/" 
          onClick={() => sound.playClick()}
          className="flex items-center gap-3 group"
        >
          <div className="w-10 h-10 rounded-xl bg-gradient-to-tr from-violet-600 via-fuchsia-600 to-cyan-500 flex items-center justify-center shadow-neon-indigo group-hover:scale-110 transition-all duration-300">
            <Gamepad2 className="w-6 h-6 text-white" />
          </div>
          <div className="flex flex-col">
            <span className="font-mono font-black text-lg text-white tracking-wider group-hover:text-transparent group-hover:bg-clip-text group-hover:bg-gradient-to-r group-hover:from-violet-400 group-hover:to-cyan-300 transition-all">
              TEST YOUR KNOWLEDGE
            </span>
            <span className="text-[9px] font-mono font-bold tracking-widest text-cyan-400">
              PYTHON FULL-STACK
            </span>
          </div>
        </Link>

        {/* Center Nav Links */}
        <nav className="hidden md:flex items-center gap-1 bg-slate-900/60 p-1 rounded-2xl border border-slate-800">
          <Link
            to="/topics"
            onClick={() => sound.playClick()}
            className="px-3.5 py-1.5 rounded-xl text-xs font-bold text-slate-300 hover:text-white hover:bg-violet-600/20 transition-all flex items-center gap-1.5 font-mono"
          >
            Topics
          </Link>
          <Link
            to="/multiplayer"
            onClick={() => sound.playClick()}
            className="px-3.5 py-1.5 rounded-xl text-xs font-bold text-slate-300 hover:text-white hover:bg-cyan-600/20 transition-all flex items-center gap-1.5 font-mono"
          >
            <Users className="w-3.5 h-3.5 text-cyan-400" />
            Multiplayer
          </Link>
          <Link
            to="/leaderboard"
            onClick={() => sound.playClick()}
            className="px-3.5 py-1.5 rounded-xl text-xs font-bold text-slate-300 hover:text-white hover:bg-amber-600/20 transition-all flex items-center gap-1.5 font-mono"
          >
            <Trophy className="w-3.5 h-3.5 text-amber-400" />
            Leaderboard
          </Link>
          <Link
            to="/achievements"
            onClick={() => sound.playClick()}
            className="px-3.5 py-1.5 rounded-xl text-xs font-bold text-slate-300 hover:text-white hover:bg-rose-600/20 transition-all flex items-center gap-1.5 font-mono"
          >
            <Award className="w-3.5 h-3.5 text-rose-400" />
            Medals
          </Link>
          <Link
            to="/challenges/daily"
            onClick={() => sound.playClick()}
            className="px-3.5 py-1.5 rounded-xl text-xs font-bold text-slate-300 hover:text-white hover:bg-emerald-600/20 transition-all flex items-center gap-1.5 font-mono"
          >
            <Calendar className="w-3.5 h-3.5 text-emerald-400" />
            Daily Quest
          </Link>
        </nav>

        {/* Right Action Icons & User Status */}
        <div className="flex items-center gap-3">
          <button
            onClick={toggleSound}
            className="p-2 rounded-xl glass-panel hover:bg-slate-800 text-slate-300 hover:text-cyan-400 transition-colors cursor-pointer"
            title={muted ? "Unmute Audio" : "Mute Audio"}
          >
            {muted ? <VolumeX className="w-4 h-4 text-rose-400" /> : <Volume2 className="w-4 h-4 text-cyan-400" />}
          </button>

          {isAuthenticated ? (
            <div className="flex items-center gap-2">
              {isAdmin && (
                <Link
                  to="/admin"
                  onClick={() => sound.playClick()}
                  className="px-3 py-1.5 rounded-xl bg-amber-500/20 border border-amber-500/40 text-amber-300 text-xs font-bold font-mono hover:bg-amber-500/30 flex items-center gap-1"
                >
                  <Shield className="w-3.5 h-3.5" />
                  Admin
                </Link>
              )}

              <Link
                to="/profile"
                onClick={() => sound.playClick()}
                className="flex items-center gap-2 p-1.5 pr-3 rounded-xl glass-panel hover:border-violet-500/50 transition-all"
              >
                <img
                  src={user?.profile?.avatar_url || `https://api.dicebear.com/7.x/bottts/svg?seed=${user?.username}`}
                  alt=""
                  className="w-7 h-7 rounded-lg border border-violet-500/40"
                />
                <span className="text-xs font-bold font-mono text-white hidden sm:inline">
                  {user?.profile?.display_name || user?.username}
                </span>
              </Link>

              <button
                onClick={handleLogout}
                className="p-2 rounded-xl glass-panel hover:bg-rose-950/50 text-slate-400 hover:text-rose-400 transition-colors cursor-pointer"
                title="Sign Out"
              >
                <LogOut className="w-4 h-4" />
              </button>
            </div>
          ) : (
            <div className="flex items-center gap-2 font-mono text-xs">
              <Link
                to="/login"
                onClick={() => sound.playClick()}
                className="px-4 py-2 rounded-xl glass-panel hover:bg-slate-800 text-slate-200 font-bold transition-all"
              >
                Sign In
              </Link>
              <Link
                to="/register"
                onClick={() => sound.playClick()}
                className="px-4 py-2 rounded-xl bg-gradient-to-r from-violet-600 to-cyan-600 hover:from-violet-500 hover:to-cyan-500 text-white font-bold shadow-neon-indigo transition-all"
              >
                Register
              </Link>
            </div>
          )}
        </div>
      </div>
    </header>
  );
};
