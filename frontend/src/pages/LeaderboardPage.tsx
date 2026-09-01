import React, { useEffect, useState } from 'react';
import { Trophy, Medal, Crown, Flame, Sparkles } from 'lucide-react';
import api from '../services/api';
import { LeaderboardEntry } from '../types';

export const LeaderboardPage: React.FC = () => {
  const [entries, setEntries] = useState<LeaderboardEntry[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    api.get('/leaderboards/global')
      .then(res => setEntries(res.data))
      .catch(() => {})
      .finally(() => setLoading(false));
  }, []);

  return (
    <div className="max-w-5xl mx-auto px-4 py-8 space-y-8">
      <div className="text-center space-y-3">
        <h1 className="text-3xl sm:text-4xl font-black text-slate-100 font-mono tracking-wide flex items-center justify-center gap-3">
          <Trophy className="w-8 h-8 text-amber-400" />
          GLOBAL <span className="text-amber-400">HALL OF FAME</span>
        </h1>
        <p className="text-sm text-slate-400 max-w-lg mx-auto">
          Top-ranked knowledge gladiators across all topics and multiplayer battles.
        </p>
      </div>

      {loading ? (
        <div className="min-h-[50vh] flex items-center justify-center">
          <div className="w-10 h-10 border-4 border-amber-500 border-t-transparent rounded-full animate-spin"></div>
        </div>
      ) : (
        <div className="space-y-6">
          {entries.length >= 3 && (
            <div className="grid grid-cols-1 md:grid-cols-3 gap-4 pt-6">
              <div className="glass-panel p-6 rounded-3xl border border-slate-700 text-center space-y-3 order-2 md:order-1">
                <div className="w-16 h-16 mx-auto rounded-2xl border-2 border-slate-400 p-0.5 relative">
                  <img src={entries[1].avatar_url} alt={entries[1].username} className="w-full h-full rounded-2xl" />
                  <span className="absolute -top-2 -right-2 w-6 h-6 bg-slate-400 text-slate-950 font-black rounded-full text-xs flex items-center justify-center font-mono">
                    2
                  </span>
                </div>
                <h3 className="font-bold text-white font-mono text-base">{entries[1].display_name}</h3>
                <span className="text-xs text-slate-400 block font-mono">LVL {entries[1].level}</span>
                <p className="text-xl font-black text-slate-300 font-mono">{entries[1].total_score} pts</p>
              </div>

              <div className="glass-panel-glow p-8 rounded-3xl border border-amber-500/50 text-center space-y-3 order-1 md:order-2 md:-translate-y-4">
                <Crown className="w-8 h-8 text-amber-400 mx-auto" />
                <div className="w-20 h-20 mx-auto rounded-2xl border-2 border-amber-400 p-0.5 shadow-neon-gold relative">
                  <img src={entries[0].avatar_url} alt={entries[0].username} className="w-full h-full rounded-2xl" />
                  <span className="absolute -top-2 -right-2 w-7 h-7 bg-amber-400 text-slate-950 font-black rounded-full text-sm flex items-center justify-center font-mono shadow-neon-gold">
                    1
                  </span>
                </div>
                <h3 className="font-bold text-white font-mono text-lg">{entries[0].display_name}</h3>
                <span className="text-xs text-amber-400 font-bold block font-mono">LVL {entries[0].level} CHAMPION</span>
                <p className="text-2xl font-black text-amber-400 font-mono">{entries[0].total_score} pts</p>
              </div>

              <div className="glass-panel p-6 rounded-3xl border border-amber-800/40 text-center space-y-3 order-3 md:order-3">
                <div className="w-16 h-16 mx-auto rounded-2xl border-2 border-amber-700 p-0.5 relative">
                  <img src={entries[2].avatar_url} alt={entries[2].username} className="w-full h-full rounded-2xl" />
                  <span className="absolute -top-2 -right-2 w-6 h-6 bg-amber-700 text-white font-black rounded-full text-xs flex items-center justify-center font-mono">
                    3
                  </span>
                </div>
                <h3 className="font-bold text-white font-mono text-base">{entries[2].display_name}</h3>
                <span className="text-xs text-slate-400 block font-mono">LVL {entries[2].level}</span>
                <p className="text-xl font-black text-amber-600 font-mono">{entries[2].total_score} pts</p>
              </div>
            </div>
          )}

          <div className="glass-panel rounded-2xl border border-slate-800 overflow-hidden">
            <table className="w-full text-left text-sm">
              <thead className="bg-slate-900/90 text-xs text-slate-400 font-mono uppercase tracking-wider border-b border-slate-800">
                <tr>
                  <th className="py-3.5 px-4 text-center">Rank</th>
                  <th className="py-3.5 px-4">Gladiator</th>
                  <th className="py-3.5 px-4 text-center">Level</th>
                  <th className="py-3.5 px-4 text-center">Win Rate</th>
                  <th className="py-3.5 px-4 text-center">Best Streak</th>
                  <th className="py-3.5 px-4 text-right">Total Score</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-slate-800 font-mono">
                {entries.map((entry) => (
                  <tr key={entry.user_id} className="hover:bg-slate-800/40 transition-colors">
                    <td className="py-3.5 px-4 text-center font-bold text-slate-400">
                      #{entry.rank}
                    </td>
                    <td className="py-3.5 px-4 flex items-center gap-3">
                      <img src={entry.avatar_url} alt="" className="w-8 h-8 rounded-lg border border-slate-700" />
                      <div>
                        <span className="font-bold text-white font-sans block">{entry.display_name}</span>
                        <span className="text-[11px] text-slate-500 font-sans">@{entry.username}</span>
                      </div>
                    </td>
                    <td className="py-3.5 px-4 text-center text-cyan-400 font-bold">
                      LVL {entry.level}
                    </td>
                    <td className="py-3.5 px-4 text-center text-emerald-400">
                      {entry.win_rate}%
                    </td>
                    <td className="py-3.5 px-4 text-center text-orange-400">
                      {entry.best_streak}
                    </td>
                    <td className="py-3.5 px-4 text-right font-black text-indigo-400">
                      {entry.total_score}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      )}
    </div>
  );
};
