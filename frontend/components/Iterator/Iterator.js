// import PropTypes from 'prop-types';
import s from './Iterator.module.css';
import { Grid, Card, Text } from '@nextui-org/react';

const Iterator = () => {
    const names = ['Ada Lovelace', 'Grace Hopper', 'Margaret Hamilton'];

    return <div className={s.Root}>

    <div>
    <Grid.Container gap={2}>

        {names.map((name) => (
          <Grid xs={4}>
          <Card key={name} css={{ mw: "400px" }}>Header

      <Card.Body>
        <Text>{name} </Text>
      </Card.Body>
    </Card>
    </Grid>
        ))}

    </Grid.Container>
      </div>



    </div>;
};

Iterator.propTypes = {};

Iterator.defaultProps = {};

export default Iterator;
