import React, { useState } from 'react';

const URLForm = () => {
    const [url, setUrl] = useState('');

    const handleSubmit = async (event: { preventDefault: () => void; }) => {
        event.preventDefault();
        const formData = new FormData();
        formData.append('playlist_link', url);
    
        try {
            const response = await fetch('http://127.0.0.1:8000/analysis/', {
                method: 'POST',
                body: formData,
                credentials: 'include'
            });
            const data = await response.json();
            console.log(data);
        } catch (error) {
            console.error(error);
        }
    };

    return (
        <form className="form" onSubmit={handleSubmit}>
            <label htmlFor="URL-input">Please enter the URL for your Spotify playlist</label>
            <input 
                id="URL-input"
                type="text" 
                placeholder="URL" 
                value={url}
                onChange={e => setUrl(e.target.value)}
            />
            <button type="submit">Submit</button>
        </form>
    );
}

export default URLForm;