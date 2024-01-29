import { useLayoutEffect, useRef } from 'react';
import { useState } from 'react';
import PropTypes from 'prop-types';

ScrollingTitle.propTypes = {
    text: PropTypes.string.isRequired,
};

function ScrollingTitle({ text }) {
    const titleRef = useRef(null);
    const [isTooLong, setIsTooLong] = useState(false);

    useLayoutEffect(() => {
        const titleWidth = titleRef.current.scrollWidth;
        const containerWidth = titleRef.current.offsetWidth;
        if (titleWidth > containerWidth) {
            // If the text is too long, add the 'animate' class
            titleRef.current.classList.add('animate');
            setIsTooLong(true);
        }
    }, [text]); // Re-run this effect whenever `text` changes

    return (
        <h1 className="playlist-title">
            <div ref={titleRef} className="title-container">
                <span>{text}</span>
                {isTooLong && <span>{text}</span>}
            </div>
        </h1>
    );
}

export default ScrollingTitle;