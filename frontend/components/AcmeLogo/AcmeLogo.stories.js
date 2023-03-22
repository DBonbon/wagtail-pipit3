/* global module */

import React from 'react';
import AcmeLogo from './AcmeLogo';
import data from './AcmeLogo.data';

const AcmeLogoStory = {
    title: 'Components/AcmeLogo',
    component: AcmeLogo,
};
export default AcmeLogoStory;

export const AcmeLogoWithData = () => <AcmeLogo {...data} />;
export const AcmeLogoWithoutData = () => <AcmeLogo />;
