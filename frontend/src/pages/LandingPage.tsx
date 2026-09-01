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
    <div className="space-y-24 py-8">
      <section className="relative overflow-hidden pt-12 pb-20 text-center px-4">
        <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[600px] h-[350px] bg-indigo-600/20 blur-[120px] rounded-full pointer-events-none"></div>

        <div className="relative max-w-4xl mx-auto space-y-6">
          <div className="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full glass-panel border border-indigo-500/30 text-xs font-semibold text-indigo-300 shadow-neon-indigo">
            <Sparkles className="w-3.5 h-3.5 text-cyan-400" />
            <span>Next-Gen Full-Stack Python Gaming Platform</span>
          </div>

          <h1 className="text-4xl sm:text-6xl lg:text-7xl font-black tracking-tight text-slate-100">
            MASTER KNOWLEDGE IN <br />
            <span className="text-transparent bg-clip-text bg-gradient-to-r from-indigo-400 via-cyan-300 to-emerald-400 font-mono glow-text-indigo">
              REAL-TIME BATTLES
            </span>
          </h1>

          <p className="text-lg sm:text-xl text-slate-400 max-w-2xl mx-auto font-normal leading-relaxed">
            Test your programming, computer science, and trivia mastery across 5 competitive game modes. Climb global leaderboards and challenge players in live WebSocket rooms.
          </p>

          <div className="flex flex-wrap items-center justify-center gap-4 pt-4">
            <button
              onClick={handleQuickPlay}
              className="flex items-center gap-2.5 px-8 py-4 rounded-xl bg-gradient-to-r from-indigo-600 via-indigo-500 to-cyan-500 hover:from-indigo-500 hover:to-cyan-400 font-bold text-white shadow-neon-indigo hover:scale-105 transition-all text-base font-mono cursor-pointer"
            >
              <Play className="w-5 h-5 fill-white" />
              PLAY QUICK MATCH
            </button>
            <Link
              to="/multiplayer"
              onClick={() => sound.playClick()}
              className="flex items-center gap-2 px-7 py-4 rounded-xl glass-panel hover:bg-slate-800/80 border border-slate-700 text-slate-200 font-semibold hover:text-white transition-all text-base"
            >
              <Users className="w-5 h-5 text-indigo-400" />
              Multiplayer Lobby
            </Link>
          </div>
        </div>
      </section>

      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-10">
        <div className="text-center space-y-3">
          <h2 className="text-3xl font-black text-slate-100 font-mono">
            CHOOSE YOUR <span className="text-indigo-400">BATTLEGROUND</span>
          </h2>
          <p className="text-slate-400 text-sm max-w-lg mx-auto">
            From frantic 60-second speedruns to live multiplayer showdowns and sudden-death survival.
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          <div 
            onClick={() => { sound.playClick(); navigate('/play/quick'); }}
            className="glass-panel p-6 rounded-2xl border border-indigo-500/20 hover:border-indigo-500/60 hover:shadow-neon-indigo transition-all cursor-pointer group flex flex-col justify-between"
          >
            <div className="space-y-4">
              <div className="w-12 h-12 rounded-xl bg-indigo-500/10 border border-indigo-500/30 flex items-center justify-center group-hover:scale-110 transition-transform">
                <Zap className="w-6 h-6 text-indigo-400" />
              </div>
              <h3 className="text-xl font-bold text-slate-100 group-hover:text-indigo-300 transition-colors">
                Quick Challenge
              </h3>
              <p className="text-slate-400 text-sm leading-relaxed">
                Randomized instant challenge across all topics with dynamic speed scoring and streak multipliers.
              </p>
            </div>
            <div className="pt-6 flex items-center justify-between text-indigo-400 text-sm font-semibold">
              <span>Instant Match</span>
              <ArrowRight className="w-4 h-4 group-hover:translate-x-1 transition-transform" />
            </div>
          </div>

          <div 
            onClick={() => { sound.playClick(); navigate('/topics'); }}
            className="glass-panel p-6 rounded-2xl border border-cyan-500/20 hover:border-cyan-500/60 hover:shadow-neon-cyan transition-all cursor-pointer group flex flex-col justify-between"
          >
            <div className="space-y-4">
              <div className="w-12 h-12 rounded-xl bg-cyan-500/10 border border-cyan-500/30 flex items-center justify-center group-hover:scale-110 transition-transform">
                <Brain className="w-6 h-6 text-cyan-400" />
              </div>
              <h3 className="text-xl font-bold text-slate-100 group-hover:text-cyan-300 transition-colors">
                Topic Mastery
              </h3>
              <p className="text-slate-400 text-sm leading-relaxed">
                Pick specific topics and difficulty levels (Easy, Medium, Hard, Expert) to target your progression.
              </p>
            </div>
            <div className="pt-6 flex items-center justify-between text-cyan-400 text-sm font-semibold">
              <span>Explore Topics</span>
              <ArrowRight className="w-4 h-4 group-hover:translate-x-1 transition-transform" />
            </div>
          </div>

          <div 
            onClick={() => { sound.playClick(); navigate('/play/time-attack'); }}
            className="glass-panel p-6 rounded-2xl border border-amber-500/20 hover:border-amber-500/60 hover:shadow-neon-gold transition-all cursor-pointer group flex flex-col justify-between"
          >
            <div className="space-y-4">
              <div className="w-12 h-12 rounded-xl bg-amber-500/10 border border-amber-500/30 flex items-center justify-center group-hover:scale-110 transition-transform">
                <Clock className="w-6 h-6 text-amber-400" />
              </div>
              <h3 className="text-xl font-bold text-slate-100 group-hover:text-amber-300 transition-colors">
                Time Attack (60s)
              </h3>
              <p className="text-slate-400 text-sm leading-relaxed">
                Answer as many questions as possible within a high-intensity 60-second countdown.
              </p>
            </div>
            <div className="pt-6 flex items-center justify-between text-amber-400 text-sm font-semibold">
              <span>Speed Challenge</span>
              <ArrowRight className="w-4 h-4 group-hover:translate-x-1 transition-transform" />
            </div>
          </div>

          <div 
            onClick={() => { sound.playClick(); navigate('/play/survival'); }}
            className="glass-panel p-6 rounded-2xl border border-rose-500/20 hover:border-rose-500/60 hover:shadow-neon-rose transition-all cursor-pointer group flex flex-col justify-between"
          >
            <div className="space-y-4">
              <div className="w-12 h-12 rounded-xl bg-rose-500/10 border border-rose-500/30 flex items-center justify-center group-hover:scale-110 transition-transform">
                <ShieldAlert className="w-6 h-6 text-rose-400" />
              </div>
              <h3 className="text-xl font-bold text-slate-100 group-hover:text-rose-300 transition-colors">
                Survival Mode
              </h3>
              <p className="text-slate-400 text-sm leading-relaxed">
                Start with 3 lives. Difficulty escalates with every streak combo until your lives run out!
              </p>
            </div>
            <div className="pt-6 flex items-center justify-between text-rose-400 text-sm font-semibold">
              <span>Sudden Death</span>
              <ArrowRight className="w-4 h-4 group-hover:translate-x-1 transition-transform" />
            </div>
          </div>

          <div 
            onClick={() => { sound.playClick(); navigate('/multiplayer'); }}
            className="glass-panel p-6 rounded-2xl border border-emerald-500/20 hover:border-emerald-500/60 hover:shadow-neon-emerald transition-all cursor-pointer group flex flex-col justify-between md:col-span-2 lg:col-span-2"
          >
            <div className="space-y-4">
              <div className="w-12 h-12 rounded-xl bg-emerald-500/10 border border-emerald-500/30 flex items-center justify-center group-hover:scale-110 transition-transform">
                <Users className="w-6 h-6 text-emerald-400" />
              </div>
              <h3 className="text-xl font-bold text-slate-100 group-hover:text-emerald-300 transition-colors">
                Real-Time Multiplayer Showdown
              </h3>
              <p className="text-slate-400 text-sm leading-relaxed">
                Create or join custom rooms with real-time WebSocket connectivity. Synchronized questions, live scoreboard updates, and winner podium calculation.
              </p>
            </div>
            <div className="pt-6 flex items-center justify-between text-emerald-400 text-sm font-semibold">
              <span>Enter Arena Lobby</span>
              <ArrowRight className="w-4 h-4 group-hover:translate-x-1 transition-transform" />
            </div>
          </div>
        </div>
      </section>
    </div>
  );
};
