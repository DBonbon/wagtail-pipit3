import { render, /* screen */ } from '@testing-library/react';
import Iterator from './';
// import data from './Iterator.data';

describe('<Iterator />', () => {
    it('Renders an empty Iterator', () => {
        render(<Iterator />);
    });

    // it('Renders Iterator with data', () => {
    //     const { container } = render(<Iterator {...data} />);
    //     expect(container).toMatchSnapshot();
    // });
});
