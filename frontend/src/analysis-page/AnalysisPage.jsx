import { useLocation } from "react-router-dom";
import { useState, useEffect } from "react";
import './AnalysisPage.css';
import ProgressRing from "./ProgressRing";

const AnalysisPage = () => {
    const location = useLocation();
    const data = location.state.data;
    // name of playlist
    const name = data.playlist.name;
    // dictionary of avg values
    const avgValues = data.avg_values;
    const playlistURL = data.playlist.url;
    const image = data.playlist.thumbnail;
    const author = data.playlist.author;
    useEffect(() => {
        document.title = name + " - Analysis";
    }, [name]);

    const handleButtonClick = () => {
        setShowRings(true);
        // decrease the playlist-title font size
        const playlistTitle = document.querySelector('.playlist-title');
        playlistTitle.style.fontSize = '2rem';
        // hide the author header
        const authorHeader = document.querySelector('.author-header');
        authorHeader.style.display = 'none';
        // decrease the size of the album art
        const albumArt = document.querySelector('.album-art');
        albumArt.style.transform = 'scale(0.6) translateY(-27.5%)'; // Decrease size to 75% and move up a little
        // animate the progress rings
        const progressBars = document.querySelectorAll('.progress-ring');
        progressBars.forEach(bar => {
            bar.classList.add('progress-ring-filled');
            bar.style.width = bar.dataset.value + '%'; // Set the width to the desired value
        });
    };
    const [showRings, setShowRings] = useState(false);
    return (
        <div className="main-div">
            <div 
                className="background-image" 
                style={{backgroundImage:`url(${image})`}}
            />
            <a className="playlist-title" href={playlistURL} target="_blank" rel="noopener noreferrer">
                <h1>{name}</h1>
            </a>
            <h3 className="author-header"> By: {author}</h3>
            <img 
                src={image} 
                className="album-art"/>
            <button className = "page-button" onClick={handleButtonClick}>▼</button>
            <div className="progress-ring-container">
                {showRings && Object.entries(avgValues).map(([key, value]) => (
                <ProgressRing key={key} text={key} value={value} style="" />
                ))}
            </div>
        </div>
    );
};

export default AnalysisPage;
