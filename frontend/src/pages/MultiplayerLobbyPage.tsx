import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Users, Plus, KeyRound, Play, RefreshCw, Zap, Shield, Crown } from 'lucide-react';
import api from '../services/api';
import { MultiplayerRoom, Topic } from '../types';
import { useAuth } from '../store/useAuthStore';
import { sound } from '../services/sound';

export const MultiplayerLobbyPage: React.FC = () => {
  const [rooms, setRooms] = useState<MultiplayerRoom[]>([]);
  const [topics, setTopics] = useState<Topic[]>([]);
  const [showCreateModal, setShowCreateModal] = useState(false);
  const [roomCodeInput, setRoomCodeInput] = useState('');
  const [roomName, setRoomName] = useState('');
  const [selectedTopicId, setSelectedTopicId] = useState<number | ''>('');
  const [selectedDifficulty, setSelectedDifficulty] = useState('MEDIUM');
  const [loading, setLoading] = useState(false);

  const { isAuthenticated } = useAuth();
  const navigate = useNavigate();

  const fetchRooms = () => {
    api.get('/multiplayer/rooms').then(res => setRooms(res.data)).catch(() => {});
  };

  useEffect(() => {
    fetchRooms();
    api.get('/topics').then(res => setTopics(res.data)).catch(() => {});
    const interval = setInterval(fetchRooms, 4000);
    return () => clearInterval(interval);
  }, []);

  const handleCreateRoom = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!isAuthenticated) {
      navigate('/login');
      return;
    }
    sound.playClick();
    setLoading(true);

    try {
      const res = await api.post('/multiplayer/rooms', {
        name: roomName || 'Battle Arena',
        topic_id: selectedTopicId ? Number(selectedTopicId) : null,
        difficulty: selectedDifficulty,
        max_players: 4,
        question_count: 10,
        time_per_question: 15
      });
      setShowCreateModal(false);
      navigate(`/multiplayer/room/${res.data.room_code}`);
    } catch (e) {
      console.error(e);
    } finally {
      setLoading(false);
    }
  };

  const handleJoinByCode = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!isAuthenticated) {
      navigate('/login');
      return;
    }
    if (!roomCodeInput) return;
    sound.playClick();

    try {
      await api.post('/multiplayer/rooms/join', { room_code: roomCodeInput.toUpperCase() });
      navigate(`/multiplayer/room/${roomCodeInput.toUpperCase()}`);
    } catch (e) {
      alert('Room not found or game already in progress.');
    }
  };

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-8">
      {/* Header */}
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
        <div>
          <h1 className="text-3xl font-black text-slate-100 font-mono tracking-wide flex items-center gap-3">
            <Users className="w-8 h-8 text-indigo-400" />
            MULTIPLAYER <span className="text-indigo-400">ARENA</span>
          </h1>
          <p className="text-sm text-slate-400">
            Compete against real players in synchronized real-time WebSocket challenge battles
          </p>
        </div>

        <div className="flex items-center gap-3">
          <button
            onClick={fetchRooms}
            className="p-2.5 rounded-xl glass-panel hover:bg-slate-800 text-slate-300 transition-colors"
            title="Refresh Rooms"
          >
            <RefreshCw className="w-4 h-4" />
          </button>
          <button
            onClick={() => { sound.playClick(); setShowCreateModal(true); }}
            className="flex items-center gap-2 px-5 py-2.5 rounded-xl bg-gradient-to-r from-indigo-600 to-cyan-600 hover:from-indigo-500 hover:to-cyan-500 text-white font-bold text-sm shadow-neon-indigo transition-all cursor-pointer font-mono"
          >
            <Plus className="w-4 h-4" />
            CREATE ROOM
          </button>
        </div>
      </div>

      {/* Join by Room Code Bar */}
      <div className="glass-panel p-5 rounded-2xl border border-indigo-500/20 max-w-xl">
        <form onSubmit={handleJoinByCode} className="flex gap-3">
          <div className="relative flex-1">
            <KeyRound className="w-4 h-4 text-slate-500 absolute left-3.5 top-1/2 -translate-y-1/2" />
            <input
              type="text"
              maxLength={8}
              value={roomCodeInput}
              onChange={(e) => setRoomCodeInput(e.target.value.toUpperCase())}
              placeholder="ENTER 6-DIGIT ROOM CODE"
              className="w-full bg-slate-900/90 border border-slate-700 rounded-xl py-2.5 pl-10 pr-4 text-sm font-mono tracking-widest text-slate-200 focus:outline-none focus:border-indigo-500 uppercase"
            />
          </div>
          <button
            type="submit"
            className="px-6 py-2.5 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white font-bold text-sm shadow-neon-indigo transition-all font-mono"
          >
            JOIN
          </button>
        </form>
      </div>

      {/* Active Rooms Listing */}
      <div className="space-y-4">
        <h2 className="text-xl font-black text-slate-200 font-mono tracking-wider">
          LIVE MATCH LOBBIES ({rooms.length})
        </h2>

        {rooms.length === 0 ? (
          <div className="glass-panel p-12 text-center rounded-3xl border border-slate-800 space-y-3">
            <Users className="w-12 h-12 text-slate-600 mx-auto" />
            <p className="text-slate-400 font-mono text-sm">No waiting rooms at the moment.</p>
            <p className="text-xs text-slate-500">Create the first room and invite other challengers!</p>
          </div>
        ) : (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            {rooms.map((room) => (
              <div
                key={room.id}
                className="glass-panel p-5 rounded-2xl border border-slate-800 hover:border-indigo-500/50 transition-all flex flex-col justify-between"
              >
                <div className="space-y-3">
                  <div className="flex items-center justify-between">
                    <span className="font-mono text-xs font-bold text-indigo-400 bg-indigo-950/60 px-2.5 py-1 rounded-lg border border-indigo-500/30">
                      CODE: {room.room_code}
                    </span>
                    <span className="text-xs font-mono font-bold text-slate-400">
                      {room.players.length} / {room.max_players} PLAYERS
                    </span>
                  </div>

                  <h3 className="font-bold text-white text-base truncate">{room.name}</h3>

                  <div className="flex items-center gap-2 text-xs text-slate-400 font-mono">
                    <span className="bg-slate-800 px-2 py-0.5 rounded">{room.difficulty}</span>
                    <span>{room.question_count} Questions</span>
                    <span>{room.time_per_question}s / Q</span>
                  </div>
                </div>

                <button
                  onClick={() => {
                    sound.playClick();
                    if (!isAuthenticated) navigate('/login');
                    else navigate(`/multiplayer/room/${room.room_code}`);
                  }}
                  className="mt-5 w-full py-2.5 rounded-xl bg-gradient-to-r from-indigo-600 to-cyan-600 hover:from-indigo-500 hover:to-cyan-500 text-white font-bold text-xs shadow-neon-indigo transition-all font-mono"
                >
                  ENTER LOBBY
                </button>
              </div>
            ))}
          </div>
        )}
      </div>

      {/* Create Room Modal */}
      {showCreateModal && (
        <div className="fixed inset-0 z-50 bg-black/70 backdrop-blur-sm flex items-center justify-center p-4">
          <div className="glass-panel p-6 sm:p-8 rounded-3xl border border-indigo-500/40 w-full max-w-md space-y-6">
            <h2 className="text-2xl font-black text-white font-mono">CREATE MULTIPLAYER ROOM</h2>

            <form onSubmit={handleCreateRoom} className="space-y-4">
              <div>
                <label className="block text-xs font-semibold text-slate-300 mb-1.5">Room Name</label>
                <input
                  type="text"
                  required
                  value={roomName}
                  onChange={(e) => setRoomName(e.target.value)}
                  placeholder="e.g. Python Masters Arena"
                  className="w-full bg-slate-900 border border-slate-700 rounded-xl py-2.5 px-4 text-sm text-slate-200 focus:outline-none focus:border-indigo-500"
                />
              </div>

              <div>
                <label className="block text-xs font-semibold text-slate-300 mb-1.5">Topic</label>
                <select
                  value={selectedTopicId}
                  onChange={(e) => setSelectedTopicId(e.target.value ? Number(e.target.value) : '')}
                  className="w-full bg-slate-900 border border-slate-700 rounded-xl py-2.5 px-4 text-sm text-slate-200 focus:outline-none focus:border-indigo-500"
                >
                  <option value="">All Topics (Randomized)</option>
                  {topics.map(t => (
                    <option key={t.id} value={t.id}>{t.name}</option>
                  ))}
                </select>
              </div>

              <div>
                <label className="block text-xs font-semibold text-slate-300 mb-1.5">Difficulty</label>
                <select
                  value={selectedDifficulty}
                  onChange={(e) => setSelectedDifficulty(e.target.value)}
                  className="w-full bg-slate-900 border border-slate-700 rounded-xl py-2.5 px-4 text-sm text-slate-200 focus:outline-none focus:border-indigo-500"
                >
                  <option value="EASY">Easy</option>
                  <option value="MEDIUM">Medium</option>
                  <option value="HARD">Hard</option>
                  <option value="EXPERT">Expert</option>
                </select>
              </div>

              <div className="flex gap-3 pt-4">
                <button
                  type="button"
                  onClick={() => setShowCreateModal(false)}
                  className="flex-1 py-3 rounded-xl glass-panel text-slate-300 text-sm font-semibold hover:bg-slate-800"
                >
                  Cancel
                </button>
                <button
                  type="submit"
                  disabled={loading}
                  className="flex-1 py-3 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white text-sm font-bold shadow-neon-indigo font-mono"
                >
                  {loading ? 'Creating...' : 'Create & Host'}
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
};
