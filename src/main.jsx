import React from 'react';
import { Routes, Router , HashRouter } from 'react-router-dom';
import ReactDOM from 'react-dom/client';
import './index.css'  
import App from './App.jsx'

ReactDOM.createRoot(document.getElementById('root')).render(
  <HashRouter>
      <App/>
  </HashRouter>
);
