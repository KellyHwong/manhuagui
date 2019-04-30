const pages = Array.from(document.querySelectorAll('img.image-item'));
let currentPage = 0;

function changePage(pageNum) {
    const previous = pages[currentPage];
    const current = pages[pageNum];

    if (current == null) {
        return;
    }
    
    previous.classList.remove('current');
    current.classList.add('current');

    currentPage = pageNum;

    const display = document.getElementById('dest');
    display.style.backgroundImage = `url("${current.src}")`;

    document.getElementById('page-num')
        .innerText = [
                (pageNum + 1).toLocaleString(),
                pages.length.toLocaleString()
            ].join('\u200a/\u200a');
}

changePage(0);

document.getElementById('list').onclick = event => {
    if (pages.includes(event.target)) {
        changePage(pages.indexOf(event.target));
    }
};

document.getElementById('image-container').onclick = event => {
    const width = document.getElementById('image-container').clientWidth;
    const clickPos = event.clientX / width;

    if (clickPos < 0.5) {
        changePage(currentPage - 1);
    } else {
        changePage(currentPage + 1);
    }
};

document.onkeypress = event => {
    switch (event.key.toLowerCase()) {
        // Previous Image
        case 'arrowleft':
        case 'a':
            changePage(currentPage - 1);
            break;

        // Next Image
        case ' ':
        case 'enter':
        case 'arrowright':
        case 'd':
            changePage(currentPage + 1);
            break;
    }
};