import React, { useEffect, useState, useRef } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { 
  Users, 
  Crown, 
  CheckCircle2, 
  XCircle, 
  Send, 
  Play, 
  Flame, 
  Trophy, 
  Clock, 
  Zap,
  ArrowRight
} from 'lucide-react';
import api from '../services/api';
import { useAuth } from '../store/useAuthStore';
import { sound } from '../services/sound';
import { TimerRing } from '../components/game/TimerRing';

export const MultiplayerRoomPage: React.FC = () => {
  const { roomCode } = useParams<{ roomCode: string }>();
  const { user } = useAuth();
  const navigate = useNavigate();

  const [players, setPlayers] = useState<any[]>([]);
  const [roomStatus, setRoomStatus] = useState<string>('WAITING');
  const [isReady, setIsReady] = useState(false);
  const [messages, setMessages] = useState<any[]>([]);
  const [inputMsg, setInputMsg] = useState('');
  const [countdown, setCountdown] = useState<number | null>(null);

  // Active question state during match
  const [currentQ, setCurrentQ] = useState<any | null>(null);
  const [qIndex, setQIndex] = useState(1);
  const [totalQ, setTotalQ] = useState(5);
  const [selectedAnsId, setSelectedAnsId] = useState<number | null>(null);
  const [ansFeedback, setAnsFeedback] = useState<any | null>(null);
  const [matchWinner, setMatchWinner] = useState<any | null>(null);
  const [matchResults, setMatchResults] = useState<any[]>([]);

  const [timeRemaining, setTimeRemaining] = useState<number>(15);
  const [timeLimit, setTimeLimit] = useState<number>(15);

  const wsRef = useRef<WebSocket | null>(null);
  const timerRef = useRef<any>(null);
  const questionStartRef = useRef<number>(Date.now());

  useEffect(() => {
    const token = localStorage.getItem('gameverse_access_token');
    if (!token) {
      navigate('/login');
      return;
    }

    const host = window.location.hostname || '127.0.0.1';
    const wsUrl = `ws://${host}:8008/ws/multiplayer/${roomCode}?token=${token}`;
    const ws = new WebSocket(wsUrl);
    wsRef.current = ws;

    ws.onopen = () => {
      console.log('Connected to multiplayer room WebSocket');
    };

    ws.onmessage = (event) => {
      const data = JSON.parse(event.data);

      if (data.type === 'ROOM_UPDATE') {
        setPlayers(data.players);
        setRoomStatus(data.status);
      } else if (data.type === 'GAME_STARTING') {
        setCountdown(data.countdown);
        setTotalQ(data.total_questions);
        setTimeLimit(data.time_per_question);
        sound.playLevelUp();
      } else if (data.type === 'NEW_QUESTION') {
        setCountdown(null);
        setRoomStatus('IN_PROGRESS');
        setCurrentQ(data.question);
        setQIndex(data.question_index);
        setTotalQ(data.total_questions);
        setSelectedAnsId(null);
        setAnsFeedback(null);
        setTimeRemaining(data.question.time_limit || 15);
        setTimeLimit(data.question.time_limit || 15);
        questionStartRef.current = Date.now();
      } else if (data.type === 'PLAYER_ANSWERED') {
        if (data.user_id === user?.id) {
          setAnsFeedback(data);
          if (data.is_correct) sound.playCorrect();
          else sound.playWrong();
        }
        if (data.leaderboard) {
          setPlayers(data.leaderboard);
        }
      } else if (data.type === 'MATCH_OVER') {
        setRoomStatus('FINISHED');
        setMatchWinner(data.winner);
        setMatchResults(data.results || []);
        sound.playLevelUp();
      } else if (data.type === 'CHAT') {
        setMessages(prev => [...prev, data]);
      }
    };

    return () => {
      ws.close();
      if (timerRef.current) clearInterval(timerRef.current);
    };
  }, [roomCode, user]);

  // Question countdown
  useEffect(() => {
    if (roomStatus !== 'IN_PROGRESS' || !currentQ || ansFeedback !== null) return;
    if (timerRef.current) clearInterval(timerRef.current);

    timerRef.current = setInterval(() => {
      setTimeRemaining(prev => {
        if (prev <= 1) {
          clearInterval(timerRef.current);
          handleTimeOut();
          return 0;
        }
        return prev - 1;
      });
    }, 1000);

    return () => {
      if (timerRef.current) clearInterval(timerRef.current);
    };
  }, [roomStatus, currentQ, ansFeedback]);

  const handleTimeOut = () => {
    if (!currentQ || ansFeedback !== null) return;
    submitAnswer(null);
  };

  const handleToggleReady = () => {
    sound.playClick();
    const nextState = !isReady;
    setIsReady(nextState);
    wsRef.current?.send(JSON.stringify({
      type: 'PLAYER_READY',
      is_ready: nextState
    }));
  };

  const handleStartGame = () => {
    sound.playClick();
    wsRef.current?.send(JSON.stringify({
      type: 'START_GAME'
    }));
  };

  const submitAnswer = (ansId: number | null) => {
    if (ansFeedback !== null || !currentQ) return;
    setSelectedAnsId(ansId);
    const timeSpent = Math.min(timeLimit, (Date.now() - questionStartRef.current) / 1000);
    wsRef.current?.send(JSON.stringify({
      type: 'SUBMIT_ANSWER',
      task_id: currentQ.id,
      answer_id: ansId,
      time_spent: timeSpent
    }));
  };

  const sendChatMessage = (e: React.FormEvent) => {
    e.preventDefault();
    if (!inputMsg.trim()) return;
    wsRef.current?.send(JSON.stringify({
      type: 'CHAT_MESSAGE',
      message: inputMsg
    }));
    setInputMsg('');
  };

  const isHost = players.find(p => p.user_id === user?.id)?.is_host;

  return (
    <div className="max-w-6xl mx-auto px-4 py-8 space-y-6">
      {/* Top Status Banner */}
      <div className="glass-panel p-5 rounded-2xl flex flex-wrap items-center justify-between gap-4 border border-indigo-500/30">
        <div>
          <span className="text-xs font-mono font-bold text-indigo-400 uppercase tracking-widest block">
            Multiplayer Room
          </span>
          <h1 className="text-2xl font-black text-white font-mono">
            CODE: <span className="text-cyan-400">{roomCode}</span>
          </h1>
        </div>

        {roomStatus === 'IN_PROGRESS' && currentQ && (
          <div className="flex items-center gap-4">
            <span className="font-mono text-sm font-bold text-slate-300">
              QUESTION {qIndex} / {totalQ}
            </span>
            <TimerRing timeRemaining={timeRemaining} totalTime={timeLimit} size={50} />
          </div>
        )}
      </div>

      {/* Countdown overlay */}
      {countdown !== null && (
        <div className="glass-panel p-12 text-center rounded-3xl border border-indigo-500/40 space-y-4 animate-pulse">
          <span className="text-xs font-bold text-indigo-400 font-mono tracking-widest uppercase">
            MATCH STARTING IN
          </span>
          <div className="text-7xl font-black text-cyan-400 font-mono">
            {countdown}
          </div>
        </div>
      )}

      {/* Room Lobby View */}
      {roomStatus === 'WAITING' && countdown === null && (
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          {/* Players Slot List */}
          <div className="lg:col-span-2 glass-panel p-6 rounded-3xl border border-slate-800 space-y-6">
            <div className="flex items-center justify-between">
              <h2 className="font-mono font-bold text-lg text-white flex items-center gap-2">
                <Users className="w-5 h-5 text-indigo-400" />
                PLAYERS ({players.length})
              </h2>
              {isHost && (
                <button
                  onClick={handleStartGame}
                  className="flex items-center gap-2 px-6 py-2.5 rounded-xl bg-gradient-to-r from-indigo-600 to-cyan-600 hover:from-indigo-500 hover:to-cyan-500 text-white font-bold text-xs shadow-neon-indigo transition-all font-mono cursor-pointer"
                >
                  <Play className="w-4 h-4 fill-white" />
                  START GAME
                </button>
              )}
            </div>

            <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
              {players.map((pl) => (
                <div 
                  key={pl.user_id}
                  className="p-4 rounded-2xl bg-slate-900/80 border border-slate-800 flex items-center justify-between"
                >
                  <div className="flex items-center gap-3">
                    <img 
                      src={`https://api.dicebear.com/7.x/bottts/svg?seed=${pl.username}`} 
                      alt={pl.username}
                      className="w-10 h-10 rounded-xl border border-slate-700" 
                    />
                    <div>
                      <div className="flex items-center gap-1.5">
                        <span className="font-bold text-sm text-white">{pl.username}</span>
                        {pl.is_host && <Crown className="w-3.5 h-3.5 text-amber-400" />}
                      </div>
                      <span className="text-xs text-slate-500 font-mono">
                        {pl.is_host ? 'Host' : 'Challenger'}
                      </span>
                    </div>
                  </div>

                  <span className={`text-xs font-mono font-bold px-2.5 py-1 rounded-lg ${
                    pl.is_ready ? 'bg-emerald-500/20 text-emerald-400 border border-emerald-500/30' : 'bg-slate-800 text-slate-400'
                  }`}>
                    {pl.is_ready ? 'READY' : 'WAITING'}
                  </span>
                </div>
              ))}
            </div>

            {!isHost && (
              <button
                onClick={handleToggleReady}
                className={`w-full py-3.5 rounded-2xl font-bold font-mono text-sm transition-all cursor-pointer ${
                  isReady 
                    ? 'bg-emerald-600 text-white shadow-neon-emerald' 
                    : 'bg-indigo-600 text-white shadow-neon-indigo'
                }`}
              >
                {isReady ? 'READY TO BATTLE (CLICK TO CANCEL)' : 'CLICK WHEN READY'}
              </button>
            )}
          </div>

          {/* Lobby Live Chat */}
          <div className="glass-panel p-6 rounded-3xl border border-slate-800 flex flex-col justify-between h-96">
            <h3 className="font-mono font-bold text-sm text-slate-300 mb-3">ROOM CHAT</h3>

            <div className="flex-1 overflow-y-auto space-y-2 pr-1 text-xs">
              {messages.map((m, i) => (
                <div key={i} className="p-2 rounded-lg bg-slate-900/60 border border-slate-800">
                  <span className="font-bold text-indigo-400 font-mono">{m.username}: </span>
                  <span className="text-slate-200">{m.message}</span>
                </div>
              ))}
            </div>

            <form onSubmit={sendChatMessage} className="flex gap-2 pt-3">
              <input
                type="text"
                value={inputMsg}
                onChange={(e) => setInputMsg(e.target.value)}
                placeholder="Type a message..."
                className="flex-1 bg-slate-900 border border-slate-700 rounded-xl px-3 py-2 text-xs text-slate-200 focus:outline-none focus:border-indigo-500"
              />
              <button type="submit" className="p-2 rounded-xl bg-indigo-600 text-white">
                <Send className="w-3.5 h-3.5" />
              </button>
            </form>
          </div>
        </div>
      )}

      {/* Match In Progress Arena */}
      {roomStatus === 'IN_PROGRESS' && currentQ && (
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          {/* Main Question Card */}
          <div className="lg:col-span-2 glass-panel-glow p-6 sm:p-8 rounded-3xl border border-indigo-500/30 space-y-6">
            <h2 className="text-xl sm:text-2xl font-bold text-slate-100 leading-relaxed font-mono">
              {currentQ.question}
            </h2>

            <div className="grid grid-cols-1 gap-3.5">
              {currentQ.answers.map((ans: any, idx: number) => {
                const isSelected = selectedAnsId === ans.id;
                const isAnswered = ansFeedback !== null;
                const isCorrect = isAnswered && ans.id === ansFeedback.correct_answer_id;
                const isWrong = isAnswered && isSelected && !ansFeedback.is_correct;

                let btnStyle = 'bg-slate-900/80 border-slate-800 text-slate-200 hover:border-indigo-500/50 hover:bg-slate-800/60';
                if (isCorrect) btnStyle = 'bg-emerald-950/80 border-emerald-500 text-emerald-100 shadow-neon-emerald';
                else if (isWrong) btnStyle = 'bg-rose-950/80 border-rose-500 text-rose-100 shadow-neon-rose';
                else if (isAnswered) btnStyle = 'bg-slate-900/40 border-slate-800/40 text-slate-500 opacity-60';

                return (
                  <button
                    key={ans.id}
                    disabled={isAnswered}
                    onClick={() => submitAnswer(ans.id)}
                    className={`w-full p-4 rounded-2xl border text-left flex items-center justify-between transition-all duration-200 cursor-pointer ${btnStyle}`}
                  >
                    <div className="flex items-center gap-3">
                      <span className="w-7 h-7 rounded-lg bg-slate-800 flex items-center justify-center text-xs font-mono font-bold text-slate-300">
                        {idx + 1}
                      </span>
                      <span className="text-sm sm:text-base font-medium">{ans.text}</span>
                    </div>

                    {isCorrect && <CheckCircle2 className="w-5 h-5 text-emerald-400" />}
                    {isWrong && <XCircle className="w-5 h-5 text-rose-400" />}
                  </button>
                );
              })}
            </div>

            {ansFeedback && (
              <div className="p-4 rounded-xl bg-slate-900/90 border border-slate-800 flex items-center justify-between">
                <span className={`font-mono font-bold text-sm ${ansFeedback.is_correct ? 'text-emerald-400' : 'text-rose-400'}`}>
                  {ansFeedback.is_correct ? `CORRECT! +${ansFeedback.points} PTS` : 'INCORRECT'}
                </span>
                {isHost && (
                  <button
                    onClick={() => wsRef.current?.send(JSON.stringify({ type: 'NEXT_QUESTION' }))}
                    className="flex items-center gap-2 px-4 py-2 rounded-xl bg-indigo-600 text-white font-bold text-xs font-mono shadow-neon-indigo"
                  >
                    Next Question <ArrowRight className="w-3.5 h-3.5" />
                  </button>
                )}
              </div>
            )}
          </div>

          {/* Live Scoreboard */}
          <div className="glass-panel p-6 rounded-3xl border border-slate-800 space-y-4">
            <h3 className="font-mono font-bold text-sm text-slate-300 flex items-center gap-2">
              <Trophy className="w-4 h-4 text-amber-400" />
              LIVE LEADERBOARD
            </h3>

            <div className="space-y-2">
              {players.map((pl, idx) => (
                <div 
                  key={pl.user_id}
                  className="p-3 rounded-xl bg-slate-900/80 border border-slate-800 flex items-center justify-between text-xs"
                >
                  <div className="flex items-center gap-2">
                    <span className="font-mono font-bold text-slate-500 w-4">{idx + 1}</span>
                    <span className="font-bold text-slate-200">{pl.username}</span>
                  </div>
                  <span className="font-mono font-bold text-indigo-400">{pl.score || 0} pts</span>
                </div>
              ))}
            </div>
          </div>
        </div>
      )}

      {/* Match Over Podium */}
      {roomStatus === 'FINISHED' && (
        <div className="glass-panel p-8 sm:p-12 text-center rounded-3xl border border-amber-500/40 space-y-6 max-w-2xl mx-auto animate-fadeIn">
          <div className="w-20 h-20 mx-auto rounded-3xl bg-gradient-to-tr from-amber-500 to-yellow-300 flex items-center justify-center shadow-neon-gold">
            <Crown className="w-10 h-10 text-slate-950" />
          </div>

          <h2 className="text-3xl font-black text-white font-mono">
            WINNER: <span className="text-amber-400">{matchWinner?.username || 'Challenger'}</span>
          </h2>

          <div className="space-y-2">
            {matchResults.map((res) => (
              <div 
                key={res.user_id}
                className={`p-4 rounded-2xl flex items-center justify-between text-sm ${
                  res.is_winner ? 'bg-amber-950/40 border border-amber-500/60 font-bold' : 'bg-slate-900/80 border border-slate-800'
                }`}
              >
                <div className="flex items-center gap-3">
                  <span className="font-mono text-slate-400">#{res.rank}</span>
                  <span className="text-white">{res.username}</span>
                </div>
                <span className="font-mono font-bold text-amber-400">{res.score} pts</span>
              </div>
            ))}
          </div>

          <button
            onClick={() => navigate('/multiplayer')}
            className="px-8 py-3 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white font-bold font-mono text-sm shadow-neon-indigo transition-all cursor-pointer"
          >
            RETURN TO LOBBY
          </button>
        </div>
      )}
    </div>
  );
};
