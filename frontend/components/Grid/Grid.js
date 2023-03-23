import { Grid, Card, Text } from "@nextui-org/react";
import {useMediaQuery} from './useMediaQuery.js'
export default function App() {
  const isMd = useMediaQuery(960);
  const names = ['Ada Lovelace', 'Grace Hopper', 'Margaret Hamilton'];

  const MockItem = ({ text }) => {
    return (
      <Card css={{ h: "$20", $$cardColor: '$colors$primary' }}>
        <Card.Body>
          <Text h6 size={15} color="white" css={{ m: 0 }}>
            {text}
          </Text>
        </Card.Body>
      </Card>
    );
  };
  return (
    <Grid.Container gap={2} justify="center">


      <Grid xs={6} md={3}>
        <MockItem text={isMd ? "2 of 2" : "1 of 3"} />
      </Grid>
      <Grid xs={6} md={3}>
        <MockItem text={isMd ? "1 of 2" : "2 of 3"} />
      </Grid>
      <Grid xs={6} md={3}>
        <MockItem text={isMd ? "2 of 2" : "3 of 3"} />
      </Grid>
    </Grid.Container>

        {names.map((name) => (
          <li key={name}>{name}</li>
        ))}


  );
}
