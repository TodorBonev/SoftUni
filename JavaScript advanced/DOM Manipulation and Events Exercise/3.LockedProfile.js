function lockedProfile() {
    document.querySelectorAll('button').forEach(button =>
        button.addEventListener('click', ({ target }) => {
            const profile = target.parentNode;
            const moreInfo = profile.querySelector('div');
            const isLocked = profile.querySelector('input[type="radio"][value="lock"]').checked;

            if (!isLocked) {
                moreInfo.style.display = target.textContent === 'Show more' ? 'inline-block' : 'none';
                target.textContent = target.textContent === 'Show more' ? 'Hide it' : 'Show more';
            }
        })
    );
}


