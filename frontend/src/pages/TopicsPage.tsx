import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Search, Code, Play } from 'lucide-react';
import api from '../services/api';
import { Topic } from '../types';
import { sound } from '../services/sound';

export const TopicsPage: React.FC = () => {
  const [topics, setTopics] = useState<Topic[]>([]);
  const [search, setSearch] = useState('');
  const [difficulty, setDifficulty] = useState<'ALL' | 'EASY' | 'MEDIUM' | 'HARD' | 'EXPERT'>('ALL');
  const navigate = useNavigate();

  useEffect(() => {
    api.get('/topics').then(res => setTopics(res.data)).catch(() => {});
  }, []);

  const filteredTopics = topics.filter(t => 
    t.name.toLowerCase().includes(search.toLowerCase()) || 
    (t.description && t.description.toLowerCase().includes(search.toLowerCase()))
  );

  const startTopicGame = (topicId: number) => {
    sound.playClick();
    navigate(`/play/topic/${topicId}?difficulty=${difficulty !== 'ALL' ? difficulty : ''}`);
  };

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-8">
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
        <div>
          <h1 className="text-3xl font-black text-slate-100 font-mono tracking-wide">
            TOPIC <span className="text-indigo-400">UNIVERSE</span>
          </h1>
          <p className="text-sm text-slate-400">
            Select a knowledge domain to start a customized challenge session
          </p>
        </div>

        <div className="flex items-center gap-2 bg-slate-900/80 border border-slate-800 p-1 rounded-xl">
          {['ALL', 'EASY', 'MEDIUM', 'HARD', 'EXPERT'].map((lvl) => (
            <button
              key={lvl}
              onClick={() => { sound.playClick(); setDifficulty(lvl as any); }}
              className={`px-3 py-1.5 rounded-lg text-xs font-bold font-mono transition-all ${
                difficulty === lvl 
                  ? 'bg-indigo-600 text-white shadow-neon-indigo' 
                  : 'text-slate-400 hover:text-white'
              }`}
            >
              {lvl}
            </button>
          ))}
        </div>
      </div>

      <div className="relative max-w-md">
        <Search className="w-4 h-4 text-slate-500 absolute left-3.5 top-1/2 -translate-y-1/2" />
        <input
          type="text"
          value={search}
          onChange={(e) => setSearch(e.target.value)}
          placeholder="Search topics (e.g. Python, SQL, AI, Cybersecurity)..."
          className="w-full bg-slate-900/80 border border-slate-700 rounded-xl py-2.5 pl-10 pr-4 text-sm text-slate-200 focus:outline-none focus:border-indigo-500"
        />
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {filteredTopics.map((topic) => (
          <div
            key={topic.id}
            className="glass-panel p-6 rounded-2xl border border-slate-800 hover:border-indigo-500/50 hover:shadow-neon-indigo transition-all flex flex-col justify-between group"
          >
            <div className="space-y-4">
              <div className="flex items-center justify-between">
                <div 
                  className="w-12 h-12 rounded-xl flex items-center justify-center group-hover:scale-110 transition-transform"
                  style={{ backgroundColor: `${topic.color}20`, border: `1px solid ${topic.color}40` }}
                >
                  <Code className="w-6 h-6" style={{ color: topic.color }} />
                </div>
                <span className="text-xs bg-slate-800/80 text-slate-300 font-mono px-2.5 py-1 rounded-full border border-slate-700">
                  {topic.task_count || 5}+ Questions
                </span>
              </div>

              <div>
                <h3 className="text-xl font-bold text-white group-hover:text-indigo-300 transition-colors">
                  {topic.name}
                </h3>
                <p className="text-xs text-slate-400 mt-2 leading-relaxed line-clamp-3">
                  {topic.description || 'Dynamic topic challenge tasks.'}
                </p>
              </div>
            </div>

            <div className="pt-6 border-t border-slate-800/80 mt-6 flex items-center justify-between">
              <span className="text-xs font-semibold text-slate-400 font-mono">
                {difficulty !== 'ALL' ? `${difficulty} Mode` : 'Mixed Difficulty'}
              </span>
              <button
                onClick={() => startTopicGame(topic.id)}
                className="flex items-center gap-1.5 px-4 py-2 rounded-xl bg-gradient-to-r from-indigo-600 to-cyan-600 hover:from-indigo-500 hover:to-cyan-500 text-white font-bold text-xs shadow-neon-indigo transition-all cursor-pointer"
              >
                <Play className="w-3.5 h-3.5 fill-white" />
                Start Challenge
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
