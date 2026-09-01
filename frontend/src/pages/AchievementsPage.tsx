import React, { useEffect, useState } from 'react';
import { Award, Lock, CheckCircle2 } from 'lucide-react';
import api from '../services/api';
import { Achievement } from '../types';

export const AchievementsPage: React.FC = () => {
  const [achievements, setAchievements] = useState<Achievement[]>([]);

  useEffect(() => {
    api.get('/achievements').then(res => setAchievements(res.data)).catch(() => {});
  }, []);

  return (
    <div className="max-w-6xl mx-auto px-4 py-8 space-y-8">
      <div className="text-center space-y-3">
        <h1 className="text-3xl sm:text-4xl font-black text-slate-100 font-mono tracking-wide flex items-center justify-center gap-3">
          <Award className="w-8 h-8 text-rose-400" />
          MEDALS & <span className="text-rose-400">ACHIEVEMENTS</span>
        </h1>
        <p className="text-sm text-slate-400 max-w-lg mx-auto">
          Unlock exclusive honorary badges and earn massive XP rewards for completing gaming milestones.
        </p>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-5">
        {achievements.map((ach) => (
          <div
            key={ach.id}
            className={`p-6 rounded-3xl border transition-all relative overflow-hidden flex flex-col justify-between ${
              ach.unlocked 
                ? 'glass-panel-glow border-amber-500/40' 
                : 'glass-panel border-slate-800 opacity-70'
            }`}
          >
            <div className="space-y-4">
              <div className="flex items-center justify-between">
                <div 
                  className="w-12 h-12 rounded-2xl flex items-center justify-center"
                  style={{ backgroundColor: `${ach.badge_color}20`, border: `1px solid ${ach.badge_color}40` }}
                >
                  <Award className="w-6 h-6" style={{ color: ach.badge_color }} />
                </div>

                {ach.unlocked ? (
                  <span className="flex items-center gap-1 text-xs font-bold text-emerald-400 font-mono bg-emerald-950/60 border border-emerald-500/30 px-2.5 py-1 rounded-full">
                    <CheckCircle2 className="w-3.5 h-3.5" /> UNLOCKED
                  </span>
                ) : (
                  <span className="flex items-center gap-1 text-xs font-bold text-slate-500 font-mono bg-slate-900 border border-slate-800 px-2.5 py-1 rounded-full">
                    <Lock className="w-3.5 h-3.5" /> LOCKED
                  </span>
                )}
              </div>

              <div>
                <h3 className="font-bold text-base text-white">{ach.title}</h3>
                <p className="text-xs text-slate-400 mt-1 leading-relaxed">{ach.description}</p>
              </div>
            </div>

            <div className="pt-4 mt-4 border-t border-slate-800 flex items-center justify-between text-xs font-mono">
              <span className="text-slate-500 uppercase">{ach.category}</span>
              <span className="font-bold text-amber-400">+{ach.xp_reward} XP</span>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
