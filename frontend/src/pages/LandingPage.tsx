import React, { useEffect, useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { 
  Zap, 
  Flame, 
  Clock, 
  ShieldAlert, 
  Users, 
  Trophy, 
  ArrowRight, 
  Play, 
  Brain, 
  CheckCircle2 
} from 'lucide-react';
import api from '../services/api';
import { Topic } from '../types';
import { sound } from '../services/sound';

export const LandingPage: React.FC = () => {
  const [topics, setTopics] = useState<Topic[]>([]);
  const navigate = useNavigate();

  useEffect(() => {
    api.get('/topics').then(res => setTopics(res.data)).catch(() => {});
  }, []);

  const handleQuickPlay = () => {
    sound.playClick();
    navigate('/play/quick');
  };

  return (
    <div className="space-y-24 py-6">
      {/* Hero Section */}
      <section className="pt-14 pb-10 text-center px-4 max-w-4xl mx-auto space-y-6">
        <h1 className="text-4xl sm:text-6xl font-black tracking-tight text-white leading-tight font-mono">
          TEST YOUR <span className="text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-indigo-400">KNOWLEDGE</span>
        </h1>

        <p className="text-base sm:text-lg text-slate-300 max-w-2xl mx-auto leading-relaxed">
          Compete in real-time challenge modes, test your expertise across 15 subject categories, build score streaks, and climb the global leaderboards.
        </p>

        <div className="flex flex-wrap items-center justify-center gap-4 pt-4">
          <button
            onClick={handleQuickPlay}
            className="flex items-center gap-2.5 px-8 py-3.5 rounded-xl bg-indigo-600 hover:bg-indigo-500 font-bold text-white shadow-lg shadow-indigo-600/30 hover:scale-105 transition-all text-sm font-mono cursor-pointer"
          >
            <Play className="w-4 h-4 fill-white" />
            PLAY QUICK MATCH
          </button>
          <Link
            to="/multiplayer"
            onClick={() => sound.playClick()}
            className="flex items-center gap-2 px-7 py-3.5 rounded-xl glass-panel hover:bg-slate-800 text-slate-200 font-bold hover:text-white transition-all text-sm font-mono"
          >
            <Users className="w-4 h-4 text-blue-400" />
            Multiplayer Arena
          </Link>
        </div>
      </section>

      {/* Game Modes Grid */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-10">
        <div className="text-center space-y-2">
          <h2 className="text-2xl sm:text-3xl font-bold text-white font-mono">
            GAME MODES
          </h2>
          <p className="text-slate-400 text-sm">
            Select your preferred challenge format below
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
          {/* Quick Challenge */}
          <div 
            onClick={() => { sound.playClick(); navigate('/play/quick'); }}
            className="glass-panel p-6 rounded-2xl border border-slate-800 hover:border-indigo-500/60 hover:-translate-y-1 transition-all duration-200 cursor-pointer group flex flex-col justify-between"
          >
            <div className="space-y-3">
              <div className="w-12 h-12 rounded-xl bg-indigo-600/10 border border-indigo-500/30 flex items-center justify-center text-indigo-400 group-hover:scale-110 transition-transform">
                <Zap className="w-6 h-6" />
              </div>
              <h3 className="text-xl font-bold text-white font-mono">
                Quick Challenge
              </h3>
              <p className="text-slate-400 text-sm leading-relaxed">
                Random questions across all topics with speed bonus scoring and streak multipliers.
              </p>
            </div>
            <div className="pt-6 flex items-center justify-between text-indigo-400 text-xs font-bold font-mono">
              <span>10 Questions</span>
              <ArrowRight className="w-4 h-4 group-hover:translate-x-1 transition-transform" />
            </div>
          </div>

          {/* Topic Challenge */}
          <div 
            onClick={() => { sound.playClick(); navigate('/topics'); }}
            className="glass-panel p-6 rounded-2xl border border-slate-800 hover:border-blue-500/60 hover:-translate-y-1 transition-all duration-200 cursor-pointer group flex flex-col justify-between"
          >
            <div className="space-y-3">
              <div className="w-12 h-12 rounded-xl bg-blue-600/10 border border-blue-500/30 flex items-center justify-center text-blue-400 group-hover:scale-110 transition-transform">
                <Brain className="w-6 h-6" />
              </div>
              <h3 className="text-xl font-bold text-white font-mono">
                Topic Mastery
              </h3>
              <p className="text-slate-400 text-sm leading-relaxed">
                Focus on specific subject tracks with 20 curated questions per topic across all difficulty levels.
              </p>
            </div>
            <div className="pt-6 flex items-center justify-between text-blue-400 text-xs font-bold font-mono">
              <span>15 Topics (20 Qs Each)</span>
              <ArrowRight className="w-4 h-4 group-hover:translate-x-1 transition-transform" />
            </div>
          </div>

          {/* Time Attack */}
          <div 
            onClick={() => { sound.playClick(); navigate('/play/time-attack'); }}
            className="glass-panel p-6 rounded-2xl border border-slate-800 hover:border-amber-500/60 hover:-translate-y-1 transition-all duration-200 cursor-pointer group flex flex-col justify-between"
          >
            <div className="space-y-3">
              <div className="w-12 h-12 rounded-xl bg-amber-600/10 border border-amber-500/30 flex items-center justify-center text-amber-400 group-hover:scale-110 transition-transform">
                <Clock className="w-6 h-6" />
              </div>
              <h3 className="text-xl font-bold text-white font-mono">
                Time Attack (60s)
              </h3>
              <p className="text-slate-400 text-sm leading-relaxed">
                High-intensity 60-second speed blitz. Answer as many questions correctly as possible.
              </p>
            </div>
            <div className="pt-6 flex items-center justify-between text-amber-400 text-xs font-bold font-mono">
              <span>60s Countdown</span>
              <ArrowRight className="w-4 h-4 group-hover:translate-x-1 transition-transform" />
            </div>
          </div>

          {/* Survival Mode */}
          <div 
            onClick={() => { sound.playClick(); navigate('/play/survival'); }}
            className="glass-panel p-6 rounded-2xl border border-slate-800 hover:border-rose-500/60 hover:-translate-y-1 transition-all duration-200 cursor-pointer group flex flex-col justify-between"
          >
            <div className="space-y-3">
              <div className="w-12 h-12 rounded-xl bg-rose-600/10 border border-rose-500/30 flex items-center justify-center text-rose-400 group-hover:scale-110 transition-transform">
                <ShieldAlert className="w-6 h-6" />
              </div>
              <h3 className="text-xl font-bold text-white font-mono">
                Survival Mode
              </h3>
              <p className="text-slate-400 text-sm leading-relaxed">
                Start with 3 lives. Difficulty escalates with each streak until you run out of lives.
              </p>
            </div>
            <div className="pt-6 flex items-center justify-between text-rose-400 text-xs font-bold font-mono">
              <span>3 Lives Sudden Death</span>
              <ArrowRight className="w-4 h-4 group-hover:translate-x-1 transition-transform" />
            </div>
          </div>

          {/* Multiplayer Showdown */}
          <div 
            onClick={() => { sound.playClick(); navigate('/multiplayer'); }}
            className="glass-panel p-6 rounded-2xl border border-slate-800 hover:border-emerald-500/60 hover:-translate-y-1 transition-all duration-200 cursor-pointer group flex flex-col justify-between md:col-span-2 lg:col-span-2"
          >
            <div className="space-y-3">
              <div className="w-12 h-12 rounded-xl bg-emerald-600/10 border border-emerald-500/30 flex items-center justify-center text-emerald-400 group-hover:scale-110 transition-transform">
                <Users className="w-6 h-6" />
              </div>
              <h3 className="text-xl font-bold text-white font-mono">
                Real-Time Multiplayer
              </h3>
              <p className="text-slate-400 text-sm leading-relaxed">
                Create custom match rooms with room codes, invite friends, and compete live with synchronized questions and live scoreboard standings.
              </p>
            </div>
            <div className="pt-6 flex items-center justify-between text-emerald-400 text-xs font-bold font-mono">
              <span>Multiplayer Lobby</span>
              <ArrowRight className="w-4 h-4 group-hover:translate-x-1 transition-transform" />
            </div>
          </div>
        </div>
      </section>
    </div>
  );
};
