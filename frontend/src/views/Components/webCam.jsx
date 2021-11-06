import React,{useRef, useCallback, useState, useEffect} from "react";
import Webcam from "react-webcam";
import * as faceapi from 'face-api.js';

import './webCam.css'
// MUI
import Button from '@mui/material/Button';
import Grid from '@mui/material/Grid';
import Typography from '@mui/material/Typography';

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
        camHeight = Math.round(camWidth * aspectRatio)
    } else {
        camHeight = Math.round(camHeight * 0.9)
        camWidth = Math.round(camHeight / aspectRatio)
    }
    const videoConstraints = {
        height: camHeight,
        width: camWidth,
        facingMode: "user"
    };
    //1024 x 768
    
    const videoRef = useRef()
    const canvasRef = useRef()
    

    useEffect( () =>
        {
            console.log(videoConstraints.height)
            console.log(videoConstraints.width)
        }, [videoConstraints.height, videoConstraints.width]
    )
    // const webcamRef = useRef(null);
    // const capture = useCallback(
    //     () => {
    //         const imageSrc = webcamRef.current.getScreenshot();
    //         console.log(imageSrc)
    //     }, [webcamRef]
    // );
    const handleCapture = () => {
        // capture();
    }
    
    const [initialising, setInitialising] = useState(false)
    useEffect(()=>{
        const loadModels = async () => {
            const MODEL_URI = process.env.PUBLIC_URL + '/models';
            setInitialising(true)
            Promise.all([
                faceapi.nets.tinyFaceDetector.loadFromUri(MODEL_URI),
                faceapi.nets.faceLandmark68Net.loadFromUri(MODEL_URI),
                faceapi.nets.faceRecognitionNet.loadFromUri(MODEL_URI),
                faceapi.nets.faceExpressionNet.loadFromUri(MODEL_URI),
            ]).then(startVideo);
        }
        loadModels();
    },[])
    
    const startVideo = () => {
        navigator.getUserMedia = ( navigator.getUserMedia ||
                       navigator.webkitGetUserMedia ||
                       navigator.mozGetUserMedia ||
                       navigator.msGetUserMedia);
        navigator.getUserMedia(
            {
                video: {},
            },
            (stream) => (videoRef.current.srcObject = stream),
            (err) => console.log(err)
        );
    }

    const handleVideoOnPlay = () => {
        setInterval( async () => {
            if(initialising) {
                setInitialising(false)
            }
            const detections = await faceapi.detectAllFaces(videoRef.current, new faceapi.TinyFaceDetectorOptions());
            // console.log(detections)
        }, 100)
    }

    return (
    <>
        <Grid item>
        <Typography variant="h5" component="div" textAlign="center">
            {initialising ? "Initialising..." : "Ready"}
        </Typography>
            {/* <Webcam
            id="webcam"
            audio={false}
            height={videoConstraints.height}
            width={videoConstraints.width}
            ref={webcamRef}
            screenshotFormat="image/jpeg"
            videoConstraints={videoConstraints}>
            </Webcam> */}
            <video ref={videoRef} autoPlay muted 
            height={videoConstraints.height}
            width={videoConstraints.width}
            onPlay={handleVideoOnPlay}>
                <canvas ref={canvasRef} id="overlay"
                height={videoConstraints.height}
                width={videoConstraints.width}/>
            </video>
        </Grid>
        <Grid item xs={12}>
            <Button 
            onClick={handleCapture} 
            variant="contained"
            disabled={initialising}
            fullWidth>
                Capture photo
            </Button>
        </Grid>
    </>
    );
};

export default WebcamCapture