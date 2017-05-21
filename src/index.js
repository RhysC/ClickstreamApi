'use strict';
var AWS = require('aws-sdk');

console.log('Loading function');

var firehose = new AWS.Firehose({
    apiVersion: '2015-08-04',
    region : 'eu-west-1'
});

exports.handler = (event, context, callback) => {
    //console.log('Received event:', JSON.stringify(event, null, 2));
    event.Records.forEach((record) => {
        // Kinesis data is base64 encoded so decode here
        const payload = new Buffer(record.kinesis.data, 'base64').toString('ascii');
        console.log('Decoded payload:', payload);
        //Firehose
        var params = {
          DeliveryStreamName: 'clickstreamfirehose',
          Record: {
            Data: payload
          }
        };
        firehose.putRecord(params, function(err, data) {
          if (err){
            console.log(err, err.stack); // an error occurred
          } else {
             console.log(data);           // successful response
          }
        });
    });
    callback(null, 'Successfully processed ${event.Records.length} records.');
};
