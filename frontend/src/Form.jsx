import { useState } from 'react';
import { useNavigate } from 'react-router-dom';

const PlaylistURL = "http://localhost:8000/analysis/"

function Form() {
  const [text, setText] = useState('');
  const navigate = useNavigate();

  const handleSubmit = async (event) => {
    event.preventDefault();
    const responseFromServer = await MakeRequest(PlaylistURL, text );
    navigate('/new-page', { state: { data: responseFromServer } });
  }

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Text:
        <input
          type="text"
          value={text}
          onChange={(e) => setText(e.target.value)}
        />
      </label>
      <button type="submit">Submit</button>
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