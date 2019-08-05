var express = require("express");
var app = express();

var appRoute = require("./router/appRoute");
var main = require("./router/main");

app.set("views", __dirname + "/views");
app.set("view engine", "ejs");
app.engine("html", require("ejs").renderFile);
app.use(express.static("views"));
app.use(express.json());

app.use("/", main);
app.use("/app", appRoute);

app.listen(3000, function() {
  console.log("Express server has started on port 3000");
});
