import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Calendar, Play } from 'lucide-react';
import api from '../services/api';
import { DailyChallenge } from '../types';
import { sound } from '../services/sound';

export const DailyChallengesPage: React.FC = () => {
  const [daily, setDaily] = useState<DailyChallenge | null>(null);
  const navigate = useNavigate();

  useEffect(() => {
    api.get('/challenges/daily').then(res => setDaily(res.data)).catch(() => {});
  }, []);

  const startDailyMatch = () => {
    sound.playClick();
    navigate('/play/quick');
  };

  if (!daily) {
    return (
      <div className="min-h-[50vh] flex items-center justify-center">
        <div className="w-10 h-10 border-4 border-emerald-500 border-t-transparent rounded-full animate-spin"></div>
      </div>
    );
  }

  return (
    <div className="max-w-4xl mx-auto px-4 py-8 space-y-8">
      <div className="glass-panel p-8 sm:p-12 rounded-3xl border border-emerald-500/40 text-center space-y-6 relative overflow-hidden">
        <div className="w-16 h-16 mx-auto rounded-2xl bg-emerald-500/20 border border-emerald-500/40 flex items-center justify-center shadow-neon-emerald">
          <Calendar className="w-8 h-8 text-emerald-400" />
        </div>

        <div className="space-y-2 max-w-xl mx-auto">
          <h1 className="text-2xl sm:text-3xl font-black text-white font-mono">{daily.title}</h1>
          <p className="text-sm text-slate-300 leading-relaxed">{daily.description}</p>
        </div>

        <div className="flex items-center justify-center gap-6 py-2">
          <div className="bg-slate-900/80 border border-slate-800 px-5 py-3 rounded-2xl">
            <span className="text-xs text-slate-400 block font-mono">BONUS XP</span>
            <span className="text-xl font-black text-amber-400 font-mono">+{daily.bonus_xp} XP</span>
          </div>

          <div className="bg-slate-900/80 border border-slate-800 px-5 py-3 rounded-2xl">
            <span className="text-xs text-slate-400 block font-mono">BONUS SCORE</span>
            <span className="text-xl font-black text-emerald-400 font-mono">+{daily.bonus_score} PTS</span>
          </div>
        </div>

        <div>
          <button
            onClick={startDailyMatch}
            className="px-8 py-3.5 rounded-xl bg-gradient-to-r from-emerald-600 to-cyan-600 hover:from-emerald-500 hover:to-cyan-500 text-white font-bold font-mono text-sm shadow-neon-emerald transition-all cursor-pointer inline-flex items-center gap-2"
          >
            <Play className="w-4 h-4 fill-white" />
            START DAILY QUEST
          </button>
        </div>
      </div>
    </div>
  );
};
