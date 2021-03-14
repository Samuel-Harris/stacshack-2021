import React from "react";
import {
  Box,
  Card,
  CardActionArea,
  CardMedia,
  Typography,
} from "@material-ui/core";

import { makeStyles } from "@material-ui/core/styles";

const useStyles = makeStyles({
  media: {
    height: 500,
    backgroundPosition: "top",
  },
  card: {
    backgroundColor: "#233a41",
  },
  text: {
    position: "absolute",
    top: "50%",
    left: "50%",
    transform: "translate(-50%, -50%)",
    textShadow: "2px 2px 5px black",
  },
});

function MainCard() {
  const classes = useStyles();
  const [line, setLine] = React.useState("");
  const url = "https://amc51.host.cs.st-andrews.ac.uk/mi_flute.mp3";

  const handleClick = async (e) => {
    e.preventDefault();
    const audio = document.getElementById("audio");
    audio.volume = 0.03;
    audio.play();
    const response = await fetch("/api/data");
    const body = await response.json();
    if (response.status === 200) {
      setLine('"' + body + '"');
    } else {
      console.log(body.message);
    }
  };

  const image =
    "https://media.gq-magazine.co.uk/photos/5e6270c2f399d1000844382b/master/pass/20200304-April-cover-06.jpg";

  return (
    <Box position="relative" textAlign="center" paddingTop="2rem">
      <Typography
        style={{ fontFamily: "Georgia" }}
        className={classes.text}
        color="secondary"
        variant="h4"
      >
        {line}
      </Typography>
      <Card className={classes.card} elevation={3}>
        <CardMedia className={classes.media} image={image} />
        <CardActionArea onClick={handleClick}>
          <Box padding="0.5rem" textAlign="center">
            <Typography
              style={{ fontFamily: "Trebuchet MS" }}
              color="primary"
              variant="body1"
            >
              {"GENERATE NEW LINE"}
            </Typography>
          </Box>
        </CardActionArea>
      </Card>
      <audio id="audio">
        <source src={url} type="audio/mpeg" />
      </audio>
    </Box>
  );
}

export default MainCard;
