import React,{useState} from 'react';
import WebcamCapture from './Components/webCam'


// MUI
import Grid from '@mui/material/Grid';
import Container from '@mui/material/Container';

function ImageInput() {
    const [imageSrc, setImageSrc] = useState(null)
    if(imageSrc !== null) {
        console.log("we got an image")
    }
    return (
        <>
            <Container maxWidth="xs" sx={{padding: 0}} alignItems="center" spacing={1}>
                <Grid container justify="center">
                    <WebcamCapture setImageSrc={setImageSrc}/>
                </Grid>
            </Container>
        </>
    )
}

export default ImageInput
