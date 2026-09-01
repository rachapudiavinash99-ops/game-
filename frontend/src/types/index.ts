export interface UserProfile {
  id: number;
  display_name: string | null;
  avatar_url: string;
  bio: string | null;
  level: number;
  current_xp: number;
  next_level_xp: number;
  total_score: number;
  total_games: number;
  wins: number;
  win_rate: number;
  current_streak: number;
  best_streak: number;
}

export interface User {
  id: number;
  username: string;
  email: string;
  role: 'USER' | 'MODERATOR' | 'ADMIN';
  is_active: boolean;
  is_verified: boolean;
  profile?: UserProfile;
}

export interface AuthTokens {
  access_token: string;
  refresh_token: string;
  token_type: string;
  user_id: number;
  username: string;
  role: string;
}

export interface Category {
  id: number;
  topic_id: number;
  name: string;
  slug: string;
  description: string | null;
}

export interface Topic {
  id: number;
  name: string;
  slug: string;
  description: string | null;
  icon: string;
  color: string;
  is_active: boolean;
  order: number;
  task_count?: number;
  categories: Category[];
}

export interface Answer {
  id: number;
  text: string;
  order: number;
  is_correct?: boolean;
}

export interface Task {
  id: number;
  topic_id: number;
  category_id: number | null;
  title: string;
  question: string;
  task_type: string;
  difficulty: 'EASY' | 'MEDIUM' | 'HARD' | 'EXPERT';
  points: number;
  time_limit_seconds: number;
  explanation: string | null;
  tags: string;
  is_active: boolean;
  answers: Answer[];
}

export interface GameQuestion {
  order: number;
  task: Task;
  time_limit_seconds: number;
}

export interface GameSession {
  id: number;
  mode: string;
  topic_id: number | null;
  difficulty: string | null;
  status: string;
  score: number;
  xp_earned: number;
  lives_remaining: number;
  streak_count: number;
  total_questions: number;
  questions: GameQuestion[];
  started_at: string;
}

export interface SubmitAnswerResponse {
  is_correct: boolean;
  correct_answer_id: number;
  points_earned: number;
  streak: number;
  explanation: string | null;
  current_score: number;
  lives_remaining: number;
  is_game_over: boolean;
}

export interface GameResult {
  session_id: number;
  mode: string;
  status: string;
  score: number;
  xp_earned: number;
  accuracy: number;
  time_taken_seconds: number;
  total_questions: number;
  correct_count: number;
  wrong_count: number;
  best_streak: number;
  level_up: boolean;
  new_level: number;
  unlocked_achievements: string[];
}

export interface Achievement {
  id: number;
  code: string;
  title: string;
  description: string;
  icon: string;
  category: string;
  requirement_type: string;
  requirement_value: number;
  xp_reward: number;
  badge_color: string;
  unlocked: boolean;
  unlocked_at: string | null;
}

export interface DailyChallenge {
  id: number;
  challenge_date: string;
  title: string;
  description: string;
  topic_id: number | null;
  topic_name: string | null;
  bonus_xp: number;
  bonus_score: number;
  is_completed: boolean;
  tasks: Task[];
}

export interface MultiplayerPlayer {
  id: number;
  user_id: number;
  username: string;
  is_host: boolean;
  is_ready: boolean;
  score: number;
  streak: number;
  correct_answers: number;
  is_connected: boolean;
}

export interface MultiplayerRoom {
  id: number;
  room_code: string;
  name: string;
  host_user_id: number | null;
  topic_id: number | null;
  difficulty: string;
  max_players: number;
  question_count: number;
  time_per_question: number;
  status: 'WAITING' | 'IN_PROGRESS' | 'FINISHED' | 'CANCELLED';
  current_question_index: number;
  winner_user_id: number | null;
  players: MultiplayerPlayer[];
  created_at: string;
}

export interface LeaderboardEntry {
  rank: number;
  user_id: number;
  username: string;
  display_name: string;
  avatar_url: string;
  level: number;
  xp: number;
  total_score: number;
  total_games: number;
  wins: number;
  win_rate: number;
  best_streak: number;
}
