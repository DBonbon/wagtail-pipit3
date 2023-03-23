import { render, /* screen */ } from '@testing-library/react';
import Navbar from './';
// import data from './Navbar.data';

describe('<Navbar />', () => {
    it('Renders an empty Navbar', () => {
        render(<Navbar />);
    });

    // it('Renders Navbar with data', () => {
    //     const { container } = render(<Navbar {...data} />);
    //     expect(container).toMatchSnapshot();
    // });
});
