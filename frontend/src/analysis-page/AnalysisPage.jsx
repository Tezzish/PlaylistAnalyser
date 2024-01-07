import { useLocation } from "react-router-dom";
import { useEffect } from "react";
import './AnalysisPage.css';

const AnalysisPage = () => {
    const location = useLocation();
    const data = location.state.data;
    // name of playlist
    const name = data.playlist.name;
    // dictionary of avg values
    // const avgValues = data.avg_values;
    const playlistURL = data.playlist.url;
    const image = data.playlist.thumbnail;
    const author = data.playlist.author;
    console.log(image);

    useEffect(() => {
        document.title = name + " - Analysis";
    }, [name]);

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
            <button className = "page-button">▼</button>
        </div>
    );
};

export default AnalysisPage;
