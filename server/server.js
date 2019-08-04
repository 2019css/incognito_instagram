var express = require('express');
var app = express();

app.get('/', function (request, response) {
    response.send('Server is working')   
})

app.listen(3000);
console.log('App is running on port 3000')