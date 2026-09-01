import React from 'react';
import { Flame } from 'lucide-react';

interface StreakFlameProps {
  streak: number;
}

export const StreakFlame: React.FC<StreakFlameProps> = ({ streak }) => {
  if (streak <= 0) return null;

  const multiplier = Math.min(2.5, 1.0 + streak * 0.1).toFixed(1);

  return (
    <div className="flex items-center gap-1.5 bg-gradient-to-r from-orange-500/20 to-red-500/20 border border-orange-500/40 px-3 py-1 rounded-full animate-bounce">
      <Flame className="w-4 h-4 text-orange-400 fill-orange-500 animate-pulse" />
      <span className="text-xs font-black text-orange-400 font-mono">
        {streak} STREAK
      </span>
      <span className="text-[10px] bg-orange-500 text-black font-black px-1.5 py-0.5 rounded font-mono">
        {multiplier}x
      </span>
    </div>
  );
};
