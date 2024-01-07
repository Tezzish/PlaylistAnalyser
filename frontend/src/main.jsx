import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Form from './Form.jsx';
import NewPage from './NewPage.jsx';
import './index.css';

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <Router>
      <Routes>
        <Route path="/" element={<Form />} />
        <Route path="/new-page" element={<NewPage />} />
      </Routes>
    </Router>
  </React.StrictMode>,
);