import React from "react";
import { Container, Grid } from "@material-ui/core";
import MainCard from "../components/MainCard";

function Home() {
  return (
    <Container maxWidth="lg">
      <Grid container spacing={3} direction="column">
        <Grid item>
          <MainCard />
        </Grid>
      </Grid>
    </Container>
  );
}

export default Home;
