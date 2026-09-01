import React, { useEffect, useState } from 'react';
import { Shield, Plus, Users, Database } from 'lucide-react';
import api from '../services/api';
import { User, Topic } from '../types';
import { sound } from '../services/sound';

export const AdminDashboardPage: React.FC = () => {
  const [users, setUsers] = useState<User[]>([]);
  const [topics, setTopics] = useState<Topic[]>([]);
  const [activeTab, setActiveTab] = useState<'users' | 'task_creator' | 'logs'>('users');
  const [auditLogs, setAuditLogs] = useState<any[]>([]);

  const [topicId, setTopicId] = useState<number>(1);
  const [title, setTitle] = useState('');
  const [question, setQuestion] = useState('');
  const [difficulty, setDifficulty] = useState('MEDIUM');
  const [points, setPoints] = useState(20);
  const [timeLimit, setTimeLimit] = useState(20);
  const [explanation, setExplanation] = useState('');
  const [answers, setAnswers] = useState([
    { text: '', is_correct: true },
    { text: '', is_correct: false },
    { text: '', is_correct: false },
    { text: '', is_correct: false }
  ]);
  const [msg, setMsg] = useState<string | null>(null);

  useEffect(() => {
    api.get('/admin/users').then(res => setUsers(res.data)).catch(() => {});
    api.get('/topics').then(res => setTopics(res.data)).catch(() => {});
    api.get('/admin/audit-logs').then(res => setAuditLogs(res.data)).catch(() => {});
  }, []);

  const handleCreateTask = async (e: React.FormEvent) => {
    e.preventDefault();
    sound.playClick();
    try {
      await api.post('/admin/tasks', {
        topic_id: Number(topicId),
        title,
        question,
        difficulty,
        points: Number(points),
        time_limit_seconds: Number(timeLimit),
        explanation,
        tags: 'custom,admin',
        answers
      });
      setMsg('New challenge task created successfully!');
      sound.playLevelUp();
      setTitle('');
      setQuestion('');
      setExplanation('');
    } catch (e: any) {
      setMsg('Error creating task.');
    }
  };

  const handleToggleUserStatus = async (userId: number, currentStatus: boolean) => {
    sound.playClick();
    try {
      await api.put(`/admin/users/${userId}/status`, { is_active: !currentStatus });
      setUsers(prev => prev.map(u => u.id === userId ? { ...u, is_active: !currentStatus } : u));
    } catch (e) {
      console.error(e);
    }
  };

  return (
    <div className="max-w-6xl mx-auto px-4 py-8 space-y-8">
      <div className="flex flex-col sm:flex-row items-center justify-between gap-4">
        <h1 className="text-3xl font-black text-white font-mono flex items-center gap-3">
          <Shield className="w-8 h-8 text-amber-400" />
          ADMIN <span className="text-amber-400">CONTROL PORTAL</span>
        </h1>

        <div className="flex bg-slate-900 border border-slate-800 p-1 rounded-xl">
          <button
            onClick={() => setActiveTab('users')}
            className={`px-3 py-1.5 rounded-lg text-xs font-bold font-mono transition-all ${
              activeTab === 'users' ? 'bg-amber-600 text-white' : 'text-slate-400 hover:text-white'
            }`}
          >
            Users ({users.length})
          </button>
          <button
            onClick={() => setActiveTab('task_creator')}
            className={`px-3 py-1.5 rounded-lg text-xs font-bold font-mono transition-all ${
              activeTab === 'task_creator' ? 'bg-amber-600 text-white' : 'text-slate-400 hover:text-white'
            }`}
          >
            Create Task
          </button>
          <button
            onClick={() => setActiveTab('logs')}
            className={`px-3 py-1.5 rounded-lg text-xs font-bold font-mono transition-all ${
              activeTab === 'logs' ? 'bg-amber-600 text-white' : 'text-slate-400 hover:text-white'
            }`}
          >
            Audit Logs
          </button>
        </div>
      </div>

      {activeTab === 'users' && (
        <div className="glass-panel rounded-2xl border border-slate-800 overflow-hidden">
          <table className="w-full text-left text-sm">
            <thead className="bg-slate-900 text-xs text-slate-400 font-mono uppercase">
              <tr>
                <th className="py-3 px-4">ID</th>
                <th className="py-3 px-4">Username</th>
                <th className="py-3 px-4">Email</th>
                <th className="py-3 px-4">Role</th>
                <th className="py-3 px-4">Status</th>
                <th className="py-3 px-4 text-right">Action</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-800">
              {users.map(u => (
                <tr key={u.id} className="hover:bg-slate-800/40">
                  <td className="py-3 px-4 font-mono">{u.id}</td>
                  <td className="py-3 px-4 font-bold text-white">{u.username}</td>
                  <td className="py-3 px-4 text-slate-400 text-xs">{u.email}</td>
                  <td className="py-3 px-4 font-mono text-xs text-amber-400">{u.role}</td>
                  <td className="py-3 px-4">
                    <span className={`text-xs px-2 py-0.5 rounded font-mono font-bold ${
                      u.is_active ? 'bg-emerald-950 text-emerald-400' : 'bg-rose-950 text-rose-400'
                    }`}>
                      {u.is_active ? 'ACTIVE' : 'SUSPENDED'}
                    </span>
                  </td>
                  <td className="py-3 px-4 text-right">
                    <button
                      onClick={() => handleToggleUserStatus(u.id, u.is_active)}
                      className={`text-xs font-bold px-3 py-1 rounded-lg ${
                        u.is_active ? 'bg-rose-900/60 text-rose-300 hover:bg-rose-800' : 'bg-emerald-900/60 text-emerald-300 hover:bg-emerald-800'
                      }`}
                    >
                      {u.is_active ? 'Suspend' : 'Activate'}
                    </button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}

      {activeTab === 'task_creator' && (
        <div className="glass-panel p-6 sm:p-8 rounded-3xl border border-amber-500/30 space-y-6">
          <h2 className="text-xl font-bold text-white font-mono">ADD NEW CHALLENGE TASK</h2>

          {msg && (
            <div className="p-3 bg-slate-900 border border-slate-700 rounded-xl text-xs text-amber-300">
              {msg}
            </div>
          )}

          <form onSubmit={handleCreateTask} className="space-y-4">
            <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
              <div>
                <label className="block text-xs font-semibold text-slate-300 mb-1">Topic</label>
                <select
                  value={topicId}
                  onChange={(e) => setTopicId(Number(e.target.value))}
                  className="w-full bg-slate-900 border border-slate-700 rounded-xl py-2 px-3 text-sm text-white"
                >
                  {topics.map(t => (
                    <option key={t.id} value={t.id}>{t.name}</option>
                  ))}
                </select>
              </div>

              <div>
                <label className="block text-xs font-semibold text-slate-300 mb-1">Difficulty</label>
                <select
                  value={difficulty}
                  onChange={(e) => setDifficulty(e.target.value)}
                  className="w-full bg-slate-900 border border-slate-700 rounded-xl py-2 px-3 text-sm text-white"
                >
                  <option value="EASY">Easy</option>
                  <option value="MEDIUM">Medium</option>
                  <option value="HARD">Hard</option>
                  <option value="EXPERT">Expert</option>
                </select>
              </div>

              <div>
                <label className="block text-xs font-semibold text-slate-300 mb-1">Points</label>
                <input
                  type="number"
                  value={points}
                  onChange={(e) => setPoints(Number(e.target.value))}
                  className="w-full bg-slate-900 border border-slate-700 rounded-xl py-2 px-3 text-sm text-white"
                />
              </div>
            </div>

            <div>
              <label className="block text-xs font-semibold text-slate-300 mb-1">Task Title</label>
              <input
                type="text"
                required
                value={title}
                onChange={(e) => setTitle(e.target.value)}
                placeholder="e.g. Memory Layout in CPython"
                className="w-full bg-slate-900 border border-slate-700 rounded-xl py-2 px-3 text-sm text-white"
              />
            </div>

            <div>
              <label className="block text-xs font-semibold text-slate-300 mb-1">Question Description</label>
              <textarea
                required
                value={question}
                onChange={(e) => setQuestion(e.target.value)}
                placeholder="Enter full question text..."
                className="w-full bg-slate-900 border border-slate-700 rounded-xl py-2 px-3 text-sm text-white h-24"
              />
            </div>

            <div className="space-y-2 pt-2">
              <label className="block text-xs font-semibold text-slate-300">Answer Options (Select correct one)</label>
              {answers.map((ans, idx) => (
                <div key={idx} className="flex items-center gap-3">
                  <input
                    type="radio"
                    name="correct_answer"
                    checked={ans.is_correct}
                    onChange={() => {
                      setAnswers(prev => prev.map((a, i) => ({ ...a, is_correct: i === idx })));
                    }}
                    className="w-4 h-4 text-emerald-500"
                  />
                  <input
                    type="text"
                    required
                    value={ans.text}
                    onChange={(e) => {
                      const val = e.target.value;
                      setAnswers(prev => prev.map((a, i) => i === idx ? { ...a, text: val } : a));
                    }}
                    placeholder={`Answer option ${idx + 1}`}
                    className="flex-1 bg-slate-900 border border-slate-700 rounded-xl py-1.5 px-3 text-sm text-white"
                  />
                </div>
              ))}
            </div>

            <div>
              <label className="block text-xs font-semibold text-slate-300 mb-1">Explanation</label>
              <input
                type="text"
                value={explanation}
                onChange={(e) => setExplanation(e.target.value)}
                placeholder="Brief explanation for why this answer is correct..."
                className="w-full bg-slate-900 border border-slate-700 rounded-xl py-2 px-3 text-sm text-white"
              />
            </div>

            <button
              type="submit"
              className="py-3 px-8 rounded-xl bg-amber-600 hover:bg-amber-500 text-slate-950 font-black text-sm font-mono"
            >
              CREATE TASK
            </button>
          </form>
        </div>
      )}

      {activeTab === 'logs' && (
        <div className="glass-panel p-6 rounded-3xl border border-slate-800 space-y-3 font-mono text-xs">
          <h3 className="text-sm font-bold text-white mb-2">SYSTEM AUDIT TRAIL</h3>
          {auditLogs.map((log) => (
            <div key={log.id} className="p-3 bg-slate-900/80 rounded-xl border border-slate-800 flex justify-between">
              <div>
                <span className="text-amber-400 font-bold">{log.action}</span>
                <span className="text-slate-400 ml-2">[{log.resource_type} #{log.resource_id}]</span>
              </div>
              <span className="text-slate-500">{new Date(log.created_at).toLocaleString()}</span>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};
