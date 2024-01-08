import { useState } from 'react';
import { useNavigate } from 'react-router-dom';

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
    navigate('/analysis/', { state: { playlist_link: text } });
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

export default Form;