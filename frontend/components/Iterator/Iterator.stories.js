/* global module */

import React from 'react';
import Iterator from './Iterator';
import data from './Iterator.data';

const IteratorStory = {
    title: 'Components/Iterator',
    component: Iterator,
};
export default IteratorStory;

export const IteratorWithData = () => <Iterator {...data} />;
export const IteratorWithoutData = () => <Iterator />;
