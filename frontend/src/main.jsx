import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import HomePage from './home-page/HomePage.jsx';
import AnalysisPage from './analysis-page/AnalysisPage.jsx';
// import Loader from 'react-loader-spinner';
import './index.css';

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <Router>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/analysis/" element={<AnalysisPage />} />
      </Routes>
    </Router>
  </React.StrictMode>,
);