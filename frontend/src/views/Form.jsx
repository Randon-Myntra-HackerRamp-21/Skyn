import React, { useState, setState, useRef, useCallback, useEffect } from "react";
import CssBaseline from '@mui/material/CssBaseline';
import Container from '@mui/material/Container';
import Grid from '@mui/material/Grid';
import Radio from '@mui/material/Radio';
import RadioGroup from '@mui/material/RadioGroup';
import FormControlLabel from '@mui/material/FormControlLabel';
import FormControl from '@mui/material/FormControl';
import FormLabel from '@mui/material/FormLabel';
import FormGroup from '@mui/material/FormGroup';
import FormHelperText from '@mui/material/FormHelperText';
import Checkbox from '@mui/material/Checkbox';
import Button from '@mui/material/Button';



// function Alert(props) {
//   return <MuiAlert elevation={6} variant="filled" {...props} />;
// }
// const useStyles = makeStyles((theme) => ({
//     root: {
//       '& > *': {
//         margin: theme.spacing(1),
//       },
//     },
//     input: {
//       display: 'none',
//     },
//   }));


const Form = () => {


    const [features, setFeatures] = useState({normal:false, dry:false, oily:false, combination:false, 
    acne:false, sensitive:false, fineLines:false, wrinkles:false, 
    "redness":false, dull:false, pore:false, pigmentation:false, 
    blackheads:false, whiteheads:false, blemishes:false, darkCircles:false, 
    eyeBags:false, darkSpots:false});
    const handleChange = (event) => {
    setFeatures({
      ...features,
      [event.target.name]: event.target.checked,
    });
    console.log(features)
  };
    return (<Container fixed sx={{ p: 10, textAlign:"center" }}>
        
        {/* <FormControl component="fieldset" > */}
           
        <FormLabel component="legend">Skin type</FormLabel>
            <RadioGroup row aria-label="gender" name="row-radio-buttons-group" sx={{ m:"auto" }}>
            <FormControlLabel value="female" control={<Radio />} label="Female"  sx = {{
                m:"auto"
            }}/>
                <FormControlLabel value="male" control={<Radio />} label="Male"  sx = {{
                m:"auto"
            }}/>
                <FormControlLabel value="other" control={<Radio />} label="Other"  sx = {{
                m:"auto"
            }}/>
            </RadioGroup>
            <p></p>

            <FormLabel component="legend">Skin tone</FormLabel>
            <RadioGroup row aria-label="gender" name="row-radio-buttons-group" >
                <FormControlLabel value="female" control={<Radio />} label="Female"  sx = {{
                m:"auto"
            }}/>
                <FormControlLabel value="male" control={<Radio />} label="Male"  sx = {{
                m:"auto"
            }}/>
                <FormControlLabel value="other" control={<Radio />} label="Other"  sx = {{
                m:"auto"
            }}/>
                
            </RadioGroup>
            <p></p>
            <FormLabel component="legend">Other concerns</FormLabel>
            <Grid container spacing={2}>
                <Grid item xs={3}>
                    <FormControlLabel control={<Checkbox checked={features.acne} onChange={handleChange} name = "acne" />} label="acne" />
                </Grid>
                <Grid item xs={3}>
                    <FormControlLabel control={<Checkbox checked={features.sensitive} onChange={handleChange}  name = "sensitive"/>} label="sensitive" />
                </Grid>
                <Grid item xs={3}>
                    <FormControlLabel control={<Checkbox checked={features.fineLines} onChange={handleChange} name = "fineLines"/>} label="fine Lines" />
                </Grid>
                <Grid item xs={3}>
                    <FormControlLabel control={<Checkbox checked={features.wrinkles} onChange={handleChange} name="wrinkles" />} label="wrinkles" />
                </Grid>



                <Grid item xs={3}>
                    <FormControlLabel control={<Checkbox checked={features.redness} onChange={handleChange} name = "redness" />} label="redness" />
                </Grid>
                <Grid item xs={3}>
                    <FormControlLabel control={<Checkbox checked={features.dull} onChange={handleChange} name = "dullness" />} label="dullness" />
                </Grid>
                <Grid item xs={3}>
                    <FormControlLabel control={<Checkbox checked={features.pore} onChange={handleChange} name="pore"/>} label="large pores" />
                </Grid>
                <Grid item xs={3}>
                    <FormControlLabel control={<Checkbox checked={features.pigmentation} onChange={handleChange} name="pigmentation" />} label="pigmentation" />
                </Grid>



                <Grid item xs={3}>
                    <FormControlLabel control={<Checkbox checked={features.blackheads} onChange={handleChange} name = "blackheads" />} label="blackheads" />
                </Grid>
                <Grid item xs={3}>
                    <FormControlLabel control={<Checkbox checked={features.whiteheads} onChange={handleChange} name="whiteheads" />} label="whiteheads" />
                </Grid>
                <Grid item xs={3}>
                    <FormControlLabel control={<Checkbox checked={features.blemishes} onChange={handleChange} name = "blemishes" />} label="blemishes" />
                </Grid>
                <Grid item xs={3}>
                    <FormControlLabel control={<Checkbox checked={features.darkCircles} onChange={handleChange} name="darkCircles" />} label="dark circles" />
                </Grid>



                <Grid item xs={3}>
                    <FormControlLabel control={<Checkbox checked={features.eyeBags} onChange={handleChange} name = "eyeBags"/>} label="eye bags" />
                </Grid>
                <Grid item xs={3}>
                    <FormControlLabel control={<Checkbox checked={features.darkSpots} onChange={handleChange} name = "darkSpots" />} label="dark spots" />
                </Grid>
                
                
                
            </Grid>
            <Button variant="outlined" sx = {{ m:"auto"}}>Outlined</Button>






        {/* </FormControl> */}



    </Container>);
}




export default Form;
