/* global module */

import React from 'react';
import Grid from './Grid';
import data from './Grid.data';

const GridStory = {
    title: 'Components/Grid',
    component: Grid,
};
export default GridStory;

export const GridWithData = () => <Grid {...data} />;
export const GridWithoutData = () => <Grid />;
