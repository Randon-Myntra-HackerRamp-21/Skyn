import React,{useState} from 'react';
import WebcamCapture from './Components/webCam'


// MUI
import Grid from '@mui/material/Grid';
import Container from '@mui/material/Container';

function ImageInput() {
    const [imageSrc, setImageSrc] = useState(null)
    if(imageSrc !== null) {
        console.log("we got an image")
        const data = new FormData()
            data.append("file", imageSrc)
            fetch("predict", {
                method: "put",
                body: data
            })
                .then(res => res.json())
                .then(data => {
                    if (data.error) {
                        console.log("Please add a photograph")
                    }
                    else {
                        console.log("All fin")
                    }

                })
                .catch(err => {

                    console.log(err.message)
                })
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
