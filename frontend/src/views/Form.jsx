import React, { useState, useRef, useCallback, useEffect } from "react";
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
                    <FormControlLabel control={<Checkbox defaultChecked />} label="Label" />
                </Grid>
                <Grid item xs={3}>
                    <FormControlLabel control={<Checkbox defaultChecked />} label="Label" />
                </Grid>
                <Grid item xs={3}>
                    <FormControlLabel control={<Checkbox defaultChecked />} label="Label" />
                </Grid>
                <Grid item xs={3}>
                    <FormControlLabel control={<Checkbox defaultChecked />} label="Label" />
                </Grid>



                <Grid item xs={3}>
                    <FormControlLabel control={<Checkbox defaultChecked />} label="Label" />
                </Grid>
                <Grid item xs={3}>
                    <FormControlLabel control={<Checkbox defaultChecked />} label="Label" />
                </Grid>
                <Grid item xs={3}>
                    <FormControlLabel control={<Checkbox defaultChecked />} label="Label" />
                </Grid>
                <Grid item xs={3}>
                    <FormControlLabel control={<Checkbox defaultChecked />} label="Label" />
                </Grid>



                <Grid item xs={3}>
                    <FormControlLabel control={<Checkbox defaultChecked />} label="Label" />
                </Grid>
                <Grid item xs={3}>
                    <FormControlLabel control={<Checkbox defaultChecked />} label="Label" />
                </Grid>
                <Grid item xs={3}>
                    <FormControlLabel control={<Checkbox defaultChecked />} label="Label" />
                </Grid>
                <Grid item xs={3}>
                    <FormControlLabel control={<Checkbox defaultChecked />} label="Label" />
                </Grid>



                <Grid item xs={3}>
                    <FormControlLabel control={<Checkbox defaultChecked />} label="Label" />
                </Grid>
                <Grid item xs={3}>
                    <FormControlLabel control={<Checkbox defaultChecked />} label="Label" />
                </Grid>
                <Grid item xs={3}>
                    <FormControlLabel control={<Checkbox defaultChecked />} label="Label" />
                </Grid>
                <Grid item xs={3}>
                    <FormControlLabel control={<Checkbox defaultChecked />} label="Label" />
                </Grid>

                <Button variant="outlined" sx = {{ m:"auto"}}>Outlined</Button>
            </Grid>






        {/* </FormControl> */}



    </Container>);
}




export default Form;