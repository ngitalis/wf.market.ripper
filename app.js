var express = require('express');
var MongoClient = require('mongodb').MongoClient;

var app = express( );
app.use(express.static(__dirname + '/public'));


app.get('/orders', function (req, res) {
    MongoClient.connect("mongodb://localhost:27017/warframe", function(err, db) {
        var orders = db.collection('orders');
        orders.find().toArray(function(err, docs) {
            res.send(docs);
        });
    });
})


var server = app.listen(3000, function( ) {
	console.log( "Server Up @: " + 3000 );
});


















