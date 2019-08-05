var express = require("express");
var router = express.Router();

/**
 * 
 * @param {String} friendID 이름
 */
function greetfrom(friendID) {
  console.log("실행: ", friendID);
  // 인스타그램 요청보내기
}

/* GET home page. */
router.post("/great", function(req, res, next) {
  greetfrom(req.body.privateID);
  res.status(200).json({
      data :req.body.privateID
  });
});

module.exports = router;
