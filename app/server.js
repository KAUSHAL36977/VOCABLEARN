
const express = require('express'); // Import Express framework
const mysql = require('mysql'); // Import MySQL library
const cors = require('cors'); // Import CORS middleware

const app = express(); // Create an Express application
const PORT = process.env.PORT || 5000; // Set the port for the server

// Middleware
app.use(cors()); // Enable CORS for all routes
app.use(express.json()); // Parse JSON bodies

// MySQL database connection
const db = mysql.createConnection({
    host: 'localhost', // Database host
    user: 'root', // Database user
    password: 'your_password', // Database password
    database: 'word_database' // Database name
});

// Connect to the database
db.connect((err) => {
    if (err) {
        console.error('Database connection failed:', err);
        return;
    }
    console.log('Connected to MySQL database');
});

// API endpoint to get random words
app.get('/api/words', (req, res) => {
    const query = 'SELECT * FROM words ORDER BY RAND() LIMIT 10'; // SQL query to get random words
    db.query(query, (err, results) => {
        if (err) {
            return res.status(500).json({ error: 'Database query failed' });
        }
        res.json(results); // Send the results as JSON
    });
});

// API endpoint to add a new word
app.post('/api/words', (req, res) => {
    const { word, meaning } = req.body; // Destructure word and meaning from request body
    const query = 'INSERT INTO words (word, meaning) VALUES (?, ?)'; // SQL query to insert a new word
    db.query(query, [word, meaning], (err, results) => {
        if (err) {
            return res.status(500).json({ error: 'Failed to insert word' });
        }
        res.status(201).json({ id: results.insertId, word, meaning }); // Send back the created word
    });
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
