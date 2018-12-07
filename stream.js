function plasma(content) {
    var python = require('python-shell')
    var path = require('path')
    dU = document.getElementById('downloadUrl').value
    if (!dU) {
        alert('Please enter a url')
    } else {
        var options = {
            scriptPath: path.join(__dirname, './'),
            args: [dU, content]
        }

        var down = new python('youDown.py', options);
        document.getElementById('status').innerHTML = "Starting download... "
        document.getElementById('status').innerHTML += "<br>          Downloading... "
        down.on('message', function (message) {
            document.getElementById('status').innerHTML = "Downloaded"
            alert(message);
        })

    }
}