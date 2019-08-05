var express = require('express');
var app = express();
var bodyParser = require('body-parser');
var router = require('./router/main')(app);
var greet = require('./app');

app.set('views', __dirname + '/views');
app.set('view engine', 'ejs');
app.engine('html', require('ejs').renderFile);

var server = app.listen(3000, function(){
    console.log("Express server has started on port 3000")
});

app.use(express.static('views'));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended : true}));

app.post('/app', function(req,res){
    greet();
    res.send("Hi");
});