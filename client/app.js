const express = require("express");

const app = express();
const handlebars = require("express-handlebars").create({ defaultLayout: "main" });
const bodyParser = require("body-parser");

app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static("public"));	//for serving static files
app.use(bodyParser.json());

var XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;
var cookie = require('cookie');
var setCookie = require('set-cookie');
var cookieCount = 0;

app.engine("handlebars", handlebars.engine);
app.set("view engine", "handlebars");
app.set("port", 8080);

app.post("/results", function (req, res) {
    console.log(req.body.submitButton.value);
    if (req.body.submitButton == 'Start the crawler') {
        var payload = { page: null, method: null, limit: 2, keyword: null };
        payload.page = req.body.page;
        payload.limit = parseInt(req.body.limit);
        payload.method = req.body.method;
        payload.keyword = req.body.keyword;
        var payloadJson = JSON.stringify(payload);
        console.log(payload);

        //get previous cookies for count
        var cookies = cookie.parse(req.headers.cookie || '');

        //create cookie with search information
        setCookie('myCookie' + Object.keys(cookies).length, payloadJson, { path: '/', res: res });
    } else {
        var payloadJson = req.body.cookies;
        console.log(payloadJson);
        //if select none was clicked, then redirect back to homepage
        if (payloadJson == "") {
            res.redirect("/");
            return;
        }
    }

    console.log(payloadJson);
    //send json to server
	var request = new XMLHttpRequest();
	request.open('POST', 'https://webcrawler-201200.appspot.com', false);
	request.setRequestHeader('Content-Type', 'application/json');
	request.send(payloadJson);
	var response = JSON.parse(request.responseText);
	//console.log(request.responseText);

	//var response = '{"start": "0", "cookie": "test", "URLs": {"0": {"found": false, "edges": ["1"], "title": "title0"}, "1": {"found": false, "edges": [], "title": "title1"}}}';
	//if (response && request.status == 200) {
	if (request.status == 200) {
	//if (response) {
	//	console.log(request.responseText);
		res.render("results", { "jsonObj": JSON.stringify(response) });
	} else {
		alert('Error!');
	}
});

app.get("/", function (req, res) {
    var cookies = cookie.parse(req.headers.cookie || '');
    //revert cookies back to an array of json objects
    var parsedCookies = [];
    var keys = Object.keys(cookies);
    for (var i = 0; i < keys.length; i++) {
        try {
            parsedCookies.push(JSON.parse(cookies[keys[i]]));
        } catch(SyntaxError) {
            console.log("Error");
        }
        //parsedCookies.push(JSON.parse(cookies[keys[i]]));
    }
    //render page
    res.render("index", { 'cookies': parsedCookies });
});


app.get("/force", function (req, res) {
	res.render("force");
});

//app.get("/results", function (req, res) {
//	res.render("results");
//});

app.get("/practice", function (req, res) {
	res.render("practice");
});

app.get("/llprac", function (req, res) {
	res.render("llprac");
});

app.use(function (req, res) {
	res.status(404);
	res.render("404");
});

//error handler function
app.use(function (err, req, res, next) {
	console.error(err.stack);
	res.type("plain/text");
	res.status(500);
	res.render("500");
});

app.listen(app.get("port"), function () {
	console.log('Express started on http://localhost:' + app.get("port"));
});
