import React from 'react';
import PropTypes from 'prop-types';
import { basePageWrap } from '../BasePage';
import Hero from '../../components/Hero';
import RawHtml from '../../components/RawHtml';
import s from './BlogPage.module.css';

const BlogPage = ({ title, intro, body, caption }) => {
    return (
        <div className={s.Container}>
            <Hero title={title} />
            <RawHtml html={intro} />



            <div>
   {body.map((card, key) => (
   <div>
       <p>{card.value.caption}</p>
       <p>{card.value.image.url}</p>...
       <img src={card.value.image.url} alt="BigCo Inc. logo"/>
       </div>
   ))}
</div>


        </div>
    );
};

BlogPage.defaultProps = {
    title: '',
    body: '',
    intro: '',
    caption: '',
    image: '',
};

BlogPage.propTypes = {
    title: PropTypes.string.isRequired,
    intro: PropTypes.string,
    image: PropTypes.string.isrequired,
    caption: PropTypes.string,
};

export default basePageWrap(BlogPage);
