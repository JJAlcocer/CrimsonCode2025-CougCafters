// App.js
import React from 'react';
import './App.css';
import ExternalLinkButton from './components/ExternalLinkButton';

//Test
function ExternalLinkButton({ href, children, ...rest }) {
    console.log("Button rendered!", href, children, rest);
    return ( 0 );
}
//

function App() {
    return (
        <div className="App">
            <ExternalLinkButton
                href="https://open.spotify.com"
                className="spotify-button"
                style={{ backgroundColor: '#1DB954', color: 'white', padding: '10px 20px', borderRadius: '5px', textDecoration: 'none' }}
            >
                Connect to Spotify
            </ExternalLinkButton>
        </div>
    );
}

export default App;