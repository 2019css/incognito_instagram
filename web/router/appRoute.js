var express = require("express");
var pyShell = require('python-shell');
var router = express.Router();


function greetfrom(friendID) {
  
  // Python 실행
  var options = {
    scriptPath: 'crawling/',
    args: [friendID]
  };
  
  pyShell.run('request_follow.py', options, function(err, results){
    if(err) throw err;
    console.log('result: %j', results);
  });
}


/* GET home page. */
router.post("/great", function(req, res, next) {
  greetfrom(req.body.privateID);
  res.status(200).json({
      data :req.body.privateID
  });
});

module.exports = router;