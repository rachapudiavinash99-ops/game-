import React, { useEffect, useState, useRef } from 'react';
import { useParams, useSearchParams, useNavigate } from 'react-router-dom';
import { 
  Heart, 
  Flame, 
  HelpCircle, 
  ArrowRight, 
  CheckCircle2, 
  XCircle, 
  Clock, 
  AlertCircle,
  Zap,
  Sparkles
} from 'lucide-react';
import api from '../services/api';
import { GameSession, Task, Answer } from '../types';
import { TimerRing } from '../components/game/TimerRing';
import { StreakFlame } from '../components/game/StreakFlame';
import { sound } from '../services/sound';

export const GameArenaPage: React.FC = () => {
  const { mode = 'QUICK_CHALLENGE', topicId } = useParams();
  const [searchParams] = useSearchParams();
  const difficulty = searchParams.get('difficulty') || undefined;
  const navigate = useNavigate();

  const [session, setSession] = useState<GameSession | null>(null);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [selectedAnswerId, setSelectedAnswerId] = useState<number | null>(null);
  const [answerResult, setAnswerResult] = useState<any | null>(null);
  const [timeRemaining, setTimeRemaining] = useState<number>(20);
  const [totalTime, setTotalTime] = useState<number>(20);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);
  const [lives, setLives] = useState<number>(3);
  const [currentScore, setCurrentScore] = useState<number>(0);
  const [currentStreak, setCurrentStreak] = useState<number>(0);

  const timerRef = useRef<any>(null);
  const questionStartTimeRef = useRef<number>(Date.now());

  // Initialize Game Session
  useEffect(() => {
    let activeMode = 'QUICK_CHALLENGE';
    if (mode === 'quick') activeMode = 'QUICK_CHALLENGE';
    else if (mode === 'topic') activeMode = 'TOPIC_CHALLENGE';
    else if (mode === 'time-attack') activeMode = 'TIME_ATTACK';
    else if (mode === 'survival') activeMode = 'SURVIVAL';

    const reqPayload: any = {
      mode: activeMode,
      question_count: activeMode === 'SURVIVAL' ? 20 : (activeMode === 'TIME_ATTACK' ? 25 : 10),
    };
    if (topicId) reqPayload.topic_id = parseInt(topicId);
    if (difficulty) reqPayload.difficulty = difficulty;

    setError(null);
    setLoading(true);

    api.post('/games/start', reqPayload)
      .then(res => {
        const sess: GameSession = res.data;
        setSession(sess);
        setLives(sess.lives_remaining);
        setCurrentScore(0);
        setCurrentStreak(0);
        if (sess.questions.length > 0) {
          const qTime = sess.questions[0].time_limit_seconds || 20;
          setTimeRemaining(qTime);
          setTotalTime(qTime);
        }
        questionStartTimeRef.current = Date.now();
        setLoading(false);
      })
      .catch((err) => {
        setLoading(false);
        setError(err.response?.data?.message || err.response?.data?.detail || 'Failed to start game session.');
      });

    return () => {
      if (timerRef.current) clearInterval(timerRef.current);
    };
  }, [mode, topicId, difficulty]);

  // Question Timer Countdown Loop
  useEffect(() => {
    if (!session || answerResult !== null) return;

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
  }, [session, currentIndex, answerResult]);

  // Handle Timeout
  const handleTimeOut = () => {
    if (!session || answerResult !== null) return;
    submitCurrentAnswer(null, totalTime);
  };

  // Submit Answer
  const submitCurrentAnswer = async (ansId: number | null, timeSpent: number) => {
    if (!session || answerResult !== null) return;
    if (timerRef.current) clearInterval(timerRef.current);

    const currentQ = session.questions[currentIndex];
    setSelectedAnswerId(ansId);

    try {
      const res = await api.post('/games/submit-answer', {
        session_id: session.id,
        task_id: currentQ.task.id,
        selected_answer_id: ansId,
        time_spent_seconds: timeSpent
      });

      const data = res.data;
      setAnswerResult(data);
      setCurrentScore(data.current_score);
      setCurrentStreak(data.streak);
      setLives(data.lives_remaining);

      if (data.is_correct) {
        sound.playCorrect();
        if (data.streak >= 3) sound.playStreak();
      } else {
        sound.playWrong();
      }

    } catch (e) {
      console.error(e);
    }
  };

  // Next Question or Finish
  const handleNext = () => {
    sound.playClick();
    if (!session || !answerResult) return;

    if (answerResult.is_game_over || currentIndex + 1 >= session.questions.length) {
      api.post(`/games/finish/${session.id}`).then(res => {
        sound.playLevelUp();
        navigate('/play/result', { state: { result: res.data } });
      }).catch(() => {
        navigate('/dashboard');
      });
      return;
    }

    const nextIdx = currentIndex + 1;
    setCurrentIndex(nextIdx);
    setSelectedAnswerId(null);
    setAnswerResult(null);

    const nextQ = session.questions[nextIdx];
    const qTime = nextQ.time_limit_seconds || 20;
    setTimeRemaining(qTime);
    setTotalTime(qTime);
    questionStartTimeRef.current = Date.now();
  };

  // Keyboard shortcut listener (1, 2, 3, 4)
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (answerResult !== null || !session) {
        if (e.key === 'Enter' || e.key === ' ') {
          handleNext();
        }
        return;
      }
      const num = parseInt(e.key);
      const currentQ = session.questions[currentIndex];
      if (num >= 1 && num <= currentQ.task.answers.length) {
        const ans = currentQ.task.answers[num - 1];
        const timeSpent = Math.min(totalTime, (Date.now() - questionStartTimeRef.current) / 1000);
        submitCurrentAnswer(ans.id, timeSpent);
      }
    };

    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [session, currentIndex, answerResult, totalTime]);

  if (error) {
    return (
      <div className="min-h-[60vh] flex flex-col items-center justify-center space-y-4 text-center px-4 animate-scaleIn">
        <AlertCircle className="w-12 h-12 text-rose-500 mx-auto" />
        <h3 className="text-xl font-bold text-white font-mono">COULD NOT START GAME</h3>
        <p className="text-sm text-slate-400 max-w-md">{error}</p>
        <div className="flex gap-3 pt-2">
          <button 
            onClick={() => window.location.reload()} 
            className="px-5 py-2.5 bg-violet-600 hover:bg-violet-500 rounded-xl font-bold text-white text-xs font-mono shadow-neon-indigo cursor-pointer transition-all hover:scale-105"
          >
            Retry Match
          </button>
          <button 
            onClick={() => navigate('/dashboard')} 
            className="px-5 py-2.5 glass-panel text-slate-300 hover:text-white rounded-xl font-bold text-xs font-mono cursor-pointer"
          >
            Dashboard
          </button>
        </div>
      </div>
    );
  }

  if (loading || !session) {
    return (
      <div className="min-h-[70vh] flex flex-col items-center justify-center space-y-4">
        <div className="w-14 h-14 border-4 border-violet-500 border-t-cyan-400 rounded-full animate-spin"></div>
        <p className="text-slate-300 font-mono text-xs tracking-widest animate-pulse">INITIALIZING GAME ARENA...</p>
      </div>
    );
  }

  const currentQ = session.questions[currentIndex];
  const isSurvival = session.mode === 'SURVIVAL';

  return (
    <div className="relative max-w-4xl mx-auto px-4 py-8 space-y-6">
      {/* Ambient background glow */}
      <div className="ambient-orb-1 top-0 left-1/4"></div>

      {/* Arena Top Bar */}
      <div className="glass-panel p-4 sm:p-5 rounded-2xl flex items-center justify-between border border-white/10 backdrop-blur-xl animate-fadeInUp">
        <div className="flex items-center gap-3">
          <span className="font-mono text-xs font-black text-slate-300 bg-slate-900/90 px-3 py-1.5 rounded-xl border border-slate-800">
            QUESTION {currentIndex + 1} / {session.questions.length}
          </span>
          <span className="bg-gradient-to-r from-violet-600/30 to-cyan-600/30 text-cyan-300 text-xs px-3 py-1.5 rounded-xl font-mono font-bold border border-cyan-500/30">
            {currentQ.task.difficulty}
          </span>
          {isSurvival && (
            <div className="flex items-center gap-1.5 ml-2 bg-rose-950/40 border border-rose-800/50 px-2.5 py-1 rounded-xl">
              {[...Array(3)].map((_, i) => (
                <Heart 
                  key={i} 
                  className={`w-4 h-4 transition-all duration-300 ${i < lives ? 'text-rose-500 fill-rose-500 animate-pulse' : 'text-slate-700'}`} 
                />
              ))}
            </div>
          )}
        </div>

        <div className="flex items-center gap-4">
          <StreakFlame streak={currentStreak} />
          <div className="flex items-center gap-1.5 bg-slate-900/90 px-3.5 py-1.5 rounded-xl border border-violet-500/40 shadow-neon-indigo">
            <Zap className="w-4 h-4 text-amber-400 fill-amber-400" />
            <span className="font-mono font-black text-violet-300 text-sm">{currentScore} pts</span>
          </div>
          <TimerRing timeRemaining={timeRemaining} totalTime={totalTime} size={54} />
        </div>
      </div>

      {/* Question Card */}
      <div 
        key={currentIndex}
        className={`glass-panel-glow p-6 sm:p-9 rounded-3xl border border-violet-500/40 relative overflow-hidden space-y-7 animate-scaleIn shadow-cyber-border ${
          answerResult && !answerResult.is_correct ? 'animate-shake border-rose-500/60' : ''
        }`}
      >
        <h2 className="text-xl sm:text-2xl font-bold text-white leading-relaxed font-mono">
          {currentQ.task.question}
        </h2>

        {/* Answer Options Grid */}
        <div className="grid grid-cols-1 gap-3.5 pt-1">
          {currentQ.task.answers.map((ans, idx) => {
            const isSelected = selectedAnswerId === ans.id;
            const isAnswered = answerResult !== null;
            const isCorrect = isAnswered && ans.id === answerResult.correct_answer_id;
            const isWrongSelection = isAnswered && isSelected && !answerResult.is_correct;

            let btnStyle = 'bg-slate-900/80 border-slate-800/80 text-slate-200 hover:border-violet-500/70 hover:bg-slate-800/90 hover:scale-[1.01] hover:shadow-neon-indigo';
            if (isCorrect) {
              btnStyle = 'bg-emerald-950/90 border-emerald-500 text-emerald-100 shadow-neon-emerald scale-[1.01] animate-bounceSoft';
            } else if (isWrongSelection) {
              btnStyle = 'bg-rose-950/90 border-rose-500 text-rose-100 shadow-neon-rose';
            } else if (isAnswered) {
              btnStyle = 'bg-slate-900/40 border-slate-800/40 text-slate-500 opacity-50';
            }

            return (
              <button
                key={ans.id}
                disabled={isAnswered}
                onClick={() => {
                  const timeSpent = Math.min(totalTime, (Date.now() - questionStartTimeRef.current) / 1000);
                  submitCurrentAnswer(ans.id, timeSpent);
                }}
                className={`w-full p-4 sm:p-5 rounded-2xl border text-left flex items-center justify-between transition-all duration-200 cursor-pointer ${btnStyle}`}
              >
                <div className="flex items-center gap-4">
                  <span className="w-8 h-8 rounded-xl bg-slate-800/90 border border-slate-700 flex items-center justify-center text-xs font-mono font-black text-slate-300 shrink-0">
                    {idx + 1}
                  </span>
                  <span className="text-sm sm:text-base font-medium leading-snug">{ans.text}</span>
                </div>

                {isCorrect && <CheckCircle2 className="w-5 h-5 text-emerald-400 shrink-0 ml-2" />}
                {isWrongSelection && <XCircle className="w-5 h-5 text-rose-400 shrink-0 ml-2" />}
              </button>
            );
          })}
        </div>

        {/* Instant Answer Feedback & Explanation Drawer */}
        {answerResult && (
          <div className="mt-6 p-5 sm:p-6 rounded-2xl bg-slate-900/95 border border-slate-700/80 space-y-3 animate-fadeInUp backdrop-blur-xl">
            <div className="flex items-center justify-between">
              <div className="flex items-center gap-2">
                {answerResult.is_correct ? (
                  <span className="text-emerald-400 font-black font-mono text-sm sm:text-base flex items-center gap-2 glow-text-emerald">
                    <Sparkles className="w-5 h-5 text-emerald-400 animate-spin-slow" /> 
                    CORRECT! +{answerResult.points_earned} PTS
                  </span>
                ) : (
                  <span className="text-rose-400 font-black font-mono text-sm sm:text-base flex items-center gap-2">
                    <XCircle className="w-5 h-5 text-rose-400 animate-pulse" /> 
                    INCORRECT
                  </span>
                )}
              </div>

              <button
                onClick={handleNext}
                className="flex items-center gap-2 px-6 py-2.5 rounded-xl bg-gradient-to-r from-violet-600 via-fuchsia-600 to-cyan-500 hover:from-violet-500 hover:to-cyan-400 text-white font-bold text-xs font-mono shadow-neon-indigo transition-all hover:scale-105 cursor-pointer"
              >
                {answerResult.is_game_over || currentIndex + 1 >= session.questions.length ? 'View Results' : 'Next Question'}
                <ArrowRight className="w-4 h-4" />
              </button>
            </div>

            {answerResult.explanation && (
              <p className="text-xs sm:text-sm text-slate-300 leading-relaxed pt-3 border-t border-slate-800">
                <strong className="text-cyan-300">Explanation: </strong> {answerResult.explanation}
              </p>
            )}
          </div>
        )}
      </div>
    </div>
  );
};
