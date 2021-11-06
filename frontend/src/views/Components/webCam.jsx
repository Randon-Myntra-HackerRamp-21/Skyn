import React,{useRef, useCallback, useState, useEffect} from "react";
import Webcam from "react-webcam";

// MUI
import Button from '@mui/material/Button';
import Grid from '@mui/material/Grid';

function getWindowDimensions() {
  const { innerWidth: width, innerHeight: height } = window;
  return {
    width,
    height
  };
}

function useWindowDimensions() {
  const [windowDimensions, setWindowDimensions] = useState(getWindowDimensions());

  useEffect(() => {
    function handleResize() {
      setWindowDimensions(getWindowDimensions());
    }
    window.addEventListener('resize', handleResize);
    return () => window.removeEventListener('resize', handleResize);}, []);

    return windowDimensions;
}

const aspectRatio = 4/3;

const WebcamCapture = () => {
    let camHeight = useWindowDimensions().height
    let camWidth = useWindowDimensions().width
    if(camHeight > camWidth) {
        camHeight = camWidth * aspectRatio
    } else {
        camWidth = camHeight / aspectRatio
    }

    const videoConstraints = {
        height: camHeight,
        width: camWidth,
        facingMode: "user"
    };
    //1024 x 768

    console.log(useWindowDimensions())

    useEffect( () =>
        {
            console.log(videoConstraints.height)
            console.log(videoConstraints.width)
        }, [videoConstraints.height, videoConstraints.width]
    )

    const webcamRef = useRef(null);
    const capture = useCallback(
        () => {
            const imageSrc = webcamRef.current.getScreenshot();
            console.log(imageSrc)
        },
            [webcamRef]
    );

    const handleCapture = () => {
        capture();
    }
    
    return (
    <>
    
        <Grid item>
            <Webcam
            audio={false}
            height={videoConstraints.height}
            width={videoConstraints.width}
            ref={webcamRef}
            screenshotFormat="image/jpeg"
            videoConstraints={videoConstraints}
            />
        </Grid>
        <Grid item xs={12}>
            <Button 
            onClick={handleCapture} 
            variant="contained"
            fullWidth>
                Capture photo
            </Button>
        </Grid>
    </>
    );
};

export default WebcamCapture