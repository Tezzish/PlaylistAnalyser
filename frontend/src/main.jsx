import React, { Suspense } from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import HomePage from './home-page/HomePage.jsx';
import AnalysisPage from './analysis-page/AnalysisPage.jsx';
import './index.css';

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <Router>
      <Suspense fallback={<div>Loading...</div>}>
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/analysis/" element={<AnalysisPage />} />
        </Routes>
      </Suspense>
    </Router>
  </React.StrictMode>,
);