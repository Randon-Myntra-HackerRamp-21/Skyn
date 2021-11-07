import React,{useState} from 'react';
import WebcamCapture from './Components/webCam'


// MUI
import Grid from '@mui/material/Grid';
import Container from '@mui/material/Container';
import PhotoCameraIcon from '@mui/icons-material/PhotoCamera';
import Button from '@mui/material/Button';

function ImageInput() {
    const [landingPage, setLandingPage] = useState(true)
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
            <Container maxWidth="xs" sx={{padding: 0}} alignitems="center" spacing={1}>
                <Grid container justify="center" sx={{maxHeight:"100vh"}}>
                    {landingPage ? 
                        <Grid item xs={6} sx={{margin:"40vh auto"}} textAlign="center">
                            <PhotoCameraIcon sx={{fontSize:"5em"}}/>    
                            <Button 
                                onClick={() => {setLandingPage(false)}} 
                                variant="contained"
                                fullWidth>
                                Take a photo
                            </Button>
                        </Grid>:
                        <WebcamCapture setImageSrc={setImageSrc}/>
                    }
                </Grid>   
            </Container>
        </>
    )
}

export default ImageInput
