// src/App.js

import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [memos, setMemos] = useState([]);
  const [newMemo, setNewMemo] = useState({ id: 0, title: '', content: '' });

  useEffect(() => {
    fetchMemos();
  }, []);

  const fetchMemos = async () => {
    try {
      const response = await axios.get('http://127.0.0.1:8000/memos/');
      setMemos(response.data);
    } catch (error) {
      console.error('Failed to fetch memos: ', error);
    }
  };

  const handleCreateMemo = async () => {
    try {
      await axios.post('http://127.0.0.1:8000/memos/', newMemo);
      fetchMemos();
      setNewMemo({ id: 0, title: '', content: '' });
    } catch (error) {
      console.error('Failed to create memo: ', error);
    }
  };

  return (
    <div className="App">
      <h1>Memo App</h1>
      <div>
        <h2>Create Memo</h2>
        <input
          type="text"
          value={newMemo.title}
          onChange={(e) => setNewMemo({ ...newMemo, title: e.target.value })}
          placeholder="Title"
        />
        <textarea
          value={newMemo.content}
          onChange={(e) => setNewMemo({ ...newMemo, content: e.target.value })}
          placeholder="Content"
        />
        <button onClick={handleCreateMemo}>Create Memo</button>
      </div>
      <div>
        <h2>Memo List</h2>
        <ul>
          {memos.map((memo) => (
            <li key={memo.id}>
              <h3>{memo.title}</h3>
              <p>{memo.content}</p>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default App;
