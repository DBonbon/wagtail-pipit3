import React from 'react';
import PropTypes from 'prop-types';
import { basePageWrap } from '../BasePage';
import Hero from '../../components/Hero';
import RawHtml from '../../components/RawHtml';
import s from './ArticlePage.module.css';

const ArticlePage = ({ title, richText, image }) => {
    return (
        <div className={s.Container}>
            <Hero title={title} />
            <RawHtml html={richText} />
            <img src={image.src} alt="BigCo Inc. logo"/>
        </div>
    );
};

ArticlePage.defaultProps = {
    title: '',
    richText: '',
    image: '',
};

ArticlePage.propTypes = {
    title: PropTypes.string.isRequired,
    richText: PropTypes.string,
    image: PropTypes.string.isrequired,
};

export default basePageWrap(ArticlePage);
