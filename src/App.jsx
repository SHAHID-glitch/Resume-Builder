import React from 'react';
import { Routes, Route, Router } from 'react-router-dom';
import FrontPage from './components/FrontPage.jsx';
import GetInfo from './components/GetInfo.jsx';

const App = () => {
  return (
    // <>
    //   <QuizCam/>
    // </>
      <Routes>
        <Route path="/" element={<FrontPage />} />
        <Route path="/GetInfo" element={<GetInfo />} />
        {/* <Route path="/GetInfo/QuizCam" element={<QuizCam />} />  */}
      </Routes>
  );
}

export default App;