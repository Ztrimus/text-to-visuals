
import { useState } from 'react';
import Mermaid from 'react-mermaid2';
import './App.css';

function App() {
  const [text, setText] = useState('');
  const [mermaid, setMermaid] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');
    setMermaid('');
    try {
      const res = await fetch('http://127.0.0.1:8000/generate_mermaid', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text })
      });
      if (!res.ok) throw new Error('Server error');
      const data = await res.json();
      setMermaid(data.mermaid);
    } catch (err) {
      setError('Failed to generate diagram.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <h1>Text to Mermaid Visualizer</h1>
      <form onSubmit={handleSubmit} style={{ marginBottom: 20 }}>
        <textarea
          value={text}
          onChange={e => setText(e.target.value)}
          rows={3}
          placeholder="Describe your diagram..."
          style={{ width: '100%', maxWidth: 500 }}
        />
        <br />
        <button type="submit" disabled={loading || !text.trim()}>
          {loading ? 'Generating...' : 'Generate Diagram'}
        </button>
      </form>
      {error && <div style={{ color: 'red' }}>{error}</div>}
      {mermaid && (
        <div style={{ background: '#fff', padding: 16, borderRadius: 8, maxWidth: 700 }}>
          <Mermaid chart={mermaid} />
        </div>
      )}
    </div>
  );
}

export default App;
