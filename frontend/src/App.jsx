import { useState } from 'react'
import './App.css'

export default function App() {
  return (
    <form className="URL-form">
      <label htmlFor="URL">Enter a Spotify playlist URL:</label>
      <input type="text" placeholder="https://open.spotify.com/playlist/37i9dQZEVXbMDoHDwVN2tF?si=ff3ab5b167d84320" />
      <button type="submit">Analyse!</button>
    </form>
  )
}