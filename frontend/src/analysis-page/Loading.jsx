import { Audio } from 'react-loader-spinner';

function Loading() {
    return (
            <div className="Loading-div">
                <Audio
                    height="80"
                    width="80"
                    radius="9"
                    color="#1DB954"
                    ariaLabel="loading"
                    wrapperStyle
                    wrapperClass
                />
                <h2>Crunching the numbers...</h2>
            </div>
        );
}

export default Loading;