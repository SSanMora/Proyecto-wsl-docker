const express = require('express');
const app = express();
const PORT = 3000;

app.get('/api', (req, res) => {
    res.json({
        status: "success",
        message: "API Node.js segura y respondiendo a través del proxy inverso de Nginx en WSL2",
        timestamp: new Date()
    });
});

app.listen(PORT, () => {
    console.log(`Servidor de la API corriendo en el puerto ${PORT}`);
});
