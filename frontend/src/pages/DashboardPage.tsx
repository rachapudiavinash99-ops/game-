import React, { useEffect, useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { 
  Zap, 
  Flame, 
  Trophy, 
  Clock, 
  ShieldAlert, 
  Calendar, 
  History
} from 'lucide-react';
import api from '../services/api';
import { useAuth } from '../store/useAuthStore';
import { sound } from '../services/sound';
import { DailyChallenge } from '../types';

export const DashboardPage: React.FC = () => {
  const { user } = useAuth();
  const navigate = useNavigate();
  const [daily, setDaily] = useState<DailyChallenge | null>(null);
  const [recentHistory, setRecentHistory] = useState<any[]>([]);

  useEffect(() => {
    api.get('/challenges/daily').then(res => setDaily(res.data)).catch(() => {});
    api.get('/scores/my-history?limit=5').then(res => setRecentHistory(res.data)).catch(() => {});
  }, []);

  const p = user?.profile;
  const xpPercent = p ? Math.min(100, Math.round((p.current_xp / Math.max(1, p.next_level_xp)) * 100)) : 0;

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-8">
      <div className="glass-panel p-6 sm:p-8 rounded-3xl border border-indigo-500/30 relative overflow-hidden">
        <div className="absolute top-0 right-0 w-96 h-96 bg-indigo-600/10 blur-[90px] rounded-full pointer-events-none"></div>

        <div className="relative flex flex-col md:flex-row items-center md:items-start justify-between gap-6">
          <div className="flex flex-col sm:flex-row items-center gap-5 text-center sm:text-left">
            <img 
              src={p?.avatar_url || `https://api.dicebear.com/7.x/bottts/svg?seed=${user?.username || 'player'}`} 
              alt="Avatar"
              className="w-20 h-20 sm:w-24 sm:h-24 rounded-2xl border-2 border-indigo-500/60 shadow-neon-indigo"
            />
            <div className="space-y-1.5">
              <div className="flex items-center justify-center sm:justify-start gap-2">
                <h1 className="text-2xl sm:text-3xl font-black text-white font-mono">
                  {p?.display_name || user?.username || 'Guest Challenger'}
                </h1>
                <span className="bg-indigo-500/20 text-indigo-300 text-xs font-bold px-2.5 py-0.5 rounded-full border border-indigo-500/30 font-mono">
                  LVL {p?.level || 1}
                </span>
              </div>
              <p className="text-xs text-slate-400">{user?.email || 'Active Gamer'}</p>

              <div className="pt-2 w-64 sm:w-80">
                <div className="flex justify-between text-xs font-semibold text-slate-400 mb-1">
                  <span>Level Progress</span>
                  <span className="font-mono text-cyan-400">{p?.current_xp || 0} / {p?.next_level_xp || 100} XP</span>
                </div>
                <div className="w-full bg-slate-950/80 rounded-full h-2.5 p-0.5 border border-slate-800">
                  <div 
                    className="bg-gradient-to-r from-indigo-500 to-cyan-400 h-full rounded-full transition-all duration-500 shadow-neon-cyan"
                    style={{ width: `${xpPercent}%` }}
                  ></div>
                </div>
              </div>
            </div>
          </div>

          <div className="grid grid-cols-3 gap-3 sm:gap-4 w-full md:w-auto">
            <div className="bg-slate-900/80 border border-slate-800 p-3.5 rounded-2xl text-center">
              <span className="text-xs text-slate-400">Total Score</span>
              <p className="text-xl font-black text-indigo-400 font-mono">{p?.total_score || 0}</p>
            </div>
            <div className="bg-slate-900/80 border border-slate-800 p-3.5 rounded-2xl text-center">
              <span className="text-xs text-slate-400">Win Rate</span>
              <p className="text-xl font-black text-emerald-400 font-mono">{p?.win_rate || 0}%</p>
            </div>
            <div className="bg-slate-900/80 border border-slate-800 p-3.5 rounded-2xl text-center">
              <span className="text-xs text-slate-400">Best Streak</span>
              <p className="text-xl font-black text-orange-400 font-mono flex items-center justify-center gap-1">
                <Flame className="w-4 h-4 fill-orange-500" />
                {p?.best_streak || 0}
              </p>
            </div>
          </div>
        </div>
      </div>

      {daily && (
        <div className="glass-panel p-6 rounded-2xl border border-emerald-500/30 bg-gradient-to-r from-emerald-950/20 to-slate-900/80 flex flex-col sm:flex-row items-center justify-between gap-4">
          <div className="flex items-center gap-4">
            <div className="w-12 h-12 rounded-xl bg-emerald-500/20 border border-emerald-500/40 flex items-center justify-center shrink-0">
              <Calendar className="w-6 h-6 text-emerald-400" />
            </div>
            <div>
              <div className="flex items-center gap-2">
                <h3 className="font-bold text-lg text-white font-mono">{daily.title}</h3>
                {daily.is_completed && (
                  <span className="text-xs bg-emerald-500/20 text-emerald-300 font-bold px-2 py-0.5 rounded">
                    COMPLETED
                  </span>
                )}
              </div>
              <p className="text-xs text-slate-400">{daily.description}</p>
            </div>
          </div>
          <div className="flex items-center gap-3 shrink-0">
            <span className="text-xs font-bold text-amber-400 font-mono">+{daily.bonus_xp} XP</span>
            <Link
              to="/challenges/daily"
              onClick={() => sound.playClick()}
              className="px-5 py-2.5 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs shadow-neon-emerald transition-all"
            >
              {daily.is_completed ? 'View Quest' : 'Play Quest'}
            </Link>
          </div>
        </div>
      )}

      <div className="space-y-4">
        <h2 className="text-xl font-black text-slate-200 font-mono tracking-wider">
          GAME MODES
        </h2>
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
          <div 
            onClick={() => { sound.playClick(); navigate('/play/quick'); }}
            className="glass-panel p-5 rounded-2xl border border-indigo-500/20 hover:border-indigo-500/60 hover:shadow-neon-indigo transition-all cursor-pointer group"
          >
            <Zap className="w-8 h-8 text-indigo-400 mb-3 group-hover:scale-110 transition-transform" />
            <h3 className="font-bold text-white text-base">Quick Match</h3>
            <p className="text-xs text-slate-400 mt-1">Randomized quick battle</p>
          </div>

          <div 
            onClick={() => { sound.playClick(); navigate('/topics'); }}
            className="glass-panel p-5 rounded-2xl border border-cyan-500/20 hover:border-cyan-500/60 hover:shadow-neon-cyan transition-all cursor-pointer group"
          >
            <Trophy className="w-8 h-8 text-cyan-400 mb-3 group-hover:scale-110 transition-transform" />
            <h3 className="font-bold text-white text-base">Topic Challenge</h3>
            <p className="text-xs text-slate-400 mt-1">Target specific topics</p>
          </div>

          <div 
            onClick={() => { sound.playClick(); navigate('/play/time-attack'); }}
            className="glass-panel p-5 rounded-2xl border border-amber-500/20 hover:border-amber-500/60 hover:shadow-neon-gold transition-all cursor-pointer group"
          >
            <Clock className="w-8 h-8 text-amber-400 mb-3 group-hover:scale-110 transition-transform" />
            <h3 className="font-bold text-white text-base">Time Attack</h3>
            <p className="text-xs text-slate-400 mt-1">60-second speed challenge</p>
          </div>

          <div 
            onClick={() => { sound.playClick(); navigate('/play/survival'); }}
            className="glass-panel p-5 rounded-2xl border border-rose-500/20 hover:border-rose-500/60 hover:shadow-neon-rose transition-all cursor-pointer group"
          >
            <ShieldAlert className="w-8 h-8 text-rose-400 mb-3 group-hover:scale-110 transition-transform" />
            <h3 className="font-bold text-white text-base">Survival Mode</h3>
            <p className="text-xs text-slate-400 mt-1">3 lives sudden death</p>
          </div>
        </div>
      </div>

      <div className="space-y-4">
        <h2 className="text-xl font-black text-slate-200 font-mono tracking-wider flex items-center gap-2">
          <History className="w-5 h-5 text-slate-400" />
          RECENT MATCHES
        </h2>

        {recentHistory.length === 0 ? (
          <div className="glass-panel p-8 text-center text-slate-400 rounded-2xl text-sm">
            No recent matches yet. Play a game mode above to start recording your battle history!
          </div>
        ) : (
          <div className="space-y-2">
            {recentHistory.map((item) => (
              <div 
                key={item.id}
                className="glass-panel p-4 rounded-xl flex items-center justify-between border border-slate-800"
              >
                <div className="flex items-center gap-3">
                  <div className="w-9 h-9 rounded-lg bg-indigo-500/10 border border-indigo-500/30 flex items-center justify-center">
                    <Zap className="w-4 h-4 text-indigo-400" />
                  </div>
                  <div>
                    <h4 className="text-sm font-bold text-white">{item.mode.replace('_', ' ')}</h4>
                    <span className="text-xs text-slate-400">Accuracy: {item.accuracy}%</span>
                  </div>
                </div>
                <div className="text-right">
                  <span className="font-mono font-bold text-indigo-400 text-sm">{item.score} pts</span>
                  <span className="block text-[11px] text-cyan-400 font-mono">+{item.xp_earned} XP</span>
                </div>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
};
