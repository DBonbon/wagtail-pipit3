import { render, /* screen */ } from '@testing-library/react';
import GamePage from './';
// import data from './GamePage.data';

describe('<GamePage />', () => {
    it('Renders an empty GamePage', () => {
        render(<GamePage />);
    });

    // it('Renders GamePage with data', () => {
    //     const { container } = render(<GamePage {...data} />);
    //     expect(container).toMatchSnapshot();
    // });
});
