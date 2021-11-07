import React from "react";
import ImageInput from "./views/imageInput";
import './App.css'
import {
  BrowserRouter as Router,
  Switch,
  Route,
  useHistory

} from "react-router-dom";
import Form from "./views/Form";

import Recommendations from './views/Recommendations'
function App() {
  return (
    <>
      <Switch>
        <Route exact path="/">
          <ImageInput />
        </Route>
        <Route path="/form">
          <Form />
        </Route>
        <Route path="/results">
          <Recommendations />
        </Route>




      </Switch>

    </>
  );
}

export default App;
