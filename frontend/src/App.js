import React from "react";
import ImageInput from "./views/imageInput";
import './App.css'
import {
  BrowserRouter as Router,
  Routes as Switch,
  Route,
  useHistory

} from "react-router-dom";
import Form from "./views/Form";

import Recommendations from './views/Recommendations'
function App() {
  return (

    <Router>
     
      <Switch>
      <Route path="/" element={<ImageInput />} />
      <Route path="/form" element={<Form />} />
      <Route path="/recs" element={<Recommendations />} />




      </Switch>

    </Router>

  );
}

export default App;
