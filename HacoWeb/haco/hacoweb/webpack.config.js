const path = require('path');

module.exports = {
    mode: "development",
    watch: true,
    entry: "./static/src/index.js",
    devtool: 'source-map',
    output: {
        path: path.resolve(__dirname, './static/dist'),
        filename: "hacoweb.bundle.js"
    },
    resolve: {
        extensions: [
            '.js'
        ]
    }
}