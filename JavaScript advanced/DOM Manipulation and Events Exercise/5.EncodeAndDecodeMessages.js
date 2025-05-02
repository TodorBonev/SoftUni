function encodeAndDecodeMessages() {
    document.getElementById('main').addEventListener('click', ({ target }) => {
        if (target.tagName !== 'BUTTON') return;

        const [decodedMessage, encodedMessage] = document.getElementsByTagName('textarea');
        const shift = target.textContent.includes('Encode') ? 1 : -1;
        const source = shift === 1 ? decodedMessage : encodedMessage;

        const transformed = [...source.value].map(char => String.fromCharCode(char.charCodeAt(0) + shift)).join('');
        
        decodedMessage.value = shift === 1 ? '' : decodedMessage.value;
        encodedMessage.value = transformed;
    });
}

