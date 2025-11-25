window.sqlite3InitModule().then(function(sqlite3){
})
var sqlite3 = require("sqlite3"); //database package

let db = new sqlite3.Database("books.db");
db.run("CREATE TABLE books ( isbn VARCHAR(17) PRIMARY KEY, title VARCHAR(30), year INT, genre VARCHAR(50), status INT)");

db.close();
