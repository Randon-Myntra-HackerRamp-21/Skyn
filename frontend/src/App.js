import React from "react";
import './App.css'
import {
  BrowserRouter as Router,
  Routes as Switch,
  Route,
  useHistory  
} from "react-router-dom";

import ImageInput from "./views/imageInput";
import Recommendations from './views/Recommendations'
import Form from "./views/Form";

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
