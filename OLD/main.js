var request = require("request");
var MongoClient = require('mongodb').MongoClient;

MongoClient.connect("mongodb://localhost:27017/warframe", function(err, db) {
    var orders = db.collection('orders');
    orders.insert(order, {w:1}, function (err, res) {

    });
});


MongoClient.connect("mongodb://localhost:27017/warframe", function(err, db) {
    var master_list = db.collection('master_list');
    master_list.insert(list, {w:1}, function (err, res) {

    });
});







function wrapper(run) {
    MongoClient.connect("mongodb://localhost:27017/warframe", function(err, db) {
        run();
    });
}



function main( ) {
    var master_list = db.collection('master_list');
    var orders = db.collection('orders');

    master_list.find().toArray(function(err, docs) {
        if ( !docs.length ) {
            // get item list
            request('http://warframe.market/api/get_all_items_v2', function (error, response, body) {
                if (!error && response.statusCode == 200) {
                    var item_list = JSON.parse(body);
                    // save items.
                    master_list.insert(list, {w:1}, function (err, res) {
                        
                    });
                }
            });
        }
    }
}












function get_item(item) {
    console.log("Getting. . .");
    console.log(item);

    var uri = 'http://warframe.market/api/get_orders/'
    uri = uri + item.item_type + '/';
    uri = uri + item.item_name;
    console.log(uri)
    request(uri, function (error, response, body) {
        // console.log(arguments);
        if (!error && response.statusCode == 200) {
            var item_stats = JSON.parse(body);
            console.log(item_stats);

            // buy orders
            for ( var i in item_stats.response.buy ) {
                console.log(item_stats.response.buy[i]);
            }

            // sell orders
            for ( var i in item_stats.response.sell ) {
                console.log(item_stats.response.sell[i]);
            }

            """
            Packet:
            { 
            online_ingame: false,
            count: 2,
            online_status: false,
            price: 10,
            ingame_name: 'Avenon' 
            }
            """
        }
    });
}

function get_item_list(callback) {

}


get_item_list(function (items) {
    // console.log(items);
    // console.log(items.length);

    get_item(items[2]);
})
















