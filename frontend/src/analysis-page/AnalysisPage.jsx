import { useLocation } from "react-router-dom";
import { useEffect } from "react";

const AnalysisPage = () => {
    const location = useLocation();
    const data = location.state.data;
    // name of playlist
    const name = data.playlist.name;
    // dictionary of avg values
    const avgValues = data.avg_values;
    const playlistURL = data.playlist.url;

    useEffect(() => {
        document.title = name + " - Analysis";
    }, [name]);

    return (
        <div>
            <a href={playlistURL} target="_blank" rel="noopener noreferrer">
                <h1>{name}</h1>
            </a>
            {Object.entries(avgValues).map(([key, value], index) => (
                <p key={index}>{key}: {value}</p>
            ))}
        </div>
    );
};

export default AnalysisPage;
