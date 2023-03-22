import React from 'react';
import s from './Button.module.css';

const Button = ({onClick, text}) => (
    <button className={s.Button} onClick={onClick}>
        {text}
    </button>
);

Button.propTypes = {};

Button.defaultProps = {};

export default Button;
