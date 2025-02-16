// components/ExternalLinkButton.js
import React from 'react';

function ExternalLinkButton({ href, children, ...rest }) {
    return (
        <a href={href} target="_blank" rel="noopener noreferrer" {...rest}>
            {children}
        </a>
    );
}

export default ExternalLinkButton;