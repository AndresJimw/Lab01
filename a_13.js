var zlib = require('zlib');
var test = "hello";
var flag = "zip";

console.log("Input: ", test);

if (flag == "zip") {
    var input = Buffer.from(test);

    zlib.deflate(input, function(err, buf) {
        var res = buf.toString('base64');
        console.log("Compressed: ", res);
    });
} else {
    var input = Buffer.from(test, 'base64');

    zlib.inflate(input, function(err, buf) {
        if (buf == undefined) console.log("Incorrect format in processing Base64!");
        else console.log("Uncompressed:", buf.toString("utf8"));
    });
}
