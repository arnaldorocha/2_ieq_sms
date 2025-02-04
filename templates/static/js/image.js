// Variável global para armazenar a lista de mídias e o índice atual
let medias = [];
let currentIndex = 0;

// Função para abrir o modal e exibir a mídia selecionada
function openMedia(media) {
    // Armazena a lista de mídias e encontra o índice da mídia atual
    medias = document.querySelectorAll('.media-item');
    currentIndex = Array.from(medias).indexOf(document.querySelector(`.media-item[src="${media}"], .media-item[onclick*="${media}"]`));
    
    // Exibe o modal
    const modal = document.getElementById('mediaModal');
    const modalImage = document.getElementById('modalImage');
    const modalVideo = document.getElementById('modalVideo');
    
    // Verifica se é imagem ou vídeo
    if (media.endsWith('.mp4') || media.endsWith('.avi') || media.endsWith('.mov') || media.endsWith('.mkv')) {
        modalImage.classList.add('d-none');
        modalVideo.classList.remove('d-none');
        modalVideo.src = media;
    } else {
        modalVideo.classList.add('d-none');
        modalImage.classList.remove('d-none');
        modalImage.src = media;
    }
    
    modal.classList.remove('d-none');
}

// Função para fechar o modal
function closeMedia() {
    const modal = document.getElementById('mediaModal');
    const modalImage = document.getElementById('modalImage');
    const modalVideo = document.getElementById('modalVideo');
    
    // Reseta as fontes de mídia
    modalImage.classList.add('d-none');
    modalVideo.classList.add('d-none');
    modalVideo.src = '';
    modalImage.src = '';
    
    // Fecha o modal
    modal.classList.add('d-none');
}

// Função para ir para a mídia anterior
function prevMedia() {
    if (currentIndex > 0) {
        currentIndex--;
    } else {
        currentIndex = medias.length - 1; // Volta para o último item
    }
    
    const nextMedia = medias[currentIndex].getAttribute('src');
    openMedia(nextMedia);
}

// Função para ir para a mídia próxima
function nextMedia() {
    if (currentIndex < medias.length - 1) {
        currentIndex++;
    } else {
        currentIndex = 0; // Volta para o primeiro item
    }
    
    const nextMedia = medias[currentIndex].getAttribute('src');
    openMedia(nextMedia);
}

// Função para escutar teclas pressionadas e controlar o modal
function handleKeydown(event) {
    const modal = document.getElementById('mediaModal');

    // Se o modal está aberto
    if (!modal.classList.contains('d-none')) {
        switch (event.key) {
            case 'Escape': // Fecha o modal quando a tecla Esc é pressionada
                closeMedia();
                break;
            case 'ArrowLeft': // Vai para a mídia anterior
                prevMedia();
                break;
            case 'ArrowRight': // Vai para a próxima mídia
                nextMedia();
                break;
            default:
                break;
        }
    }
}

// Adiciona o evento de teclado para toda a página
document.addEventListener('keydown', handleKeydown);
