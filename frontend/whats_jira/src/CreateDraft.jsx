import React, { useState } from 'react'
import axios from 'axios'
import './CreateDraft.css'

function CreateDraft() {
  const [message, setMessage] = useState('');
  const [status, setStatus] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSend = () => {
    setLoading(true);
    setStatus('');
    const data = {
        "fetch" : "yes"
    }
    axios.post('http://127.0.0.1:8000/draft', data)
      .then((response) => {
        setStatus(response.data.message);
        setMessage('');
        setLoading(false);
      })
      .catch(() => {
        setStatus('Failed to send.');
        setLoading(false);
      });
  };

  return (
    <div className="create-draft-bg">
      <div className="create-draft-card">
        {/* <h2 className="create-draft-title">Message</h2> */}
        {/* <input
          type="text"
          className="draft-input"
          placeholder="Type your message..."
          value={message}
          onChange={e => setMessage(e.target.value)}
        /> */}
        <button className="draft-send-btn" onClick={handleSend} disabled={loading}>Fetch Whatsapp Messages</button>        
        {loading && <div className="draft-status">Loading...</div>}
        {!loading && status && (
          <div className={`draft-status ${status.includes('sent') ? 'success' : 'error'}`}>{status}</div>
        )}
      </div>
    </div>
  )
}

export default CreateDraft
