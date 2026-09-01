import React from 'react';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { Navbar } from './components/layout/Navbar';
import { Footer } from './components/layout/Footer';
import { LandingPage } from './pages/LandingPage';
import { LoginPage } from './pages/LoginPage';
import { RegisterPage } from './pages/RegisterPage';
import { DashboardPage } from './pages/DashboardPage';
import { TopicsPage } from './pages/TopicsPage';
import { GameArenaPage } from './pages/GameArenaPage';
import { GameResultPage } from './pages/GameResultPage';
import { MultiplayerLobbyPage } from './pages/MultiplayerLobbyPage';
import { MultiplayerRoomPage } from './pages/MultiplayerRoomPage';
import { LeaderboardPage } from './pages/LeaderboardPage';
import { AchievementsPage } from './pages/AchievementsPage';
import { DailyChallengesPage } from './pages/DailyChallengesPage';
import { ProfilePage } from './pages/ProfilePage';
import { AdminDashboardPage } from './pages/AdminDashboardPage';
import { useAuth } from './store/useAuthStore';

export function App() {
  const { isAdmin } = useAuth();

  return (
    <BrowserRouter>
      <div className="flex flex-col min-h-screen">
        <Navbar />
        <main className="flex-1">
          <Routes>
            <Route path="/" element={<LandingPage />} />
            <Route path="/login" element={<LoginPage />} />
            <Route path="/register" element={<RegisterPage />} />
            <Route path="/dashboard" element={<DashboardPage />} />
            <Route path="/topics" element={<TopicsPage />} />
            <Route path="/play/:mode" element={<GameArenaPage />} />
            <Route path="/play/:mode/:topicId" element={<GameArenaPage />} />
            <Route path="/play/result" element={<GameResultPage />} />
            <Route path="/multiplayer" element={<MultiplayerLobbyPage />} />
            <Route path="/multiplayer/room/:roomCode" element={<MultiplayerRoomPage />} />
            <Route path="/leaderboard" element={<LeaderboardPage />} />
            <Route path="/achievements" element={<AchievementsPage />} />
            <Route path="/challenges/daily" element={<DailyChallengesPage />} />
            <Route path="/profile" element={<ProfilePage />} />
            <Route path="/admin" element={isAdmin ? <AdminDashboardPage /> : <Navigate to="/" />} />
            <Route path="*" element={<Navigate to="/" />} />
          </Routes>
        </main>
        <Footer />
      </div>
    </BrowserRouter>
  );
}

export default App;
