/* global module */

import React from 'react';
import Navbar from './Navbar';
import data from './Navbar.data';

const NavbarStory = {
    title: 'Components/Navbar',
    component: Navbar,
};
export default NavbarStory;

export const NavbarWithData = () => <Navbar {...data} />;
export const NavbarWithoutData = () => <Navbar />;
