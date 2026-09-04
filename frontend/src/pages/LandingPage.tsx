import React, { useEffect, useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { 
  Zap, 
  Flame, 
  Clock, 
  ShieldAlert, 
  Users, 
  Trophy, 
  Sparkles, 
  ArrowRight, 
  Play, 
  Brain, 
  Code 
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
    <div className="relative overflow-hidden space-y-28 py-8">
      {/* Floating Animated Ambient Orbs */}
      <div className="ambient-orb-1 -top-20 -left-20"></div>
      <div className="ambient-orb-2 top-40 -right-20"></div>
      <div className="ambient-orb-3 top-[65%] left-[25%]"></div>

      {/* Hero Section */}
      <section className="relative pt-16 pb-12 text-center px-4 max-w-5xl mx-auto space-y-8 animate-fadeInUp">
        <div className="inline-flex items-center gap-2 px-4 py-2 rounded-full glass-panel border border-violet-500/40 text-xs font-bold text-violet-300 shadow-neon-indigo animate-float">
          <Sparkles className="w-4 h-4 text-cyan-400 animate-spin-slow" />
          <span>Next-Gen Competitive Python Gaming Platform</span>
        </div>

        <h1 className="text-4xl sm:text-6xl lg:text-7xl font-black tracking-tight text-white leading-tight">
          TEST YOUR KNOWLEDGE IN <br />
          <span className="text-transparent bg-clip-text bg-gradient-to-r from-violet-400 via-fuchsia-400 to-cyan-300 font-mono glow-text-indigo">
            REAL-TIME BATTLES
          </span>
        </h1>

        <p className="text-lg sm:text-xl text-slate-300 max-w-2xl mx-auto font-normal leading-relaxed">
          Master 15 rich technical domains across 5 competitive challenge modes. Score speed multipliers, unlock rare achievement medals, and dominate live multiplayer rooms!
        </p>

        <div className="flex flex-wrap items-center justify-center gap-5 pt-4">
          <button
            onClick={handleQuickPlay}
            className="flex items-center gap-3 px-9 py-4 rounded-2xl bg-gradient-to-r from-violet-600 via-fuchsia-600 to-cyan-500 hover:from-violet-500 hover:to-cyan-400 font-black text-white shadow-neon-indigo hover:scale-105 transition-all text-base font-mono cursor-pointer group"
          >
            <Play className="w-5 h-5 fill-white group-hover:scale-110 transition-transform" />
            PLAY QUICK MATCH
          </button>
          <Link
            to="/multiplayer"
            onClick={() => sound.playClick()}
            className="flex items-center gap-2.5 px-8 py-4 rounded-2xl glass-panel hover:bg-slate-800/90 border border-slate-700/80 text-slate-200 font-bold hover:text-white hover:border-violet-500/50 hover:shadow-neon-cyan transition-all text-base font-mono"
          >
            <Users className="w-5 h-5 text-cyan-400" />
            Multiplayer Lobby
          </Link>
        </div>
      </section>

      {/* Game Modes Grid */}
      <section className="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-12">
        <div className="text-center space-y-3">
          <h2 className="text-3xl sm:text-4xl font-black text-white font-mono tracking-wider">
            CHOOSE YOUR <span className="text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 to-violet-400 glow-text-cyan">BATTLEGROUND</span>
          </h2>
          <p className="text-slate-400 text-sm max-w-lg mx-auto">
            From high-speed countdown runs to live multiplayer showdowns and sudden-death survival.
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {/* Quick Challenge */}
          <div 
            onClick={() => { sound.playClick(); navigate('/play/quick'); }}
            className="glass-panel p-7 rounded-3xl border border-violet-500/30 hover:border-violet-500/80 hover:shadow-neon-indigo hover:-translate-y-2 transition-all duration-300 cursor-pointer group flex flex-col justify-between"
          >
            <div className="space-y-4">
              <div className="w-14 h-14 rounded-2xl bg-gradient-to-br from-violet-600/20 to-fuchsia-600/20 border border-violet-500/40 flex items-center justify-center group-hover:scale-110 transition-transform">
                <Zap className="w-7 h-7 text-violet-400" />
              </div>
              <h3 className="text-2xl font-bold text-white group-hover:text-violet-300 transition-colors font-mono">
                Quick Challenge
              </h3>
              <p className="text-slate-400 text-sm leading-relaxed">
                Randomized instant challenge across all topics with dynamic speed scoring and streak multipliers.
              </p>
            </div>
            <div className="pt-6 flex items-center justify-between text-violet-400 text-sm font-bold font-mono">
              <span>Instant Match (10 Qs)</span>
              <ArrowRight className="w-4 h-4 group-hover:translate-x-1.5 transition-transform" />
            </div>
          </div>

          {/* Topic Challenge */}
          <div 
            onClick={() => { sound.playClick(); navigate('/topics'); }}
            className="glass-panel p-7 rounded-3xl border border-cyan-500/30 hover:border-cyan-500/80 hover:shadow-neon-cyan hover:-translate-y-2 transition-all duration-300 cursor-pointer group flex flex-col justify-between"
          >
            <div className="space-y-4">
              <div className="w-14 h-14 rounded-2xl bg-gradient-to-br from-cyan-600/20 to-teal-600/20 border border-cyan-500/40 flex items-center justify-center group-hover:scale-110 transition-transform">
                <Brain className="w-7 h-7 text-cyan-400" />
              </div>
              <h3 className="text-2xl font-bold text-white group-hover:text-cyan-300 transition-colors font-mono">
                Topic Mastery
              </h3>
              <p className="text-slate-400 text-sm leading-relaxed">
                Pick specific topics and difficulty levels (Easy, Medium, Hard, Expert) to target your progression.
              </p>
            </div>
            <div className="pt-6 flex items-center justify-between text-cyan-400 text-sm font-bold font-mono">
              <span>Explore 15 Topics</span>
              <ArrowRight className="w-4 h-4 group-hover:translate-x-1.5 transition-transform" />
            </div>
          </div>

          {/* Time Attack */}
          <div 
            onClick={() => { sound.playClick(); navigate('/play/time-attack'); }}
            className="glass-panel p-7 rounded-3xl border border-amber-500/30 hover:border-amber-500/80 hover:shadow-neon-gold hover:-translate-y-2 transition-all duration-300 cursor-pointer group flex flex-col justify-between"
          >
            <div className="space-y-4">
              <div className="w-14 h-14 rounded-2xl bg-gradient-to-br from-amber-600/20 to-orange-600/20 border border-amber-500/40 flex items-center justify-center group-hover:scale-110 transition-transform">
                <Clock className="w-7 h-7 text-amber-400" />
              </div>
              <h3 className="text-2xl font-bold text-white group-hover:text-amber-300 transition-colors font-mono">
                Time Attack (60s)
              </h3>
              <p className="text-slate-400 text-sm leading-relaxed">
                Answer as many questions as possible within a high-intensity 60-second speedrun countdown.
              </p>
            </div>
            <div className="pt-6 flex items-center justify-between text-amber-400 text-sm font-bold font-mono">
              <span>Speed Blitz</span>
              <ArrowRight className="w-4 h-4 group-hover:translate-x-1.5 transition-transform" />
            </div>
          </div>

          {/* Survival Mode */}
          <div 
            onClick={() => { sound.playClick(); navigate('/play/survival'); }}
            className="glass-panel p-7 rounded-3xl border border-rose-500/30 hover:border-rose-500/80 hover:shadow-neon-rose hover:-translate-y-2 transition-all duration-300 cursor-pointer group flex flex-col justify-between"
          >
            <div className="space-y-4">
              <div className="w-14 h-14 rounded-2xl bg-gradient-to-br from-rose-600/20 to-red-600/20 border border-rose-500/40 flex items-center justify-center group-hover:scale-110 transition-transform">
                <ShieldAlert className="w-7 h-7 text-rose-400" />
              </div>
              <h3 className="text-2xl font-bold text-white group-hover:text-rose-300 transition-colors font-mono">
                Survival Mode
              </h3>
              <p className="text-slate-400 text-sm leading-relaxed">
                Start with 3 lives. Difficulty escalates with every streak combo until your lives run out!
              </p>
            </div>
            <div className="pt-6 flex items-center justify-between text-rose-400 text-sm font-bold font-mono">
              <span>Sudden Death (3 Lives)</span>
              <ArrowRight className="w-4 h-4 group-hover:translate-x-1.5 transition-transform" />
            </div>
          </div>

          {/* Multiplayer Battle */}
          <div 
            onClick={() => { sound.playClick(); navigate('/multiplayer'); }}
            className="glass-panel p-7 rounded-3xl border border-emerald-500/30 hover:border-emerald-500/80 hover:shadow-neon-emerald hover:-translate-y-2 transition-all duration-300 cursor-pointer group flex flex-col justify-between md:col-span-2 lg:col-span-2"
          >
            <div className="space-y-4">
              <div className="w-14 h-14 rounded-2xl bg-gradient-to-br from-emerald-600/20 to-teal-600/20 border border-emerald-500/40 flex items-center justify-center group-hover:scale-110 transition-transform">
                <Users className="w-7 h-7 text-emerald-400" />
              </div>
              <h3 className="text-2xl font-bold text-white group-hover:text-emerald-300 transition-colors font-mono">
                Real-Time Multiplayer Showdown
              </h3>
              <p className="text-slate-400 text-sm leading-relaxed">
                Create or join custom rooms with real-time WebSocket connectivity. Synchronized questions, live scoreboard updates, and winner podium calculation.
              </p>
            </div>
            <div className="pt-6 flex items-center justify-between text-emerald-400 text-sm font-bold font-mono">
              <span>Enter Arena Lobby</span>
              <ArrowRight className="w-4 h-4 group-hover:translate-x-1.5 transition-transform" />
            </div>
          </div>
        </div>
      </section>
    </div>
  );
};
