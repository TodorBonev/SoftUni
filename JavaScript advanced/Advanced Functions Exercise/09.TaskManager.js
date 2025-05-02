function solve() {

    const [taskField, descriptionField, dateField] = 
        ['task', 'description', 'date'].map(id => document.getElementById(id));
    const addBtn = document.getElementById('add');
    
    const sections = document.querySelectorAll('section');
    const [openArea, progressArea, completeArea] = 
        [1, 2, 3].map(i => sections[i].querySelector('div:nth-child(2)'));
    
    addBtn.addEventListener('click', e => {
        e.preventDefault();
        
        const task = taskField.value;
        const description = descriptionField.value;
        const date = dateField.value;
        
        if (!task || !description || !date) return;
        
        createArticle('open', task, description, date);
    });
    
    function createArticle(type, task, description, date) {

        const article = document.createElement('article');
        
        article.innerHTML = `
            <h3>${task}</h3>
            <p>Description: ${description}</p>
            <p>Due Date: ${date}</p>
        `;
        
        if (type !== 'complete') {
            const divEl = document.createElement('div');
            divEl.className = 'flex';
            
            const configs = {
                'open': [
                    { text: 'Start', class: 'green', action: () => moveTask('progress') },
                    { text: 'Delete', class: 'red', action: () => article.remove() }
                ],
                'progress': [
                    { text: 'Delete', class: 'red', action: () => article.remove() },
                    { text: 'Finish', class: 'orange', action: () => moveTask('complete') }
                ]
            };
            
            configs[type].forEach(config => {
                const btn = document.createElement('button');
                btn.textContent = config.text;
                btn.className = config.class;
                btn.addEventListener('click', config.action);
                divEl.appendChild(btn);
            });
            
            article.appendChild(divEl);
        }
        
        const targetArea = {
            'open': openArea,
            'progress': progressArea,
            'complete': completeArea
        }[type];
        
        targetArea.appendChild(article);
        
        function moveTask(newType) {
            article.remove();
            createArticle(newType, task, description, date);
        }
    }
}

