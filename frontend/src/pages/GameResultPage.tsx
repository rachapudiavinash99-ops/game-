import React from 'react';
import { useLocation, Link, useNavigate } from 'react-router-dom';
import { 
  Trophy, 
  Award, 
  RotateCcw, 
  Home, 
  Sparkles, 
  Clock, 
  CheckCircle2, 
  XCircle, 
  Flame 
} from 'lucide-react';
import { GameResult } from '../types';
import { sound } from '../services/sound';

export const GameResultPage: React.FC = () => {
  const location = useLocation();
  const navigate = useNavigate();
  const result: GameResult = location.state?.result;

  if (!result) {
    return (
      <div className="min-h-[60vh] flex flex-col items-center justify-center space-y-4">
        <p className="text-slate-400">No active result found.</p>
        <Link to="/dashboard" className="px-4 py-2 bg-indigo-600 rounded-xl text-white text-sm font-bold">
          Go to Dashboard
        </Link>
      </div>
    );
  }

  const isVictory = result.accuracy >= 60.0;

  return (
    <div className="max-w-2xl mx-auto px-4 py-12 space-y-8">
      {/* Outcome Header Banner */}
      <div className="text-center space-y-4">
        <div className={`w-20 h-20 mx-auto rounded-3xl flex items-center justify-center shadow-neon-${isVictory ? 'indigo' : 'rose'} ${
          isVictory ? 'bg-gradient-to-tr from-indigo-600 to-cyan-500' : 'bg-gradient-to-tr from-rose-600 to-amber-500'
        }`}>
          <Trophy className="w-10 h-10 text-white" />
        </div>

        <h1 className="text-3xl sm:text-4xl font-black text-slate-100 font-mono tracking-wide">
          {isVictory ? 'MATCH COMPLETED!' : 'CHALLENGE FINISHED'}
        </h1>
        <p className="text-sm text-slate-400">
          Mode: <span className="text-indigo-400 font-bold">{result.mode.replace('_', ' ')}</span>
        </p>
      </div>

      {/* Level Up Notification */}
      {result.level_up && (
        <div className="p-4 rounded-2xl bg-gradient-to-r from-amber-500/20 to-orange-500/20 border border-amber-500/40 flex items-center justify-center gap-3 animate-bounce">
          <Sparkles className="w-6 h-6 text-amber-400" />
          <span className="font-mono font-bold text-amber-300 text-sm">
            LEVEL UP! You reached Level {result.new_level}!
          </span>
        </div>
      )}

      {/* Results Summary Grid */}
      <div className="glass-panel p-6 sm:p-8 rounded-3xl border border-indigo-500/30 space-y-6">
        <div className="grid grid-cols-2 sm:grid-cols-4 gap-4 text-center">
          <div className="bg-slate-900/80 border border-slate-800 p-4 rounded-2xl">
            <span className="text-xs text-slate-400">Final Score</span>
            <p className="text-2xl font-black text-indigo-400 font-mono mt-1">{result.score}</p>
          </div>

          <div className="bg-slate-900/80 border border-slate-800 p-4 rounded-2xl">
            <span className="text-xs text-slate-400">XP Earned</span>
            <p className="text-2xl font-black text-cyan-400 font-mono mt-1">+{result.xp_earned}</p>
          </div>

          <div className="bg-slate-900/80 border border-slate-800 p-4 rounded-2xl">
            <span className="text-xs text-slate-400">Accuracy</span>
            <p className="text-2xl font-black text-emerald-400 font-mono mt-1">{result.accuracy}%</p>
          </div>

          <div className="bg-slate-900/80 border border-slate-800 p-4 rounded-2xl">
            <span className="text-xs text-slate-400">Best Streak</span>
            <p className="text-2xl font-black text-orange-400 font-mono mt-1 flex items-center justify-center gap-1">
              <Flame className="w-5 h-5 fill-orange-500" />
              {result.best_streak}
            </p>
          </div>
        </div>

        {/* Details Breakdown */}
        <div className="pt-4 border-t border-slate-800/80 flex items-center justify-around text-xs text-slate-400 font-mono">
          <span className="flex items-center gap-1.5 text-emerald-400">
            <CheckCircle2 className="w-4 h-4" /> {result.correct_count} Correct
          </span>
          <span className="flex items-center gap-1.5 text-rose-400">
            <XCircle className="w-4 h-4" /> {result.wrong_count} Wrong
          </span>
          <span className="flex items-center gap-1.5 text-slate-400">
            <Clock className="w-4 h-4" /> {result.time_taken_seconds}s Total
          </span>
        </div>

        {/* Unlocked Achievements */}
        {result.unlocked_achievements && result.unlocked_achievements.length > 0 && (
          <div className="pt-4 border-t border-slate-800/80 space-y-2">
            <span className="text-xs font-bold text-amber-400 uppercase tracking-wider block">
              Achievements Unlocked
            </span>
            <div className="flex flex-wrap gap-2">
              {result.unlocked_achievements.map((ach, idx) => (
                <span key={idx} className="flex items-center gap-1.5 bg-amber-500/10 border border-amber-500/30 text-amber-300 text-xs px-3 py-1.5 rounded-xl font-bold font-mono">
                  <Award className="w-4 h-4 text-amber-400" />
                  {ach}
                </span>
              ))}
            </div>
          </div>
        )}
      </div>

      {/* Action Buttons */}
      <div className="flex flex-wrap items-center justify-center gap-4">
        <button
          onClick={() => { sound.playClick(); navigate('/play/quick'); }}
          className="flex items-center gap-2 px-6 py-3 rounded-xl bg-gradient-to-r from-indigo-600 to-cyan-600 hover:from-indigo-500 hover:to-cyan-500 text-white font-bold text-sm shadow-neon-indigo transition-all cursor-pointer font-mono"
        >
          <RotateCcw className="w-4 h-4" />
          PLAY AGAIN
        </button>

        <Link
          to="/dashboard"
          onClick={() => sound.playClick()}
          className="flex items-center gap-2 px-6 py-3 rounded-xl glass-panel hover:bg-slate-800 text-slate-200 font-semibold text-sm transition-all"
        >
          <Home className="w-4 h-4 text-indigo-400" />
          Dashboard
        </Link>
      </div>
    </div>
  );
};
