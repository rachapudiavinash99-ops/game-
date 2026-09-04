import React from 'react';
import { Gamepad2, Heart, Shield, Terminal, Zap } from 'lucide-react';

export const Footer: React.FC = () => {
  return (
    <footer className="border-t border-game-border/40 bg-[#060910] text-slate-400 py-10 px-4 sm:px-6 lg:px-8 mt-20">
      <div className="max-w-7xl mx-auto flex flex-col md:flex-row items-center justify-between gap-6">
        <div className="flex items-center gap-3">
          <Gamepad2 className="w-6 h-6 text-indigo-400" />
          <span className="font-bold text-slate-200 font-mono tracking-wider">TEST YOUR KNOWLEDGE</span>
          <span className="text-xs text-slate-500">| Complete Full-Stack Python & React Game Engine</span>
        </div>

        <div className="flex items-center gap-6 text-sm">
          <div className="flex items-center gap-1 text-slate-400">
            <Zap className="w-4 h-4 text-amber-400" />
            <span>Real-Time WebSockets</span>
          </div>
          <div className="flex items-center gap-1 text-slate-400">
            <Shield className="w-4 h-4 text-emerald-400" />
            <span>Authoritative Server State</span>
          </div>
          <div className="flex items-center gap-1 text-slate-400">
            <Terminal className="w-4 h-4 text-cyan-400" />
            <span>FastAPI & SQLAlchemy</span>
          </div>
        </div>

        <p className="text-xs text-slate-500">
          © 2026 TEST YOUR KNOWLEDGE Engine. Built with precision.
        </p>
      </div>
    </footer>
  );
};
