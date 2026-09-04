import React from 'react';
import { Flame, Sparkles, Zap } from 'lucide-react';

interface StreakFlameProps {
  streak: number;
}

export const StreakFlame: React.FC<StreakFlameProps> = ({ streak }) => {
  if (streak <= 0) return null;

  const multiplier = Math.min(2.5, 1.0 + streak * 0.1).toFixed(1);
  const isHyper = streak >= 5;
  const isGodlike = streak >= 10;

  let badgeBg = "from-amber-500/20 via-orange-500/20 to-rose-500/20 border-orange-500/50 text-orange-400";
  let flameIcon = <Flame className="w-4 h-4 text-orange-400 fill-orange-500 animate-bounce" />;

  if (isGodlike) {
    badgeBg = "from-fuchsia-600/30 via-violet-600/30 to-cyan-500/30 border-fuchsia-500/70 text-fuchsia-300 shadow-neon-fuchsia";
    flameIcon = <Zap className="w-4 h-4 text-cyan-300 fill-cyan-400 animate-spin-slow" />;
  } else if (isHyper) {
    badgeBg = "from-rose-600/25 via-pink-600/25 to-amber-500/25 border-rose-500/60 text-rose-300 shadow-neon-rose";
    flameIcon = <Sparkles className="w-4 h-4 text-rose-400 fill-rose-500 animate-pulse" />;
  }

  return (
    <div className={`flex items-center gap-2 bg-gradient-to-r ${badgeBg} border px-3.5 py-1.5 rounded-full animate-bounce-soft backdrop-blur-md`}>
      {flameIcon}
      <span className="text-xs font-black font-mono tracking-wider">
        {streak} STREAK
      </span>
      <span className="text-[10px] bg-gradient-to-r from-amber-400 to-orange-500 text-slate-950 font-black px-2 py-0.5 rounded-full font-mono shadow-sm">
        {multiplier}x
      </span>
    </div>
  );
};
