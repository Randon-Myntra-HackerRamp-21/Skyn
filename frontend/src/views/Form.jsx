import React, { useState, useRef} from "react";
import Container from '@mui/material/Container';
import Grid from '@mui/material/Grid';
import Radio from '@mui/material/Radio';
import RadioGroup from '@mui/material/RadioGroup';
import FormControlLabel from '@mui/material/FormControlLabel';
import FormControl from '@mui/material/FormControl';
import FormLabel from '@mui/material/FormLabel';
import Checkbox from '@mui/material/Checkbox';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import Select from '@mui/material/Select';

const skinToneValues = [1, 2, 3, 4, 5, 6]
const skinToneColors = ["rgb(249, 245, 236)", 
                        "rgb(250, 245, 234)",
                        "rgb(240, 227, 171)",
                        "rgb(206, 172, 104)",
                        "rgb(105, 59, 41)",
                        "rgb(33, 28, 40)",
                    ]
const color = "red"
const skinMetrics = {
        tone :5.0, 
        type: "All", 
        acne: "Severe"
    }
const skinTypes = ["All", "Oily", "Normal", "Dry"]
const acne  = ['Low','Moderate','Severe']
const otherConcerns = ['sensitive', 'fine lines', 'wrinkles', 'redness', 'pore', 'pigmentation', 'blackheads', 'whiteheads', 'blemishes', 'dark circles', 'eye bags', 'dark spots']
const Form = () => {
    const [currType, setCurrType] = useState()
    const [currTone, setCurrTone] = useState()

    const handleChange = (e) => {
        setCurrTone(e.target.value)
    }

    const handleSubmit = () => {

    }

    return (
        <>
        <Container maxWidth="xs" sx={{ marginTop:"2vh"}} alignitems="center" width="inherit">
            <Typography variant="h5" component="div" textAlign="center">
                    Results
            </Typography>
{/* 
            <FormControl fullWidth>
            </FormControl> */}

            <FormControl component="fieldset" sx={{ marginTop:"3vh"}}>
                <Grid container>
                    <Grid item xs={9}>
                        <InputLabel id="demo-simple-select-label">Tone</InputLabel>
                        <Select
                        labelId="demo-simple-select-label"
                        id="demo-simple-select"
                        value={currTone}
                        label="Age"
                        onChange={handleChange}
                        fullWidth>
                            {skinToneValues.map((value)=>{
                                return (<MenuItem value={value}>{value}</MenuItem>)
                            })}
                        </Select>
                    </Grid>
                    <Grid item xs={3}>
                        <div 
                        style={{height:"3rem", 
                            width:"3rem", 
                            backgroundColor: skinToneColors[currTone-1],
                            margin: "0 auto",
                            justifySelf:"center",
                            borderRadius: "10%",
                            }}></div>
                    </Grid>
                </Grid>
            <Grid marginTop="2vh">
                <FormLabel component="legend">Type</FormLabel>
                <RadioGroup 
                    row 
                    name="row-radio-buttons-group" 
                    defaultValue={skinMetrics.type} 
                    value={currType}>
                        <Grid container>
                            {skinTypes.map((type)=>{
                                return (
                                    <Grid item xs={6}>
                                        <FormControlLabel 
                                        value={type} 
                                        control={<Radio />} 
                                        label={type} />
                                    </Grid>)
                            })}
                        </Grid>
                </RadioGroup>
            </Grid>
            
            <Grid marginTop="2vh">
                <FormLabel component="legend">Acne</FormLabel>
                <RadioGroup 
                    row 
                    name="row-radio-buttons-group" 
                    defaultValue={skinMetrics.acne} 
                    value={currType}>
                        <Grid container>
                            {acne.map((ac)=>{
                                return (
                                    <Grid item >
                                        <FormControlLabel 
                                        value={ac} 
                                        control={<Radio />} 
                                        label={ac} />
                                    </Grid>)
                            })}
                        </Grid>
                </RadioGroup>
            </Grid>
            
            <Grid marginTop="2vh">
            {/* <Typography variant="h6" component="div" textAlign="center">
                    Specify other skin concerns
            </Typography> */}
                <FormLabel component="legend">Specify other skin concerns</FormLabel>
                <Grid container>
                    {otherConcerns.map((concern)=>{
                        return (
                            <Grid item xs={6}>
                                <FormControlLabel control={<Checkbox />}
                                value={concern} 
                                label={concern.charAt(0).toUpperCase() + concern.slice(1)} />
                            </Grid>)
                    })}
                </Grid>
            </Grid>

            <Grid marginTop="2vh" item xs={12}>
                <Button
                    onClick={handleSubmit}
                    variant="contained"
                    fullWidth>
                    Submit
                </Button>
            </Grid>
            </FormControl>
        </Container>
        </>
    )
}




export default Form;
