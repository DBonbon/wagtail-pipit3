/* global module */

import React from 'react';
import searchIcon from './searchIcon';
import data from './searchIcon.data';

const searchIconStory = {
    title: 'Components/searchIcon',
    component: searchIcon,
};
export default searchIconStory;

export const searchIconWithData = () => <searchIcon {...data} />;
export const searchIconWithoutData = () => <searchIcon />;
