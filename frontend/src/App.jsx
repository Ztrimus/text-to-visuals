
import { useState, useEffect, useRef } from 'react';
import Mermaid from 'react-mermaid2';
import { 
  SparklesIcon, 
  ExclamationTriangleIcon,
  ChartBarIcon,
  Cog6ToothIcon,
  EyeIcon
} from '@heroicons/react/24/outline';
import './App.css';

function App() {
  const [text, setText] = useState('');
  const [mermaid, setMermaid] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [theme, setTheme] = useState('light');
  const [showSettings, setShowSettings] = useState(false);
  const settingsRef = useRef(null);

  // Theme management
  useEffect(() => {
    const savedTheme = localStorage.getItem('theme') || 'light';
    setTheme(savedTheme);
    document.documentElement.setAttribute('data-theme', savedTheme);
  }, []);

  // Close settings dropdown when clicking outside
  useEffect(() => {
    const handleClickOutside = (event) => {
      if (settingsRef.current && !settingsRef.current.contains(event.target)) {
        setShowSettings(false);
      }
    };

    document.addEventListener('mousedown', handleClickOutside);
    return () => document.removeEventListener('mousedown', handleClickOutside);
  }, []);

  const handleThemeChange = (newTheme) => {
    setTheme(newTheme);
    localStorage.setItem('theme', newTheme);
    
    if (newTheme === 'auto') {
      const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
      document.documentElement.setAttribute('data-theme', prefersDark ? 'dark' : 'light');
    } else {
      document.documentElement.setAttribute('data-theme', newTheme);
    }
    setShowSettings(false);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!text.trim()) return;
    
    setLoading(true);
    setError('');
    setMermaid('');
    
    try {
      const res = await fetch('http://127.0.0.1:8000/generate_mermaid', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text })
      });
      
      if (!res.ok) {
        throw new Error(`Server error: ${res.status}`);
      }
      
      const data = await res.json();
      setMermaid(data.mermaid);
    } catch (err) {
      setError(err.message || 'Failed to generate diagram. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div id="root">
      <div className="app-container">
        {/* StackEdit-style Header */}
        <header className="header">
          <h1>Text to Diagram</h1>
          
          <div className="header-actions">
            <div className="settings-dropdown" ref={settingsRef}>
              <button 
                className="settings-button"
                onClick={() => setShowSettings(!showSettings)}
                title="Settings"
              >
                <Cog6ToothIcon className="w-4 h-4" />
              </button>
              
              {showSettings && (
                <div className="settings-menu">
                  <div className="settings-menu-item">
                    <EyeIcon className="w-4 h-4" />
                    <span>Appearance</span>
                    <div className="theme-options">
                      <div 
                        className={`theme-option ${theme === 'light' ? 'active' : ''}`}
                        onClick={() => handleThemeChange('light')}
                      >
                        Light
                      </div>
                      <div 
                        className={`theme-option ${theme === 'dark' ? 'active' : ''}`}
                        onClick={() => handleThemeChange('dark')}
                      >
                        Dark
                      </div>
                      <div 
                        className={`theme-option ${theme === 'auto' ? 'active' : ''}`}
                        onClick={() => handleThemeChange('auto')}
                      >
                        Auto
                      </div>
                    </div>
                  </div>
                </div>
              )}
            </div>
          </div>
        </header>

        {/* Main Content - StackEdit Split Layout */}
        <main className="main-content">
          {/* Input Section - Left Panel (Editor) */}
          <section className="input-section">
            <form onSubmit={handleSubmit} className="form-container">
              <div className="textarea-container">
                <textarea
                  value={text}
                  onChange={(e) => setText(e.target.value)}
                  placeholder="Describe your diagram here...

For example:
- Create a flowchart for user authentication
- Show project timeline from start to finish  
- Design a mind map for marketing strategy"
                  className="input-textarea"
                />
                
                <button 
                  type="submit" 
                  disabled={loading || !text.trim()}
                  className={`generate-btn ${loading ? 'loading' : ''}`}
                  title={loading ? 'Generating diagram...' : 'Generate diagram'}
                >
                  {loading ? (
                    <div className="loading-content">
                      <div className="loading-spinner" />
                      <span className="loading-text">Working</span>
                    </div>
                  ) : (
                    <div className="generate-btn-text">
                      <SparklesIcon className="generate-icon" />
                      <span className="generate-label">Go</span>
                    </div>
                  )}
                </button>
              </div>
            </form>
          </section>

          {/* Output Section - Right Panel (Preview) */}
          <section className="output-section">
            {error && (
              <div className="error-message">
                <ExclamationTriangleIcon className="w-4 h-4" />
                {error}
              </div>
            )}
            
            {mermaid ? (
              <div className="diagram-container">
                <Mermaid chart={mermaid} />
              </div>
            ) : !loading && !error && (
              <div className="empty-state">
                <ChartBarIcon className="empty-state-icon" />
                <p>Your diagram will appear here</p>
                <p>Enter a description on the left and click Generate</p>
              </div>
            )}
          </section>
        </main>
      </div>
    </div>
  );
}

export default App;
