import { render, /* screen */ } from '@testing-library/react';
import searchIcon from './';
// import data from './searchIcon.data';

describe('<searchIcon />', () => {
    it('Renders an empty searchIcon', () => {
        render(<searchIcon />);
    });

    // it('Renders searchIcon with data', () => {
    //     const { container } = render(<searchIcon {...data} />);
    //     expect(container).toMatchSnapshot();
    // });
});
