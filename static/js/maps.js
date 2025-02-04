
        // Inicializar o mapa
        var map = L.map('map').setView([-25.895417470545663, -50.384092418009274], 15); // Coordenadas da igreja

        // Adicionar camada do OpenStreetMap
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '© OpenStreetMap contributors'
        }).addTo(map);

        // Adicionar marcador no local da igreja
        L.marker([-25.895417470545663, -50.384092418009274]).addTo(map)
            .bindPopup('<b>IEQ Santa Cruz</b><br>Rua Ewaldo Fischer da Silva, 32, São Mateus do Sul - PR')
            .openPopup();

