import WebcamCapture from './Components/webCam'
import React from 'react'

// MUI
import Grid from '@mui/material/Grid';
import Container from '@mui/material/Container';

function ImageInput() {
    return (
        <>
            <Container maxWidth="xs" sx={{padding: 0}} alignItems="center">
                <Grid container justify="center">
                    <WebcamCapture />
                </Grid>
            </Container>
        </>
    )
}

export default ImageInput
