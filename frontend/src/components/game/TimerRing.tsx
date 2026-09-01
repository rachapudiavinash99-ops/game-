import React from 'react';

interface TimerRingProps {
  timeRemaining: number;
  totalTime: number;
  size?: number;
}

export const TimerRing: React.FC<TimerRingProps> = ({ timeRemaining, totalTime, size = 64 }) => {
  const strokeWidth = 5;
  const radius = (size - strokeWidth * 2) / 2;
  const circumference = radius * 2 * Math.PI;
  const progress = Math.max(0, Math.min(1, timeRemaining / Math.max(1, totalTime)));
  const strokeDashoffset = circumference - progress * circumference;

  let strokeColor = '#06b6d4'; // Cyan
  if (timeRemaining <= 5) {
    strokeColor = '#ef4444'; // Red urgency
  } else if (timeRemaining <= 10) {
    strokeColor = '#f59e0b'; // Amber warning
  }

  return (
    <div className="relative flex items-center justify-center" style={{ width: size, height: size }}>
      <svg width={size} height={size} className="transform -rotate-90">
        <circle
          cx={size / 2}
          cy={size / 2}
          r={radius}
          stroke="#1e293b"
          strokeWidth={strokeWidth}
          fill="transparent"
        />
        <circle
          cx={size / 2}
          cy={size / 2}
          r={radius}
          stroke={strokeColor}
          strokeWidth={strokeWidth}
          strokeDasharray={circumference}
          strokeDashoffset={strokeDashoffset}
          strokeLinecap="round"
          fill="transparent"
          className="transition-all duration-300 ease-linear"
        />
      </svg>
      <span className={`absolute font-mono font-bold text-base ${timeRemaining <= 5 ? 'text-rose-400 animate-pulse' : 'text-slate-100'}`}>
        {Math.ceil(timeRemaining)}
      </span>
    </div>
  );
};
