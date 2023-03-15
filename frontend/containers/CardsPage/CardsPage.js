import React, { PureComponent } from 'react';

// import i18n from '../../i18n';
import PropTypes from 'prop-types';
import { basePageWrap } from '../BasePage';
import s from './CardsPage.module.css';
import RawHtml from '../../components/RawHtml';
import Hero from '../../components/Hero';

/*
export default class Display extends Component {
    render() {
        const { data } = this.props;
        return (
            <>
               {
                   data.map((value,key)=>
                       <div>{value.cardTitle}</div>
                       <div>{value.id}</div>
                   )
               }
            </>
        )
    }
*/

const CardsPage = ({ title, intro, cards, seoMetaRobots, slug, seoTitle, cardTitle, language }) => {
    return (
        <div className={s.Container}>
            <Hero title={title} />
            <RawHtml html={intro} />



            <div>
   {cards.map((card, key) => (
   <div>
       <p>{card.value.cardTitle}</p>
       <p>{card.value.cardSubtitle}</p>...   </div>
   ))}
</div>

            <p>seo_meta_robots={seoMetaRobots} </p>
             <p>My-SEO: {seoTitle} </p>
            <p>My Slug:{slug}</p>
            <p>{language}</p>
            <p>{cardTitle}</p>
        </div>
    );
};

CardsPage.defaultProps = {
    title: '',
    intro: '',
    cards: '',
    slug: '',
    language: '',
    cardTitle:'',
    seoTitle:'',
    seoMetaRobots:'',
};

CardsPage.propTypes = {
    title: PropTypes.string.isRequired,
    intro: PropTypes.string,
    body: PropTypes.string,
    slug: PropTypes.string,
    language: PropTypes.string,
    cardTitle: PropTypes.string,
    seoTitle: PropTypes.string,
    seoMetaRobots: PropTypes.string,
};

export default basePageWrap(CardsPage);
