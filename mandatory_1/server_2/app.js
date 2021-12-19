const express = require("express");
const app = express();
const port = 2222;
const cors = require("cors");
const axios = require("axios");
const xmlparser = require("express-xml-bodyparser");

// Parser for XML to JSON (currently just reference; not working properly)
// const xml2js = require("xml2js");
// const parser = new xml2js.Parser({ attrkey: "ATTR", explicitArray: false });

app.use(cors());
app.use(xmlparser());

// Helper func
const parseXmlToJson = (xml_form) => {
  const data = JSON.stringify(xml_form, null, 4);
  const json_data = JSON.parse(data).data;
  const email = json_data.email[0];
  const name = json_data.name[0];
  const pass = json_data.password[0];
  return {
    email: json_data.email[0],
    name: json_data.name[0],
    pass: json_data.password[0],
  };
};

app.get("/", (res) => {
  res.send("Welcome to System Integration mandatory 1 server 2!");
});

app.post("/signup", (req, res) => {
  console.log("Node signup");
  json_res = parseXmlToJson(req.body);

  console.log("Our data: ", json_res);

  console.log("Node signup - Send res");
  res.json(json_res);

  axios
    .post("http://127.0.0.1:3333/signup", {
      data: json_res,
    })
    .then((res) => {
      console.log(`statusCode: ${res.status}`);
    })
    .catch((error) => {
      console.error(error);
    });
});

app.listen(port, () => {
  console.log(`Server 2 listening at http://127.0.0.1:${port}`);
});
