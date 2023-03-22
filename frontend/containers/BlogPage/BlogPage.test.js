import { render, /* screen */ } from '@testing-library/react';
import BlogPage from './';
// import data from './BlogPage.data';

describe('<BlogPage />', () => {
    it('Renders an empty BlogPage', () => {
        render(<BlogPage />);
    });

    // it('Renders BlogPage with data', () => {
    //     const { container } = render(<BlogPage {...data} />);
    //     expect(container).toMatchSnapshot();
    // });
});
