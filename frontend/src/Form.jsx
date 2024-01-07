import { useState } from 'react';

const PlaylistURL = "http://localhost:8000/analysis/"

function Form() {
  const [text, setText] = useState('');

  const handleSubmit = async (event) => {
    event.preventDefault();

    MakeRequest(PlaylistURL, text );
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

    const data = await response.json();
    console.log(data);
  } catch (error) {
    console.error('Error:', error);
  }
}

export default Form;