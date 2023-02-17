const http = require("http");
const fs = require("fs");
const os = require("os");
const ip = require('ip');


//Defined as a funtion due to how much code was used, eaiser to read outside of the normal script.
function SecondsToDaysHoursMinutesSeconds(time) {
var Dnumber, Hnumber, Mnumber, Snumber, D, H, M, S;
Dnumber = Math.floor(time / (3600*24));
Hnumber = Math.floor(time % (3600*24) / 3600);
Mnumber = Math.floor(time % 3600 / 60);
Snumber = Math.floor(time % 60)

D = Dnumber + " Days, ";
H = Hnumber + " Hours, ";
M = Mnumber + " Minutes, ";
S = Snumber + " Seconds";

return (D + H + M + S)
}

const server = http.createServer((req, res) => {
    if (req.url === "/") {
        fs.readFile("./public/index.html", "UTF-8", (err, body) => {
        res.writeHead(200, {"Content-Type": "text/html"});
        res.end(body);
      });
    } else if(req.url.match("/sysinfo")) {
      myHostName=os.hostname();
      myUptime = SecondsToDaysHoursMinutesSeconds(os.uptime());
      TotalMemory = os.totalmem()/1048576;
      TotalMemoryMB = TotalMemory + " MB";
      FreeMemory = os.freemem()/1048576;
      FreeMemoryMB = FreeMemory + " MB";
      Cores = os.cpus().length;
      html=`
      <!DOCTYPE html>
      <html>
        <head>
          <title>Node JS Response</title>
        </head>
        <body>
          <p>Hostname: ${myHostName}</p>
          <p>IP: ${ip.address()}</p>
          <p>Server Uptime: ${myUptime}</p>
          <p>Total Memory: ${TotalMemoryMB}</p>
          <p>Free Memory: ${FreeMemoryMB}</p>
          <p>Number of CPUs: ${Cores} </p>
        </body>
      </html>`
      res.writeHead(200, {"Content-Type": "text/html"});
      res.end(html);
    } else {
      res.writeHead(404, {"Content-Type": "text/plain"});
      res.end(`404 File Not Found at ${req.url}`);
    }
    }).listen(3000);


console.log("Server listening on port 3000")
