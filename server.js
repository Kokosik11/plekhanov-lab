const express = require('express');
const app = express();
const path = require("path");
const port = 3000;

app.use(express.static(path.join(__dirname, "/src/")));

app.get('/admin', (req, res) => {
    res.sendFile(path.join(__dirname, "/admin/index.html"));
})

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, "/src/index.html"));
})

app.listen(port, () => console.log(`Server listening on port ${port}!`))