import React from "react";
import { BrowserRouter, Route, Routes, Link, Navigate } from 'react-router-dom';
import Home from "./pages/Home";
import Article from './pages/Article';
import Research from './pages/Research';
import About from './pages/About';


function App() {
  return (
    <BrowserRouter>
      <nav>
        <ul>
          <li>
            <Link to="/">Home</Link>
          </li>
          <li>
            <Link to="/article">Articles</Link>
          </li>
          <li>
            <Link to="/research">Researches</Link>
          </li>
          <li>
            <Link to="/about">About</Link>
          </li>
        </ul>
      </nav>
      <Routes>
        <Route 
          path="/" 
          element={
              <Home />
          }
        />
        <Route 
          path="/article" 
          element={
              <Article />
          }
        />
        <Route 
          path="/research" 
          element={
              <Research />
          }
        />
        <Route 
          path="/about" 
          element={
            <About />
          }
        />
      </Routes>
      
    </BrowserRouter>
  )
}

export default App
