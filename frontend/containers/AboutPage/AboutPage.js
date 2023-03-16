import React, { PureComponent } from 'react';

// import i18n from '../../i18n';
import PropTypes from 'prop-types';
import { basePageWrap } from '../BasePage';
import s from './AboutPage.module.css';

class AboutPage extends PureComponent {
    state = {};

    static defaultProps = {
        companyName: '',
        image:'',
    };

    static propTypes = {
        companyName: PropTypes.string,
    };

    render() {
        const { companyName, image } = this.props;
        return (
            <div className={s['AboutPage']}>
                <p>Company name: {companyName}</p>
                <p>Company name: {image.src}</p>
            </div>
        );
    }
}

export default basePageWrap(AboutPage);
