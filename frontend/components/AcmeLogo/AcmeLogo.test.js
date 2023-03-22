import { render, /* screen */ } from '@testing-library/react';
import AcmeLogo from './';
// import data from './AcmeLogo.data';

describe('<AcmeLogo />', () => {
    it('Renders an empty AcmeLogo', () => {
        render(<AcmeLogo />);
    });

    // it('Renders AcmeLogo with data', () => {
    //     const { container } = render(<AcmeLogo {...data} />);
    //     expect(container).toMatchSnapshot();
    // });
});
