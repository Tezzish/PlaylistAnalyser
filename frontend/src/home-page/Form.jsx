import { useState } from 'react';
import { useNavigate } from 'react-router-dom';

const PlaylistURL = "http://localhost:8000/analysis/"

function Form() {
  const [text, setText] = useState('');
  const [invalidInput, setInvalidInput] = useState(false);
  const navigate = useNavigate();

  function validateInput(input) {
    // Check if input is a valid Spotify playlist link
    const regex = /^https:\/\/open\.spotify\.com\/playlist\/\S+\?si=\S+$/;
    return regex.test(input);
  }

  const handleSubmit = async (event) => {
    event.preventDefault();
    if (!validateInput(text)) {
      setInvalidInput(true);
      setTimeout(() => setInvalidInput(false), 820);
      return;
    }
    const responseFromServer = await MakeRequest(PlaylistURL, text );
    navigate('/analysis/', { state: { data: responseFromServer } });
  }

  return (
    <form onSubmit={handleSubmit}>
      <div className="form-group">
        <label>
          Enter your Spotify playlist link:
        </label>
        <div className="form-control">
          <input
            type="text"
            className={`form-input ${invalidInput ? 'shake-input' : ''}`}
            placeholder="https://open.spotify.com/playlist/37i9dQZEVXbMDoHDwVN2tF?si=3d87034436a84644"
            onChange={(e) => setText(e.target.value)}
          />
          <button className={`form-button ${invalidInput ? 'shake-button' : ''}`} type="submit">Submit</button>
        </div>  
      </div>
    </form>
  );
  }

async function MakeRequest(url, link) {
  try {
    const response = await fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ 'playlist_link': link }),
      credentials: 'include',
    });

    if (!response.ok) {
      throw new Error('Network response was not ok');
    }

    return await response.json();
  } catch (error) {
    console.error('Error:', error);
  }
}

export default Form;