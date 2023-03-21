/* global module */

import React from 'react';
import GamePage from './GamePage';
import data from './GamePage.data';

const GamePageStory = {
    title: 'Containers/GamePage',
    component: GamePage,
};
export default GamePageStory;

export const GamePageWithData = () => <GamePage {...data} />;
export const GamePageWithoutData = () => <GamePage />;
