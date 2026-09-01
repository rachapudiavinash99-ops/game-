import React, { useEffect, useState } from 'react';
import { User, Edit3, Save } from 'lucide-react';
import api from '../services/api';
import { useAuth } from '../store/useAuthStore';
import { sound } from '../services/sound';

export const ProfilePage: React.FC = () => {
  const { user, refreshUser } = useAuth();
  const [displayName, setDisplayName] = useState(user?.profile?.display_name || '');
  const [bio, setBio] = useState(user?.profile?.bio || '');
  const [isEditing, setIsEditing] = useState(false);
  const [saving, setSaving] = useState(false);

  useEffect(() => {
    if (user?.profile) {
      setDisplayName(user.profile.display_name || '');
      setBio(user.profile.bio || '');
    }
  }, [user]);

  const handleSave = async () => {
    sound.playClick();
    setSaving(true);
    try {
      await api.put('/users/profile', {
        display_name: displayName,
        bio: bio
      });
      setIsEditing(false);
      refreshUser();
      sound.playCorrect();
    } catch (e) {
      console.error(e);
    } finally {
      setSaving(false);
    }
  };

  const p = user?.profile;

  return (
    <div className="max-w-4xl mx-auto px-4 py-8 space-y-8">
      <div className="glass-panel p-6 sm:p-8 rounded-3xl border border-indigo-500/30 space-y-6">
        <div className="flex flex-col sm:flex-row items-center justify-between gap-6">
          <div className="flex items-center gap-5">
            <img 
              src={p?.avatar_url || `https://api.dicebear.com/7.x/bottts/svg?seed=${user?.username || 'user'}`}
              alt=""
              className="w-20 h-20 rounded-2xl border-2 border-indigo-500/50 shadow-neon-indigo"
            />
            <div>
              <div className="flex items-center gap-2">
                <h1 className="text-2xl font-black text-white font-mono">{p?.display_name || user?.username}</h1>
                <span className="text-xs bg-indigo-500/20 text-indigo-300 font-bold px-2 py-0.5 rounded font-mono">
                  LVL {p?.level || 1}
                </span>
              </div>
              <p className="text-xs text-slate-400">@{user?.username} • {user?.email}</p>
            </div>
          </div>

          <button
            onClick={() => setIsEditing(!isEditing)}
            className="flex items-center gap-1.5 px-4 py-2 rounded-xl glass-panel text-slate-300 hover:text-white text-xs font-semibold"
          >
            <Edit3 className="w-3.5 h-3.5" />
            {isEditing ? 'Cancel Edit' : 'Edit Profile'}
          </button>
        </div>

        {isEditing && (
          <div className="pt-4 border-t border-slate-800 space-y-4">
            <div>
              <label className="block text-xs font-semibold text-slate-300 mb-1">Display Name</label>
              <input
                type="text"
                value={displayName}
                onChange={(e) => setDisplayName(e.target.value)}
                className="w-full bg-slate-900 border border-slate-700 rounded-xl py-2 px-3 text-sm text-white"
              />
            </div>
            <div>
              <label className="block text-xs font-semibold text-slate-300 mb-1">Bio</label>
              <textarea
                value={bio}
                onChange={(e) => setBio(e.target.value)}
                placeholder="Write a brief gamer bio..."
                className="w-full bg-slate-900 border border-slate-700 rounded-xl py-2 px-3 text-sm text-white h-20"
              />
            </div>
            <button
              onClick={handleSave}
              disabled={saving}
              className="flex items-center gap-1.5 px-5 py-2 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white font-bold text-xs"
            >
              <Save className="w-3.5 h-3.5" />
              {saving ? 'Saving...' : 'Save Changes'}
            </button>
          </div>
        )}

        <div className="grid grid-cols-2 sm:grid-cols-4 gap-4 pt-4 border-t border-slate-800 text-center font-mono">
          <div className="p-3 bg-slate-900/80 rounded-xl">
            <span className="text-xs text-slate-400">Total Score</span>
            <p className="text-lg font-bold text-indigo-400 mt-1">{p?.total_score || 0}</p>
          </div>
          <div className="p-3 bg-slate-900/80 rounded-xl">
            <span className="text-xs text-slate-400">Games Played</span>
            <p className="text-lg font-bold text-cyan-400 mt-1">{p?.total_games || 0}</p>
          </div>
          <div className="p-3 bg-slate-900/80 rounded-xl">
            <span className="text-xs text-slate-400">Victories</span>
            <p className="text-lg font-bold text-emerald-400 mt-1">{p?.wins || 0}</p>
          </div>
          <div className="p-3 bg-slate-900/80 rounded-xl">
            <span className="text-xs text-slate-400">Best Streak</span>
            <p className="text-lg font-bold text-orange-400 mt-1">{p?.best_streak || 0}</p>
          </div>
        </div>
      </div>
    </div>
  );
};
