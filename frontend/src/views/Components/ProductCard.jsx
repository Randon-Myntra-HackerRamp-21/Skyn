import React,{ useState } from 'react';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Typography from '@mui/material/Typography';
import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';

const unavailableImage = process.env.PUBLIC_URL+'./unavailable.png'

export default function ProductCard({name="cream", price=2000, brand="brand", url="https://www.myntra.com/", concern=[], image = ''}) {
    const redirectProduct = () => {
        window.location.replace(url);
    }
    concern = [...new Set(concern)]
    return (  
        <Box onClick={redirectProduct} sx={{lineHeight:"low"}}>
            <Card sx={{ maxWidth: "50vw" }}>
            <CardMedia
                component="img"
                height="200vh"
                image={image}
                alt="Product image"
                />
            <CardContent>
                <Typography variant="body2" color="text.secondary" gutterBottom>
                    {brand}
                    <Typography component="div" color="text.primary" variant="inline" sx={{float: "right", fontWeight:"bold"}}>
                        {price}
                    </Typography>
                </Typography>
                <Typography gutterBottom variant="h6" component="div">
                {name.length > 40 ? name.substring(0, 40)+"..." : name}
                </Typography>
                <Grid container>
                    {concern.filter(n => n).map((concern) => {
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
                                    >{concern}</Typography></Grid>
                    })}
                </Grid>
            </CardContent>
            </Card>
        </Box>
    );
}