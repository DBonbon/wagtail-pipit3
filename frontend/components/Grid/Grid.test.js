import { render, /* screen */ } from '@testing-library/react';
import Grid from './';
// import data from './Grid.data';

describe('<Grid />', () => {
    it('Renders an empty Grid', () => {
        render(<Grid />);
    });

    // it('Renders Grid with data', () => {
    //     const { container } = render(<Grid {...data} />);
    //     expect(container).toMatchSnapshot();
    // });
});
