const backendUrl = window.location.origin;  // automaticamente o domínio + a porta

// Função para alternar entre modo claro e escuro
function toggleDarkMode() {
    // Alterna a classe 'dark-mode' no body
    document.body.classList.toggle('dark-mode');

    // Atualiza o emoji do botão
    const button = document.getElementById('theme-toggle');
    if (document.body.classList.contains('dark-mode')) {
        button.innerHTML = "🌞"; // Emoji do sol para modo claro
    } else {
        button.innerHTML = "🌙"; // Emoji da lua para modo escuro
    }
}

// Adicionando o evento para o botão de alternar tema
document.querySelector('#theme-toggle').addEventListener('click', toggleDarkMode);

document.querySelector('#upload-form').addEventListener('submit', function(event) {
    event.preventDefault();  
    let formData = new FormData(this);  

    // Exibir a barra de carregamento
    document.getElementById('loading').style.display = 'block';

    fetch(`${backendUrl}/predict`, { 
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        // Esconder a barra de carregamento
        document.getElementById('loading').style.display = 'none';
        
        if (data.error) {
            document.getElementById('result').innerHTML = 'Erro: ' + data.error;
        } else {
            document.getElementById('result').innerHTML = `
                <strong>Imagem:</strong> ${data.image_name} <br>
                <strong>Predição:</strong> ${data.prediction} <br>
                <strong>Confiança:</strong> ${data.confidence} <br>
            `;
        }
    })
    .catch(error => {
        document.getElementById('loading').style.display = 'none';
        document.getElementById('result').innerHTML = 'Erro ao enviar a imagem: ' + error;
    });
});
