
import PropTypes from 'prop-types';
import { useState, useEffect } from 'react';

ProgressRing.propTypes = {
    text: PropTypes.string.isRequired,
    value: PropTypes.number.isRequired,
};

function ProgressRing({ text, value }) {
    const radius = 50;
    const circumference = 2 * Math.PI * radius;
    const unChangedValue = value;
    // if text is loudness, then we want to make sure that the quieter songs are closer to the center
    if (text === 'Loudness') {
        value = (Math.log(value + 15) / Math.log(1.5)) * 10;
    }
    if (text === 'Tempo') {
        value = value / 500 * 100;
    }
    if (text === 'Duration') {
        if (value > 500) {
            value = 100;
        }
        value = value / 500 * 100;
    }

    const [offset, setOffset] = useState(circumference);

    useEffect(() => {
        const progress = value; // Replace this with the actual progress
        const newOffset = circumference - (circumference * progress / 100);
        setOffset(newOffset);
    }, [value, circumference]);

    const newOffset = circumference - (value / 100 * circumference);
    // the amount to rotate the circle so that the bar is symmetrical across the y-axis
    const rotation = newOffset / circumference * 360 / 2;

    function getColor(value) {
        let hue;
        // maybe add random hue out of choice in the future
        hue = 325
        const lightness = 100 - value; // make color darker as value increases
        return `hsl(${hue}, 100%, ${lightness}%)`;
    }

  return (
    <div className='progress-div'>
        <h4 className="ring-header">{text}</h4>
        <svg width="120" height="120" >
        <circle
            fill="transparent"
            strokeWidth="10"
            r={radius}
            cx="60"
            cy="60"
        />
        <circle
            className="progress-ring"
            stroke={getColor(value)}
            fill="transparent"
            strokeWidth="10"
            strokeLinecap="round"
            strokeDasharray={circumference}
            strokeDashoffset={offset}
            r={radius}
            cx="60"
            cy="60"
            style={{ transform: `rotate(${rotation + 90}deg)`, transformOrigin: '60px 60px' }}
        />
        <text className="ring-text" x="60" y="60" textAnchor="middle" dy=".3em">{unChangedValue}</text>
        </svg>
    </div>
  );
}

export default ProgressRing;