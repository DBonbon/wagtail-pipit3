// import PropTypes from 'prop-types';
import { basePageWrap } from '../BasePage';
import s from './GamePage.module.css';

const GamePage = ({ title, intro, cards, slug, language }) => {
    return <div className={s.Root}>GamePage</div>;
};

export default basePageWrap(GamePage);
