import { render, /* screen */ } from '@testing-library/react';
import Layout from './';
// import data from './Layout.data';

describe('<Layout />', () => {
    it('Renders an empty Layout', () => {
        render(<Layout />);
    });

    // it('Renders Layout with data', () => {
    //     const { container } = render(<Layout {...data} />);
    //     expect(container).toMatchSnapshot();
    // });
});
