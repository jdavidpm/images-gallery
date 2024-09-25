import React from "react";
import { Container, Button } from "react-bootstrap";

const Welcome = () =>  (
  <Container className="p-5 mb-4 bg-light rounded-3">
    <h1>Images Gallery</h1>
    <p>
      This is a simple application that retrieves photos using Unsplash API.
      In order to start enter any search item in the input field.
    </p>
    <p>
      <Button bsStyle="primary">Learn more</Button>
    </p>
  </Container>
  
);

export default Welcome;