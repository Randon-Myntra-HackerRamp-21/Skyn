import React, { useState, useEffect } from 'react';

// MUI
import Container from '@mui/material/Container';
import Grid from '@mui/material/Grid';
import FormLabel from '@mui/material/FormLabel';
import Typography from '@mui/material/Typography';

import ProductCard from './Components/ProductCard'
import { useLocation } from 'react-router';



// {'face-moisturisers': [{'brand': 'azani active care',
//    'name': 'unisex acne rescue cream - 30 ml',
//    'price': '₹ 399',
//    'url': 'https://www.myntra.com/face-moisturisers/azani-active-care/azani-active-care-unisex-acne-rescue-cream---30-ml/15322518/buy',
//    'skin type': 'all',
//    'concern': ['deep nourishment', 'acne', 'blemishes', 'dull skin']},

const Products = {
    
    skinCare:
    {
        'face-moisturisers':
            [{
                'brand': 'azani active care',
                'name': 'unisex acne rescue cream - 30 ml',
                'price': '₹ 399',
                'url': 'https://www.myntra.com/face-moisturisers/azani-active-care/azani-active-care-unisex-acne-rescue-cream---30-ml/15322518/buy',
                'skin type': 'all',
                'concern': ['deep nourishment', 'acne', 'blemishes', 'dull skin']
            },
            {
                'brand': 'mamaearth',
                'name': 'vitamin c face milk with peach for skin illumination 100 ml',
                'price': '₹ 404',
                'url': 'https://www.myntra.com/face-moisturisers/mamaearth/mamaearth-vitamin-c-face-milk-with-peach-for-skin-illumination-100-ml/12411986/buy',
                'skin type': 'all',
                'concern': ['acne', 'blemishes', 'pigmentation', 'dull skin']
            }]
    },
    makeUp:
    {
        'foundations':
            [{
                'brand': 'wet n wild',
                'name': 'sustainable photo focus matte face primer - partners in prime',
                'price': '₹ 454',
                'url': 'https://www.myntra.com/foundation-and-primer/wet-n-wild/wet-n-wild-sustainable-photo-focus-matte-face-primer---partners-in-prime/12045988/buy',
                'skin type': 'normal',
                'skin tone': 'light to medium'
            },
            {
                'brand': 'faces canada',
                'name': 'ultime pro makeup fixer',
                'price': '₹ 486',
                'url': 'https://www.myntra.com/foundation-and-primer/faces-canada/faces-canada-ultime-pro-makeup-fixer/2421530/buy',
                'skin type': 'normal',
                'skin tone': 'light to medium'
            }]
    }
}


const Recommendations = () => {
    const {state} = useLocation();
    const {data} = state; 
    const {general, makeup} = data;
    return <>
        <Container sx={{ marginTop: "2vh", padding: 1 }} alignitems="center" width="inherit">
            <Typography gutterBottom variant="h4" component="div" marginTop="2vh" textAlign="center">
                Skin care
            </Typography>
            {Object.keys(general).map((type, products) => {
                return (<div><Typography gutterBottom variant="h5" component="div" marginTop="2vh" color="text.secondary">
                            {type}
                        </Typography>
                        <Grid container spacing={1}>
                    {general[type].slice(0,4).map((prod) => {
                        return <Grid item xs={6} md={3}>
                            <ProductCard
                                name={prod.name}
                                brand={prod.brand}
                                image={prod.img}
                                price={prod.price}
                                url={prod.url}
                                concern={prod.concern} />
                        </Grid>
                    })}
                </Grid></div>)
            })}

            <Typography gutterBottom variant="h4" component="div" marginTop="2vh" textAlign="center">
                Make up
            </Typography>

            <FormLabel component="legend">{ }</FormLabel>
            {/* {Object.keys(Products.makeUp).map((type, products)=>{
            return (<div><FormLabel component="legend">{type}</FormLabel><Grid container spacing={1}> */}
            <div>
            <Grid container spacing={1}>
            {makeup.map((prod) => {
                return <Grid item xs={6} md={3}>
                    <ProductCard
                        name={prod.name}
                        brand={prod.brand}
                        image={prod.img}
                        price={prod.price}
                        url={prod.url}
                        concern={prod.concern} />
                </Grid>
            })}
             </Grid></div>
            {/* </Grid></div>) */}
            {/* // })} */}
        </Container>
    </>
};

export default Recommendations;