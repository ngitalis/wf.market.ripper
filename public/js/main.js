$(document).ready(function ( ) {



    $.getJSON( "orders", function( data ) {
        $("#jsGrid").jsGrid({
            width: "100%",
            height: "100%",
     
            sorting: true,
     
            data: data,
     
            fields: [
                { name: "item_name", type: "text", width: 150 },
                { name: "lowest_price", type: "number", width: 50 },
                { name: "popularity", type: "number", width: 50 },
                { name: "near_lowest_count", type: "number", width: 50 },
                { name: "buy_lowest_price", type: "number", width: 50 },
                { name: "buy_highest_price", type: "number", width: 50 },
                { name: "buy_popularity", type: "number", width: 50 },
                { name: "online_count", type: "number", width: 50 },
            ]
        });
    });
 


});
