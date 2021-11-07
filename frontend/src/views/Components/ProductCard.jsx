import React,{ useState } from 'react';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Typography from '@mui/material/Typography';
import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';

const unavailableImage = process.env.PUBLIC_URL+'./unavailable.png'

export default function ProductCard({name="balls cream", Price=2000, brand="balls itch", url="https://www.myntra.com/", concern=['wrinkles', 'acne'], image = ''}) {
    const redirectProduct = () => {
        window.location.replace(url);
    }
    return (  
        <Box onClick={redirectProduct} sx={{lineHeight:"low"}}>
            <Card sx={{ maxWidth: "50vw" }}>
            <CardMedia
                component="img"
                height="200vh"
                image={image}
                alt="green iguana"
                />
            <CardContent>
                <Typography variant="body2" color="text.secondary" gutterBottom>
                    {brand}
                    <Typography component="div" color="text.primary" variant="inline" sx={{float: "right", fontWeight:"bold"}}>
                        ₹{Price}
                    </Typography>
                </Typography>
                <Typography gutterBottom variant="h6" component="div">
                {name.length > 40 ? name.substring(0, 40)+"..." : name}
                </Typography>
                <Grid container>
                    {concern.map((concern) => {
                        return <Grid item xs={12}><Typography 
                                    variant="body2" 
                                    color="white" 
                                    variant="inline" 
                                    backgroundColor="info.main"
                                    borderRadius="5%"
                                    paddingLeft="2%"
                                    paddingRight="2%"
                                    paddingTop="1%"
                                    paddingBottom="1%"
                                    marginRight="2%"
                                    >{concern.split(' ').join('-')}</Typography></Grid>
                    })}
                </Grid>
            </CardContent>
            </Card>
        </Box>
    );
}