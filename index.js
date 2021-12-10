/*
CodeForGeek, Shahid. (2021). Render HTML file in Node.js and Express.js framework. https://codeforgeek.com/render-html-file-expressjs/
*/
const express = require('express');
const {spawn} = require('child_process');
const path = require('path');
const router = express.Router();
const app = express();
const port = 8000;
/*-- Bring in the view engine and views directory --*/
app.set("view engine", "pug");
app.set("views", path.join(__dirname, "views"));

/*
  TODO: Run Stealy Steve's Python Script when route is called. only worked halfway through the tutorial
  Petros Koulianos 💀☠👽. (2020). How to Run a Python script from Node.js . https://medium.com/swlh/run-python-script-from-node-js-and-send-data-to-browser-15677fcf199f
*/
app.get('/home', (req, res) => {
    var dataToSend;
    // spawn new child process to call the python script
    // const python = spawn('python', ['script2.py', 'node.js', 'python']);
    // Mega Dovetail to class objective: FileI/O - file call from node with child spawn
    // TODO: call to Stealy Steve's Python script in a child process in index.js express server
    const stealyStevePythonProgram = spawn('python', ['script2.py']);

    // collect data from script
    // python.stdout.on('data', function (data) {
    //     console.log('Pipe data from python script ...');
    //     dataToSend = data.toString();
    // });
    stealyStevePythonProgram.stdout.on('data', function (data) {
        console.log('Pipe data from python script ...');
        dataToSend = data.toString();
    });
    // in close event we are sure that stream from child process is closed
    // python.on('close', (code) => {
    //     console.log(`child process close all stdio with code ${code}`);
    //     // send data to browser
    //     res.send(dataToSend)
    // });
    stealyStevePythonProgram.on('close', (code) => {
        console.log(`child process close all stdio with code ${code}`);
        // send data to browser
        res.send(dataToSend)
    });
});

router.get('/',function(req,res){
  res.render('index');
  //__dirname : It will resolve to your project folder.
});

router.get('/about',function(req,res){
  res.render("about", { title: "Hey", message: "Hello there!" });
});

//add the router
app.use('/', router);
app.listen(port, () => console.log(`Stealy Steve hanging out on the corner of Main Street and ${port} West Street!`))
